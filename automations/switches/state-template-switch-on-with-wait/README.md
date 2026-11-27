# Turn on a switch · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn on](../../../README.md#switches-on)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value → check conditions; stop this sequence if false → 4 more steps. Start settings: held for 8 min / held for 20 s.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: held for 8 min; formula: not available; trigger reference: `ID_24`
- **2.** Trigger type missing: `sensor.example_16`; to state: not available; held for 20 s; trigger reference: `ID_25`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

The automation also prepares intermediate values; their contents/formulas are not described.

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: formula: not available

   1. Turn on a stored on/off value — `input_boolean.example_11`.

   **Branch 2:** all of: condition type missing: formula: not available; condition type missing: formula: not available

   1. Turn off a stored on/off value — `input_boolean.example_11`.

   2. Check condition type missing: formula: not available. If false, stop the current sequence here.

   3. Check condition type missing: `switch.example_08`; state: not available. If false, stop the current sequence here.

   4. Wait until a formula is true; the formula is not available.

      Time limit: 30 s. Stop this sequence when the timeout expires.

   5. Ask a spoken question — `assist_satellite.example_01`; announcement tone: yes; answer choices: 2; answer phrases not available; configured to continue after supported action errors; save the returned result for later steps.

   6. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: condition type missing: formula: not available

      1. Turn on a switch — `switch.example_08`.

      **Branch 2:** all of: condition type missing: formula: not available

      1. Stop this run.

      No default branch is configured.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A voice device set up in Home Assistant.
- A toggle helper: an on/off value stored in Home Assistant.
- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
