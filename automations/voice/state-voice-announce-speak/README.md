# Use announcements and spoken text

**English** · [Deutsch](README.de.md)

[Voice and announcements](../../../README.md#voice) → [Announcements and spoken text](../../../README.md#voice-announcements)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An automation from Alex's Home Assistant setup, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Run 7 paths in parallel.

## What starts it?

- **1.** Trigger type missing: `binary_sensor.example_26`; to state: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Start these paths in parallel. Their execution order is not guaranteed.

   **Parallel path 1:**

   1. Action type not available; message text: not available; message title: not available; configured to continue after supported action errors.

   **Parallel path 2:**

   1. Send a message to your own notification destination — `notify.example_04`; message text: not available; message title: not available; configured to continue after supported action errors.

   **Parallel path 3:**

   1. Show a notice in Home Assistant; message text: not available; message title: not available.

   **Parallel path 4:**

   1. Play an announcement — `assist_satellite.example_02`; message text: not available; announcement tone: yes; configured to continue after supported action errors.

   **Parallel path 5:**

   1. Play an announcement — `assist_satellite.example_03`; message text: not available; announcement tone: yes; configured to continue after supported action errors.

   **Parallel path 6:**

   1. Play an announcement — `assist_satellite.example_01`; message text: not available; announcement tone: yes; configured to continue after supported action errors.

   **Parallel path 7:**

   1. Read text aloud — `tts.example_01`, not available; message text: not available; speech language: not available; configured to continue after supported action errors.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A voice device set up in Home Assistant.
- A configured notification destination, such as the Home Assistant app.
- Home Assistant to display the notices.
- Text-to-speech set up with a suitable media player.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
