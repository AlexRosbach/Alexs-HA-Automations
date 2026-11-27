# Combine several functions · with a delay in the routine

**English** · [Deutsch](README.de.md)

[More routines and device actions](../../../README.md#system) → [Device functions and buttons](../../../README.md#system-device-controls)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Select a device option → pause for not available → Run a device function by pressing a button. Includes condition checks before the actions.

## What starts it?

- **1.** Trigger type missing: `binary_sensor.example_23`; from state: not available; to state: not available

## What must be true first?

Before the actions run: all of: condition type missing: `binary_sensor.example_02`; state: not available.

## Actual flow

1. Select a device option — `select.example_03`; selected option: not available.

2. Pause for not available.

3. Run a device function by pressing a button — `button.example_07`.

## If it triggers again

`restart`: A new trigger stops the current run and starts it again, provided the automation's conditions pass.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A device function that Home Assistant provides as a button.
- A device with an option you can select in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
