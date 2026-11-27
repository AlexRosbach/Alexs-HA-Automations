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

Use lowercase English kebab-case. Never derive names from people, private room labels, device models, addresses, original aliases or numbered export positions. A name must describe behavior visible in the shared configuration; do not guess the original purpose when the export has removed it.

## Required files

Each example directory contains exactly these four files:

- `automation.yaml`: sanitized configuration with readable neutral references and placeholders where needed.
- `metadata.json`: structured catalogue metadata from the reviewed vocabulary.
- `README.md`: generated English explanation and setup instructions (the main version).
- `README.de.md`: matching German explanation and setup instructions.

Metadata has no free-text title or summary. Its fields are `schema_version`, `category`, `slug`, `trigger_types`, `actions`, `features`, `trigger_count`, `action_count` and `variant`. The generator derives stable English and German titles from these concepts. Concrete summaries and detailed explanations come from the retained YAML configuration through `scripts/automation_details.py`. A custom service is represented internally by a generic concept such as `script.call`; public descriptions explain that it calls a separately configured script rather than presenting this concept as an executable service.

The YAML alias and description must match the canonical values from `render_alias()` and `render_description()`. These stable technical labels are separate from the beginner-facing documentation in both languages, so improving the wording does not change the automation files. For programmatic imports, use `write_catalogue(root, examples)` from `scripts/catalogue.py`, where each example contains a sanitized `config` mapping and optional generic `trigger_types`.

Run `python scripts/catalogue.py --write` after changes, followed by `python scripts/catalogue.py --check`. The command updates both language versions together. The check rejects missing translations, stale generated documentation, malformed metadata, unexpected files, symlinks and names that do not follow the metadata.

## What the README explains

This repository showcases Alex's own Home Assistant automations, shared as inspiration for other users. Describe the shared, sanitized examples in that context. Explain the idea clearly and what readers need to adapt; do not present the collection as a ready-to-install product.

Every example README explains:

1. **What does this example do?**: a concrete summary of the retained behavior, including useful settings rather than only the action category.
2. **What starts it?**: the actual triggers and values that remain. Say explicitly when a trigger type, state or time was removed.
3. **What must be true first?**: top-level conditions, distinct from checks inside an action sequence.
4. **Actual flow**: the ordered actions, branches, waits, delays, timeouts, repetitions and parallel paths visible in the YAML.
5. **If it triggers again**: how the configured run mode handles another trigger.
6. **What do I need?**: suitable devices and any locally configured helpers or scripts.
7. **What do I need to change?**: the required local settings and a link to the [beginner guide](get-started.md).

English is the default for the root README, example READMEs and beginner guide. Provide the matching German version in `README.de.md` and `get-started.de.md`, with a language switch near the top of each page. Keep the same examples, task groups and navigation anchors in both catalogues. Links should stay in the chosen language; label English-only contributor guides as English when linking from German pages.

Keep contributor commands, metadata details and pipeline configuration out of the primary reader journey. Explain necessary terms with an example. Use the YAML structure for ordering: a delay inside a branch does not delay an unrelated earlier action, and parallel paths have no fixed execution order. In catalogue summaries, identify selected steps as selected rather than implying they are the complete sequence. The catalogue must continue to link all examples, even when category sections are collapsed for readability.

Group the reader-facing catalogue by area and task, such as lighting followed by switching on, switching off or toggling. Derive task groups from reviewed action metadata; do not invent private-room or household-use categories. Provide stable navigation anchors and a breadcrumb in each example. Every example must appear in exactly one task group.

The original export replaced some trigger types, conditions, state values and templates. A syntactically valid YAML file is therefore not evidence of a working Home Assistant automation. Clearly document that configuration or reconstruction remains necessary.

## Anonymization and publication

Start from a private source export outside the repository. Apply the [publication and security checks](security-and-privacy.md) before committing output.

**Remove whole automations that control doors or locks before anonymization.** Mixed routines are excluded as a whole. Cover actuation without enough information to rule out door or gate control is excluded too. Do not publish a renamed or partly deleted version of an excluded routine.

Keep ordinary notification messages, numeric values, schedules and safe template logic. Use readable neutral entity names when the function is clear. Replace only identifying parts of references and update their occurrences consistently, including references inside expressions. A neutral name is useful; a person's name or phone model is not.

Clean credentials, private endpoints, addresses, device and account IDs, notification recipients, identifying custom-service components and private text. Use placeholders where a meaningful neutral value cannot be retained. Real credentials belong in the user's local `secrets.yaml`.

Older examples already contain removed information. Do not turn `REPLACE_…` into guessed messages, formulas or household stories. To recover those details, work from the original private export, apply the current checks, and regenerate the documentation.

Check the entire pending change, including filenames, retained messages and documentation. Automatic checks cannot classify every private fact in arbitrary prose. Cleanup and exclusion affect current output; they do not remove earlier versions from Git history.
