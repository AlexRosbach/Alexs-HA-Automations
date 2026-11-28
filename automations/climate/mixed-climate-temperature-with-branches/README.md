# Set the desired room temperature · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Check conditions; stop this sequence if false → if state: `on`; 2 other checks: (Set the desired room temperature) → Turn off a stored on/off value. Start settings: at 18:00:00 / Home Assistant event; 2 more triggers in the details. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Scheduled time: at 18:00:00
- **2.** Home Assistant event: event: `start`
- **3.** State change: `input_text.example_03`; to state: not available
- **4.** Repeating schedule: minutes: /5

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ now\(\).hour&gt;=18 or states\('input\_text.example\_01'\) \!= now\(\).date\(\)\|string \}\}”.

## Actual flow

1. Check formula check: formula: “\{\{ states\('input\_text.example\_03'\) == '' \}\}”. If false, stop the current sequence here.

2. If all of: state check: `input_boolean.example_14`; state: `on`; state check: `climate.example_04`; state: `heat`; formula check: formula: “\{\{ state\_attr\('climate.example\_04','temperature'\)\|float\(0\)==21 and states\('input\_text.example\_04'\) in \['auto','heat'\] \}\}”:

   **Then:**

   1. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): not available; heating/cooling mode: not available.

3. Turn off a stored on/off value — `input_boolean.example_14`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A toggle helper: an on/off value stored in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
