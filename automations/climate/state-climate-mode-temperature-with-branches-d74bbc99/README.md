# Adjust heating or air conditioning · with conditions in the routine — Variant D

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Heating and cooling modes](../../../README.md#climate-modes)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Set the temperature to 5 → Set the heating or cooling mode; heating/cooling mode: `off`; otherwise: Set the heating or cooling mode; heating/cooling mode: `heat_cool` → Set the temperature to 21. Start settings: to state: `on`, `off`. Includes condition checks before the actions.

## What starts it?

- **1.** State change: `binary_sensor.example_14`, `binary_sensor.example_16`, `binary_sensor.example_17`, `binary_sensor.example_15`, `binary_sensor.example_18`, `binary_sensor.example_19`, `binary_sensor.example_20`; to state: `on`, `off`

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ false \}\}”.

## Actual flow

The automation also prepares intermediate values; their contents/formulas are not described.

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: formula: “\{\{ variable\_53 \}\}”

   1. Set the desired room temperature — `ENTITY_43`; temperature setting (unit not given): 5.

   2. Set the heating or cooling mode — `ENTITY_43`; heating/cooling mode: `off`.

   **If no branch matches:**

   1. Set the heating or cooling mode — `ENTITY_43`; heating/cooling mode: `heat_cool`.

   2. Set the desired room temperature — `ENTITY_43`; temperature setting (unit not given): 21.

## If it triggers again

`queued`: New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time. Limit for running and queued runs: 10. The automation is initially disabled.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
