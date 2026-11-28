# Send messages

**English** · [Deutsch](README.de.md)

[Messages and notices](../../../README.md#notifications) → [Send messages](../../../README.md#notifications-messages)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Store some text → Send a message to your own notification destination; message text: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; message title: “Restmüll morgen” → Send a message to your own notification destination; message text: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; message title: “Restmüll morgen”. Start settings: at 20:00:00 / to state: `on`. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Scheduled time: at 20:00:00
- **2.** State change: `binary_sensor.example_32`; to state: `on`

## What must be true first?

Before the actions run: all of: state check: `binary_sensor.example_32`; state: `on`; time check: before 23:59:59; after 19:59:59; formula check: formula: “\{\{ states\('input\_text.example\_05'\) \!= states\('input\_text.example\_06'\) \}\}”.

## Actual flow

1. Store some text — `input_text.example_05`; stored value: “\{\{ states\('input\_text.example\_06'\) \}\}”.

2. Send a message to your own notification destination — `notify.example_01`; message text: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; message title: “Restmüll morgen”.

3. Send a message to your own notification destination — `notify.example_02`; message text: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; message title: “Restmüll morgen”.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- The devices and action you want to add yourself.
- A helper that stores text.
- A configured notification destination, such as the Home Assistant app.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
