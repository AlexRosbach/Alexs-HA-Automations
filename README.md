# Alex's Home Assistant Automations

**English** · [Deutsch](README.de.md)

Hi, I'm Alex. Here I share **automations from my own Home Assistant setup**. If you are looking for ideas for your smart home, have a look around and use them as inspiration for your own routines.

The collection covers things like lighting, heating, robot vacuums and notifications. Each automation explains its actual sequence, settings and conditions so you can understand my idea and adapt it to your devices. **Door and lock control is excluded from this public collection.**

**[Explore my automations](#automation-catalogue)** · **[New to Home Assistant? Start here](how-to/get-started.md)**

> **About the shared files:** I have removed private details from my setup and replaced them with placeholders. Some triggers, conditions and formulas also need to be filled in or rebuilt. These files show the ideas behind my automations; they need your own settings before you can use them.

## New to Home Assistant? Start here

An automation follows a simple idea:

> **When** something happens, **then** Home Assistant does something.
>
> For example: When a time you choose is reached, turn on a light.

The **[step-by-step guide](how-to/get-started.md)** shows you how to build this small exercise in the Home Assistant interface. You can then add ideas from this collection.

## Take an idea and make it your own

1. **Choose an idea.** Open a category below, such as Lighting, then pick a task, such as turning lights on or off.
2. **Read the explanation.** Each example explains its intended task, what starts it and what you need to change.
3. **Build and test it with your devices.** Add the steps in Home Assistant and try them with one device first.

### Three of my automations to explore

| What the shared automation contains | Read the actual sequence |
| --- | --- |
| A 30-minute state duration, an additional condition and a light-off action with a 15-second fade | [Light-off routine](automations/lighting/state-light-off-22ac0c06/README.md) |
| An upper sensor limit of 10, switch-on, a wait for a value below 5 with a 60-minute timeout, then switch-off | [Switch with two thresholds](automations/switches/threshold-switch-on-off-with-wait/README.md) |
| Temperature settings of 24 and 21 separated by a wait of up to 3 hours, plus lighting, media and helper actions | [Combined climate routine](automations/climate/state-climate-temperature-with-wait/README.md) |

These descriptions use values that remain in the shared files. Each page also says which trigger details, conditions or formulas were removed by the earlier export. Missing details are not guessed; they need to be restored from the original automation or chosen for your own setup.

<a id="terms-explained"></a>

## Useful terms, simply explained

| Term | What it means |
| --- | --- |
| **Automation** | A routine that Home Assistant starts automatically. |
| **Trigger** | What starts the routine, such as a time or a change in a sensor reading. |
| **Condition** | An extra requirement, such as “only when it is dark”. |
| **Action** | What should happen, such as turning on a light. |
| **Entity** | One function or reading, such as a light or a temperature sensor. |
| **Placeholder** | An example value you replace with your own setting. |
| **YAML** | The settings written as text. In this collection, they are in `automation.yaml`. |

**Names and messages:** Readable, neutral entity names and ordinary notification text can stay. Personal names, identifying phone models and credentials are cleaned. Existing missing text cannot be recovered from the shared files.

**Which file should I open?** Start with an example's explanation in `README.md`. `README.de.md` has the same guide in German. `automation.yaml` contains the routine as text; `metadata.json` is used to build the catalogue automatically.

<!-- catalogue:start -->

<a id="automation-catalogue"></a>

## Shared automations (131 automations)

The shared automations are grouped into **11 categories and 36 subcategories** based on what they do.

Choose a category below and expand it. The links inside take you straight to the task you want. Then open an example to see what it does and how you could adapt it to your home.

Some routines have several variants. The letters help you tell them apart; they refer to different configurations, not particular rooms or devices.

| Category | Automations | Subcategories |
| --- | ---: | --- |
| [Heating and cooling](#climate) | 18 | Set the temperature · Heating and cooling modes · Heating and cooling presets |
| [Lights](#lighting) | 29 | Turn on · Turn off · Toggle · Turn on and off · Scenes |
| [Fans and air purifiers](#ventilation) | 4 | Turn on and off · Set the speed · Choose a preset |
| [Robot vacuums](#cleaning) | 8 | Start cleaning · Set suction power · Clean selected areas |
| [Music, media and cameras](#media) | 2 | Save camera pictures · Show a live camera view |
| [Task lists and reminders](#tasks) | 13 | Read task lists · Edit tasks · Remove tasks |
| [Switches and sockets](#switches) | 16 | Turn on · Turn off · Toggle · Turn on and off |
| [Voice and announcements](#voice) | 1 | Announcements and spoken text |
| [Messages and notices](#notifications) | 11 | Send messages · Notices in Home Assistant |
| [Counters and stored values](#helpers) | 6 | Virtual switches · Change counters · Store text |
| [More routines and device actions](#system) | 23 | Your own scripts · Device functions and buttons · MQTT messages · Control other automations · Get weather data · Maintenance and logs · Actions to set up |

<a id="climate"></a>

<details>
<summary><strong>Heating and cooling</strong> · 18 automations</summary>

**Jump to:** [Set the temperature (9)](#climate-temperature) · [Heating and cooling modes (4)](#climate-modes) · [Heating and cooling presets (5)](#climate-profiles)

<a id="climate-temperature"></a>

#### Set the temperature (9 automations)

| Automation | What happens? |
| --- | --- |
| [Set the desired room temperature · with conditions in the routine — Variant A](automations/climate/device-climate-temperature-with-branches-54a60709/README.md) | Repeat until conditions pass: Set the temperature to 5 → repeat until conditions pass: Set the temperature to 5 → if the configured conditions pass: (Set the temperature to 21) → 1 more step (see full flow). |
| [Set the desired room temperature · with conditions in the routine — Variant B](automations/climate/device-climate-temperature-with-branches-c104c302/README.md) | Repeat until conditions pass: Set the temperature to 5 → repeat until conditions pass: Set the temperature to 5 → if the configured conditions pass: (Set the temperature to 21) → 1 more step (see full flow). |
| [Set the desired room temperature · with conditions in the routine](automations/climate/mixed-climate-temperature-with-branches/README.md) | Check conditions; stop this sequence if false → if the configured conditions pass: (Set the desired room temperature) → Turn off a stored on/off value. Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine — Variant A](automations/climate/mixed-climate-temperature-with-wait-a3321799/README.md) | Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 7 more steps / prepare intermediate values → check conditions; stop this sequence if false → 6 more steps; 4 more branches. Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine — Variant B](automations/climate/mixed-climate-temperature-with-wait-f1451717/README.md) | Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 8 more steps / prepare intermediate values → check conditions; stop this sequence if false → 7 more steps; 4 more branches. Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine — Variant C](automations/climate/mixed-climate-temperature-with-wait-fc1f1012/README.md) | Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 7 more steps / prepare intermediate values → check conditions; stop this sequence if false → 6 more steps; 4 more branches. Includes condition checks before the actions. |
| [Set the desired room temperature · with conditions in the routine — Variant A](automations/climate/scheduled-climate-temperature-with-branches-47c2e215/README.md) | If the configured conditions pass: (Set the temperature to 5); otherwise: (Set the temperature to 20). |
| [Set the desired room temperature · with conditions in the routine — Variant B](automations/climate/scheduled-climate-temperature-with-branches-5aaa8edc/README.md) | Store some text → if the configured conditions pass: (Store some text → Store a number → 2 more steps). Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine](automations/climate/state-climate-temperature-with-wait/README.md) | Set the temperature to 24 → wait for another trigger (up to 3 h; continue on timeout) → Set the temperature to 21 (selected steps; 10 other actions omitted). |

<a id="climate-modes"></a>

#### Heating and cooling modes (4 automations)

| Automation | What happens? |
| --- | --- |
| [Adjust heating or air conditioning · with conditions in the routine — Variant A](automations/climate/state-climate-mode-temperature-with-branches-049416bb/README.md) | Use the first matching branch: check conditions; stop this sequence if false → Set the temperature to 5 → 1 more step / Set the heating or cooling mode → Set the temperature to 21. |
| [Adjust heating or air conditioning · with conditions in the routine — Variant B](automations/climate/state-climate-mode-temperature-with-branches-104d0276/README.md) | Use the first matching branch: check conditions; stop this sequence if false → Set the temperature to 5 → 1 more step / check conditions; stop this sequence if false → Set the heating or cooling mode → 1 more step. |
| [Adjust heating or air conditioning · with conditions in the routine — Variant C](automations/climate/state-climate-mode-temperature-with-branches-6016b2ee/README.md) | Use the first matching branch: Set the temperature to 5 → Set the heating or cooling mode; otherwise: Set the heating or cooling mode → Set the temperature to 21. Includes condition checks before the actions. |
| [Adjust heating or air conditioning · with conditions in the routine — Variant D](automations/climate/state-climate-mode-temperature-with-branches-75cb761b/README.md) | Use the first matching branch: Set the temperature to 5 → Set the heating or cooling mode / Set the heating or cooling mode → Set the temperature to 21. |

<a id="climate-profiles"></a>

#### Heating and cooling presets (5 automations)

| Automation | What happens? |
| --- | --- |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant A](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-3b582a19/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset) → 3 more steps (selected steps; 4 other actions omitted). |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant B](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-6037647c/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset) → 3 more steps (selected steps; 4 other actions omitted). |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant C](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-b8c21183/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset) → 3 more steps (selected steps; 4 other actions omitted). |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant D](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-d46bf28e/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset) → 3 more steps (selected steps; 4 other actions omitted). |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant E](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-f9d2161c/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset) → 3 more steps (selected steps; 4 other actions omitted). |


</details>

<a id="lighting"></a>

<details>
<summary><strong>Lights</strong> · 29 automations</summary>

**Jump to:** [Turn on (2)](#lighting-on) · [Turn off (7)](#lighting-off) · [Toggle (6)](#lighting-toggle) · [Turn on and off (13)](#lighting-on-off) · [Scenes (1)](#lighting-scenes)

<a id="lighting-on"></a>

#### Turn on (2 automations)

| Automation | What happens? |
| --- | --- |
| [Turn on lights · with a delay in the routine](automations/lighting/state-light-on-with-delay/README.md) | Turn on lights at 5% brightness → if the configured conditions pass: (Turn on a switch → pause for 5 min → 1 more step). Includes condition checks before the actions. |
| [Turn on lights · with a wait condition in the routine](automations/lighting/state-light-on-with-wait/README.md) | Wait for one of 2 triggers (stop on timeout) → use the first matching branch: Turn on lights at 100% brightness; transition: 3 s (selected steps; 2 other actions omitted). |

<a id="lighting-off"></a>

#### Turn off (7 automations)

| Automation | What happens? |
| --- | --- |
| [Turn off lights](automations/lighting/scheduled-light-off/README.md) | Turn off lights → Turn off a switch → Turn off a switch. |
| [Turn off lights — Variant A](automations/lighting/state-light-off-22ac0c06/README.md) | Turn off lights; transition: 15 s. Start settings: held for 30 min. Includes condition checks before the actions. |
| [Turn off lights — Variant B](automations/lighting/state-light-off-7cb13cdd/README.md) | Turn off lights. |
| [Turn off lights · with a wait condition in the routine — Variant A](automations/lighting/state-light-off-with-wait-4dccd971/README.md) | Wait for one of 11 triggers (continue on timeout) → use the first matching branch: Turn off lights → disabled: Turn off a switch → 2 more steps / Action type not available → Send a message to your own notification destination; 1 more branch; otherwise: Action type not available → Send a message to your own notification destination → 2 more steps (selected steps; 3 other actions omitted). Includes condition checks before the actions. |
| [Turn off lights · with a wait condition in the routine — Variant B](automations/lighting/state-light-off-with-wait-6fcc8f29/README.md) | Wait for one of 2 triggers (continue on timeout) → use the first matching branch: Turn off lights → Run your own script → 3 more steps / Action type not available → Send a message to your own notification destination; otherwise: Action type not available → Send a message to your own notification destination → 3 more steps (selected steps; 3 other actions omitted). Includes condition checks before the actions. |
| [Turn off lights · with a wait condition in the routine — Variant C](automations/lighting/state-light-off-with-wait-b05993d4/README.md) | Pause for 30 min → wait for one of 2 triggers (continue on timeout) → use the first matching branch: Turn off lights → Run your own script → 3 more steps / Action type not available → Send a message to your own notification destination; otherwise: Action type not available → Send a message to your own notification destination → 3 more steps (selected steps; 4 other actions omitted). |
| [Turn off lights · with a wait condition in the routine — Variant D](automations/lighting/state-light-off-with-wait-b5e8441e/README.md) | Wait for one of 2 triggers (continue on timeout) → Turn off lights (selected steps; 9 other actions omitted). Includes condition checks before the actions. |

<a id="lighting-toggle"></a>

#### Toggle (6 automations)

| Automation | What happens? |
| --- | --- |
| [Switch lights between on and off — Variant A](automations/lighting/device-light-toggle-3c5800f8/README.md) | Switch lights between on and off; brightness: 81%. |
| [Switch lights between on and off — Variant B](automations/lighting/device-light-toggle-835102aa/README.md) | Switch lights between on and off; brightness: 76%. |
| [Switch lights between on and off — Variant C](automations/lighting/device-light-toggle-8feb4762/README.md) | Switch lights between on and off; brightness: 76%; transition: 1 s. |
| [Switch lights between on and off — Variant D](automations/lighting/device-light-toggle-f2e96056/README.md) | Switch lights between on and off; brightness: 76%; transition: 1 s. |
| [Turn on or toggle lights · with conditions in the routine](automations/lighting/state-light-on-toggle-with-branches/README.md) | Use the first matching branch: Turn on lights; brightness change: 10% / Turn on lights; brightness change: -10%; 1 more branch. |
| [Switch lights between on and off](automations/lighting/triggered-light-toggle/README.md) | Switch lights between on and off; brightness: 76%. |

<a id="lighting-on-off"></a>

#### Turn on and off (13 automations)

| Automation | What happens? |
| --- | --- |
| [Turn lights on and off · with conditions in the routine — Variant A](automations/lighting/device-light-on-off-with-branches-1c0d2b3a/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). |
| [Turn lights on and off · with conditions in the routine — Variant B](automations/lighting/device-light-on-off-with-branches-5d21fa0b/README.md) | If the configured conditions pass: (use the first matching branch: Turn on lights at 86% brightness; transition: 1 s; colour temperature: 4000 K → Run your own script / Turn off lights; transition: 2 s → Run your own script) → use the first matching branch: Turn on a fan / Turn off a fan. |
| [Turn lights on and off · with conditions in the routine — Variant C](automations/lighting/device-light-on-off-with-branches-6fe09721/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). |
| [Turn lights on and off · with conditions in the routine — Variant D](automations/lighting/device-light-on-off-with-branches-c0980148/README.md) | If below 10: (Turn on lights at 5% brightness); otherwise: (Turn off lights). Start limits: below 10 / above 10. |
| [Turn lights on and off · with conditions in the routine — Variant E](automations/lighting/device-light-on-off-with-branches-fc5d4c73/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). |
| [Turn lights on and off · with conditions in the routine](automations/lighting/mqtt-light-on-off-with-branches/README.md) | Use the first matching branch: Turn on lights at 76% brightness → Run your own script → 2 more steps / if the configured conditions pass: (Start an existing script) → Run your own script → 2 more steps. |
| [Turn lights on and off · with conditions in the routine — Variant A](automations/lighting/state-light-on-off-with-branches-26b32a95/README.md) | If the configured conditions pass: (Turn on lights at 70% brightness → if the configured conditions pass: (Turn on lights at 100% brightness; transition: 3 s)); otherwise: (Turn off lights → if the configured conditions pass: (Turn on lights at 10% brightness; transition: 30 s); otherwise: (Turn off lights; transition: 5 s)). |
| [Turn lights on and off · with conditions in the routine — Variant B](automations/lighting/state-light-on-off-with-branches-a4561b61/README.md) | If the configured conditions pass: (Turn on lights at 70% brightness); otherwise: (Turn off lights). |
| [Turn lights on and off · with conditions in the routine — Variant C](automations/lighting/state-light-on-off-with-branches-af2a0600/README.md) | Use the first matching branch: Turn on a switch → Turn on lights / Turn off a switch → if the configured conditions pass: (Turn off lights). Start settings: held for 1 min / held for 5 min. Includes condition checks before the actions. |
| [Turn lights on and off · with a wait condition in the routine — Variant A](automations/lighting/state-light-on-off-with-wait-bacb991b/README.md) | If the configured conditions pass: (Turn on lights at 70% brightness → pause for 5 min → 2 more steps). |
| [Turn lights on and off · with a wait condition in the routine — Variant B](automations/lighting/state-light-on-off-with-wait-c1ab88d4/README.md) | Wait for one of 2 triggers (stop on timeout) → use the first matching branch: if the configured conditions pass: (Turn on a switch) → Turn off lights; transition: 2 s → 4 more steps / Action type not available → Send a message to your own notification destination → 1 more step (selected steps; 3 other actions omitted). Start settings: held for 10 s. Includes condition checks before the actions. |
| [Turn lights on and off · with a wait condition in the routine](automations/lighting/template-light-on-off-with-wait/README.md) | Turn on lights → wait for a condition → Turn off lights (selected steps; 1 other action omitted). Includes condition checks before the actions. |
| [Turn lights on and off · with conditions in the routine](automations/lighting/triggered-light-on-off-with-branches/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights). |

<a id="lighting-scenes"></a>

#### Scenes (1 automation)

| Automation | What happens? |
| --- | --- |
| [Activate a saved scene · with a delay in the routine](automations/lighting/device-scene-on-with-delay/README.md) | Pause for 1 s → Activate a saved scene → pause for 52 s 700 ms (selected steps; 4 other actions omitted). |


</details>

<a id="ventilation"></a>

<details>
<summary><strong>Fans and air purifiers</strong> · 4 automations</summary>

**Jump to:** [Turn on and off (1)](#ventilation-power) · [Set the speed (2)](#ventilation-speed) · [Choose a preset (1)](#ventilation-profiles)

<a id="ventilation-power"></a>

#### Turn on and off (1 automation)

| Automation | What happens? |
| --- | --- |
| [Turn fans on and off · with conditions in the routine](automations/ventilation/scheduled-fan-on-off-with-branches/README.md) | Use the first matching branch: Turn on a fan / Turn off a fan. |

<a id="ventilation-speed"></a>

#### Set the speed (2 automations)

| Automation | What happens? |
| --- | --- |
| [Adjust fans](automations/ventilation/event-fan-on-speed/README.md) | Turn on a fan → Set the fan speed to 75% (selected steps; 2 other actions omitted). |
| [Adjust fans · with conditions in the routine](automations/ventilation/periodic-fan-on-speed-with-branches/README.md) | Prepare intermediate values → use the first matching branch: Turn on a fan → Set the fan speed to 75% → 2 more steps / Action type not available → Send a message to your own notification destination. Includes condition checks before the actions. |

<a id="ventilation-profiles"></a>

#### Choose a preset (1 automation)

| Automation | What happens? |
| --- | --- |
| [Turn fans on and off and adjust their settings · with a wait condition in the routine](automations/ventilation/state-fan-on-off-preset-with-wait/README.md) | Use the first matching branch: prepare intermediate values → Turn on a fan → 5 more steps / prepare intermediate values → Turn on a fan → 5 more steps; 1 more branch. |


</details>

<a id="cleaning"></a>

<details>
<summary><strong>Robot vacuums</strong> · 8 automations</summary>

**Jump to:** [Start cleaning (5)](#cleaning-start) · [Set suction power (2)](#cleaning-power) · [Clean selected areas (1)](#cleaning-areas)

<a id="cleaning-start"></a>

#### Start cleaning (5 automations)

| Automation | What happens? |
| --- | --- |
| [Start a robot vacuum](automations/cleaning/mixed-vacuum-start/README.md) | Start a robot vacuum → Reset a counter. Start limits: above 2. Includes condition checks before the actions. |
| [Start a robot vacuum — Variant A](automations/cleaning/scheduled-vacuum-start-7aa7e1d7/README.md) | Start a robot vacuum. |
| [Start a robot vacuum — Variant B](automations/cleaning/scheduled-vacuum-start-bc976c84/README.md) | Select a device option → Start a robot vacuum. |
| [Start a robot vacuum · with conditions in the routine](automations/cleaning/state-vacuum-start-with-branches/README.md) | If the configured conditions pass: (if the configured conditions pass: (Send a message → Turn on a stored on/off value → 1 more step)). |
| [Start a robot vacuum · with a delay in the routine](automations/cleaning/state-vacuum-start-with-delay/README.md) | Pause for not available → Start a robot vacuum (selected steps; 3 other actions omitted). Includes condition checks before the actions. |

<a id="cleaning-power"></a>

#### Set suction power (2 automations)

| Automation | What happens? |
| --- | --- |
| [Start a robot vacuum and set its suction power — Variant A](automations/cleaning/scheduled-vacuum-set-fan-speed-start-9e5f40a9/README.md) | Set the suction power → Start a robot vacuum. |
| [Start a robot vacuum and set its suction power — Variant B](automations/cleaning/scheduled-vacuum-set-fan-speed-start-e5d9d1cc/README.md) | Set the suction power → Start a robot vacuum. Includes condition checks before the actions. |

<a id="cleaning-areas"></a>

#### Clean selected areas (1 automation)

| Automation | What happens? |
| --- | --- |
| [Vacuum a selected area](automations/cleaning/device-dreame-vacuum-vacuum-clean-segment/README.md) | Vacuum a selected area; cleaning passes: 1. |


</details>

<a id="media"></a>

<details>
<summary><strong>Music, media and cameras</strong> · 2 automations</summary>

**Jump to:** [Save camera pictures (1)](#media-snapshots) · [Show a live camera view (1)](#media-camera-live)

<a id="media-snapshots"></a>

#### Save camera pictures (1 automation)

| Automation | What happens? |
| --- | --- |
| [Save a camera picture · with a delay in the routine](automations/media/state-camera-snapshot-with-delay/README.md) | Save a camera picture → pause for 1 s (selected steps; 6 other actions omitted). |

<a id="media-camera-live"></a>

#### Show a live camera view (1 automation)

| Automation | What happens? |
| --- | --- |
| [Control media and cameras · with a delay in the routine](automations/media/device-state-media-playback-play-stream-snapshot-with-delay/README.md) | If the configured conditions pass: (Play media → pause for 2 s 500 ms → 1 more step) → Save a camera picture → pause for not available (selected steps; 5 other actions omitted). |


</details>

<a id="tasks"></a>

<details>
<summary><strong>Task lists and reminders</strong> · 13 automations</summary>

**Jump to:** [Read task lists (9)](#tasks-read) · [Edit tasks (3)](#tasks-edit) · [Remove tasks (1)](#tasks-remove)

<a id="tasks-read"></a>

#### Read task lists (9 automations)

| Automation | What happens? |
| --- | --- |
| [Read a task list · with conditions in the routine](automations/tasks/device-todo-read-with-branches/README.md) | Read a task list (selected steps; 4 other actions omitted). |
| [Read a task list · with conditions in the routine — Variant A](automations/tasks/scheduled-todo-read-with-branches-42ac304c/README.md) | Read a task list → prepare intermediate values → if the configured conditions pass: (Run your own script). |
| [Read a task list · with conditions in the routine — Variant B](automations/tasks/scheduled-todo-read-with-branches-8247970e/README.md) | Read a task list → prepare intermediate values → if the configured conditions pass: (Run your own script). |
| [Read a task list · with conditions in the routine — Variant A](automations/tasks/state-todo-read-with-branches-433b7d45/README.md) | Read a task list (selected steps; 3 other actions omitted). Start settings: held for 2 min. |
| [Read a task list · with conditions in the routine — Variant B](automations/tasks/state-todo-read-with-branches-46a1dac1/README.md) | Read a task list (selected steps; 3 other actions omitted). Includes condition checks before the actions. |
| [Read a task list · with conditions in the routine — Variant C](automations/tasks/state-todo-read-with-branches-ad85ca77/README.md) | If the configured conditions pass: (Send a message) → if the configured conditions pass: (Send a message → Read a task list → 2 more steps). |
| [Read a task list · with conditions in the routine — Variant D](automations/tasks/state-todo-read-with-branches-c96c1391/README.md) | Read a task list (selected steps; 3 other actions omitted). Includes condition checks before the actions. |
| [Read a task list · with a delay in the routine](automations/tasks/state-todo-read-with-delay/README.md) | Increase a counter → pause for 1 s → if above 20: (Read a task list → prepare intermediate values → 5 more steps). Start settings: held for 3 s. Includes condition checks before the actions. |
| [Read a task list · with conditions in the routine](automations/tasks/threshold-state-todo-read-with-branches/README.md) | Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value → Action type not available → 4 more steps. Start settings: above 10; held for 2 min / below 5; held for 20 min; 1 more trigger in the details. |

<a id="tasks-edit"></a>

#### Edit tasks (3 automations)

| Automation | What happens? |
| --- | --- |
| [Read and edit a task list · with conditions in the routine — Variant A](automations/tasks/periodic-todo-read-update-with-branches-67bcce5a/README.md) | Read a task list → prepare intermediate values → repeat for each list item: prepare intermediate values. |
| [Read and edit a task list · with conditions in the routine — Variant B](automations/tasks/periodic-todo-read-update-with-branches-79a8b952/README.md) | Read a task list → repeat for each list item: prepare intermediate values. |
| [Read and edit a task list · with conditions in the routine — Variant C](automations/tasks/periodic-todo-read-update-with-branches-a6071dba/README.md) | Read a task list → prepare intermediate values → repeat for each list item: prepare intermediate values. |

<a id="tasks-remove"></a>

#### Remove tasks (1 automation)

| Automation | What happens? |
| --- | --- |
| [Read a task list and remove items · with conditions in the routine](automations/tasks/periodic-todo-read-remove-with-branches/README.md) | Read a task list → repeat for each list item: prepare intermediate values (selected steps; 4 other actions omitted). |


</details>

<a id="switches"></a>

<details>
<summary><strong>Switches and sockets</strong> · 16 automations</summary>

**Jump to:** [Turn on (4)](#switches-on) · [Turn off (3)](#switches-off) · [Toggle (4)](#switches-toggle) · [Turn on and off (5)](#switches-on-off)

<a id="switches-on"></a>

#### Turn on (4 automations)

| Automation | What happens? |
| --- | --- |
| [Turn on a switch · with a delay in the routine](automations/switches/mqtt-switch-on-with-delay/README.md) | If the configured conditions pass: (Turn on a switch → pause for 10 s) → check conditions; stop this sequence if false → Action type not available. |
| [Turn on a switch](automations/switches/state-switch-on/README.md) | Turn on a switch → Run your own script. Includes condition checks before the actions. |
| [Turn on a switch · with a wait condition in the routine](automations/switches/state-template-switch-on-with-wait/README.md) | Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value → check conditions; stop this sequence if false → 4 more steps. Start settings: held for 8 min / held for 20 s. |
| [Turn on a switch](automations/switches/template-switch-on/README.md) | Turn on a switch. |

<a id="switches-off"></a>

#### Turn off (3 automations)

| Automation | What happens? |
| --- | --- |
| [Turn off a switch · with a wait condition in the routine](automations/switches/state-switch-off-with-wait/README.md) | Wait for a value above 7.999 or 5 other triggers (continue on timeout) → if the configured conditions pass: (Turn off a switch) (selected steps; 2 other actions omitted). Includes condition checks before the actions. |
| [Turn off a switch](automations/switches/template-switch-off/README.md) | Turn off a switch. |
| [Turn off a switch · with a wait condition in the routine](automations/switches/triggered-switch-off-with-wait/README.md) | Wait for a value below 8 (continue on timeout) → if the configured conditions pass: (Turn off a switch); otherwise: (Show a notice in Home Assistant) (selected steps; 3 other actions omitted). Includes condition checks before the actions. |

<a id="switches-toggle"></a>

#### Toggle (4 automations)

| Automation | What happens? |
| --- | --- |
| [Switch between on and off](automations/switches/device-switch-toggle/README.md) | Switch between on and off. |
| [Switch between on and off](automations/switches/state-switch-toggle/README.md) | Switch between on and off. |
| [Switch between on and off — Variant A](automations/switches/triggered-switch-toggle-24cc2d6e/README.md) | Switch between on and off. |
| [Switch between on and off — Variant B](automations/switches/triggered-switch-toggle-c9419015/README.md) | Switch between on and off. |

<a id="switches-on-off"></a>

#### Turn on and off (5 automations)

| Automation | What happens? |
| --- | --- |
| [Turn switches on and off · with a wait condition in the routine](automations/switches/state-periodic-switch-on-off-with-wait/README.md) | Run 3 paths in parallel. Includes condition checks before the actions. |
| [Turn switches on and off · with conditions in the routine](automations/switches/state-switch-on-off-with-branches/README.md) | Use the first matching branch: Turn on a switch / Turn off a switch. Start settings: held for 5 min. |
| [Turn switches on and off · with a delay in the routine — Variant A](automations/switches/state-switch-on-off-with-delay-91d3deba/README.md) | Turn on a switch → pause for 10 min → Turn off a switch. |
| [Turn switches on and off · with a delay in the routine — Variant B](automations/switches/state-switch-on-off-with-delay-d9a93573/README.md) | Use the first matching branch: Turn on a switch → pause for 3 min → 2 more steps / check conditions; stop this sequence if false → Turn off a switch. Start settings: held for 5 min. |
| [Turn switches on and off · with a wait condition in the routine](automations/switches/threshold-switch-on-off-with-wait/README.md) | Turn on a switch → wait for a value below 5 (up to 60 min; continue on timeout) → Turn off a switch. Start limits: above 10. |


</details>

<a id="voice"></a>

<details>
<summary><strong>Voice and announcements</strong> · 1 automation</summary>

**Jump to:** [Announcements and spoken text (1)](#voice-announcements)

<a id="voice-announcements"></a>

#### Announcements and spoken text (1 automation)

| Automation | What happens? |
| --- | --- |
| [Use announcements and spoken text](automations/voice/state-voice-announce-speak/README.md) | Run 7 paths in parallel. |


</details>

<a id="notifications"></a>

<details>
<summary><strong>Messages and notices</strong> · 11 automations</summary>

**Jump to:** [Send messages (9)](#notifications-messages) · [Notices in Home Assistant (2)](#notifications-ha-notices)

<a id="notifications-messages"></a>

#### Send messages (9 automations)

| Automation | What happens? |
| --- | --- |
| [Send messages — Variant A](automations/notifications/device-notification-send-4fffe63e/README.md) | Reset a counter → Run your own script → Send a message. |
| [Send messages — Variant B](automations/notifications/device-notification-send-6b699d26/README.md) | Send a message to your own notification destination (selected steps; 3 other actions omitted). |
| [Send messages — Variant C](automations/notifications/device-notification-send-8e742eeb/README.md) | Send a message. Start settings: held for 5 min. |
| [Send messages · with a delay in the routine](automations/notifications/device-notification-send-with-delay/README.md) | Repeat until conditions pass: Send a message. Start limits: below 5. |
| [Send messages · with conditions in the routine](automations/notifications/periodic-notification-send-with-branches/README.md) | Get a weather forecast → prepare intermediate values → use the first matching branch: Action type not available → Send a message to your own notification destination. Includes condition checks before the actions. |
| [Send messages — Variant A](automations/notifications/state-notification-send-0989a580/README.md) | Check conditions; stop this sequence if false → Press a configured virtual button → Send a message. Includes condition checks before the actions. |
| [Send messages — Variant B](automations/notifications/state-notification-send-3e58df61/README.md) | Send a message. |
| [Send messages — Variant C](automations/notifications/state-notification-send-a0e2d0da/README.md) | Prepare intermediate values → Action type not available → Send a message to your own notification destination. Includes condition checks before the actions. |
| [Send messages](automations/notifications/state-scheduled-notification-send/README.md) | Store some text → Action type not available → Send a message to your own notification destination. Includes condition checks before the actions. |

<a id="notifications-ha-notices"></a>

#### Notices in Home Assistant (2 automations)

| Automation | What happens? |
| --- | --- |
| [Send messages and show notices — Variant A](automations/notifications/device-notifications-create-notify-42c8182d/README.md) | Send a message → Show a notice in Home Assistant. Start settings: held for 5 min. |
| [Send messages and show notices — Variant B](automations/notifications/device-notifications-create-notify-713dfa68/README.md) | Send a message → Show a notice in Home Assistant. Start settings: held for 2 min. |


</details>

<a id="helpers"></a>

<details>
<summary><strong>Counters and stored values</strong> · 6 automations</summary>

**Jump to:** [Virtual switches (4)](#helpers-switches) · [Change counters (1)](#helpers-counters) · [Store text (1)](#helpers-text)

<a id="helpers-switches"></a>

#### Virtual switches (4 automations)

| Automation | What happens? |
| --- | --- |
| [Turn off a stored on/off value](automations/helpers/scheduled-input-boolean-off/README.md) | Turn off a stored on/off value. |
| [Change stored on/off values · with conditions in the routine](automations/helpers/scheduled-input-boolean-on-off-with-branches/README.md) | If the configured conditions pass: (Turn on a stored on/off value); otherwise: (Turn off a stored on/off value). |
| [Change stored on/off values · with a delay in the routine](automations/helpers/state-input-boolean-on-off-with-delay/README.md) | Turn on a stored on/off value → pause for 180 s → Turn off a stored on/off value (selected steps; 1 other action omitted). Includes condition checks before the actions. |
| [Change stored on/off values · with conditions in the routine](automations/helpers/state-scheduled-input-boolean-on-off-with-branches/README.md) | Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value. |

<a id="helpers-counters"></a>

#### Change counters (1 automation)

| Automation | What happens? |
| --- | --- |
| [Increase a counter](automations/helpers/device-counter-increment/README.md) | Increase a counter. Start settings: held for 8 s. |

<a id="helpers-text"></a>

#### Store text (1 automation)

| Automation | What happens? |
| --- | --- |
| [Store some text](automations/helpers/template-input-text-value/README.md) | Store some text. Includes condition checks before the actions. |


</details>

<a id="system"></a>

<details>
<summary><strong>More routines and device actions</strong> · 23 automations</summary>

**Jump to:** [Your own scripts (6)](#system-scripts) · [Device functions and buttons (1)](#system-device-controls) · [MQTT messages (3)](#system-mqtt) · [Control other automations (1)](#system-automations) · [Get weather data (1)](#system-weather) · [Maintenance and logs (1)](#system-maintenance) · [Actions to set up (10)](#system-unfinished)

<a id="system-scripts"></a>

#### Your own scripts (6 automations)

| Automation | What happens? |
| --- | --- |
| [Run an existing script](automations/system/event-script-run/README.md) | Run your own script. Includes condition checks before the actions. |
| [Run an existing script · with conditions in the routine — Variant A](automations/system/mqtt-script-on-with-branches/README.md) | If the configured conditions pass: (Start an existing script); otherwise: (Start an existing script). |
| [Run an existing script](automations/system/mqtt-script-run/README.md) | Run your own script. |
| [Run an existing script · with conditions in the routine — Variant B](automations/system/mqtt-script-run-with-branches/README.md) | Use the first matching branch: Action type not available; otherwise: Run your own script. |
| [Run an existing script](automations/system/periodic-script-run/README.md) | Run your own script. |
| [Run an existing script](automations/system/state-scheduled-script-run/README.md) | Repeat for each list item: check conditions; stop this sequence if false. |

<a id="system-device-controls"></a>

#### Device functions and buttons (1 automation)

| Automation | What happens? |
| --- | --- |
| [Combine several functions · with a delay in the routine](automations/system/state-system-press-select-option-with-delay/README.md) | Select a device option → pause for not available → Run a device function by pressing a button. Includes condition checks before the actions. |

<a id="system-mqtt"></a>

#### MQTT messages (3 automations)

| Automation | What happens? |
| --- | --- |
| [Send an MQTT message](automations/system/periodic-mqtt-publish/README.md) | Send an MQTT message. |
| [Send an MQTT message — Variant A](automations/system/state-mqtt-publish-03a56ab8/README.md) | Send an MQTT message. Includes condition checks before the actions. |
| [Send an MQTT message — Variant B](automations/system/state-mqtt-publish-4d55a0f6/README.md) | Send an MQTT message. |

<a id="system-automations"></a>

#### Control other automations (1 automation)

| Automation | What happens? |
| --- | --- |
| [Enable and disable other automations · with a delay in the routine](automations/system/device-automation-on-off-with-delay/README.md) | Action type not available → Enable another automation → Disable another automation → 2 more steps (see full flow). |

<a id="system-weather"></a>

#### Get weather data (1 automation)

| Automation | What happens? |
| --- | --- |
| [Combine several functions · with a delay in the routine](automations/system/state-periodic-system-custom-action-get-forecasts-with-delay/README.md) | Get a weather forecast → check conditions; stop this sequence if false → prepare intermediate values → 3 more steps (see full flow). Includes condition checks before the actions. |

<a id="system-maintenance"></a>

#### Maintenance and logs (1 automation)

| Automation | What happens? |
| --- | --- |
| [Combine several functions](automations/system/periodic-system-reload-config-entry-write/README.md) | Write an entry in the system log → Reload a device integration. Includes condition checks before the actions. |

<a id="system-unfinished"></a>

#### Actions to set up (10 automations)

| Automation | What happens? |
| --- | --- |
| [Set up your own action — Variant A](automations/system/device-generic-action-15407118/README.md) | Action type not available. |
| [Set up your own action — Variant B](automations/system/device-generic-action-15407118-a/README.md) | Action type not available. |
| [Set up your own action — Variant C](automations/system/device-generic-action-ddc77372/README.md) | Action type not available. Includes condition checks before the actions. |
| [Set up your own action — Variant D](automations/system/device-generic-action-f594a0ff/README.md) | Action type not available. Includes condition checks before the actions. |
| [Set up your own action · with conditions in the routine](automations/system/device-generic-action-with-branches/README.md) | If the configured conditions pass: (Action type not available → Action type not available); otherwise: (Action type not available → Action type not available). |
| [Set up your own action · with a wait condition in the routine — Variant A](automations/system/device-generic-action-with-wait-31e6d1d6/README.md) | If the configured conditions pass: (if below 10: (Action type not available → wait for another trigger (up to 1 min; continue on timeout) → 1 more step)). |
| [Set up your own action · with a wait condition in the routine — Variant B](automations/system/device-generic-action-with-wait-4ebede39/README.md) | Action type not available → wait for a value below 60 → Action type not available. Start limits: above 60. |
| [Set up your own action · with conditions in the routine](automations/system/periodic-generic-action-with-branches/README.md) | If below 0.2: (Action type not available); otherwise: (Action type not available). |
| [Set up your own action](automations/system/state-generic-action/README.md) | Action type not available. |
| [Set up your own action](automations/system/triggered-generic-action/README.md) | Blueprint logic is external. |


</details>

<!-- catalogue:end -->

## Need help setting it up?

The **[getting-started guide](how-to/get-started.md)** shows you where to click in Home Assistant, explains the placeholders and helps you test your automation.

A green GitHub check means the collection's checks have passed. Test your adapted example in your own Home Assistant to make sure it works with your devices.

<details>
<summary><strong>For contributors: maintain the documentation and checks</strong></summary>

Both language versions of the catalogue and example explanations are generated together. Folder names stay stable; reader-facing text comes from reviewed, generic metadata.

```sh
python -m pip install -r requirements-dev.txt
python scripts/catalogue.py --write
python scripts/catalogue.py --check
```

- [Document an example](how-to/document-an-automation.md)
- [Privacy and security checks](how-to/security-and-privacy.md)
- [Checklist for automated contributions](how-to/agent-documentation-checklist.md)

GitHub checks run whenever a pull request is opened or reopened, new commits are added, its draft status changes, or its title, description or target branch is edited.

</details>
