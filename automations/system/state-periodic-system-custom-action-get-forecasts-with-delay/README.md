# Combine several functions · with a delay in the routine

**English** · [Deutsch](README.de.md)

[More routines and device actions](../../../README.md#system) → [Get weather data](../../../README.md#system-weather)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Get a weather forecast → check conditions; stop this sequence if false → prepare intermediate values → 3 more steps (see full flow). Start settings: to state: `on`; held for 30 s / held for 30 s; 1 more trigger in the details. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_13`; to state: `on`; held for 00:00:30 (time format)
- **2.** State change: `binary_sensor.example_14`, `binary_sensor.example_15`, `binary_sensor.example_16`, `binary_sensor.example_17`, `binary_sensor.example_18`, `binary_sensor.example_19`, `binary_sensor.example_20`, `binary_sensor.example_21`, `binary_sensor.example_22`; to state: `on`; held for 00:00:30 (time format)
- **3.** State change: `weather.example_01`; to state: not available; held for 00:00:30 (time format)
- **4.** Repeating schedule: minutes: /5

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ 6 &lt;= now\(\).hour &lt; 21 \}\}”; state check: `binary_sensor.example_13`; state: `on`; held for 00:00:30 (time format); formula check: formula: “\{\{ expand\(\["binary\_sensor.example\_14","binary\_sensor.example\_15","binary\_sensor.example\_16","binary\_sensor.example\_17","binary\_sensor.example\_18","binary\_sensor.example\_19","binary\_sensor.example\_20","binary\_sensor.example\_21","binary\_sensor.example\_22"\]\) \| selectattr\('state', 'eq', 'IDENTIFIER\_160'\) \| list \| count &gt; 0 \}\}”.

## Actual flow

1. Get a weather forecast — `weather.example_01`; save the returned result for later steps.

2. Check formula check: formula: “\{% set prognose = variable\_54.get\('weather.example\_01', \{\}\).get\('forecast', \[\]\) %\} \{\{ is\_state\('weather.example\_01', 'pouring'\) or \(prognose \| count &gt; 0 and prognose\[0\].get\('condition'\) == 'pouring'\) \}\}”. If false, stop the current sequence here.

3. Prepare 2 intermediate values; their contents/formulas are not described.

4. Check formula check: formula: “\{\{ variable\_56 \| count &gt; 0 \}\}”. If false, stop the current sequence here.

5. Run your own script — `script.example_10`.

6. Pause for 00:30:00 (time format).

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- An existing Home Assistant script: a saved sequence of actions.
- A weather integration that provides forecasts.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
