# Turn lights on and off · with conditions in the routine — Variant C

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn on and off](../../../README.md#lighting-on-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: Turn on a switch → Turn on lights / Turn off a switch → if the configured conditions pass: (Turn off lights). Start settings: from state: `off`; to state: `on`; held for 1 min / to state: `off`; held for 5 min. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_31`; from state: `off`; to state: `on`; held for 1 min; trigger reference: not available
- **2.** State change: `binary_sensor.example_31`; to state: `off`; held for 5 min; trigger reference: not available

## What must be true first?

Before the actions run: all of: state check: `input_boolean.example_03`; state: `off`.

## Actual flow

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: trigger-reference check: trigger reference: not available

   1. Turn on a switch — `switch.example_03`.

   2. Turn on lights — `light.example_01`.

   **Branch 2:** all of: trigger-reference check: trigger reference: not available

   1. Turn off a switch — `switch.example_03`.

   2. If all of: formula check: formula: “\{\{ state\_attr\('automation.example\_04', 'current'\) \| int\(0\) == 0 \}\}”:

      **Then:**

      1. Turn off lights — `light.example_01`.

   No default branch is configured.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- Lights that Home Assistant can control.
- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
