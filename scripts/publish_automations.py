#!/usr/bin/env python3
"""Publish named, anonymized examples from a JSON export stored outside Git.

Original inputs never enter the repository. Generate and validate a complete
temporary catalogue before replacing the known generated output. This command
does not rewrite Git history, publish to GitHub or alter a running HA instance.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

from privacy_guard import Anonymizer, PrivacyError, check_repository


MAX_EXPORT_BYTES = 32 * 1024 * 1024
ROOT_READMES = ("README.md", "README.de.md")
MANAGED_FILES = frozenset(("automation.yaml", "metadata.json", *ROOT_READMES))


def _no_symlinks(path: Path) -> None:
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise PrivacyError("Publication paths must not contain symlinks")
    if ".git" in path.parts:
        raise PrivacyError("Git metadata is not a publication input or output")


def _validate_existing_output(target: Path) -> None:
    if not target.exists():
        return
    if not target.is_dir() or target.is_symlink():
        raise PrivacyError("The existing catalogue is not a safe directory")
    for path in target.rglob("*"):
        if path.is_symlink():
            raise PrivacyError("The existing catalogue contains a symlink")
        if path.is_file() and (path.name not in MANAGED_FILES or path.parent == target):
            raise PrivacyError("The existing catalogue contains unmanaged files; no output was replaced")
    folders = list(target.iterdir())
    if not folders:
        return
    if all(folder.is_dir() and re.fullmatch(r"automation-\d{3}", folder.name) for folder in folders):
        if any({path.name for path in folder.iterdir()} != {"automation.yaml", "README.md"} for folder in folders):
            raise PrivacyError("Legacy catalogue contains unmanaged files")
        return
    try:
        from catalogue import load_entries
        load_entries(target.parent, allow_missing_translations=True)
    except (ValueError, OSError, TypeError, KeyError):
        raise PrivacyError("Existing output is not a managed catalogue; no files were replaced") from None


def _validate_root_readmes(output: Path) -> None:
    for name in ROOT_READMES:
        path = output / name
        _no_symlinks(path)
        if path.exists() and not path.is_file():
            raise PrivacyError("Root READMEs must be regular files")


def _promote_output(stage: Path, output: Path) -> None:
    # Keep the backup outside the automatically removed stage. If the filesystem
    # also refuses rollback, the previous files must remain available to recover.
    backup = Path(tempfile.mkdtemp(prefix=".ha-publication-backup-", dir=output.parent))
    backed_up: list[str] = []
    installed: list[str] = []
    complete = False
    try:
        for name in ("automations", *ROOT_READMES):
            destination = output / name
            if destination.exists():
                os.replace(destination, backup / name)
                backed_up.append(name)
            os.replace(stage / name, destination)
            installed.append(name)
        complete = True
    except OSError:
        try:
            for name in reversed(installed):
                os.replace(output / name, stage / name)
            for name in reversed(backed_up):
                os.replace(backup / name, output / name)
        except OSError:
            raise PrivacyError("Publication rollback failed; previous files retained in the publication backup directory") from None
        complete = True
        raise PrivacyError("Could not publish catalogue; previous automations and root READMEs restored") from None
    finally:
        if complete:
            shutil.rmtree(backup)


def _source_records(path: Path) -> list[dict[str, Any]]:
    if not path.is_file() or path.stat().st_size > MAX_EXPORT_BYTES:
        raise PrivacyError("The source must be a bounded JSON export file")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError, OSError):
        raise PrivacyError("Invalid JSON export; source details suppressed") from None
    if not isinstance(raw, list) or not raw or len(raw) > 10000:
        raise PrivacyError("Source must be a non-empty JSON list with at most 10000 automations")
    records = []
    for item in raw:
        if not isinstance(item, dict):
            raise PrivacyError("Every export item must be an automation object")
        config = item.get("config", item)
        if not isinstance(config, dict):
            raise PrivacyError("Every automation config must be a mapping")
        records.append(config)
    return records


def publish(source: Path, output: Path, private_terms_file: Path | None = None) -> int:
    from catalogue import infer_trigger_types, write_catalogue
    from publication_policy import forbidden_reasons, policy_check

    source, output = source.absolute(), output.absolute()
    _no_symlinks(source)
    _no_symlinks(output)
    source, output = source.resolve(), output.resolve()
    script_root = Path(__file__).resolve().parents[1]
    if source.is_relative_to(script_root) or source.is_relative_to(output):
        raise PrivacyError("Keep private source exports outside the repository and output directory")
    if output == Path(output.anchor):
        raise PrivacyError("The filesystem root cannot be a publication directory")
    if output.exists() and not output.is_dir():
        raise PrivacyError("The output must be a directory")
    if output.exists():
        result = subprocess.run(["git", "-C", str(output), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if result.returncode == 0 and source.is_relative_to(Path(result.stdout.strip()).resolve()):
            raise PrivacyError("Keep private source exports outside the repository")
    target = output / "automations"
    _validate_existing_output(target)
    _validate_root_readmes(output)
    records = _source_records(source)
    # Exclude complete routines before changing names that identify their use.
    records = [config for config in records if not forbidden_reasons(config)]
    if not records:
        raise PrivacyError("No publishable automations remain after the door-control policy; existing output was not replaced")
    private_terms: tuple[str, ...] = ()
    if private_terms_file is not None:
        terms_path = private_terms_file.absolute()
        _no_symlinks(terms_path)
        terms_path = terms_path.resolve()
        if terms_path.is_relative_to(script_root) or terms_path.is_relative_to(output):
            raise PrivacyError("Keep private name lists outside the repository and output directory")
        if output.exists():
            repository = subprocess.run(["git", "-C", str(output), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
            if repository.returncode == 0 and terms_path.is_relative_to(Path(repository.stdout.strip()).resolve()):
                raise PrivacyError("Keep private name lists outside the repository")
        if not terms_path.is_file() or terms_path.stat().st_size > 65536:
            raise PrivacyError("Private name list must be a bounded regular text file")
        private_terms = tuple(line.strip() for line in terms_path.read_text(encoding="utf-8").splitlines() if line.strip())
        if len(private_terms) > 1000 or any(not 2 <= len(term) <= 100 for term in private_terms):
            raise PrivacyError("Private name list has unsupported entries")
    anonymizer = Anonymizer(private_terms=private_terms)
    anonymizer.reserve(records)
    examples = [
        {"config": anonymizer.automation(config), "trigger_types": infer_trigger_types(config)}
        for config in records
    ]
    # Stage beside the output so both directory renames use the same filesystem.
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ha-publication-", dir=output.parent) as temporary:
        stage = Path(temporary) / "candidate"
        stage.mkdir()
        for name in ROOT_READMES:
            existing_readme = output / name
            if existing_readme.exists():
                shutil.copyfile(existing_readme, stage / name)
        write_catalogue(stage, examples)
        if policy_check(stage).blocked:
            raise PrivacyError("Generated catalogue failed the door-control policy; no output was replaced")
        changed, unresolved, _ = check_repository(stage)
        if changed or unresolved:
            raise PrivacyError("Generated catalogue failed privacy validation; no output was replaced")
        _validate_existing_output(target)
        _validate_root_readmes(output)
        output.mkdir(parents=True, exist_ok=True)
        _promote_output(stage, output)
    return len(records)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Private JSON export outside the repository")
    parser.add_argument("output", type=Path, help="Repository or public output directory")
    parser.add_argument("--private-terms-file", type=Path, help="Optional private text file outside Git, one personal name or identifying phrase per line")
    args = parser.parse_args()
    try:
        count = publish(args.source, args.output, args.private_terms_file)
    except (PrivacyError, OSError, ValueError, TypeError, RecursionError):
        print("Publication failed safely. Validate the external source, paths and generated metadata; source details suppressed.", file=sys.stderr)
        return 1
    print(f"Published {count} anonymized, named examples. Run repository checks before committing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
