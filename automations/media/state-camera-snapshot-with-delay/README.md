# Save a camera picture · with a delay in the routine

**English** · [Deutsch](README.de.md)

[Music, media and cameras](../../../README.md#media) → [Save camera pictures](../../../README.md#media-snapshots)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Save a camera picture → pause for 1 s (selected steps; 6 other actions omitted). Start settings: from state: `off`; to state: `on`.

## What starts it?

- **1.** State change: `binary_sensor.example_30`; from state: `off`; to state: `on`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Save a camera picture — `camera.example_01`; file destination: not available; configured to continue after supported action errors.

2. Pause for 1 s.

3. Read a task list — `todo.example_01`; task status: `needs_action`; save the returned result for later steps.

4. Prepare 2 intermediate values; their contents/formulas are not described.

5. If all of: formula check: formula: “\{\{ variable\_20 not in variable\_19 \}\}”:

   **Then:**

   1. Run your own script — `script.example_01`.

6. Send a message to your own notification destination — `notify.example_02`; message text: “person wurde geöffnet”; message title: “📬 person”.

7. Send a message to your own notification destination — `notify.example_01`; message text: “person wurde geöffnet”; message title: “📬 person”.

8. Send a message — `notify.example_03`; message text: “person person wurde geöffnet.”; message title: “person”.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected camera with the picture or video function you need.
- The devices and action you want to add yourself.
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
