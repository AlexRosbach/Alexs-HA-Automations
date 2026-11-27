# How to document an automation

## Descriptive names

Publish each example at `automations/<category>/<trigger>-<target>-<action>[-<qualifier>]/`.

| Part | Convention | Example |
| --- | --- | --- |
| Category | Reviewed generic function | `lighting`, `climate`, `switches`, `tasks` |
| Trigger | Generic trigger type | `state`, `threshold`, `scheduled`, `device` |
| Target and action | Public Home Assistant concept | `light-toggle`, `switch-on-off` |
| Qualifier | Identifiable control structure, when relevant | `with-wait`, `with-delay`, `with-branches` |
| Variant | Stable short fingerprint only when behavior names collide | Generated automatically |

Use lowercase English kebab-case. Never derive names from people, rooms, real devices, addresses, original aliases or numbered export positions. A name must describe behavior visible in the public template; do not guess the original purpose when the export has removed it.

## Required files

Each example directory contains exactly these three files:

- `automation.yaml`: public example configuration with placeholders.
- `metadata.json`: structured catalogue metadata from the reviewed vocabulary.
- `README.md`: generated explanation and setup instructions.

Metadata has no free-text title or summary. Its fields are `schema_version`, `category`, `slug`, `trigger_types`, `actions`, `features`, `trigger_count`, `action_count` and `variant`. The generator derives the title and explanation from those concepts. A custom service is represented as a generic catalogue concept such as `script.call`; documentation renders it as `script.custom_action`, which is not an executable service name.

The YAML alias and description must match the generated title and description. For programmatic imports, use `write_catalogue(root, examples)` from `scripts/catalogue.py`, where each example contains a sanitized `config` mapping and optional generic `trigger_types`.

Run `python scripts/catalogue.py --write` after changes, followed by `python scripts/catalogue.py --check`. The check rejects stale generated documentation, malformed metadata, unexpected files, symlinks and names that do not follow the metadata.

## What the README explains

Every example README contains:

1. **What it does**: identifiable service actions, generic trigger types and control structure.
2. **How to use it**: placeholder replacement, reconstruction of missing expressions, local validation and a safe test.
3. **Privacy and safety**: what must stay private and how to run the repository checks.

The original export replaced some trigger types, conditions, state values and templates. A syntactically valid YAML file is therefore not evidence of a working Home Assistant automation. Clearly document that configuration or reconstruction remains necessary.

## Anonymization and publication

Start from a private source export outside the repository. Use the publishing tool and [security workflow](security-and-privacy.md) before committing any output.

Remove or consistently replace:

- Original entity, device, area, floor, config-entry, person, user and automation identifiers.
- Custom script/service names, notification recipients, variable or dictionary keys that identify the installation, and household labels.
- URLs, IP/MAC addresses, hostnames, email addresses, phone numbers, webhooks, passwords, tokens and keys.
- Private text, exact personal schedules or coordinates, and private content inside templates and metadata.

Use neutral placeholders such as `light.example_01`, `DEVICE_01`, `AREA_01`, `REPLACE_WITH_YOUR_OWN_TEXT` and `REPLACE_WITH_YOUR_OWN_SECRET`. Real credentials belong in the user's local `secrets.yaml`.

Check the entire pending change before publication, including filenames and documentation. Known patterns can be cleaned automatically; unusual prose and unknown formats need review. A cleanup commit does not remove already published values from Git history.
