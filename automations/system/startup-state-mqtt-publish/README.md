# Send an MQTT message

**English** · [Deutsch](README.de.md)

[More routines and device actions](../../../README.md#system) → [MQTT messages](../../../README.md#system-mqtt)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Send an MQTT message. Start settings: State change / Home Assistant event.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `sensor.example_21`
- **2.** Home Assistant event: event: `start`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Send an MQTT message; MQTT topic: “awtrix\_58fb64/custom/youtube”; MQTT content: “\{"text":"\{\{ states\('sensor.example\_21'\) \}\}","textOffset":10,"center":false,"draw":\[\{"df":\[0,1,8,6,"\#FF0000"\]\},\{"dp":\[0,1,"\#000000"\]\},\{"dp":\[7,1,"\#000000"\]\},\{"dp":\[0,6,"\#000000"\]\},\{"dp":\[7,6,"\#000000"\]\},\{"dp":\[3,2,"\#FFFFFF"\]\},\{"dp":\[3,3,"\#FFFFFF"\]\},\{"dp":\[4,3,"\#FFFFFF"\]\},\{"dp":\[3,4,"\#FFFFFF"\]\}\]\}”.

## If it triggers again

`restart`: A new trigger stops the current run and starts it again, provided the automation's conditions pass.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- An MQTT integration set up to exchange messages between devices.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
