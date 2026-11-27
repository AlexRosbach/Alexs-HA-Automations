# How to document an automation

Each published automation must live in `automations/automation-NNN/` and contain exactly these public-facing files:

```text
automation-NNN/
├── automation.yaml
└── README.md
```

## Required README sections

1. **What it does** — plain language, one short paragraph.
2. **How to use it** — exact setup steps, prerequisites, and safe test steps.
3. **Privacy and safety** — which placeholders must be replaced and what not to publish.

Write for a Home Assistant user who does not know the author’s home or hardware. Explain terms briefly and never rely on screenshots containing personal data.

## Anonymization rules

Before publishing, replace or remove:

- entity, device, area, floor, config-entry, user, person, and automation IDs;
- names of people, rooms, addresses, Wi-Fi networks, pets, routines, companies, and household-specific labels;
- URLs, IP/MAC addresses, hostnames, email addresses, phone numbers, webhooks, tokens, passwords, and keys;
- notification recipients and message text that reveals private context.

Use clear neutral placeholders such as `light.example_01`, `DEVICE_01`, `AREA_01`, `REPLACE_WITH_YOUR_OWN_TEXT`, and `REPLACE_WITH_YOUR_OWN_SECRET`. If a user needs a Home Assistant `!secret`, they should define it in their own `secrets.yaml` and replace the placeholder locally.

## Review before merge

Search the complete change for identifiers and secrets. A reviewer must confirm that the YAML is functional only after the user supplies their own values, and that the README explains every placeholder.
