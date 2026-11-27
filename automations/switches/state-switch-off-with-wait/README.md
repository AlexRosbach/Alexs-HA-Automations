# Turn off a switch · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn off](../../../README.md#switches-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for a value above 7.999 or 5 other triggers (continue on timeout) → if the configured conditions pass: (Turn off a switch) (selected steps; 2 other actions omitted). Includes condition checks before the actions.

## What starts it?

- **1.** Trigger type missing: `sensor.example_18`; from state: not available, not available; to state: not available; held for not available

## What must be true first?

Before the actions run: all of: condition type missing: `switch.example_15`; state: not available; held for not available; condition type missing: `script.example_01`; state: not available; condition type missing: `automation.example_06`; below 1; attribute name: not available.

## Actual flow

1. If all of: condition type missing: nested tests; connecting rule missing [condition type missing: `sensor.example_19`; above -0.001; below 8]:

   **Then:**

   1. Wait for one of these triggers:

      - Trigger type missing: `sensor.example_19`; below 8
      - Trigger type missing: `sensor.example_18`; to state: not available
      - Trigger type missing: `switch.example_15`; to state: not available

      Time limit: not available. Continue with the next step when the timeout expires.

2. Check condition type missing: nested tests; connecting rule missing [condition type missing: `switch.example_15`; state: not available; held for not available; condition type missing: `script.example_01`; state: not available; condition type missing: `sensor.example_18`; state: not available; held for not available; condition type missing: `automation.example_06`; below 1; attribute name: not available; condition type missing: `sensor.example_19`; above -0.001; below 8]. If false, stop the current sequence here.

3. Wait for one of these triggers:

   - Trigger type missing: `sensor.example_19`; above 7.999
   - Trigger type missing: `sensor.example_19`; to state: not available, not available
   - Trigger type missing: `sensor.example_18`; from state: not available
   - Trigger type missing: `switch.example_15`; from state: not available
   - Trigger type missing: `script.example_01`; to state: not available
   - Trigger type missing: `automation.example_06`; above 0; attribute name: not available

   Time limit: not available. Continue with the next step when the timeout expires.

4. If all of: condition type missing: `switch.example_15`; state: not available; held for not available; condition type missing: `script.example_01`; state: not available; condition type missing: `sensor.example_18`; state: not available; held for not available; condition type missing: `automation.example_06`; below 1; attribute name: not available; condition type missing: `sensor.example_19`; above -0.001; below 8; condition type missing: formula: not available; condition type missing: formula: not available:

   **Then:**

   1. Turn off a switch — `switch.example_15`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
