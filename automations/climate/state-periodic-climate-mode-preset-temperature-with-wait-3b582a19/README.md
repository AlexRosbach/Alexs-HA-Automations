# Adjust heating or air conditioning · with a wait condition in the routine — Variant A

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Heating and cooling presets](../../../README.md#climate-profiles)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset) → 3 more steps (selected steps; 4 other actions omitted).

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `binary_sensor.example_06`; to state: not available, not available
- **2.** Trigger type missing: `climate.example_02`; held for not available; attribute name: not available
- **3.** Trigger type missing: `climate.example_02`; held for not available; attribute name: not available
- **4.** Trigger type missing: `climate.example_02`; to state: not available, not available; held for not available
- **5.** Trigger type missing: event: not available
- **6.** Trigger type missing: minutes: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Prepare 3 intermediate values; their contents/formulas are not described.

2. Check condition type missing: formula: not available. If false, stop the current sequence here.

3. Prepare 3 intermediate values; their contents/formulas are not described.

4. Prepare 1 intermediate values; their contents/formulas are not described.

5. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: formula: not available

   1. If all of: condition type missing: formula: not available:

      **Then:**

      1. Store some text — `input_text.example_06`; stored value: not available.

   2. If all of: condition type missing: formula: not available:

      **Then:**

      1. Choose a heating or cooling preset — `climate.example_02`; preset: not available.

   3. If all of: condition type missing: formula: not available:

      **Then:**

      1. Set the heating or cooling mode — `climate.example_02`; heating/cooling mode: not available.

   4. If all of: condition type missing: formula: not available:

      **Then:**

      1. Set the desired room temperature — `climate.example_02`; temperature setting (unit not given): 5.

   **Branch 2:** all of: condition type missing: formula: not available

   1. Set the heating or cooling mode — `climate.example_02`; heating/cooling mode: not available.

   2. If all of: condition type missing: formula: not available:

      **Then:**

      1. Choose a heating or cooling preset — `climate.example_02`; preset: not available.

   3. Set the desired room temperature — `climate.example_02`; temperature setting (unit not given): not available.

   4. Wait until a formula is true; the formula is not available.

      Time limit: not available. Stop this sequence when the timeout expires.

   5. Store some text — `input_text.example_06`; stored value: not available.

   No default branch is configured.

## If it triggers again

`queued`: New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time. Limit for running and queued runs: 10.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A helper that stores text.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
