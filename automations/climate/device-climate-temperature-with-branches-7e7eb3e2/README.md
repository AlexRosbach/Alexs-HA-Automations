# Set the desired room temperature · with conditions in the routine — Variant A

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Repeat until conditions pass: Set the temperature to 5; heating/cooling mode: `off` → repeat until conditions pass: Set the temperature to 5; heating/cooling mode: `off` → if the configured conditions pass: (Set the temperature to 21; heating/cooling mode: `heat_cool`) → 1 more step (see full flow). Start settings: Device event.

## What starts it?

Any enabled trigger below can start a run.

- **1.** Device event: `ENTITY_31`, `DEVICE_40`; device event/action: `opened`
- **2.** Device event: `ENTITY_31`, `DEVICE_40`; device event/action: `not_opened`
- **3.** Device event: `ENTITY_32`, `DEVICE_41`; device event/action: `opened`
- **4.** Device event: `ENTITY_32`, `DEVICE_41`; device event/action: `not_opened`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Run at least once, then repeat until all of: device check: `ENTITY_31`, `DEVICE_40`; device event/action: not available.

   1. Set the desired room temperature — `climate.example_06`; temperature setting (unit not given): 5; heating/cooling mode: `off`.

2. Run at least once, then repeat until all of: device check: `ENTITY_31`, `DEVICE_40`; device event/action: not available.

   1. Set the desired room temperature — `climate.example_05`; temperature setting (unit not given): 5; heating/cooling mode: `off`.

3. If all of: device check: `ENTITY_32`, `DEVICE_41`; device event/action: not available:

   **Then:**

   1. Set the desired room temperature — `climate.example_06`; temperature setting (unit not given): 21; heating/cooling mode: `heat_cool`.

4. If all of: device check: `ENTITY_32`, `DEVICE_41`; device event/action: not available:

   **Then:**

   1. Set the desired room temperature — `climate.example_06`; temperature setting (unit not given): 21; heating/cooling mode: `heat_cool`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected thermostat or air conditioner.
- A connected device that provides a suitable event as a trigger.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
