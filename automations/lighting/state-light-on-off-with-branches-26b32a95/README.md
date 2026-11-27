# Turn lights on and off · with conditions in the routine — Variant A

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on and off](../../../README.md#lighting-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

If the configured conditions pass: (Turn on lights at 70% brightness → if the configured conditions pass: (Turn on lights at 100% brightness; transition: 3 s)); otherwise: (Turn off lights → if the configured conditions pass: (Turn on lights at 10% brightness; transition: 30 s); otherwise: (Turn off lights; transition: 5 s)).

## What starts it?

- **1.** Trigger type missing: `binary_sensor.example_02`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. If all of: condition type missing: `ENTITY_08`, `DEVICE_09`; device event/action: not available; condition type missing: `ENTITY_09`, `DEVICE_09`; below 1998; device event/action: not available:

   **Then:**

   1. Turn on lights — `light.example_04`, `light.example_05`; brightness: 70%.

   2. If all of: condition type missing: `input_boolean.example_02`; state: not available:

      **Then:**

      1. Turn on lights — `light.example_06`; brightness: 100%; transition: 3 s.

   **Otherwise:**

   1. Turn off lights — `AREA_02`.

   2. If all of: condition type missing: `input_boolean.example_02`; state: not available:

      **Then:**

      1. Turn on lights — `light.example_07`; brightness: 10%; transition: 30 s.

      **Otherwise:**

      1. Turn off lights — `light.example_07`; transition: 5 s.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
