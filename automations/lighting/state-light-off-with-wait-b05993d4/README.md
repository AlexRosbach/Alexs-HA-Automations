# Turn off lights · with a wait condition in the routine — Variant C

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn off](../../../README.md#lighting-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Pause for 30 min → wait for one of 2 triggers (continue on timeout) → use the first matching branch: Turn off lights → Run your own script → 3 more steps / Action type not available → Send a message to your own notification destination; otherwise: Action type not available → Send a message to your own notification destination → 3 more steps (selected steps; 4 other actions omitted).

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `person.example_01`; to state: not available
- **2.** Trigger type missing: `person.example_02`; to state: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Pause for 30 min.

2. Check condition type missing: `person.example_01`; state: not available. If false, stop the current sequence here.

3. Check condition type missing: `person.example_02`; state: not available. If false, stop the current sequence here.

4. Action type not available; message text: not available; message title: not available.

5. Send a message to your own notification destination — `notify.example_04`; message text: not available; message title: not available.

6. Wait for one of these triggers:

   - Trigger type missing: event name: not available
   - Trigger type missing: event name: not available

   Time limit: not available. Continue with the next step when the timeout expires.

7. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: formula: not available

   1. Turn off lights — `light.example_13`, `light.example_14`, `light.example_10`, `light.example_12`, `light.example_06`, `light.example_01`, `light.example_11`.

   2. Run your own script — `script.led_aus`; configured to continue after supported action errors.

   3. Turn off a switch — `switch.example_08`.

   4. Action type not available; message text: not available.

   5. Send a message to your own notification destination — `notify.example_04`; message text: not available.

   **Branch 2:** all of: condition type missing: formula: not available

   1. Action type not available; message text: not available.

   2. Send a message to your own notification destination — `notify.example_04`; message text: not available.

   **If no branch matches:**

   1. Action type not available; message text: not available.

   2. Send a message to your own notification destination — `notify.example_04`; message text: not available.

   3. Turn off lights — `light.example_13`, `light.example_14`, `light.example_10`, `light.example_12`, `light.example_01`, `light.example_11`.

   4. Run your own script — `script.led_aus`; configured to continue after supported action errors.

   5. Turn off a switch — `switch.example_04`, `switch.example_08`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.
- A configured notification destination, such as the Home Assistant app.
- An existing Home Assistant script: a saved sequence of actions.
- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
