# Control media and cameras · with a delay in the routine

**English** · [Deutsch](README.de.md)

[Music, media and cameras](../../../README.md#media) → [Show a live camera view](../../../README.md#media-camera-live)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

If the configured conditions pass: (Play media → pause for 2 s 500 ms → 1 more step) → Save a camera picture → pause for not available (selected steps; 5 other actions omitted).

## What starts it?

Any enabled trigger below can start a run.

- **1.** Trigger type missing: `binary_sensor.example_17`; from state: unspecified (null); to state: not available
- **2.** Trigger type missing: `event.example_05`; to state: not available; attribute name: not available
- **3.** Trigger type missing: `binary_sensor.example_17`; to state: not available
- **4.** Trigger type missing: `ENTITY_43`, `DEVICE_49`; device event/action: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. If all of: condition type missing: `input_boolean.example_09`; state: not available:

   **Then:**

   1. Play media — `media_player.example_03`; media selection not available.

   2. Pause for 2 s 500 ms.

   3. Play media — `media_player.example_03`; media selection not available.

2. Save a camera picture — `camera.example_01`; file destination: not available.

3. Pause for not available.

4. Send a message to your own notification destination — `notify.example_04`; message text: not available; message title: not available.

5. Action type not available; message text: not available; message title: not available.

6. Turn on a stored on/off value — `input_boolean.example_03`, `input_boolean.example_04`.

7. If all of: condition type missing: `media_player.example_04`; state: not available:

   **Then:**

   1. Show a live camera view — `camera.example_01`; stream format: not available.

   2. Action type not available; message text: not available; message title: not available.

8. Action type not available — `ENTITY_44`, `DEVICE_50`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected camera with the picture or video function you need.
- A toggle helper: an on/off value stored in Home Assistant.
- A connected media player, such as a speaker.
- A configured notification destination, such as the Home Assistant app.
- A connected device that provides a suitable event as a trigger.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
