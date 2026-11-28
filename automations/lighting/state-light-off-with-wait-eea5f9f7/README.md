# Turn off lights · with a wait condition in the routine — Variant D

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn off](../../../README.md#lighting-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for one of 2 triggers (up to 15 min; continue on timeout) (selected steps; 4 other actions omitted). Start settings: to state: `off`; held for 55 min. Includes condition checks before the actions.

## What starts it?

- **1.** State change: `binary_sensor.example_27`; to state: `off`; held for 00:55:00 (time format)

## What must be true first?

Before the actions run: all of: at least one of [state check: `light.example_10`; state: `on`; state check: `light.example_12`; state: `on`; state check: `light.example_11`; state: `on`; state check: `switch.example_08`; state: `on`]; formula check: formula: “\{\{ as\_timestamp\(now\(\)\) - as\_timestamp\(states\('input\_datetime.example\_01'\),0\) &gt; 7200 \}\}”.

## Actual flow

1. Prepare 1 intermediate values; their contents/formulas are not described.

2. Send a message to your own notification destination — `notify.example_01`; message text: “Seit 55 Minuten keine Bewegung. Soll ich alles ausschalten?”; message title: “Büro”.

3. Send a message to your own notification destination — `notify.example_02`; message text: “Seit 55 Minuten keine Bewegung. Soll ich alles ausschalten?”; message title: “Büro”.

4. Wait for one of these triggers:

   - Event: event name: not available
   - Event: event name: not available

   Time limit: 00:15:00 (time format). Continue with the next step when the timeout expires.

5. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: formula check: formula: “\{\{ wait.trigger is not none and wait.trigger.event.example\_05.action == 'BU\_SHUTDOWN\_YES' \}\}”

   1. Turn off lights — `light.example_10`, `light.example_12`, `light.example_11`.

   2. Run your own script — `script.example_07`; configured to continue after supported action errors.

   3. Run your own script — `script.example_08`.

   4. Send a message to your own notification destination — `notify.example_01`; message text: “Alles klar. Büro ist aus.”.

   5. Send a message to your own notification destination — `notify.example_02`; message text: “Alles klar. Büro ist aus.”.

   **Branch 2:** all of: formula check: formula: “\{\{ wait.trigger is not none and wait.trigger.event.example\_05.action == 'BU\_SHUTDOWN\_NO' \}\}”

   1. Send a message to your own notification destination — `notify.example_01`; message text: “Okay. Ich mache nichts.”.

   2. Send a message to your own notification destination — `notify.example_02`; message text: “Okay. Ich mache nichts.”.

   **If no branch matches:**

   1. Send a message to your own notification destination — `notify.example_01`; message text: “Na gut. Wenn keiner antwortet, mach ich’s selbst. 😤”.

   2. Send a message to your own notification destination — `notify.example_02`; message text: “Na gut. Wenn keiner antwortet, mach ich’s selbst. 😤”.

   3. Turn off lights — `light.example_10`, `light.example_12`, `light.example_11`.

   4. Run your own script — `script.example_07`; configured to continue after supported action errors.

   5. Run your own script — `script.example_08`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- The devices and action you want to add yourself.
- Lights that Home Assistant can control.
- A configured notification destination, such as the Home Assistant app.
- An existing Home Assistant script: a saved sequence of actions.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
