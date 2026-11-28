# Turn fans on and off and adjust their settings · with a wait condition in the routine

**English** · [Deutsch](README.de.md)

[Fans and air purifiers](../../../README.md#ventilation) → [Choose a preset](../../../README.md#ventilation-profiles)

[Browse all automations](../../../README.md#automation-catalogue) · [Set up step by step](../../../how-to/get-started.md)

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

Use the first matching branch: prepare intermediate values → Turn on a fan → 5 more steps / prepare intermediate values → Turn on a fan → 5 more steps; 1 more branch. Start settings: to state: `cleaning`.

## What starts it?

Any enabled trigger below can start a run.

- **1.** State change: `vacuum.example_06`; to state: `cleaning`; trigger reference: not available
- **2.** State change: `vacuum.example_05`; to state: `cleaning`; trigger reference: not available
- **3.** State change: `vacuum.example_02`; to state: `cleaning`; trigger reference: not available

## What must be true first?

No top-level conditions are configured. Checks inside the steps still apply.

## Actual flow

1. Use the first matching branch; later branches in this choice are skipped.

   **Branch 1:** all of: trigger-reference check: trigger reference: not available

   1. Prepare 2 intermediate values; their contents/formulas are not described.

   2. Turn on a fan — `fan.example_02`.

   3. Choose a fan preset — `fan.example_02`; preset: “turbo”.

   4. Start these paths in parallel. Their execution order is not guaranteed.

      **Parallel path 1:**

      1. Send a message to your own notification destination — `notify.example_01`; message text: “Büro: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; message title: “person Turbo”.

      **Parallel path 2:**

      1. Send a message to your own notification destination — `notify.example_02`; message text: “Büro: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; message title: “person Turbo”.

   5. Wait for one of these triggers:

      - State change: `vacuum.example_06`; from state: `cleaning`
      - State change: `vacuum.example_06`; from state: `returning`
      - Event: event name: not available

      Time limit: 04:00:00 (time format). Continue with the next step when the timeout expires.

   6. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' \}\}”

      1. Send a message; message text: “Büro: person-Automatik für diese Roboter-Reinigung wurde abgebrochen.”; message title: “person-Steuerung gestoppt”.

      No default branch is configured.

   7. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ previous\_fan\_state == 'IDENTIFIER\_159' \}\}”

      1. Turn off a fan — `fan.example_02`.

      **Branch 2:** all of: formula check: formula: “\{\{ previous\_fan\_preset not in \[none, 'unknown', 'unavailable', ''\] \}\}”

      1. Choose a fan preset — `fan.example_02`; preset: “\{\{ previous\_fan\_preset \}\}”.

      **If no branch matches:**

      1. Choose a fan preset — `fan.example_02`; preset: “auto”.

   **Branch 2:** all of: trigger-reference check: trigger reference: not available

   1. Prepare 2 intermediate values; their contents/formulas are not described.

   2. Turn on a fan — `fan.example_01`.

   3. Choose a fan preset — `fan.example_01`; preset: “turbo”.

   4. Start these paths in parallel. Their execution order is not guaranteed.

      **Parallel path 1:**

      1. Send a message to your own notification destination — `notify.example_01`; message text: “Schlafzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; message title: “person Turbo”.

      **Parallel path 2:**

      1. Send a message to your own notification destination — `notify.example_02`; message text: “Schlafzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; message title: “person Turbo”.

   5. Wait for one of these triggers:

      - State change: `vacuum.example_05`; from state: `cleaning`
      - State change: `vacuum.example_05`; from state: `returning`
      - Event: event name: not available

      Time limit: 04:00:00 (time format). Continue with the next step when the timeout expires.

   6. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' \}\}”

      1. Send a message; message text: “Schlafzimmer: person-Automatik für diese Roboter-Reinigung wurde abgebrochen.”; message title: “person-Steuerung gestoppt”.

      No default branch is configured.

   7. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ previous\_fan\_state == 'IDENTIFIER\_159' \}\}”

      1. Turn off a fan — `fan.example_01`.

      **Branch 2:** all of: formula check: formula: “\{\{ previous\_fan\_preset not in \[none, 'unknown', 'unavailable', ''\] \}\}”

      1. Choose a fan preset — `fan.example_01`; preset: “\{\{ previous\_fan\_preset \}\}”.

      **If no branch matches:**

      1. Choose a fan preset — `fan.example_01`; preset: “auto”.

   **Branch 3:** all of: trigger-reference check: trigger reference: not available

   1. Prepare 2 intermediate values; their contents/formulas are not described.

   2. Turn on a fan — `fan.example_03`.

   3. Choose a fan preset — `fan.example_03`; preset: “turbo”.

   4. Start these paths in parallel. Their execution order is not guaranteed.

      **Parallel path 1:**

      1. Send a message to your own notification destination — `notify.example_01`; message text: “Wohnzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; message title: “person Turbo”.

      **Parallel path 2:**

      1. Send a message to your own notification destination — `notify.example_02`; message text: “Wohnzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; message title: “person Turbo”.

   5. Wait for one of these triggers:

      - State change: `vacuum.example_02`; from state: `cleaning`
      - State change: `vacuum.example_02`; from state: `returning`
      - Event: event name: not available

      Time limit: 04:00:00 (time format). Continue with the next step when the timeout expires.

   6. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' \}\}”

      1. Send a message; message text: “Wohnzimmer: person-Automatik für diese Roboter-Reinigung wurde abgebrochen.”; message title: “person-Steuerung gestoppt”.

      No default branch is configured.

   7. Use the first matching branch; later branches in this choice are skipped.

      **Branch 1:** all of: formula check: formula: “\{\{ previous\_fan\_state == 'IDENTIFIER\_159' \}\}”

      1. Turn off a fan — `fan.example_03`.

      **Branch 2:** all of: formula check: formula: “\{\{ previous\_fan\_preset not in \[none, 'unknown', 'unavailable', ''\] \}\}”

      1. Choose a fan preset — `fan.example_03`; preset: “\{\{ previous\_fan\_preset \}\}”.

      **If no branch matches:**

      1. Choose a fan preset — `fan.example_03`; preset: “auto”.

   No default branch is configured.

## If it triggers again

`parallel`: Each new trigger can start an independent run alongside existing runs. Limit for running and queued runs: 6.

Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.

Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).

## What do I need?

Home Assistant and these devices or features:

- A fan or air purifier that Home Assistant can control.
- The devices and action you want to add yourself.
- A configured notification destination, such as the Home Assistant app.
- A value or state whose change should start the routine, for example from a device, sensor or helper.

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/get-started.md).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
