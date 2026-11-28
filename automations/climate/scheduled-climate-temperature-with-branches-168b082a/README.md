# Set the desired room temperature · with conditions in the routine — Variant A

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Store some text → if state: `off`; 2 other checks: (Store some text → Store a number → 2 more steps). Start settings: at 06:45:00. Includes condition checks before the actions.

## What starts it?

- **1.** Scheduled time: at 06:45:00

## What must be true first?

Before the actions run: all of: time check: weekdays: `mon`, `tue`, `wed`, `thu`, `fri`; state check: `person.example_02`; state: `home`; state check: `sensor.example_22`; state: not available; held for 00:10:00 (time format); formula check: formula: “\{\{ states\('input\_text.example\_02'\) \!= now\(\).date\(\)\|string \}\}”; formula check: formula: “\{\{ not is\_state\('calendar.example\_01','IDENTIFIER\_160'\) \}\}”.

## Actual flow

1. Store some text — `input_text.example_01`; stored value: “\{\{ now\(\).date\(\) \}\}”.

2. If all of: state check: `binary_sensor.example_15`; state: `off`; formula check: formula: “\{\{ states\('climate.example\_04'\) in \['auto','heat'\] and state\_attr\('climate.example\_04','temperature'\) is number \}\}”; formula check: formula: “\{\{ states\('input\_text.example\_03'\) == '' \}\}”:

   **Then:**

   1. Store some text — `input_text.example_04`; stored value: “\{\{ states\('climate.example\_04'\) \}\}”.

   2. Store a number — `input_number.example_01`; stored value: “\{\{ state\_attr\('climate.example\_04','temperature'\) \}\}”.

   3. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 21; heating/cooling mode: `heat`.

   4. Turn on a stored on/off value — `input_boolean.example_14`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A toggle helper: an on/off value stored in Home Assistant.
- A helper that stores a number.
- A helper that stores text.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
