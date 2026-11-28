# Read a task list · with conditions in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Task lists and reminders](../../../README.md#tasks) → [Read task lists](../../../README.md#tasks-read)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Read a task list; task status: `needs_action` (selected steps; 3 other actions omitted). Start settings: to state: `unavailable`; held for 2 min.

## What starts it?

- **1.** State change: `vacuum.example_03`, `vacuum.example_02`, `vacuum.example_05`, `vacuum.example_04`, `vacuum.example_01`, `vacuum.example_06`; to state: `unavailable`; held for 2 min

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Send a message; message text: “\{\{ trigger.to\_state.attributes.friendly\_name \}\} ist offline\!”; message title: “🤖 Staubsauger”.

2. Read a task list — `todo.example_01`; task status: `needs_action`; save the returned result for later steps.

3. Prepare 2 intermediate values; their contents/formulas are not described.

4. If all of: formula check: formula: “\{\{ variable\_20 not in variable\_19 \}\}”:

   **Then:**

   1. Run your own script — `script.example_01`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A configured notification destination, such as the Home Assistant app.
- An existing Home Assistant script: a saved sequence of actions.
- A task list set up in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
