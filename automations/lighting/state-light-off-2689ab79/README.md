# Turn off lights — Variant A

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn off](../../../README.md#lighting-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Turn off lights; transition: 15 s. Start settings: to state: `off`; held for 30 min. Includes condition checks before the actions.

## What starts it?

- **1.** State change: `binary_sensor.example_12`; to state: `off`; held for 30 min

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ state\_attr\('automation.example\_03', 'current'\) \| int\(0\) == 0 and state\_attr\('automation.example\_04', 'current'\) \| int\(0\) == 0 and is\_state\('input\_boolean.example\_03', 'IDENTIFIER\_159'\) \}\}”.

## Actual flow

1. Turn off lights — `light.example_01`; transition: 15 s.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

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
