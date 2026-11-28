# Turn off a switch

**English** · [Deutsch](README.de.md)

[Switches and sockets](../../../README.md#switches) → [Turn off](../../../README.md#switches-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Turn off a switch. Start settings: held for 10 min.

## What starts it?

- **1.** Formula becomes true: held for 00:10:00 (time format); formula: “\{\{ states\('sensor.example\_31'\)\|is\_number and states\('input\_number.example\_02'\)\|float\(65\)&gt;states\('input\_number.example\_03'\)\|float\(60\) and states\('sensor.example\_31'\)\|float\(100\)&lt;states\('input\_number.example\_03'\)\|float\(60\) \}\}”

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Turn off a switch — `switch.example_16`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A switch or smart socket in Home Assistant.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
