# Read a task list and remove items · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Task lists and reminders](../../../README.md#tasks) → [Remove tasks](../../../README.md#tasks-remove)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Read a task list → repeat for each list item: prepare intermediate values (selected steps; 4 other actions omitted). Start settings: hours: /1.

## What starts it?

- **1.** Repeating schedule: hours: /1

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Prepare 1 intermediate values; their contents/formulas are not described.

2. Read a task list — `todo.example_01`; save the returned result for later steps.

3. Prepare 1 intermediate values; their contents/formulas are not described.

4. Prepare 1 intermediate values; their contents/formulas are not described.

5. Repeat for each list item; item count: not available.

   1. Prepare 4 intermediate values; their contents/formulas are not described.

   2. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** formula: “\{\{ variable\_14 not in variable\_10 \}\}”

      1. Run your own script — `script.example_01`.

      No default branch is configured.

6. Repeat for each list item; item count: not available.

   1. Prepare 1 intermediate values; their contents/formulas are not described.

   2. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** formula: “\{\{ variable\_15.startswith\('Offline:'\) and variable\_15 not in variable\_11 \}\}”

      1. Remove an item from a task list — `todo.example_01`; task item: “\{\{ variable\_15 \}\}”.

      No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- An existing Home Assistant script: a saved sequence of actions.
- A task list set up in Home Assistant.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
