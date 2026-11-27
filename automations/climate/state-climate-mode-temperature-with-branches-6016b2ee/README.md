# Adjust heating or air conditioning · with conditions in the routine — Variant C

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Heating and cooling modes](../../../README.md#climate-modes)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Set the temperature to 5 → Set the heating or cooling mode; otherwise: Set the heating or cooling mode → Set the temperature to 21. Includes condition checks before the actions.

## What starts it?

- **1.** Trigger type missing: `binary_sensor.example_06`, `binary_sensor.example_08`, `binary_sensor.example_09`, `binary_sensor.example_07`, `binary_sensor.example_10`, `binary_sensor.example_11`, `binary_sensor.example_12`; to state: not available, not available

## What must be true first?

Before the actions run: all of: condition type missing: formula: not available.

## Actual flow

The automation also prepares intermediate values; their contents/formulas are not described.

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition formula not available

   1. Set the desired room temperature — `ENTITY_45`; temperature setting (unit not given): 5.

   2. Set the heating or cooling mode — `ENTITY_45`; heating/cooling mode: not available.

   **If no branch matches:**

   1. Set the heating or cooling mode — `ENTITY_45`; heating/cooling mode: not available.

   2. Set the desired room temperature — `ENTITY_45`; temperature setting (unit not given): 21.

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
