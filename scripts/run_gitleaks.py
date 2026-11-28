#!/usr/bin/env python3
"""Run Gitleaks without publishing secrets, source lines, or Git identities.

Reports and scanner output are confined to a private temporary directory.
The fixer replaces literal secret values only and checks its result again.
Historical findings never trigger a history rewrite.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


class ScanError(Exception):
    """A deliberately value-free error suitable for public CI logs."""


def repository_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ['git', '-C', str(root), 'rev-parse', '--show-toplevel'],
        capture_output=True, text=True,
    )
    if result.returncode == 0 and Path(result.stdout.strip()).resolve() == root:
        listing = subprocess.run(
            ['git', '-C', str(root), 'ls-files', '--cached', '--others',
             '--exclude-standard', '-z'], capture_output=True, check=True,
        ).stdout
        paths = [root / os.fsdecode(p) for p in set(listing.split(b'\0')) if p]
    else:
        paths = list(root.rglob('*'))
    files = []
    for path in paths:
        if '.git' in path.relative_to(root).parts:
            continue
        if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != root.parent):
            raise ScanError('Symlinks cannot be scanned safely.')
        if path.is_file():
            if not path.resolve().is_relative_to(root):
                raise ScanError('A scan path leaves the repository.')
            files.append(path)
    return sorted(files)


def scanner(binary: str, root: Path, target: Path, report: Path,
            mode: str, redact: bool) -> list[dict]:
    ignore_file = report.parent / 'empty-ignore'
    ignore_file.touch(mode=0o600)
    command = [binary, 'git' if mode == 'history' else 'dir', str(target),
               '--no-banner', '--no-color', '--log-level', 'error',
               '--report-format', 'json', '--report-path', str(report),
               '--gitleaks-ignore-path', str(ignore_file),
               '--ignore-gitleaks-allow', '--timeout', '240']
    config = root / '.gitleaks.toml'
    if config.is_file():
        command += ['--config', str(config)]
    if redact:
        command.append('--redact=100')
    if mode == 'history':
        command += ['--log-opts=--all --full-history']
    # No scanner output may reach Actions logs, including exceptional output.
    result = subprocess.run(command, cwd=root, capture_output=True, timeout=260)
    if result.returncode not in (0, 1):
        raise ScanError('Gitleaks could not finish. Check its installation and configuration locally.')
    if not report.is_file():
        if result.returncode == 0:
            return []
        raise ScanError('Gitleaks did not produce a usable report.')
    report.chmod(0o600)
    try:
        findings = json.loads(report.read_text()) or []
    except (ValueError, OSError):
        raise ScanError('Gitleaks returned an invalid report.') from None
    if not isinstance(findings, list) or any(not isinstance(f, dict) for f in findings):
        raise ScanError('Gitleaks returned an invalid report.')
    if result.returncode == 1 and not findings:
        raise ScanError('Gitleaks failed without usable findings.')
    return findings


def replace_findings(root: Path, snapshot: Path, findings: list[dict]) -> int:
    replacements: dict[Path, set[str]] = {}
    for finding in findings:
        reported = Path(finding.get('File', ''))
        candidate = reported if reported.is_absolute() else snapshot / reported
        try:
            relative = candidate.resolve().relative_to(snapshot.resolve())
        except ValueError:
            raise ScanError('A finding cannot be safely mapped to a repository file.') from None
        destination = root / relative
        secret = finding.get('Secret')
        if not isinstance(secret, str) or not secret or secret == 'REDACTED':
            raise ScanError('A finding needs manual review; no literal replacement is available.')
        if destination.is_symlink() or not destination.resolve().is_relative_to(root):
            raise ScanError('A finding points outside the repository.')
        replacements.setdefault(destination, set()).add(secret)
    planned: dict[Path, str] = {}
    for path, secrets in replacements.items():
        try:
            original = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError):
            raise ScanError('A finding requires manual review of a non-text file.') from None
        updated = original
        for secret in sorted(secrets, key=len, reverse=True):
            if secret not in original:
                raise ScanError('An encoded or ambiguous finding needs manual review.')
            updated = updated.replace(secret, 'REPLACE_WITH_YOUR_OWN_SECRET')
        planned[path] = updated
    for path, text in planned.items():
        path.write_text(text, encoding='utf-8')
    return len(planned)


def scan(root: Path, mode: str, fix: bool = False) -> int:
    if (root / '.gitleaksignore').exists() or (root / '.gitleaksignore').is_symlink():
        raise ScanError('Ignore files may not bypass the credential policy.')
    binary = shutil.which('gitleaks')
    if binary is None:
        local = root / '.tools' / 'bin' / 'gitleaks'
        binary = str(local) if local.is_file() else None
    if binary is None:
        raise ScanError('Gitleaks is required. Install it or run scripts/install_gitleaks.sh on Linux x86_64.')
    if fix and mode != 'tree':
        raise ScanError('Automatic replacement is available for the current tree only.')
    with tempfile.TemporaryDirectory(prefix='ha-secret-scan-') as folder:
        private = Path(folder)
        if mode == 'history':
            findings = scanner(binary, root, root, private / 'report.json', mode, True)
        else:
            snapshot = private / 'tree'
            snapshot.mkdir(mode=0o700)
            for path in repository_files(root):
                copy = snapshot / path.relative_to(root)
                copy.parent.mkdir(parents=True, exist_ok=True)
                copy.write_bytes(path.read_bytes())
            findings = scanner(binary, root, snapshot, private / 'report.json', mode, not fix)
            if findings and fix:
                count = replace_findings(root, snapshot, findings)
                print(f'Replaced literal credential values in {count} file(s); checking again.')
                return scan(root, 'tree')
        if findings:
            scope = 'Git history' if mode == 'history' else 'current files'
            print(f'Credential scan failed: {len(findings)} finding(s) in {scope}. Values are withheld.')
            if mode == 'history':
                print('Current-file cleanup cannot erase history. Rotate exposed credentials and review history cleanup.')
            return 1
    print(f'Credential scan passed ({mode}).')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--mode', choices=('tree', 'history'), default='tree')
    parser.add_argument('--fix', action='store_true')
    args = parser.parse_args()
    try:
        return scan(args.root.resolve(), args.mode, args.fix)
    except ScanError as error:
        print(str(error))
        return 2
    except (OSError, subprocess.SubprocessError):
        # Exception strings from subprocess/filesystem APIs may contain secrets.
        print('Credential scan could not complete safely. Install Gitleaks and inspect the configuration locally.')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
