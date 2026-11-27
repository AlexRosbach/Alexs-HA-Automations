# Change stored on/off values · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Counters and stored values](../../../README.md#helpers) → [Virtual switches](../../../README.md#helpers-switches)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `switch.example_14`; from state: not available; to state: not available; trigger reference: `ID_28`
- **2.** Trigger type missing: `switch.example_14`; from state: not available; to state: not available; trigger reference: `ID_28`
- **3.** Trigger type missing: at not available; trigger reference: `ID_29`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: trigger reference: `ID_28`; condition type missing: formula: not available

   1. Turn on a stored on/off value — `input_boolean.example_12`.

   **Branch 2:** all of: condition type missing: trigger reference: `ID_29`

   1. Turn off a stored on/off value — `input_boolean.example_12`.

   No default branch is configured.

## If it triggers again

`queued`: New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time. Limit for running and queued runs: 10.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A toggle helper: an on/off value stored in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
