# Security and privacy

These are public automation **templates**. Keep private exports and a working Home Assistant configuration outside this repository. Placeholders deliberately require local configuration; they are not credentials or real device identifiers.

## What is checked and replaced

- Automation YAML is parsed with a strict loader, then checked against a finite publication policy. Entity and device IDs, custom notification destinations, custom script/REST names, mapping keys, messages, templates and unknown values become consistent neutral placeholders. Known Home Assistant services and safe schema values remain.
- Credentials, addresses, private endpoints and recognizable identifiers are checked in other text files too. Raw exports, credential files, unreviewed binaries, unsafe paths and symlinks fail closed instead of being silently published.
- Gitleaks adds its standard credential-provider rules. The current-file fixer replaces literal detected secrets and scans the result again. Ambiguous or encoded findings require manual review.
- Catalogue metadata has a finite vocabulary. The checker verifies names, categories, unique entries, aliases, per-example documentation and the generated README index.

This is not a universal personal-data classifier. An arbitrary person's name in prose cannot always be identified reliably. Review documentation and changes before publishing; do not add personal data to examples or their documentation.

## Local setup

Install Python 3.12 or newer, Git, and the dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

On Linux x86_64, the installer downloads the pinned official Gitleaks release and checks its SHA256:

```bash
bash scripts/install_gitleaks.sh
```

On other systems, install [Gitleaks](https://github.com/gitleaks/gitleaks#installing) for your platform and put it on `PATH`. The repository's `.tools/bin` location is also supported.

Enable the local hook in each clone:

```bash
git config core.hooksPath .githooks
```

The hook checks a temporary snapshot of the **complete Git index**, not just the current worktree. Cleaning a working file without staging that cleanup will still block the commit. Missing scanners, unresolved conflicts, symlinks and failed checks also block it. Hooks are local and can be bypassed, so CI and required branch checks remain necessary.

## Clean and check changes

```bash
python scripts/privacy_guard.py --fix
python scripts/run_gitleaks.py --mode tree --fix
python scripts/catalogue.py --write
python scripts/privacy_guard.py --check
python scripts/catalogue.py --check
python scripts/run_gitleaks.py --mode tree
python -m unittest discover -s tests -v
git add --all
```

Inspect the sanitized result before committing. The fixer never edits a running Home Assistant installation. Never add a `.gitleaksignore` file or broad scanner exclusions to suppress real findings.

## GitHub Actions

The **Security and catalogue** workflow runs on branch pushes, pull requests, manual dispatch and daily at 04:19 UTC.

| Job | Behaviour |
| --- | --- |
| Privacy, secrets and catalogue | Checks the current tree, generated documentation and regression tests with read-only permissions. |
| Credential history audit | Scans all fetched Git history; reports counts without source lines, credentials or commit identities. |
| Sanitize trusted branch changes | Runs only for a trusted branch push, replaces recognized values, regenerates the catalogue, validates the cleaned result, and commits it. |

Fork pull requests never receive the cleanup job or a write token. There is no `pull_request_target` execution of candidate code. Actions are pinned to commit SHAs; the Gitleaks download is pinned and checksum verified.

The cleanup job uses an ordinary non-force push. If protection or a concurrent change rejects it, it publishes a separate `automation/privacy-cleanup-…` branch and opens a cleanup pull request. The protected source branch changes only after that PR is merged. If GitHub disallows Actions-created PRs, the run fails visibly and provides the clean branch and compare link.

GitHub token pushes do not start another push workflow. The job therefore checks the sanitized result before publication and explicitly requests a verification run for the new commit. GitHub may require approval before running checks on a bot-created PR.

Enable **Allow GitHub Actions to create and approve pull requests** in the repository Actions settings if the protected-branch fallback is needed. The workflow does not approve or merge its own PRs.

To enforce the checks before merging, add these two required status checks to the existing branch ruleset after their first run:

- `Privacy, secrets and catalogue`
- `Credential history audit`

A failing workflow by itself does not prevent a maintainer from merging unless branch rules require that check. Existing review requirements are respected.

## Already published information

A cleanup commit changes current files. It does **not** erase earlier commits, branches, pull-request diffs, clones or caches. Anything pushed to a public branch may be exposed before Actions runs. The external-source publisher and local hook provide the earlier checks.

If a real credential was published, revoke or rotate it first. Historical cleanup requires a coordinated review of all affected references and, where appropriate, GitHub support. This pipeline never force-pushes or rewrites history automatically. A historical credential finding remains a failed audit until addressed; it is not hidden by a baseline.

Scanner reports and raw scanner output stay in temporary private files and are deleted. No raw finding artifacts, matched values, source lines or Git author/email metadata are uploaded or printed.

References: [Gitleaks](https://github.com/gitleaks/gitleaks), [GitHub workflow triggering](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow), [removing sensitive repository data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
