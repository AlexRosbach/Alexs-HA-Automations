# Set the desired room temperature · with a wait condition in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 8 more steps / prepare intermediate values → check conditions; stop this sequence if false → 7 more steps; 4 more branches. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `binary_sensor.example_20`; from state: not available; to state: not available; trigger reference: `ID_32`
- **2.** Trigger type missing: `binary_sensor.example_20`; to state: not available; held for not available; trigger reference: `ID_33`
- **3.** Trigger type missing: held for not available; formula: not available; trigger reference: `ID_34`
- **4.** Trigger type missing: at not available; trigger reference: `ID_35`
- **5.** Trigger type missing: at not available; trigger reference: `ID_36`
- **6.** Trigger type missing: `climate.example_04`; trigger reference: `ID_37`
- **7.** Trigger type missing: `binary_sensor.example_07`; trigger reference: `ID_38`

## What must be true first?

Before the actions run: all of: condition type missing: formula: not available.

## Actual flow

The automation also prepares intermediate values; their contents/formulas are not described.

1. Prepare 1 intermediate values; their contents/formulas are not described.

2. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: formula: not available

   1. Prepare 2 intermediate values; their contents/formulas are not described.

   2. Store some text — `input_text.example_10`; stored value: not available.

   3. Check condition type missing: formula: not available. If false, stop the current sequence here.

   4. Check condition type missing: formula: not available. If false, stop the current sequence here.

   5. Check condition type missing: formula: not available. If false, stop the current sequence here.

   6. Check condition type missing: formula: not available. If false, stop the current sequence here.

   7. Turn off a stored on/off value — `input_boolean.example_14`.

   8. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 21; heating/cooling mode: not available.

   9. Wait until a formula is true; the formula is not available.

      Time limit: not available. Stop this sequence when the timeout expires.

   10. Store some text — `input_text.example_10`; stored value: not available.

   **Branch 2:** all of: condition type missing: formula: not available

   1. Prepare 1 intermediate values; their contents/formulas are not described.

   2. Check condition type missing: formula: not available. If false, stop the current sequence here.

   3. Check condition type missing: formula: not available. If false, stop the current sequence here.

   4. Check condition type missing: formula: not available. If false, stop the current sequence here.

   5. Check condition type missing: formula: not available. If false, stop the current sequence here.

   6. Turn off a stored on/off value — `input_boolean.example_14`.

   7. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 21; heating/cooling mode: not available.

   8. Wait until a formula is true; the formula is not available.

      Time limit: not available. Stop this sequence when the timeout expires.

   9. Store some text — `input_text.example_10`; stored value: not available.

   **Branch 3:** all of: condition type missing: formula: not available

   1. Check condition type missing: formula: not available. If false, stop the current sequence here.

   2. Check condition type missing: formula: not available. If false, stop the current sequence here.

   3. Check condition type missing: formula: not available. If false, stop the current sequence here.

   4. Check condition type missing: formula: not available. If false, stop the current sequence here.

   5. Check condition type missing: formula: not available. If false, stop the current sequence here.

   6. Check condition type missing: formula: not available. If false, stop the current sequence here.

   7. Turn off a stored on/off value — `input_boolean.example_14`.

   8. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 19; heating/cooling mode: not available.

   9. Wait until a formula is true; the formula is not available.

      Time limit: not available. Stop this sequence when the timeout expires.

   10. Store some text — `input_text.example_10`; stored value: not available.

   **Branch 4:** all of: condition type missing: formula: not available

   1. Check condition type missing: formula: not available. If false, stop the current sequence here.

   2. Prepare 1 intermediate values; their contents/formulas are not described.

   3. Check condition type missing: formula: not available. If false, stop the current sequence here.

   4. Check condition type missing: formula: not available. If false, stop the current sequence here.

   5. Check condition type missing: formula: not available. If false, stop the current sequence here.

   6. Turn off a stored on/off value — `input_boolean.example_14`.

   7. Set the desired room temperature — `climate.example_04`; temperature setting (unit not given): 21; heating/cooling mode: not available.

   8. Wait until a formula is true; the formula is not available.

      Time limit: not available. Stop this sequence when the timeout expires.

   9. Store some text — `input_text.example_10`; stored value: not available.

   **Branch 5:** all of: condition type missing: formula: not available; condition type missing: formula: not available

   1. Store some text — `input_text.example_10`; stored value: not available.

   **Branch 6:** all of: condition type missing: formula: not available; condition type missing: formula: not available

   1. Store some text — `input_text.example_10`; stored value: not available.

   No default branch is configured.

## If it triggers again

`queued`: New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time. Limit for running and queued runs: 50.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A toggle helper: an on/off value stored in Home Assistant.
- A helper that stores text.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
