# Set the desired room temperature · with conditions in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Store some text → if the configured conditions pass: (Store some text → Store a number → 2 more steps). Includes condition checks before the actions.

## What starts it?

- **1.** Trigger type missing: at not available

## What must be true first?

Before the actions run: all of: condition type missing: weekdays: not available, not available, not available, not available, not available; condition type missing: `person.example_02`; state: not available; condition type missing: `sensor.example_16`; state: not available; held for not available; condition type missing: formula: not available; condition type missing: formula: not available.

## Actual flow

1. Store some text — `input_text.example_02`; stored value: not available.

2. If all of: condition type missing: `binary_sensor.example_07`; state: not available; condition type missing: formula: not available; condition type missing: formula: not available:

   **Then:**

   1. Store some text — `input_text.example_03`; stored value: not available.

   2. Store a number — `input_number.example_01`; stored value: not available.

   3. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 21; heating/cooling mode: not available.

   4. Turn on a stored on/off value — `input_boolean.example_14`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A toggle helper: an on/off value stored in Home Assistant.
- A helper that stores a number.
- A helper that stores text.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
