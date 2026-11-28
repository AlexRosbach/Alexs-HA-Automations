# Turn lights on and off · with conditions in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on and off](../../../README.md#lighting-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). Start settings: Device event.

## What starts it?

- **1.** Device event: `DEVICE_15`; device event/action: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. If all of: at least one of [device check: `ENTITY_10`, `DEVICE_11`; device event/action: `is_on`; device check: `ENTITY_11`, `DEVICE_12`; device event/action: `is_on`]:

   **Then:**

   1. Turn off lights — `AREA_02`.

   **Otherwise:**

   1. Turn on lights — `AREA_02`; brightness: 70%.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.
- A connected device that provides a suitable event as a trigger.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
