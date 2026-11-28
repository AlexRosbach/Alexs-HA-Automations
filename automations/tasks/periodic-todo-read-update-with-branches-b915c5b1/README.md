# Read and edit a task list · with conditions in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Task lists and reminders](../../../README.md#tasks) → [Edit tasks](../../../README.md#tasks-edit)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Read a task list → prepare intermediate values → repeat for each list item: prepare intermediate values. Start settings: hours: /1.

## What starts it?

- **1.** Repeating schedule: hours: /1

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Read a task list — `todo.example_01`; save the returned result for later steps.

2. Prepare 2 intermediate values; their contents/formulas are not described.

3. Repeat for each list item; item count: not available.

   1. Prepare 6 intermediate values; their contents/formulas are not described.

   2. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ level &lt; 10 and variable\_07 not in variable\_02 \}\}”

      1. Run your own script — `script.example_01`.

      **Branch 2:** all of: formula check: formula: “\{\{ level &gt;= 10 and variable\_07 in variable\_02 \}\}”

      1. Prepare 1 intermediate values; their contents/formulas are not described.

      2. If all of: formula check: formula: “\{\{ variable\_08 is defined and variable\_08 \}\}”:

         **Then:**

         1. Update an item in a task list — `todo.example_01`; task status: `completed`; task reference: “\{\{ variable\_08.uid \}\}”.

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
