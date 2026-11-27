# Turn on lights · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on](../../../README.md#lighting-on)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for one of 2 triggers (stop on timeout) → use the first matching branch: Turn on lights at 100% brightness; transition: 3 s (selected steps; 2 other actions omitted).

## What starts it?

- **1.** Trigger type missing: `binary_sensor.example_16`; from state: not available; to state: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Prepare 2 intermediate values; their contents/formulas are not described.

2. Action type not available; message text: not available; message title: not available.

3. Wait for one of these triggers:

   - Trigger type missing: event name: not available
   - Trigger type missing: event name: not available

   Time limit: not available. Stop this sequence when the timeout expires.

4. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: formula: not available

   1. Turn on lights — `DEVICE_28`, `DEVICE_29`; brightness: 100%; transition: 3 s; colour values: not available.

   No default branch is configured.

## If it triggers again

`restart`: A new trigger stops the current run and starts it again, provided the automation's conditions pass.

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
