# Turn switches on and off · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn on and off](../../../README.md#switches-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Run 3 paths in parallel. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `person.example_02`, `person.example_01`, `input_boolean.example_06`; to state: unspecified (null); trigger reference: `ID_11`
- **2.** Trigger type missing: event: not available; trigger reference: `ID_04`
- **3.** Trigger type missing: minutes: not available; trigger reference: `ID_12`

## What must be true first?

Before the actions run: all of: condition type missing: formula: not available.

## Actual flow

1. Start these paths in parallel. Their execution order is not guaranteed.

   **Parallel path 1:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: condition type missing: formula: not available

      1. Check condition type missing: formula: not available. If false, stop the current sequence here.

      2. Run a device function by pressing a button — `button.example_02`; configured to continue after supported action errors.

      3. Run a device function by pressing a button — `button.example_03`.

      4. Pause for not available.

      5. Run a device function by pressing a button — `button.example_02`.

      6. Turn on a switch — `switch.example_09`; configured to continue after supported action errors.

      **If no branch matches:**

      1. Check condition type missing: formula: not available. If false, stop the current sequence here.

      2. Turn off a switch — `switch.example_09`; configured to continue after supported action errors.

      3. Wait until a formula is true; the formula is not available.

         Time limit: not available. Stop this sequence when the timeout expires.

      4. Run a device function by pressing a button — `button.example_02`; configured to continue after supported action errors.

      5. Run a device function by pressing a button — `button.example_04`; configured to continue after supported action errors.

   **Parallel path 2:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: condition type missing: formula: not available

      1. Check condition type missing: formula: not available. If false, stop the current sequence here.

      2. Run a device function by pressing a button — `button.example_05`; configured to continue after supported action errors.

      3. Run a device function by pressing a button — `button.example_06`.

      4. Pause for not available.

      5. Run a device function by pressing a button — `button.example_05`.

      6. Turn on a switch — `switch.example_10`; configured to continue after supported action errors.

      **If no branch matches:**

      1. Check condition type missing: formula: not available. If false, stop the current sequence here.

      2. Turn off a switch — `switch.example_10`; configured to continue after supported action errors.

      3. Wait until a formula is true; the formula is not available.

         Time limit: not available. Stop this sequence when the timeout expires.

      4. Run a device function by pressing a button — `button.example_05`; configured to continue after supported action errors.

      5. Run a device function by pressing a button — `button.example_07`; configured to continue after supported action errors.

   **Parallel path 3:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: condition type missing: formula: not available

      1. Check condition type missing: formula: not available. If false, stop the current sequence here.

      2. Run a device function by pressing a button — `button.example_08`; configured to continue after supported action errors.

      3. Run a device function by pressing a button — `button.example_09`.

      4. Pause for not available.

      5. Run a device function by pressing a button — `button.example_08`.

      6. Turn on a switch — `switch.example_11`; configured to continue after supported action errors.

      **If no branch matches:**

      1. Check condition type missing: formula: not available. If false, stop the current sequence here.

      2. Turn off a switch — `switch.example_11`; configured to continue after supported action errors.

      3. Wait until a formula is true; the formula is not available.

         Time limit: not available. Stop this sequence when the timeout expires.

      4. Run a device function by pressing a button — `button.example_08`; configured to continue after supported action errors.

      5. Run a device function by pressing a button — `button.example_10`; configured to continue after supported action errors.

## If it triggers again

`restart`: A new trigger stops the current run and starts it again, provided the automation's conditions pass.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A device function that Home Assistant provides as a button.
- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
