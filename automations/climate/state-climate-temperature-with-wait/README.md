# Set the desired room temperature · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Heating and cooling](../../../README.md#climate) → [Set the temperature](../../../README.md#climate-temperature)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Set the temperature to 24; heating/cooling mode: `heat` → wait for from state: `on`; to state: `off` (up to 3 h; continue on timeout) → Set the temperature to 21; heating/cooling mode: `auto` (selected steps; 10 other actions omitted). Start settings: to state: `on`.

## What starts it?

- **1.** State change: `input_boolean.example_03`; to state: `on`

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Turn on a stored on/off value — `input_boolean.example_04`.

2. Turn on lights — `light.example_01`; brightness: 60%; transition: 2 s; colour values: 200, 0, 255.

3. Turn off a switch — `switch.example_01`, `switch.example_03`.

4. Disable another automation — `automation.example_05`, `automation.example_03`; stop affected running actions: yes.

5. Set the volume — `media_player.example_02`; volume (0–1): 0.2.

6. Play media — `media_player.example_02`; media selection not available.

7. Set the desired room temperature — `climate.example_02`; temperature setting (unit not given): 24; heating/cooling mode: `heat`.

8. Wait for one of these triggers:

   - State change: `input_boolean.example_03`; from state: `on`; to state: `off`

   Time limit: 3 h. Continue with the next step when the timeout expires.

9. Turn on lights — `light.example_01`; brightness: 60%; transition: 5 s; colour temperature: 6500 K.

10. Enable another automation — `automation.example_05`, `automation.example_03`.

11. Set the desired room temperature — `climate.example_02`; temperature setting (unit not given): 21; heating/cooling mode: `auto`.

12. Pause media — `media_player.example_02`.

13. Turn off a stored on/off value — `input_boolean.example_04`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- The other automations you want to start or control.
- A connected thermostat or air conditioner.
- A toggle helper: an on/off value stored in Home Assistant.
- Lights that Home Assistant can control.
- A connected media player, such as a speaker.
- A switch or smart socket in Home Assistant.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
