# Turn off lights · with a wait condition in the routine — Variant B

**English** · [Deutsch](README.de.md)

[Lights](../../../README.md#lighting) → [Turn off](../../../README.md#lighting-off)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Wait for one of 2 triggers (up to 15 min; continue on timeout) → Turn off lights (selected steps; 9 other actions omitted). Start settings: held for 30 min. Includes condition checks before the actions.

## What starts it?

- **1.** State change: `sensor.example_22`; to state: not available; held for 00:30:00 (time format)

## What must be true first?

Before the actions run: all of: formula check: formula: “\{\{ is\_state\('switch.example\_08','IDENTIFIER\_160'\) or expand\(\['light.example\_10', 'light.example\_11', 'light.example\_12', 'light.example\_18', 'light.example\_19', 'light.example\_20'\]\)\|selectattr\('state','eq','IDENTIFIER\_160'\)\|list\|length&gt;0 \}\}”; formula check: formula: “\{\{ as\_timestamp\(now\(\)\) - as\_timestamp\(states\('input\_datetime.example\_01'\),0\)&gt;7200 \}\}”.

## Actual flow

1. Store a date or time — `input_datetime.example_01`; stored time: “\{\{ now\(\).timestamp\(\) \}\}”.

2. Prepare 2 intermediate values; their contents/formulas are not described.

3. Send a message to your own notification destination — `notify.example_01`; message text: “Du bist seit 30 Minuten im Schlafzimmer. Soll ich das Büro person ausschalten?”; message title: “Büro ausschalten?”.

4. Wait for one of these triggers:

   - Event: event name: not available
   - Event: event name: not available

   Time limit: 00:15:00 (time format). Continue with the next step when the timeout expires.

5. Send a message to your own notification destination — `notify.example_01`; message text: “clear\_notification”.

6. Check formula check: formula: “\{\{ wait.trigger is not none and wait.trigger.event.example\_05.action==variable\_58 \}\}”. If false, stop the current sequence here.

7. Check state check: `sensor.example_22`; state: not available. If false, stop the current sequence here.

8. Check state check: `binary_sensor.example_27`; state: `off`. If false, stop the current sequence here.

9. Turn off lights — `light.example_10`, `light.example_11`, `light.example_12`, `light.example_18`, `light.example_19`, `light.example_20`.

10. Run your own script — `script.example_07`; configured to continue after supported action errors.

11. If all of: state check: `switch.example_08`; state: `on`:

    **Then:**

    1. Run your own script — `script.example_08`.

## If it triggers again

`single`: If it triggers again while running, the new run is not started.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- The devices and action you want to add yourself.
- A helper that stores a date or time.
- Lights that Home Assistant can control.
- A configured notification destination, such as the Home Assistant app.
- An existing Home Assistant script: a saved sequence of actions.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
