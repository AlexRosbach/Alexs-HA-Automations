# Turn off a switch · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn off](../../../README.md#switches-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for a value below 8 (up to 10 min; continue on timeout) → if the configured conditions pass: (Turn off a switch); otherwise: (Show a notice in Home Assistant; message text: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 …“; message title: “person-Steckdose bleibt an”) (selected steps; 3 other actions omitted). Includes condition checks before the actions.

## What starts it?

No trigger definition is included in this file.

## What must be true first?

Before the actions run: all of: state check: `sensor.example_23`; state: not available.

## Actual flow

1. Prepare 1 intermediate values; their contents/formulas are not described.

2. Run a configured web request — `rest_command.example_01`; simulation only: no; configured to continue after supported action errors; save the returned result for later steps.

3. If all of: formula check: formula: “\{\{ variable\_57 is not defined or variable\_57.status \!= 202 or not variable\_57.content.accepted \}\}”:

   **Then:**

   1. Show a notice in Home Assistant; message text: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 person 8 W mit aktuellen Messwerten melden. Bitte person oder person Programme prüfen.”; message title: “person-Steckdose bleibt an”.

   2. Stop this run with an error.

4. Wait for one of these triggers:

   - Numeric threshold crossing: `sensor.example_24`; below 8; held for 00:01:00 (time format)

   Time limit: 00:10:00 (time format). Continue with the next step when the timeout expires.

5. If all of: formula check: formula: “\{\{ wait.completed and states\('sensor.example\_23'\) in \['unavailable','unknown'\] and is\_number\(states\('sensor.example\_24'\)\) and 0 &lt;= states\('sensor.example\_24'\) \| float &lt; 8 and as\_timestamp\(states.sensor.example\_24.last\_updated\) &gt; request\_time \| float and as\_timestamp\(now\(\)\) - as\_timestamp\(states.sensor.example\_24.last\_reported\) &lt; 90 \}\}”:

   **Then:**

   1. Turn off a switch — `switch.example_15`.

   **Otherwise:**

   1. Show a notice in Home Assistant; message text: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 person 8 W mit aktuellen Messwerten melden. Bitte person oder person Programme prüfen.”; message title: “person-Steckdose bleibt an”.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Home Assistant to display the notices.
- A web request configured as a REST command in Home Assistant.
- A switch or smart socket in Home Assistant.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
