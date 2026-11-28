# Send messages — Variant A

**English** · [Deutsch](README.de.md)

[Messages and notices](../../../README.md#notifications) → [Send messages](../../../README.md#notifications-messages)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Prepare intermediate values → Send a message to your own notification destination; message text: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; message title: “🌧️ Regenalarm · \{\{ variable\_16 \}\}” → Send a message to your own notification destination; message text: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; message title: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”. Start settings: to state: `on`. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_13`; to state: `on`
- **2.** State change: `binary_sensor.example_14`, `binary_sensor.example_15`, `binary_sensor.example_16`, `binary_sensor.example_17`, `binary_sensor.example_18`, `binary_sensor.example_19`, `binary_sensor.example_20`, `binary_sensor.example_21`, `binary_sensor.example_22`; to state: `on`

## What must be true first?

Before the actions run: all of: state check: `binary_sensor.example_13`; state: `on`; formula check: formula: “\{\{ expand\(\[ 'binary\_sensor.example\_14', 'binary\_sensor.example\_15', 'binary\_sensor.example\_16', 'binary\_sensor.example\_17', 'binary\_sensor.example\_18', 'binary\_sensor.example\_19', 'binary\_sensor.example\_20', 'binary\_sensor.example\_21', 'binary\_sensor.example\_22' \]\) \| selectattr\('state', 'eq', 'IDENTIFIER\_160'\) \| list \| count &gt; 0 \}\}”.

## Actual flow

1. Prepare 2 intermediate values; their contents/formulas are not described.

2. Send a message to your own notification destination — `notify.example_01`; message text: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; message title: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”.

3. Send a message to your own notification destination — `notify.example_02`; message text: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; message title: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A configured notification destination, such as the Home Assistant app.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
