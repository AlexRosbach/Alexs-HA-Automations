# Turn off a switch · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn off](../../../README.md#switches-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for a value above 7.999 or 5 other triggers (up to 1 min; continue on timeout) → if state: `on`; held for 3 min; 6 other checks: (Turn off a switch) (selected steps; 2 other actions omitted). Start settings: to state: `unavailable`; held for 1 min. Includes condition checks before the actions.

## What starts it?

- **1.** State change: `sensor.example_23`; from state: not available, not available; to state: `unavailable`; held for 00:01:00 (time format)

## What must be true first?

Before the actions run: all of: state check: `switch.example_15`; state: `on`; held for 00:03:00 (time format); state check: `script.example_04`; state: `off`; number check: `automation.example_06`; below 1; attribute name: not available.

## Actual flow

1. If all of: none of [number check: `sensor.example_24`; above -0.001; below 8]:

   **Then:**

   1. Wait for one of these triggers:

      - Numeric threshold crossing: `sensor.example_24`; below 8
      - State change: `sensor.example_23`; to state: not available
      - State change: `switch.example_15`; to state: `off`

      Time limit: 00:10:00 (time format). Continue with the next step when the timeout expires.

2. Check all of [state check: `switch.example_15`; state: `on`; held for 00:03:00 (time format); state check: `script.example_04`; state: `off`; state check: `sensor.example_23`; state: `unavailable`; held for 00:01:00 (time format); number check: `automation.example_06`; below 1; attribute name: not available; number check: `sensor.example_24`; above -0.001; below 8]. If false, stop the current sequence here.

3. Wait for one of these triggers:

   - Numeric threshold crossing: `sensor.example_24`; above 7.999
   - State change: `sensor.example_24`; to state: `unknown`, `unavailable`
   - State change: `sensor.example_23`; from state: `unavailable`
   - State change: `switch.example_15`; from state: `on`
   - State change: `script.example_04`; to state: `on`
   - Numeric threshold crossing: `automation.example_06`; above 0; attribute name: not available

   Time limit: 00:01:00 (time format). Continue with the next step when the timeout expires.

4. If all of: state check: `switch.example_15`; state: `on`; held for 00:03:00 (time format); state check: `script.example_04`; state: `off`; state check: `sensor.example_23`; state: `unavailable`; held for 00:01:00 (time format); number check: `automation.example_06`; below 1; attribute name: not available; number check: `sensor.example_24`; above -0.001; below 8; formula check: formula: “\{\{ not wait.completed \}\}”; formula check: formula: “\{\{ as\_timestamp\(now\(\)\) - as\_timestamp\(states.sensor.example\_24.last\_reported, 0\) &lt; 90 \}\}”:

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
