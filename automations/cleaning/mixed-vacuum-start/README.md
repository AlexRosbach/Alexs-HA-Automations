# Start a robot vacuum

**English** · [Deutsch](README.de.md)

[Robot vacuums](../../../README.md#cleaning) → [Start cleaning](../../../README.md#cleaning-start)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Start a robot vacuum → Reset a counter. Start settings: above 2 / at 08:00:00; 1 more trigger in the details. Includes condition checks before the actions.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Numeric threshold crossing: `counter.example_03`; above 2
- **2.** Scheduled time: at 08:00:00
- **3.** State change: `input_boolean.example_01`; to state: `off`

## What must be true first?

Before the actions run: all of: number check: `counter.example_03`; above 6; state check: `input_boolean.example_01`; state: `off`; time check: before 18:00:00; after 08:00:00.

## Actual flow

1. Start a robot vacuum — `vacuum.example_01`.

2. Reset a counter — `counter.example_03`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A counter helper in Home Assistant.
- A robot vacuum connected to Home Assistant.
- A suitable sensor or other number in Home Assistant, and the limit you want to use.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
