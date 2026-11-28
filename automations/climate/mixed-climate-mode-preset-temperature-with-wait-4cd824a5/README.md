# Adjust heating or air conditioning · with a wait condition in the routine — Variant C

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Heating and cooling presets](../../../README.md#climate-profiles)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset; preset: “Default”) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset; preset: “\{\{ variable\_61.p \}\}”) → 3 more steps (selected steps; 4 other actions omitted). Start settings: to state: `on`, `off` / held for 10 s; 3 more triggers in the details.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_16`, `binary_sensor.example_17`; to state: `on`, `off`
- **2.** State change: `climate.example_03`; held for 00:00:10 (time format); attribute name: not available
- **3.** State change: `climate.example_03`; held for 00:00:10 (time format); attribute name: not available
- **4.** State change: `climate.example_03`; to state: `auto`, `heat`; held for 00:00:10 (time format)
- **5.** Home Assistant event: event: `start`
- **6.** Repeating schedule: minutes: /5

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Prepare 3 intermediate values; their contents/formulas are not described.

2. Check formula check: formula: “\{\{ states\(thermostat\) in \['auto','heat'\] and state\_attr\(thermostat,'temperature'\) is number and states\(variable\_60\) not in \['unknown','unavailable'\] \}\}”. If false, stop the current sequence here.

3. Prepare 3 intermediate values; their contents/formulas are not described.

4. Prepare 1 intermediate values; their contents/formulas are not described.

5. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: formula check: formula: “\{\{ variable\_62 or \(variable\_64 and not variable\_63\) \}\}”

   1. If all of: formula check: formula: “\{\{ not variable\_64 \}\}”:

      **Then:**

      1. Store some text — `input_text.example_08`; stored value: “\{\{ \{'t':state\_attr\(thermostat,'temperature'\),'m':states\(thermostat\),'p':state\_attr\(thermostat,'preset\_mode'\)\}\|to\_json \}\}”.

   2. If all of: formula check: formula: “\{\{ state\_attr\(thermostat,'preset\_mode'\) == 'boost' \}\}”:

      **Then:**

      1. Choose a heating or cooling preset — `climate.example_03`; preset: “Default”.

   3. If all of: formula check: formula: “\{\{ not is\_state\(thermostat,'heat'\) \}\}”:

      **Then:**

      1. Set the heating or cooling mode — `climate.example_03`; heating/cooling mode: `heat`.

   4. If all of: formula check: formula: “\{\{ state\_attr\(thermostat,'temperature'\) \!= 5 \}\}”:

      **Then:**

      1. Set the desired room temperature — `climate.example_03`; temperature setting (unit not given): 5.

   **Branch 2:** all of: formula check: formula: “\{\{ variable\_63 and variable\_64 \}\}”

   1. Set the heating or cooling mode — `climate.example_03`; heating/cooling mode: not available.

   2. If all of: formula check: formula: “\{\{ variable\_61.get\('p'\) not in \[none,'none','unknown','unavailable'\] and variable\_61.get\('p'\) in \(state\_attr\(thermostat,'preset\_modes'\) or \[\]\) and state\_attr\(thermostat,'preset\_mode'\) \!= variable\_61.p \}\}”:

      **Then:**

      1. Choose a heating or cooling preset — `climate.example_03`; preset: “\{\{ variable\_61.p \}\}”.

   3. Set the desired room temperature — `climate.example_03`; temperature setting (unit not given): not available.

   4. Wait until this formula is true: “\{\{ states\(thermostat\) == variable\_61.m and state\_attr\(thermostat,'temperature'\) == variable\_61.t \}\}”.

      Time limit: 00:00:20 (time format). Stop this sequence when the timeout expires.

   5. Store some text — `input_text.example_08`; stored value: “”.

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
