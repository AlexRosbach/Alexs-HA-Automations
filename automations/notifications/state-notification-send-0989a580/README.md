# Send messages — Variant A

**English** · [Deutsch](README.de.md)

[Messages and notices](../../../README.md#notifications) → [Send messages](../../../README.md#notifications-messages)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Check conditions; stop this sequence if false → Press a configured virtual button → Send a message. Includes condition checks before the actions.

## What starts it?

- **1.** Trigger type missing: `sensor.example_17`; excluded previous state: not available, not available; excluded new state: not available, not available

## What must be true first?

Before the actions run: all of: condition type missing: `sensor.example_16`; state: not available; condition type missing: formula: not available.

## Actual flow

1. Check condition type missing: `sensor.example_16`; state: not available. If false, stop the current sequence here.

2. Press a configured virtual button — `input_button.example_01`.

3. Send a message — `notify.example_02`, `notify.example_03`; message text: not available; message title: not available.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A button set up as a helper in Home Assistant.
- A configured notification destination, such as the Home Assistant app.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
