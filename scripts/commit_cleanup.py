#!/usr/bin/env python3
"""Publish already validated cleanup without force pushes or raw command logs."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import quote


class PublishError(Exception):
    pass


def run(command: list[str], env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(command, capture_output=True, text=True, env=env, timeout=120)


def checked(command: list[str], env: dict | None = None) -> str:
    result = run(command, env)
    if result.returncode:
        raise PublishError('Cleanup publication failed; no command output is printed because it may contain private values.')
    return result.stdout.strip()


def main() -> int:
    event = os.environ.get('GITHUB_EVENT_NAME', '')
    ref = os.environ.get('GITHUB_REF', '')
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    if event != 'push' or not ref.startswith('refs/heads/'):
        raise PublishError('Only a trusted branch push can publish automatic cleanup.')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise PublishError('Repository identity is missing or invalid.')
    checked(['git', 'check-ref-format', ref])
    branch = ref.removeprefix('refs/heads/')
    checked(['git', 'add', '--all'])
    changed = run(['git', 'diff', '--cached', '--quiet'])
    if changed.returncode == 0:
        print('No automatic cleanup is needed.')
        return 0
    if changed.returncode != 1:
        raise PublishError('The cleanup diff could not be inspected.')
    checked(['git', '-c', 'user.name=github-actions[bot]',
             '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
             'commit', '-m', 'security: sanitize public examples and refresh catalogue'])
    run_id = os.environ.get('GITHUB_RUN_ID', '')
    attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '1')
    if not run_id.isdecimal() or not attempt.isdecimal():
        raise PublishError('Run identity is missing or invalid.')
    with tempfile.TemporaryDirectory(prefix='ha-cleanup-auth-') as folder:
        askpass = Path(folder) / 'askpass'
        askpass.write_text('#!/bin/sh\ncase "$1" in\n*Username*) printf "%s\\n" x-access-token ;;\n*Password*) printf "%s\\n" "$GH_TOKEN" ;;\nesac\n')
        askpass.chmod(0o700)
        env = dict(os.environ, GIT_ASKPASS=str(askpass), GIT_TERMINAL_PROMPT='0')
        pushed = run(['git', 'push', 'origin', f'HEAD:{ref}'], env)
        if pushed.returncode == 0:
            target = branch
            print('Sanitized files and the generated catalogue were committed to the source branch.')
        else:
            # Ordinary push rejection also covers a concurrently updated source branch.
            # Preserve that branch and open a reviewable cleanup PR from a unique ref.
            target = f'automation/privacy-cleanup-{run_id}-{attempt}'
            checked(['git', 'push', 'origin', f'HEAD:refs/heads/{target}'], env)
            body = (
                'Automated cleanup replaced recognized secrets and private identifiers with neutral '
                'placeholders and refreshed the catalogue. The sanitized tree passed privacy, '
                'credential, catalogue and regression checks before this commit. '
                'Direct publication to the source branch was rejected, so this PR respects its '
                'protection and any concurrent updates. Historical findings require separate review.'
            )
            result = run(['gh', 'pr', 'create', '--repo', repository,
                          '--base', branch, '--head', target,
                          '--title', 'security: apply automatic privacy cleanup', '--body', body], env)
            if result.returncode:
                print(f'Cleaned files are on branch {target}, but GitHub rejected PR creation.')
                print(f'https://github.com/{repository}/compare/{quote(branch, safe="")}...{target}?expand=1')
                print('Enable Actions pull-request creation or open the cleanup PR manually. Source cleanup remains pending.')
                return 1
            print('A cleanup pull request was opened because the source branch could not be updated directly.')
        # Token pushes do not start push checks. Explicit dispatch checks the new SHA.
        payload = json.dumps({'ref': target}).encode()
        result = subprocess.run(
            ['gh', 'api', '--method', 'POST', f'repos/{repository}/actions/workflows/security.yml/dispatches',
             '--input', '-'], input=payload, capture_output=True, env=env, timeout=120,
        )
        if result.returncode:
            print('Cleanup was published and validated here, but new-commit CI could not be dispatched. Start Security and catalogue manually.')
            return 1
        print('A verification run was requested for the published cleanup commit.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (PublishError, OSError, subprocess.SubprocessError):
        print('Automatic cleanup publication failed. No branch protections were bypassed; inspect the run configuration.')
        raise SystemExit(1)
