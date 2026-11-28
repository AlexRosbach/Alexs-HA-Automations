# Send messages · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Messages and notices](../../../README.md#notifications) → [Send messages](../../../README.md#notifications-messages)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Get a weather forecast → prepare intermediate values → 1 more step (see full flow). Start settings: minutes: 10 / Home Assistant event. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Repeating schedule: minutes: 10
- **2.** Home Assistant event: event: `start`

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ 7 &lt;= now\(\).hour &lt;= 21 \}\}”; formula check: formula: “\{% set last = this.attributes.last\_triggered %\} \{\{ last is none or \(now\(\) - last\).total\_seconds\(\) &gt; 7200 \}\}”.

## Actual flow

1. Get a weather forecast — `weather.example_01`; save the returned result for later steps.

2. Prepare 10 intermediate values; their contents/formulas are not described.

3. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: formula check: formula: “\{\{ variable\_49 \| bool \}\}”

   1. Send a message to your own notification destination — `notify.example_01`; message text: “Forecast: max \{\{ variable\_44 \}\} °C, UV \{\{ variable\_45 \}\}, min. Bewoelkung \{\{ variable\_46 \}\} %. Innen: Schlafzimmer \{\{ variable\_40 \}\} °C, Haus \{\{ variable\_47 \}\} °C. Solar Resttag \{\{ variable\_48 \}\} kWh. \{\{ variable\_43 \}\}”; message title: “Proaktiver Hitzeschutz”.

   2. Send a message to your own notification destination — `notify.example_02`; message text: “Forecast: max \{\{ variable\_44 \}\} °C, UV \{\{ variable\_45 \}\}, min. Bewoelkung \{\{ variable\_46 \}\} %. Innen: Schlafzimmer \{\{ variable\_40 \}\} °C, Haus \{\{ variable\_47 \}\} °C. Solar Resttag \{\{ variable\_48 \}\} kWh. \{\{ variable\_43 \}\}”; message title: “Proaktiver Hitzeschutz”.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A configured notification destination, such as the Home Assistant app.
- A weather integration that provides forecasts.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
