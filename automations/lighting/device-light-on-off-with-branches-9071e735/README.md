# Turn lights on and off · with conditions in the routine — Variant C

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on and off](../../../README.md#lighting-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

If the configured conditions pass: (use the first matching branch: Turn on lights at 86% brightness; transition: 1 s; colour temperature: 4000 K → Run your own script / Turn off lights; transition: 2 s → Run your own script) → use the first matching branch: Turn on a fan / Turn off a fan. Start settings: Device event.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Device event: `ENTITY_33`, `DEVICE_42`; device event/action: `occupied`
- **2.** Device event: `ENTITY_33`, `DEVICE_42`; device event/action: `not_occupied`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. If all of: device check: `ENTITY_14`, `DEVICE_16`; device event/action: `is_off`:

   **Then:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: device check: `ENTITY_33`, `DEVICE_42`; device event/action: not available

      1. Turn on lights — `light.example_10`, `light.example_11`, `light.example_12`; brightness: 86%; transition: 1 s; colour temperature: 4000 K.

      2. Run your own script — `script.example_06`; configured to continue after supported action errors.

      **Branch 2:** all of: device check: `ENTITY_33`, `DEVICE_42`; device event/action: not available

      1. Turn off lights — `light.example_10`, `light.example_11`, `light.example_12`; transition: 2 s.

      2. Run your own script — `script.example_07`; configured to continue after supported action errors.

      No default branch is configured.

2. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: device check: `ENTITY_33`, `DEVICE_42`; device event/action: not available

   1. Turn on a fan — `DEVICE_43`.

   **Branch 2:** all of: device check: `ENTITY_33`, `DEVICE_42`; device event/action: not available

   1. Turn off a fan — `DEVICE_43`.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A fan or air purifier that Home Assistant can control.
- Lights that Home Assistant can control.
- An existing Home Assistant script: a saved sequence of actions.
- A connected device that provides a suitable event as a trigger.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
