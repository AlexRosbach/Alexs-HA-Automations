# Turn switches on and off · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn on and off](../../../README.md#switches-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Run 3 paths in parallel. Start settings: State change / Home Assistant event; 1 more trigger in the details. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `person.example_02`, `person.example_01`, `input_boolean.example_04`; to state: unspecified (null); trigger reference: not available
- **2.** Home Assistant event: event: `start`; trigger reference: not available
- **3.** Repeating schedule: minutes: /5; trigger reference: not available

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ is\_state\('input\_boolean.example\_04','IDENTIFIER\_159'\) or \(is\_state\('input\_boolean.example\_04','IDENTIFIER\_160'\) and \(is\_state\('person.example\_02','home'\) or is\_state\('person.example\_01','home'\) or \(states\('person.example\_02'\) not in \['unknown','unavailable'\] and states\('person.example\_01'\) not in \['unknown','unavailable'\]\)\)\) \}\}”.

## Actual flow

1. Start these paths in parallel. Their execution order is not guaranteed.

   **Parallel path 1:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ is\_state\('input\_boolean.example\_04','IDENTIFIER\_160'\) and \(is\_state\('person.example\_02','home'\) or is\_state\('person.example\_01','home'\)\) \}\}”

      1. Check formula check: formula: “\{\{ not is\_state\('switch.example\_09','IDENTIFIER\_160'\) \}\}”. If false, stop the current sequence here.

      2. Run a device function by pressing a button — `button.example_01`; configured to continue after supported action errors.

      3. Run a device function by pressing a button — `button.example_02`.

      4. Pause for 00:00:04 (time format).

      5. Run a device function by pressing a button — `button.example_01`.

      6. Turn on a switch — `switch.example_09`; configured to continue after supported action errors.

      **If no branch matches:**

      1. Check formula check: formula: “\{\{ not is\_state\('switch.example\_09','IDENTIFIER\_159'\) or trigger is not defined or trigger.id \| default\(''\) \!= 'IDENTIFIER\_81' \}\}”. If false, stop the current sequence here.

      2. Turn off a switch — `switch.example_09`; configured to continue after supported action errors.

      3. Wait until this formula is true: “\{\{ is\_state\('switch.example\_09','IDENTIFIER\_159'\) and states\('button.example\_03'\) \!= 'unavailable' \}\}”.

         Time limit: 00:00:30 (time format). Stop this sequence when the timeout expires.

      4. Run a device function by pressing a button — `button.example_01`; configured to continue after supported action errors.

      5. Run a device function by pressing a button — `button.example_03`; configured to continue after supported action errors.

   **Parallel path 2:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ is\_state\('input\_boolean.example\_04','IDENTIFIER\_160'\) and \(is\_state\('person.example\_02','home'\) or is\_state\('person.example\_01','home'\)\) \}\}”

      1. Check formula check: formula: “\{\{ not is\_state\('switch.example\_10','IDENTIFIER\_160'\) \}\}”. If false, stop the current sequence here.

      2. Run a device function by pressing a button — `button.example_04`; configured to continue after supported action errors.

      3. Run a device function by pressing a button — `button.example_05`.

      4. Pause for 00:00:04 (time format).

      5. Run a device function by pressing a button — `button.example_04`.

      6. Turn on a switch — `switch.example_10`; configured to continue after supported action errors.

      **If no branch matches:**

      1. Check formula check: formula: “\{\{ not is\_state\('switch.example\_10','IDENTIFIER\_159'\) or trigger is not defined or trigger.id \| default\(''\) \!= 'IDENTIFIER\_81' \}\}”. If false, stop the current sequence here.

      2. Turn off a switch — `switch.example_10`; configured to continue after supported action errors.

      3. Wait until this formula is true: “\{\{ is\_state\('switch.example\_10','IDENTIFIER\_159'\) and states\('button.example\_06'\) \!= 'unavailable' \}\}”.

         Time limit: 00:00:30 (time format). Stop this sequence when the timeout expires.

      4. Run a device function by pressing a button — `button.example_04`; configured to continue after supported action errors.

      5. Run a device function by pressing a button — `button.example_06`; configured to continue after supported action errors.

   **Parallel path 3:**

   1. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ is\_state\('input\_boolean.example\_04','IDENTIFIER\_160'\) and \(is\_state\('person.example\_02','home'\) or is\_state\('person.example\_01','home'\)\) \}\}”

      1. Check formula check: formula: “\{\{ not is\_state\('switch.example\_11','IDENTIFIER\_160'\) \}\}”. If false, stop the current sequence here.

      2. Run a device function by pressing a button — `button.example_07`; configured to continue after supported action errors.

      3. Run a device function by pressing a button — `button.example_08`.

      4. Pause for 00:00:04 (time format).

      5. Run a device function by pressing a button — `button.example_07`.

      6. Turn on a switch — `switch.example_11`; configured to continue after supported action errors.

      **If no branch matches:**

      1. Check formula check: formula: “\{\{ not is\_state\('switch.example\_11','IDENTIFIER\_159'\) or trigger is not defined or trigger.id \| default\(''\) \!= 'IDENTIFIER\_81' \}\}”. If false, stop the current sequence here.

      2. Turn off a switch — `switch.example_11`; configured to continue after supported action errors.

      3. Wait until this formula is true: “\{\{ is\_state\('switch.example\_11','IDENTIFIER\_159'\) and states\('button.example\_09'\) \!= 'unavailable' \}\}”.

         Time limit: 00:00:30 (time format). Stop this sequence when the timeout expires.

      4. Run a device function by pressing a button — `button.example_07`; configured to continue after supported action errors.

      5. Run a device function by pressing a button — `button.example_09`; configured to continue after supported action errors.

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
