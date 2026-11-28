# Read a task list · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Task lists and reminders](../../../README.md#tasks) → [Read task lists](../../../README.md#tasks-read)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value → Send a message to your own notification destination; message text: “Die Waschmaschine ist IDENTIFIER\_104.”; message title: “Waschmaschine” → 4 more steps. Start settings: above 10; held for 2 min / below 5; held for 20 min; 1 more trigger in the details.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Numeric threshold crossing: `sensor.example_01`; above 10; held for 2 min; trigger reference: not available
- **2.** Numeric threshold crossing: `sensor.example_01`; below 5; held for 20 min; trigger reference: not available
- **3.** State change: `switch.example_13`; to state: `off`; held for 1 min; trigger reference: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: trigger-reference check: trigger reference: not available

   1. Turn on a stored on/off value — `input_boolean.example_10`.

   **Branch 2:** all of: trigger-reference check: trigger reference: not available, not available; state check: `input_boolean.example_10`; state: `on`

   1. Turn off a stored on/off value — `input_boolean.example_10`.

   2. Send a message to your own notification destination — `notify.example_01`; message text: “Die Waschmaschine ist IDENTIFIER\_104.”; message title: “Waschmaschine”.

   3. Send a message to your own notification destination — `notify.example_02`; message text: “Die Waschmaschine ist IDENTIFIER\_104.”; message title: “Waschmaschine”.

   4. Read a task list — `todo.example_01`; task status: `needs_action`; save the returned result for later steps.

   5. Prepare 1 intermediate values; their contents/formulas are not described.

   6. If all of: formula check: formula: “\{\{ 'Waschmaschine ausraeumen' not in variable\_37 \}\}”:

      **Then:**

      1. Run your own script — `script.example_01`.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A toggle helper: an on/off value stored in Home Assistant.
- A configured notification destination, such as the Home Assistant app.
- An existing Home Assistant script: a saved sequence of actions.
- A task list set up in Home Assistant.
- A suitable sensor or other number in Home Assistant, and the limit you want to use.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
