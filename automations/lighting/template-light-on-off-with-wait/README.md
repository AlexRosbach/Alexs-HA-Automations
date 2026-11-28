# Turn lights on and off · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on and off](../../../README.md#lighting-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Turn on lights → wait for a condition → Turn off lights (selected steps; 1 other action omitted). Start settings: held for 3 min. Includes condition checks before the actions.

## What starts it?

- **1.** Formula becomes true: held for 00:03:00 (time format); formula: “\{\{ states\('sensor.example\_22'\) \| lower == 'bad' \}\}”

## What must be true first?

Before the actions run: all of: state check: `input_boolean.example_13`; state: `on`; state check: `input_boolean.example_02`; state: `off`; state check: `input_boolean.example_03`; state: `off`.

## Actual flow

1. Turn on lights — `light.example_01`.

2. Wait until this formula is true: “\{\{ states\('sensor.example\_22'\) \| lower not in \['bad','unknown','unavailable','not\_home','none',''\] \}\}”.

   No timeout is configured.

3. Check state check: `input_boolean.example_03`; state: `off`. If false, stop the current sequence here.

4. Turn off lights — `light.example_01`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
