# Home Assistant automation examples

This repository is a public, privacy-safe catalogue of Home Assistant automation examples.

**Catalogue build:** `20261127.0001`

- Each directory under [`automations/`](automations/) is self-contained.
- Every example uses placeholders instead of real entity IDs, device IDs, areas, names, URLs, notification targets, and credentials.
- Start with [the documentation guide](how-to/document-an-automation.md) before adding an automation.
- Agents should follow [the agent checklist](how-to/agent-documentation-checklist.md) without exception.

## Use an example

1. Choose an automation directory.
2. Read its `README.md` completely.
3. Replace every placeholder in `automation.yaml` with values from your own Home Assistant instance.
4. Validate the YAML and test it with a non-critical device before enabling it.

Never copy credentials, internal addresses, entity registries, device registries, or full Home Assistant backups into this repository.
