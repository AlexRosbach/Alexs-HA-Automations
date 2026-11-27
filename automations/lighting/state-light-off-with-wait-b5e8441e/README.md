# Turn off lights · with a wait condition in the routine — Variant D

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn off](../../../README.md#lighting-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for one of 2 triggers (continue on timeout) → Turn off lights (selected steps; 9 other actions omitted). Includes condition checks before the actions.

## What starts it?

- **1.** Trigger type missing: `sensor.example_16`; to state: not available; held for not available

## What must be true first?

Before the actions run: all of: condition type missing: formula: not available; condition type missing: formula: not available.

## Actual flow

1. Store a date or time — `input_datetime.example_01`; stored time: not available.

2. Prepare 2 intermediate values; their contents/formulas are not described.

3. Action type not available; message text: not available; message title: not available.

4. Wait for one of these triggers:

   - Trigger type missing: event name: not available
   - Trigger type missing: event name: not available

   Time limit: not available. Continue with the next step when the timeout expires.

5. Action type not available; message text: not available.

6. Check condition type missing: formula: not available. If false, stop the current sequence here.

7. Check condition type missing: `sensor.example_16`; state: not available. If false, stop the current sequence here.

8. Check condition type missing: `binary_sensor.example_20`; state: not available. If false, stop the current sequence here.

9. Turn off lights — `light.example_10`, `light.example_11`, `light.example_12`, `light.example_18`, `light.example_19`, `light.example_20`.

10. Run your own script — `script.led_aus`; configured to continue after supported action errors.

11. If all of: condition type missing: `switch.example_08`; state: not available:

    **Then:**

    1. Run your own script — `script.ausschalten`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A helper that stores a date or time.
- Lights that Home Assistant can control.
- An existing Home Assistant script: a saved sequence of actions.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
