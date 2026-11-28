# Security and privacy

Alex shares automations from his own Home Assistant setup so other users can understand the ideas and adapt them. The English `README.md` is the main entry; `README.de.md` contains the matching German version. Keep private exports and your working Home Assistant configuration outside this repository.

## What is kept, cleaned and excluded

- Keep useful automation behavior: ordinary notification text, numeric settings, times, trigger and condition types, and template expressions that pass the privacy checks. A message such as “The washing machine has finished” does not need to become a text placeholder.
- Entity and custom action references may use readable neutral names, such as `light.main` or `notify.phone_notification`. The sanitizer removes private name and phone-model components, keeps recognized functional words and consistently updates references inside expressions. Device, area and other identifying IDs still use placeholders.
- Replace credentials, personal identifiers, addresses and private endpoints. Check other text files as well as YAML. Raw exports, credential files, unreviewed binaries, unsafe paths and symlinks fail closed.
- **Exclude door and lock control completely.** Remove the whole automation, including mixed routines containing an excluded action. Cover actuation whose door or gate purpose cannot be ruled out is excluded too. Run this policy before anonymization so identifying labels cannot hide the excluded function.
- Gitleaks adds credential-provider rules. Its current-file fixer replaces literal detected secrets and scans again. Ambiguous or encoded findings require review.
- Catalogue checks verify the finite metadata vocabulary, names, categories, unique entries, canonical aliases and both language versions. Descriptions use the actual retained configuration: triggers, conditions, action order, settings, waits and repeat-run behavior.

Normal text and logic are not blanket-replaced in new exports. Existing examples already lost some trigger types, conditions, messages and formulas during an earlier export. The checks cannot recover those values: restoring them requires the original private source. Documentation must say which details are missing rather than inventing them.

The checks do not recognize every possible person's name or private fact in free text. Review retained messages, expressions and documentation before publication. Known patterns and identifying parts found in configuration references can be cleaned automatically; unfamiliar personal details still need review.

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

The hook checks the door-control policy, privacy, catalogue and credentials against a temporary snapshot of the **complete Git index**, not just the current worktree. Cleaning a working file without staging that cleanup will still block the commit. Missing scanners, unresolved conflicts, symlinks and failed checks also block it. Hooks are local and can be bypassed, so CI and required branch checks remain necessary.

## Publish from an original export

The publisher filters door-control routines from the external source before anonymization and checks the generated output again. It preserves ordinary messages and functional settings while replacing identifying references.

```bash
python scripts/publish_automations.py /path/outside-repo/private-input.json .
```

For personal names or identifying phrases that occur only in prose, supply a private text file with one term per line:

```bash
python scripts/publish_automations.py /path/outside-repo/private-input.json . --private-terms-file /path/outside-repo/private-names.txt
```

Keep that list outside Git. Its contents are applied locally and are not copied into the generated repository. The publisher rejects a source containing no allowed routines and leaves the existing output intact.

## Clean and check changes

```bash
python scripts/publication_policy.py --fix
python scripts/privacy_guard.py --fix
python scripts/run_gitleaks.py --mode tree --fix
python scripts/catalogue.py --write
python scripts/publication_policy.py --check
python scripts/privacy_guard.py --check
python scripts/catalogue.py --check
python scripts/run_gitleaks.py --mode tree
python -m unittest discover -s tests -v
git add --all
```

The publication-policy fixer deletes entire excluded example folders. It runs first; after sanitizing and regenerating documentation, the policy is checked again. Inspect the result before committing. The fixer never edits a running Home Assistant installation. Never add a `.gitleaksignore` file or broad scanner exclusions to suppress real findings.

## GitHub Actions

The **Security and catalogue** workflow runs on all branch pushes and all pull requests, without path or target-branch filters, plus manual dispatch and daily at 04:19 UTC.

Pull-request checks run when a PR is opened, receives new commits, is reopened, has its title/body/base branch edited, becomes ready for review, or returns to draft. These are the explicit `opened`, `synchronize`, `reopened`, `edited`, `ready_for_review` and `converted_to_draft` events.

| Job | Behaviour |
| --- | --- |
| Privacy, secrets and catalogue | Checks the door-control exclusion policy, privacy, credentials, generated English/German documentation and regression tests with read-only permissions. |
| Credential history audit | Scans all fetched Git history; reports counts without source lines, credentials or commit identities. |
| Sanitize trusted branch changes | Runs only for a trusted branch push. Excludes whole door-control automations first, cleans private values and credentials, regenerates both catalogues, checks the result again, and commits it. |

Fork pull requests never receive the cleanup job or a write token. There is no `pull_request_target` execution of candidate code. Actions are pinned to commit SHAs; the Gitleaks download is pinned and checksum verified.

The cleanup job uses an ordinary non-force push. If protection or a concurrent change rejects it, it publishes a separate `automation/privacy-cleanup-…` branch and opens a cleanup pull request. The protected source branch changes only after that PR is merged. If GitHub disallows Actions-created PRs, the run fails visibly and provides the clean branch and compare link.

GitHub token pushes do not start another push workflow. The job therefore checks the sanitized result before publication and explicitly requests a verification run for the new commit. GitHub may require approval before running checks on a bot-created PR.

Enable **Allow GitHub Actions to create and approve pull requests** in the repository Actions settings if the protected-branch fallback is needed. The workflow does not approve or merge its own PRs.

To enforce the checks before merging, add these two required status checks to the existing branch ruleset after their first run:

- `Privacy, secrets and catalogue`
- `Credential history audit`

A failing workflow by itself does not prevent a maintainer from merging unless branch rules require that check. Existing review requirements are respected.

## Already published information

A cleanup commit changes current files. It does **not** erase earlier commits, branches, pull-request diffs, clones or caches. This also applies to removed door-control examples. Anything pushed to a public branch may be exposed before Actions runs. The external-source publisher and local hook provide the earlier checks.

If a real credential was published, revoke or rotate it first. Historical cleanup requires a coordinated review of all affected references and, where appropriate, GitHub support. This pipeline never force-pushes or rewrites history automatically. A historical credential finding remains a failed audit until addressed; it is not hidden by a baseline.

Scanner reports and raw scanner output stay in temporary private files and are deleted. No raw finding artifacts, matched values, source lines or Git author/email metadata are uploaded or printed.

References: [Gitleaks](https://github.com/gitleaks/gitleaks), [GitHub workflow triggering](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow), [removing sensitive repository data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
