# Adjust heating or air conditioning · with conditions in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Heating and cooling modes](../../../README.md#climate-modes)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: check conditions; stop this sequence if false → Set the temperature to 5 → 1 more step / check conditions; stop this sequence if false → Set the heating or cooling mode; heating/cooling mode: `heat_cool` → 1 more step. Start settings: to state: `on` / to state: `off`.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_15`; to state: `on`; trigger reference: not available
- **2.** State change: `binary_sensor.example_15`; to state: `off`; trigger reference: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: trigger-reference check: trigger reference: not available

   1. Check formula check: formula: “\{\{ not \(state\_attr\('climate.example\_04','hvac\_mode'\) == 'IDENTIFIER\_159' and \(state\_attr\('climate.example\_04','temperature'\)\|float\(0\)\) == 5\) \}\}”. If false, stop the current sequence here.

   2. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 5.

   3. Set the heating or cooling mode — `climate.example_04`; heating/cooling mode: `off`.

   **Branch 2:** all of: trigger-reference check: trigger reference: not available

   1. Check formula check: formula: “\{\{ not \(state\_attr\('climate.example\_04','hvac\_mode'\) in \['heat\_cool','heat'\] and \(state\_attr\('climate.example\_04','temperature'\)\|float\(0\)\) == 21\) \}\}”. If false, stop the current sequence here.

   2. Set the heating or cooling mode — `climate.example_04`; heating/cooling mode: `heat_cool`.

   3. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 21.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
