# Store some text

**English** · [Deutsch](README.de.md)

[Counters and stored values](../../../README.md#helpers) → [Store text](../../../README.md#helpers-text)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Store some text. Start settings: held for 3 min. Includes condition checks before the actions.

## What starts it?

- **1.** Formula becomes true: held for 00:03:00 (time format); formula: “\{\{ states\('sensor.example\_22'\) in \['bad','buero','IDENTIFIER\_115','flurunten','AREA\_02','kueche','person'\] \}\}”

## What must be true first?

Before the actions run: all of: time check: before 06:45:00; after 04:00:00.

## Actual flow

1. Store some text — `input_text.example_02`; stored value: “\{\{ now\(\).date\(\) \}\}”.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A helper that stores text.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
