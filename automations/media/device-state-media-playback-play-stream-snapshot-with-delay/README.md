# Control media and cameras · with a delay in the routine

**English** · [Deutsch](README.de.md)

[Music, media and cameras](../../../README.md#media) → [Show a live camera view](../../../README.md#media-camera-live)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

If state: `off`: (Play media → pause for 2 s 500 ms → 1 more step) → Save a camera picture → pause for 1 s (selected steps; 5 other actions omitted). Start settings: to state: `on` / State change; 1 more trigger in the details.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `binary_sensor.example_29`; from state: unspecified (null); to state: `on`
- **2.** State change: `event.example_07`; to state: not available; attribute name: not available
- **3.** State change: `binary_sensor.example_29`; to state: `on`
- **4.** Device event: `ENTITY_41`, `DEVICE_48`; device event/action: `turned_on`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. If all of: state check: `input_boolean.example_07`; state: `off`:

   **Then:**

   1. Play media — `media_player.example_03`; media selection not available.

   2. Pause for 2 s 500 ms.

   3. Play media — `media_player.example_03`; media selection not available.

2. Save a camera picture — `camera.example_01`; file destination: not available.

3. Pause for 00:00:01 (time format).

4. Send a message to your own notification destination — `notify.example_02`; message text: “Es hat an person Haustür geklingelt.”; message title: “person”.

5. Send a message to your own notification destination — `notify.example_01`; message text: “Es hat an person Haustür geklingelt.”; message title: “person”.

6. Turn on a stored on/off value — `input_boolean.example_08`, `input_boolean.example_09`.

7. If all of: state check: `media_player.example_05`; state: `on`:

   **Then:**

   1. Show a live camera view — `camera.example_01`; stream format: `hls`.

   2. Send a message to your own notification destination — `notify.example_01`; message text: “Haustürkamera wird auf dem person TV angezeigt.”; message title: “person”.

8. Device action: `turn_on` — `ENTITY_42`, `DEVICE_49`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A connected camera with the picture or video function you need.
- The devices and action you want to add yourself.
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
