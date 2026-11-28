# Adjust fans · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Fans and air purifiers](../../../README.md#ventilation) → [Set the speed](../../../README.md#ventilation-speed)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Prepare intermediate values → 1 more step (see full flow). Start settings: minutes: 0. Includes condition checks before the actions.

## What starts it?

- **1.** Repeating schedule: minutes: 0

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ states\('sensor.example\_16'\) \| float\(0\) &gt;= 26.5 \}\}”.

## Actual flow

1. Prepare 5 intermediate values; their contents/formulas are not described.

2. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: formula check: formula: “\{\{ 8 &lt;= now\(\).hour &lt; 18 \}\}”; state check: `fan.example_01`; state: `off`

   1. Turn on a fan — `fan.example_01`.

   2. Set the fan speed — `fan.example_01`; fan speed: 75%.

   3. Send a message to your own notification destination — `notify.example_01`; message text: “\{\{ variable\_40 \}\} °C im Schlafzimmer \(Thermostat \{\{ variable\_41 \}\} °C\). Luefter wurde eingeschaltet. \{\{ variable\_43 \}\}”; message title: “Schlafzimmer zu warm”.

   4. Send a message to your own notification destination — `notify.example_02`; message text: “\{\{ variable\_40 \}\} °C im Schlafzimmer \(Thermostat \{\{ variable\_41 \}\} °C\). Luefter wurde eingeschaltet. \{\{ variable\_43 \}\}”; message title: “Schlafzimmer zu warm”.

   **Branch 2:** all of: formula check: formula: “\{\{ now\(\).hour &gt;= 18 or now\(\).hour &lt; 8 \}\}”; state check: `fan.example_01`; state: `off`

   1. Send a message to your own notification destination — `notify.example_01`; message text: “\{\{ variable\_40 \}\} °C im Schlafzimmer \(Thermostat \{\{ variable\_41 \}\} °C\). Luefter einschalten? \{\{ variable\_43 \}\}”; message title: “Schlafzimmer zu warm”.

   2. Send a message to your own notification destination — `notify.example_02`; message text: “\{\{ variable\_40 \}\} °C im Schlafzimmer \(Thermostat \{\{ variable\_41 \}\} °C\). Luefter einschalten? \{\{ variable\_43 \}\}”; message title: “Schlafzimmer zu warm”.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A fan or air purifier that Home Assistant can control.
- The devices and action you want to add yourself.
- A configured notification destination, such as the Home Assistant app.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
