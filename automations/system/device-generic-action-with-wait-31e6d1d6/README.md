# Set up your own action · with a wait condition in the routine — Variant A

**English** · [Deutsch](README.de.md)

[More routines and device actions](../../../README.md#system) → [Actions to set up](../../../README.md#system-unfinished)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

If the configured conditions pass: (if below 10: (Action type not available → wait for another trigger (up to 1 min; continue on timeout) → 1 more step)).

## What starts it?

- **1.** Trigger type missing: `ENTITY_38`, `DEVICE_46`; device event/action: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. If all of: condition type missing: `ENTITY_38`, `DEVICE_46`; device event/action: not available:

   **Then:**

   1. If all of: condition type missing: `sensor.example_05`; below 10:

      **Then:**

      1. Action type not available — `ENTITY_39`, `DEVICE_47`.

      2. Wait for one of these triggers:

         - Trigger type missing: `binary_sensor.example_21`; from state: not available; to state: not available

         Time limit: 1 min. Continue with the next step when the timeout expires.

      3. Action type not available — `ENTITY_39`, `DEVICE_47`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- The devices and action you want to add yourself.
- A connected device that provides a suitable event as a trigger.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
