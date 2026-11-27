# Configurable: action — repeating schedule · with branches

## What it does

Uses `generic.action`; 1 top-level action step(s).

- **Category:** System and scripts
- **Triggers:** Repeating schedule (1 configured trigger block(s))
- **Structure:** branches, conditions

The title describes only the behavior still identifiable in this exported template. Original trigger values, expressions and labels may already have been replaced during the earlier export. They cannot be recovered from this file. Custom action labels in this documentation describe anonymized actions, not literal service names to copy.

## How to use it

1. Read [the catalogue](../../../README.md) and [the setup guide](../../../how-to/document-an-automation.md).
2. Inspect [`automation.yaml`](automation.yaml). Reconstruct missing trigger, condition and template expressions; replacing entity IDs alone may not be enough.
3. Replace every `example_…`, `REPLACE_…`, `DEVICE_…`, `AREA_…` and other placeholder with your own local configuration. Keep credentials in your own Home Assistant `secrets.yaml`.
4. Validate the completed configuration with Home Assistant. Test it manually with a non-critical device before enabling it.

## Privacy and safety

This is a configurable example, not a ready-to-run backup. Do not commit your local credentials, identifiers, recipient names, internal addresses or completed personal configuration. Run the repository's [security checks](../../../how-to/security-and-privacy.md) before publishing changes.

The public title and summary are generated from [`metadata.json`](metadata.json), which accepts only reviewed generic concepts.
