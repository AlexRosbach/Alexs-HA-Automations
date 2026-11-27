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
MANAGED_FILES = frozenset(("automation.yaml", "README.md", "metadata.json"))


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
        load_entries(target.parent)
    except (ValueError, OSError, TypeError, KeyError):
        raise PrivacyError("Existing output is not a managed catalogue; no files were replaced") from None


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


def publish(source: Path, output: Path) -> int:
    from catalogue import infer_trigger_types, write_catalogue

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
    records = _source_records(source)
    anonymizer = Anonymizer()
    for config in records:
        anonymizer.reserve(config)
    examples = [
        {"config": anonymizer.automation(config), "trigger_types": infer_trigger_types(config)}
        for config in records
    ]
    # Stage beside the output so both directory renames use the same filesystem.
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ha-publication-", dir=output.parent) as temporary:
        stage = Path(temporary) / "candidate"
        stage.mkdir()
        existing_readme = output / "README.md"
        if existing_readme.exists():
            _no_symlinks(existing_readme)
            shutil.copyfile(existing_readme, stage / "README.md")
        write_catalogue(stage, examples)
        changed, unresolved, _ = check_repository(stage)
        if changed or unresolved:
            raise PrivacyError("Generated catalogue failed privacy validation; no output was replaced")
        _validate_existing_output(target)
        output.mkdir(parents=True, exist_ok=True)
        backup = Path(temporary) / "previous-automations"
        replaced = False
        try:
            if target.exists():
                os.replace(target, backup)
            os.replace(stage / "automations", target)
            replaced = True
            if (stage / "README.md").exists():
                os.replace(stage / "README.md", existing_readme)
        except OSError:
            if replaced:
                os.replace(target, stage / "automations")
            if backup.exists():
                os.replace(backup, target)
            raise PrivacyError("Could not publish catalogue; previous automation output restored") from None
    return len(records)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Private JSON export outside the repository")
    parser.add_argument("output", type=Path, help="Repository or public output directory")
    args = parser.parse_args()
    try:
        count = publish(args.source, args.output)
    except (PrivacyError, OSError, ValueError, TypeError, RecursionError):
        print("Publication failed safely. Validate the external source, paths and generated metadata; source details suppressed.", file=sys.stderr)
        return 1
    print(f"Published {count} anonymized, named examples. Run repository checks before committing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
