# Combine several functions · with a delay in the routine

**English** · [Deutsch](README.de.md)

[More routines and device actions](../../../README.md#system) → [Get weather data](../../../README.md#system-weather)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Get a weather forecast → check conditions; stop this sequence if false → prepare intermediate values → 3 more steps (see full flow). Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `binary_sensor.example_05`; to state: not available; held for not available
- **2.** Trigger type missing: `binary_sensor.example_06`, `binary_sensor.example_07`, `binary_sensor.example_08`, `binary_sensor.example_09`, `binary_sensor.example_10`, `binary_sensor.example_11`, `binary_sensor.example_12`, `binary_sensor.example_13`, `binary_sensor.example_14`; to state: not available; held for not available
- **3.** Trigger type missing: `weather.example_01`; to state: not available; held for not available
- **4.** Trigger type missing: minutes: not available

## What must be true first?

Before the actions run: all of: condition type missing: formula: not available; condition type missing: `binary_sensor.example_05`; state: not available; held for not available; condition type missing: formula: not available.

## Actual flow

1. Get a weather forecast — `weather.example_01`; save the returned result for later steps.

2. Check condition type missing: formula: not available. If false, stop the current sequence here.

3. Prepare 2 intermediate values; their contents/formulas are not described.

4. Check condition type missing: formula: not available. If false, stop the current sequence here.

5. Run your own script — `script.example_03`.

6. Pause for not available.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- An existing Home Assistant script: a saved sequence of actions.
- A weather integration that provides forecasts.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
