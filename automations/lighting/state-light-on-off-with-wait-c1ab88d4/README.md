# Turn lights on and off · with a wait condition in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on and off](../../../README.md#lighting-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for one of 2 triggers (stop on timeout) → use the first matching branch: if the configured conditions pass: (Turn on a switch) → Turn off lights; transition: 2 s → 4 more steps / Action type not available → Send a message to your own notification destination → 1 more step (selected steps; 3 other actions omitted). Start settings: held for 10 s. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `media_player.example_04`; from state: not available; to state: not available; held for 10 s
- **2.** Trigger type missing: `media_player.example_04`; from state: not available; to state: not available; held for 10 s
- **3.** Trigger type missing: `remote.example_01`; from state: not available; to state: not available; held for 10 s

## What must be true first?

Before the actions run: all of: condition type missing: `media_player.example_04`; state: not available.

## Actual flow

1. Prepare 6 intermediate values; their contents/formulas are not described.

2. Action type not available; message text: not available; message title: not available.

3. Send a message to your own notification destination — `notify.example_04`; message text: not available; message title: not available.

4. Wait for one of these triggers:

   - Trigger type missing: event name: not available
   - Trigger type missing: event name: not available

   Time limit: not available. Stop this sequence when the timeout expires.

5. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: formula: not available

   1. If all of: condition type missing: `binary_sensor.example_08`; state: not available:

      **Then:**

      1. Turn on a switch — `switch.example_06`.

   2. Turn off lights — `light.example_13`; transition: 2 s.

   3. Turn on lights — `light.example_14`; brightness: 10%; transition: 2 s; colour temperature: 2202 K.

   4. Action type not available; message text: not available; message title: not available.

   5. Send a message to your own notification destination — `notify.example_04`; message text: not available; message title: not available.

   6. Pause for not available.

   **Branch 2:** all of: condition type missing: formula: not available

   1. Action type not available; message text: not available; message title: not available.

   2. Send a message to your own notification destination — `notify.example_04`; message text: not available; message title: not available.

   3. Pause for not available.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.
- A configured notification destination, such as the Home Assistant app.
- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
