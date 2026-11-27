# Turn on or toggle lights · with conditions in the routine

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Toggle](../../../README.md#lighting-toggle)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Turn on lights; brightness change: 10% / Turn on lights; brightness change: -10%; 1 more branch.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `event.example_07`; trigger reference: `ID_19`
- **2.** Trigger type missing: `event.example_08`; trigger reference: `ID_20`
- **3.** Trigger type missing: `event.example_09`; trigger reference: `ID_21`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: condition type missing: trigger reference: `ID_19`

   1. Turn on lights — `light.example_16`; brightness change: 10%.

   **Branch 2:** all of: condition type missing: trigger reference: `ID_20`

   1. Turn on lights — `light.example_16`; brightness change: -10%.

   **Branch 3:** all of: condition type missing: trigger reference: `ID_21`

   1. Switch lights between on and off — `light.example_16`.

   No default branch is configured.

## If it triggers again

`queued`: New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time. Limit for running and queued runs: 10.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
