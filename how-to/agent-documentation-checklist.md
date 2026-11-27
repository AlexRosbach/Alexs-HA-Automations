# Agent checklist for publishing automations

Use this checklist for every automation. Do not skip an item because a value appears generic.

1. Work from a private source export; never commit it.
2. Give the published example a neutral sequential directory name (`automation-NNN`).
3. Remove the original automation `id` and replace the alias and description with neutral text.
4. Replace every entity/device/area/floor/config-entry/person/user ID consistently with placeholders.
5. Remove or replace addresses, URLs, hostnames, IP/MAC addresses, webhook paths, tokens, credentials, email addresses, phone numbers, notification destinations, and free-text labels.
6. Preserve only generic Home Assistant concepts (triggers, conditions, services, modes, delays) and document any placeholders.
7. Create a short `README.md` using the required sections from the documentation guide.
8. Validate YAML syntax and scan all generated text for likely identifiers or secrets.
9. Ask for review if an expression cannot be safely anonymized without changing its behaviour.

An automation is publishable only if someone outside the author’s household can understand it and cannot infer private people, rooms, devices, schedules, addresses, or identifiers from it.
