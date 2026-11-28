# Set the desired room temperature · with a wait condition in the routine — Variant C

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 7 more steps / prepare intermediate values → check conditions; stop this sequence if false → 6 more steps; 4 more branches. Start settings: from state: `off`; to state: `on` / to state: `on`; held for 2 min; 4 more triggers in the details. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_34`, `binary_sensor.example_28`, `binary_sensor.example_35`; from state: `off`; to state: `on`; trigger reference: not available
- **2.** State change: `binary_sensor.example_34`, `binary_sensor.example_28`, `binary_sensor.example_35`; to state: `on`; held for 00:02:00 (time format); trigger reference: not available
- **3.** Formula becomes true: held for 00:30:00 (time format); formula: “\{\{ \['binary\_sensor.example\_34', 'binary\_sensor.example\_28', 'binary\_sensor.example\_35'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 3 \}\}”; trigger reference: not available
- **4.** Scheduled time: at 08:00:00; trigger reference: not available
- **5.** Scheduled time: at 18:00:00; trigger reference: not available
- **6.** State change: `climate.example_01`; trigger reference: not available
- **7.** State change: `binary_sensor.example_22`; trigger reference: not available

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ states\('input\_text.example\_13'\) not in \['unknown','unavailable'\] \}\}”.

## Actual flow

The automation also prepares intermediate values; their contents/formulas are not described.

1. Prepare 1 intermediate values; their contents/formulas are not described.

2. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: formula check: formula: “\{\{ trigger.id == 'IDENTIFIER\_164' \}\}”

   1. Prepare 2 intermediate values; their contents/formulas are not described.

   2. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':variable\_66,'d':variable\_65.get\('d',''\)\}\|to\_json \}\}”.

   3. Check formula check: formula: “\{\{ variable\_66\|count &gt;= 4 and as\_timestamp\(now\(\)\) - \(variable\_66\[-1\]\|float\) &lt;= 600 \}\}”. If false, stop the current sequence here.

   4. Check formula check: formula: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. If false, stop the current sequence here.

   5. Check formula check: formula: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. If false, stop the current sequence here.

   6. Check formula check: formula: “\{\{ states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 21 \}\}”. If false, stop the current sequence here.

   7. Set the desired room temperature — `climate.example_01`; temperature setting (unit not given): 21; heating/cooling mode: `heat`.

   8. Wait until this formula is true: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 21 \}\}”.

      Time limit: 00:00:20 (time format). Stop this sequence when the timeout expires.

   9. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':variable\_66,'d':''\}\|to\_json \}\}”.

   **Branch 2:** all of: formula check: formula: “\{\{ trigger.id == 'IDENTIFIER\_165' \}\}”

   1. Prepare 1 intermediate values; their contents/formulas are not described.

   2. Check formula check: formula: “\{\{ is\_state\(trigger.entity\_id,'IDENTIFIER\_160'\) and as\_timestamp\(states\[trigger.entity\_id\].last\_changed\) &lt;= as\_timestamp\(now\(\)\) - 120 \}\}”. If false, stop the current sequence here.

   3. Check formula check: formula: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. If false, stop the current sequence here.

   4. Check formula check: formula: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. If false, stop the current sequence here.

   5. Check formula check: formula: “\{\{ states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 21 \}\}”. If false, stop the current sequence here.

   6. Set the desired room temperature — `climate.example_01`; temperature setting (unit not given): 21; heating/cooling mode: `heat`.

   7. Wait until this formula is true: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 21 \}\}”.

      Time limit: 00:00:20 (time format). Stop this sequence when the timeout expires.

   8. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':variable\_66,'d':''\}\|to\_json \}\}”.

   **Branch 3:** all of: formula check: formula: “\{\{ trigger.id in \['IDENTIFIER\_166','IDENTIFIER\_167'\] \}\}”

   1. Check formula check: formula: “\{\{ 8 &lt;= now\(\).hour &lt; 18 \}\}”. If false, stop the current sequence here.

   2. Check formula check: formula: “\{\{ \['binary\_sensor.example\_34', 'binary\_sensor.example\_28', 'binary\_sensor.example\_35'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 3 \}\}”. If false, stop the current sequence here.

   3. Check formula check: formula: “\{\{ \['binary\_sensor.example\_34', 'binary\_sensor.example\_28', 'binary\_sensor.example\_35'\] \| expand \| map\(attribute='last\_changed'\) \| map\('as\_timestamp'\) \| max &lt;= as\_timestamp\(now\(\)\) - 1800 \}\}”. If false, stop the current sequence here.

   4. Check formula check: formula: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. If false, stop the current sequence here.

   5. Check formula check: formula: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. If false, stop the current sequence here.

   6. Check formula check: formula: “\{\{ state\_attr\(thermostat,'temperature'\) &gt; 19 \}\}”. If false, stop the current sequence here.

   7. Set the desired room temperature — `climate.example_01`; temperature setting (unit not given): 19; heating/cooling mode: `heat`.

   8. Wait until this formula is true: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 19 \}\}”.

      Time limit: 00:00:20 (time format). Stop this sequence when the timeout expires.

   9. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':\[\],'d':day\}\|to\_json \}\}”.

   **Branch 4:** all of: formula check: formula: “\{\{ trigger.id == 'IDENTIFIER\_168' \}\}”

   1. Check formula check: formula: “\{\{ variable\_65.get\('d'\) == day and is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 19 \}\}”. If false, stop the current sequence here.

   2. Prepare 1 intermediate values; their contents/formulas are not described.

   3. Check formula check: formula: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. If false, stop the current sequence here.

   4. Check formula check: formula: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. If false, stop the current sequence here.

   5. Check formula check: formula: “\{\{ states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 21 \}\}”. If false, stop the current sequence here.

   6. Set the desired room temperature — `climate.example_01`; temperature setting (unit not given): 21; heating/cooling mode: `heat`.

   7. Wait until this formula is true: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 21 \}\}”.

      Time limit: 00:00:20 (time format). Stop this sequence when the timeout expires.

   8. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':variable\_66,'d':''\}\|to\_json \}\}”.

   **Branch 5:** all of: formula check: formula: “\{\{ trigger.id == 'IDENTIFIER\_169' \}\}”; formula check: formula: “\{\{ variable\_65.get\('d'\) and \(states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 19 or state\_attr\(thermostat,'preset\_mode'\) == 'boost'\) \}\}”

   1. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':variable\_65.get\('e',\[\]\),'d':''\}\|to\_json \}\}”.

   **Branch 6:** all of: formula check: formula: “\{\{ trigger.id == 'IDENTIFIER\_170' \}\}”; formula check: formula: “\{% set safe = \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 %\}\{\{ not safe \}\}”

   1. Store some text — `input_text.example_13`; stored value: “\{\{ \{'e':\[\],'d':''\}\|to\_json \}\}”.

   No default branch is configured.

## If it triggers again

`queued`: New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time. Limit for running and queued runs: 50.

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
