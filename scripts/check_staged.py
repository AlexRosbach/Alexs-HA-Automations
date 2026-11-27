#!/usr/bin/env python3
"""Check the complete Git index, including changes hidden by a clean worktree."""
from __future__ import annotations

from pathlib import Path
import os
import subprocess
import sys
import tempfile


class IndexErrorSafe(Exception):
    pass


def export_index(root: Path, destination: Path) -> None:
    listing = subprocess.run(
        ['git', '-C', str(root), 'ls-files', '--stage', '-z'],
        capture_output=True, check=True,
    ).stdout
    for entry in listing.split(b'\0'):
        if not entry:
            continue
        header, name = entry.split(b'\t', 1)
        mode, object_id, stage = header.split()
        if stage != b'0' or mode not in (b'100644', b'100755'):
            raise IndexErrorSafe('Resolve conflicts and remove symlinks/submodules before committing.')
        relative = Path(name.decode('utf-8'))
        if relative.is_absolute() or any(p in ('..', '.git') for p in relative.parts):
            raise IndexErrorSafe('The staged tree contains an unsafe path.')
        path = destination / relative
        if not path.resolve().is_relative_to(destination.resolve()):
            raise IndexErrorSafe('The staged tree contains an unsafe path.')
        contents = subprocess.run(
            ['git', '-C', str(root), 'cat-file', 'blob', object_id.decode('ascii')],
            capture_output=True, check=True,
        ).stdout
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    environment = dict(os.environ)
    environment['PATH'] = str(root / '.tools' / 'bin') + os.pathsep + environment.get('PATH', '')
    with tempfile.TemporaryDirectory(prefix='ha-staged-check-') as folder:
        snapshot = Path(folder)
        try:
            export_index(root, snapshot)
            checks = [
                ('privacy_guard.py', ['--check']),
                ('catalogue.py', ['--check']),
                ('run_gitleaks.py', ['--mode', 'tree']),
            ]
            for name, args in checks:
                # Run trusted local tools against index content, never worktree content.
                command = [sys.executable, str(root / 'scripts' / name),
                           '--root', str(snapshot), *args]
                result = subprocess.run(command, cwd=root, env=environment)
                if result.returncode:
                    print('Commit blocked. Clean the files, regenerate the catalogue, and stage the fixes.')
                    return result.returncode
        except (IndexErrorSafe, OSError, UnicodeError, subprocess.SubprocessError):
            print('The staged repository could not be checked safely; commit blocked.')
            return 2
    print('Staged privacy, catalogue, and credential checks passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
