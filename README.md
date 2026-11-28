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
| A 30-minute state duration, an additional condition and a light-off action with a 15-second fade | [Light-off routine](automations/lighting/state-light-off-2689ab79/README.md) |
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

**Names and messages:** Original entity IDs are always replaced with neutral placeholders. Ordinary notification text can stay only when it contains no private information; personal names, identifying phone models and credentials are cleaned. Existing missing text cannot be recovered from the shared files.

**Which file should I open?** Start with an example's explanation in `README.md`. `README.de.md` has the same guide in German. `automation.yaml` contains the routine as text; `metadata.json` is used to build the catalogue automatically.

<!-- catalogue:start -->

<a id="automation-catalogue"></a>

## Shared automations (126 automations)

The shared automations are grouped into **11 categories and 35 subcategories** based on what they do.

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
| [Switches and sockets](#switches) | 15 | Turn on · Turn off · Toggle · Turn on and off |
| [Voice and announcements](#voice) | 1 | Announcements and spoken text |
| [Messages and notices](#notifications) | 9 | Send messages · Notices in Home Assistant |
| [Counters and stored values](#helpers) | 5 | Virtual switches · Change counters · Store text |
| [More routines and device actions](#system) | 22 | Your own scripts · MQTT messages · Control other automations · Get weather data · Maintenance and logs · Actions to set up |

<a id="climate"></a>

<details>
<summary><strong>Heating and cooling</strong> · 18 automations</summary>

**Jump to:** [Set the temperature (9)](#climate-temperature) · [Heating and cooling modes (4)](#climate-modes) · [Heating and cooling presets (5)](#climate-profiles)

<a id="climate-temperature"></a>

#### Set the temperature (9 automations)

| Automation | What happens? |
| --- | --- |
| [Set the desired room temperature · with conditions in the routine — Variant A](automations/climate/device-climate-temperature-with-branches-7e7eb3e2/README.md) | Repeat until conditions pass: Set the temperature to 5; heating/cooling mode: `off` → repeat until conditions pass: Set the temperature to 5; heating/cooling mode: `off` → if the configured conditions pass: (Set the temperature to 21; heating/cooling mode: `heat_cool`) → 1 more step (see full flow). Start settings: Device event. |
| [Set the desired room temperature · with conditions in the routine — Variant B](automations/climate/device-climate-temperature-with-branches-8526ac3c/README.md) | Repeat until conditions pass: Set the temperature to 5; heating/cooling mode: `off` → repeat until conditions pass: Set the temperature to 5; heating/cooling mode: `off` → if the configured conditions pass: (Set the temperature to 21; heating/cooling mode: `heat_cool`) → 1 more step (see full flow). Start settings: Device event. |
| [Set the desired room temperature · with conditions in the routine](automations/climate/mixed-climate-temperature-with-branches/README.md) | Check conditions; stop this sequence if false → if state: `on`; 2 other checks: (Set the desired room temperature) → Turn off a stored on/off value. Start settings: at 18:00:00 / Home Assistant event; 2 more triggers in the details. Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine — Variant A](automations/climate/mixed-climate-temperature-with-wait-7131e10a/README.md) | Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 7 more steps / prepare intermediate values → check conditions; stop this sequence if false → 6 more steps; 4 more branches. Start settings: from state: `off`; to state: `on` / to state: `on`; held for 2 min; 4 more triggers in the details. Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine — Variant B](automations/climate/mixed-climate-temperature-with-wait-96c66e3c/README.md) | Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 8 more steps / prepare intermediate values → check conditions; stop this sequence if false → 7 more steps; 4 more branches. Start settings: from state: `off`; to state: `on` / to state: `on`; held for 2 min; 4 more triggers in the details. Includes condition checks before the actions. |
| [Set the desired room temperature · with a wait condition in the routine — Variant C](automations/climate/mixed-climate-temperature-with-wait-dc257811/README.md) | Prepare intermediate values → use the first matching branch: prepare intermediate values → Store some text → 7 more steps / prepare intermediate values → check conditions; stop this sequence if false → 6 more steps; 4 more branches. Start settings: from state: `off`; to state: `on` / to state: `on`; held for 2 min; 4 more triggers in the details. Includes condition checks before the actions. |
| [Set the desired room temperature · with conditions in the routine — Variant A](automations/climate/scheduled-climate-temperature-with-branches-168b082a/README.md) | Store some text → if state: `off`; 2 other checks: (Store some text → Store a number → 2 more steps). Start settings: at 06:45:00. Includes condition checks before the actions. |
| [Set the desired room temperature · with conditions in the routine — Variant B](automations/climate/scheduled-climate-temperature-with-branches-9653956b/README.md) | If after 22:00:00: (Set the temperature to 5); otherwise: (Set the temperature to 20). Start settings: at 21:30:00 / at 08:00:00. |
| [Set the desired room temperature · with a wait condition in the routine](automations/climate/state-climate-temperature-with-wait/README.md) | Set the temperature to 24; heating/cooling mode: `heat` → wait for from state: `on`; to state: `off` (up to 3 h; continue on timeout) → Set the temperature to 21; heating/cooling mode: `auto` (selected steps; 10 other actions omitted). Start settings: to state: `on`. |

<a id="climate-modes"></a>

#### Heating and cooling modes (4 automations)

| Automation | What happens? |
| --- | --- |
| [Adjust heating or air conditioning · with conditions in the routine — Variant A](automations/climate/state-climate-mode-temperature-with-branches-1362a589/README.md) | Use the first matching branch: Set the temperature to 5 → Set the heating or cooling mode; heating/cooling mode: `off` / Set the heating or cooling mode; heating/cooling mode: `heat_cool` → Set the temperature to 21. Start settings: to state: `on` / to state: `off`. |
| [Adjust heating or air conditioning · with conditions in the routine — Variant B](automations/climate/state-climate-mode-temperature-with-branches-49dd9c68/README.md) | Use the first matching branch: check conditions; stop this sequence if false → Set the temperature to 5 → 1 more step / check conditions; stop this sequence if false → Set the heating or cooling mode; heating/cooling mode: `heat_cool` → 1 more step. Start settings: to state: `on` / to state: `off`. |
| [Adjust heating or air conditioning · with conditions in the routine — Variant C](automations/climate/state-climate-mode-temperature-with-branches-c150b970/README.md) | Use the first matching branch: check conditions; stop this sequence if false → Set the temperature to 5 → 1 more step / Set the heating or cooling mode; heating/cooling mode: `heat_cool` → Set the temperature to 21. Start settings: to state: `on`, `off`. |
| [Adjust heating or air conditioning · with conditions in the routine — Variant D](automations/climate/state-climate-mode-temperature-with-branches-d74bbc99/README.md) | Use the first matching branch: Set the temperature to 5 → Set the heating or cooling mode; heating/cooling mode: `off`; otherwise: Set the heating or cooling mode; heating/cooling mode: `heat_cool` → Set the temperature to 21. Start settings: to state: `on`, `off`. Includes condition checks before the actions. |

<a id="climate-profiles"></a>

#### Heating and cooling presets (5 automations)

| Automation | What happens? |
| --- | --- |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant A](automations/climate/mixed-climate-mode-preset-temperature-with-wait-0e58eb87/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset; preset: “Default”) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset; preset: “\{\{ variable\_61.p \}\}”) → 3 more steps (selected steps; 4 other actions omitted). Start settings: to state: `on`, `off` / held for 10 s; 3 more triggers in the details. |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant B](automations/climate/mixed-climate-mode-preset-temperature-with-wait-21fde419/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset; preset: “Default”) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset; preset: “\{\{ variable\_61.p \}\}”) → 3 more steps (selected steps; 4 other actions omitted). Start settings: to state: `on`, `off` / held for 10 s; 3 more triggers in the details. |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant C](automations/climate/mixed-climate-mode-preset-temperature-with-wait-4cd824a5/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset; preset: “Default”) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset; preset: “\{\{ variable\_61.p \}\}”) → 3 more steps (selected steps; 4 other actions omitted). Start settings: to state: `on`, `off` / held for 10 s; 3 more triggers in the details. |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant D](automations/climate/mixed-climate-mode-preset-temperature-with-wait-740a14ea/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset; preset: “Default”) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset; preset: “\{\{ variable\_61.p \}\}”) → 3 more steps (selected steps; 4 other actions omitted). Start settings: to state: `on`, `off` / held for 10 s; 3 more triggers in the details. |
| [Adjust heating or air conditioning · with a wait condition in the routine — Variant E](automations/climate/mixed-climate-mode-preset-temperature-with-wait-a2a43d6f/README.md) | Use the first matching branch: if the configured conditions pass: (Store some text) → if the configured conditions pass: (Choose a heating or cooling preset; preset: “Default”) → 2 more steps / Set the heating or cooling mode → if the configured conditions pass: (Choose a heating or cooling preset; preset: “\{\{ variable\_61.p \}\}”) → 3 more steps (selected steps; 4 other actions omitted). Start settings: to state: `on`, `off` / held for 10 s; 3 more triggers in the details. |


</details>

<a id="lighting"></a>

<details>
<summary><strong>Lights</strong> · 29 automations</summary>

**Jump to:** [Turn on (2)](#lighting-on) · [Turn off (7)](#lighting-off) · [Toggle (6)](#lighting-toggle) · [Turn on and off (13)](#lighting-on-off) · [Scenes (1)](#lighting-scenes)

<a id="lighting-on"></a>

#### Turn on (2 automations)

| Automation | What happens? |
| --- | --- |
| [Turn on lights · with a delay in the routine](automations/lighting/state-light-on-with-delay/README.md) | Turn on lights at 5% brightness → if state: `off`: (Turn on a switch → pause for 5 min → 1 more step). Start settings: from state: `off`; to state: `on`. Includes condition checks before the actions. |
| [Turn on lights · with a wait condition in the routine](automations/lighting/state-light-on-with-wait/README.md) | Wait for one of 2 triggers (up to 5 min; stop on timeout) → use the first matching branch: Turn on lights at 100% brightness; transition: 3 s; colour values: 255, 255, 255 (selected steps; 2 other actions omitted). Start settings: from state: `off`; to state: `on`. |

<a id="lighting-off"></a>

#### Turn off (7 automations)

| Automation | What happens? |
| --- | --- |
| [Turn off lights](automations/lighting/scheduled-light-off/README.md) | Turn off lights → Turn off a switch → Turn off a switch. Start settings: at 00:00:00. |
| [Turn off lights — Variant A](automations/lighting/state-light-off-2689ab79/README.md) | Turn off lights; transition: 15 s. Start settings: to state: `off`; held for 30 min. Includes condition checks before the actions. |
| [Turn off lights — Variant B](automations/lighting/state-light-off-b89a953e/README.md) | Turn off lights. Start settings: State change. |
| [Turn off lights · with a wait condition in the routine — Variant A](automations/lighting/state-light-off-with-wait-2fed7c0d/README.md) | Pause for 30 min → wait for one of 2 triggers (up to 15 min; continue on timeout) (selected steps; 5 other actions omitted). Start settings: to state: `not_home`. |
| [Turn off lights · with a wait condition in the routine — Variant B](automations/lighting/state-light-off-with-wait-4466c2cf/README.md) | Wait for one of 2 triggers (up to 15 min; continue on timeout) → Turn off lights (selected steps; 9 other actions omitted). Start settings: held for 30 min. Includes condition checks before the actions. |
| [Turn off lights · with a wait condition in the routine — Variant C](automations/lighting/state-light-off-with-wait-5918e34f/README.md) | Wait for one of 11 triggers (up to 15 min; continue on timeout) (selected steps; 4 other actions omitted). Start settings: to state: `off`; held for 55 min. Includes condition checks before the actions. |
| [Turn off lights · with a wait condition in the routine — Variant D](automations/lighting/state-light-off-with-wait-eea5f9f7/README.md) | Wait for one of 2 triggers (up to 15 min; continue on timeout) (selected steps; 4 other actions omitted). Start settings: to state: `off`; held for 55 min. Includes condition checks before the actions. |

<a id="lighting-toggle"></a>

#### Toggle (6 automations)

| Automation | What happens? |
| --- | --- |
| [Switch lights between on and off — Variant A](automations/lighting/device-light-toggle-18a63fca/README.md) | Switch lights between on and off; brightness: 76%. Start settings: Device event. |
| [Switch lights between on and off — Variant B](automations/lighting/device-light-toggle-21f567de/README.md) | Switch lights between on and off; brightness: 76%; transition: 1 s. Start settings: Device event. |
| [Switch lights between on and off — Variant C](automations/lighting/device-light-toggle-462e05e8/README.md) | Switch lights between on and off; brightness: 81%. Start settings: Device event. |
| [Switch lights between on and off — Variant D](automations/lighting/device-light-toggle-4f78710c/README.md) | Switch lights between on and off; brightness: 76%; transition: 1 s. Start settings: Device event. |
| [Turn on or toggle lights · with conditions in the routine](automations/lighting/state-light-on-toggle-with-branches/README.md) | Use the first matching branch: Turn on lights; brightness change: 10% / Turn on lights; brightness change: -10%; 1 more branch. Start settings: State change. |
| [Switch lights between on and off](automations/lighting/triggered-light-toggle/README.md) | Switch lights between on and off; brightness: 76%. |

<a id="lighting-on-off"></a>

#### Turn on and off (13 automations)

| Automation | What happens? |
| --- | --- |
| [Turn lights on and off · with conditions in the routine — Variant A](automations/lighting/device-light-on-off-with-branches-66dd4021/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). Start settings: Device event. |
| [Turn lights on and off · with conditions in the routine — Variant B](automations/lighting/device-light-on-off-with-branches-860faef0/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). Start settings: Device event. |
| [Turn lights on and off · with conditions in the routine — Variant C](automations/lighting/device-light-on-off-with-branches-9071e735/README.md) | If the configured conditions pass: (use the first matching branch: Turn on lights at 86% brightness; transition: 1 s; colour temperature: 4000 K → Run your own script / Turn off lights; transition: 2 s → Run your own script) → use the first matching branch: Turn on a fan / Turn off a fan. Start settings: Device event. |
| [Turn lights on and off · with conditions in the routine — Variant D](automations/lighting/device-light-on-off-with-branches-a1b9296d/README.md) | If below 10: (Turn on lights at 5% brightness); otherwise: (Turn off lights). Start limits: below 10 / above 10. |
| [Turn lights on and off · with conditions in the routine — Variant E](automations/lighting/device-light-on-off-with-branches-d6dc2cef/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights at 70% brightness). Start settings: Device event. |
| [Turn lights on and off · with conditions in the routine](automations/lighting/mqtt-light-on-off-with-branches/README.md) | Use the first matching branch: Turn on lights at 76% brightness → Run your own script → 2 more steps / if state: `on`: (Start an existing script) → Run your own script → 2 more steps. Start settings: MQTT message. |
| [Turn lights on and off · with conditions in the routine — Variant A](automations/lighting/state-light-on-off-with-branches-140ac0ad/README.md) | If the configured conditions pass: (Turn on lights at 70% brightness); otherwise: (Turn off lights). Start settings: State change. |
| [Turn lights on and off · with conditions in the routine — Variant B](automations/lighting/state-light-on-off-with-branches-478eac65/README.md) | If the configured conditions pass: (Turn on lights at 70% brightness → if state: `on`: (Turn on lights at 100% brightness; transition: 3 s)); otherwise: (Turn off lights → if state: `on`: (Turn on lights at 10% brightness; transition: 30 s); otherwise: (Turn off lights; transition: 5 s)). Start settings: State change. |
| [Turn lights on and off · with conditions in the routine — Variant C](automations/lighting/state-light-on-off-with-branches-6ba1b551/README.md) | Use the first matching branch: Turn on a switch → Turn on lights / Turn off a switch → if the configured conditions pass: (Turn off lights). Start settings: from state: `off`; to state: `on`; held for 1 min / to state: `off`; held for 5 min. Includes condition checks before the actions. |
| [Turn lights on and off · with a wait condition in the routine — Variant A](automations/lighting/state-light-on-off-with-wait-de083b0a/README.md) | Wait for one of 2 triggers (up to 15 min; stop on timeout) → use the first matching branch: if state: `off`: (Turn on a switch) → Turn off lights; transition: 2 s → 4 more steps / Send a message to your own notification destination; message text: “Okay, ich mache nichts.”; message title: “Filmmodus” → Send a message to your own notification destination; message text: “Okay, ich mache nichts.”; message title: “Filmmodus” → 1 more step (selected steps; 3 other actions omitted). Start settings: from state: `off`; to state: `on`; held for 10 s / from state: `unavailable`; to state: `on`; held for 10 s. Includes condition checks before the actions. |
| [Turn lights on and off · with a wait condition in the routine — Variant B](automations/lighting/state-light-on-off-with-wait-dff24f3d/README.md) | If the configured conditions pass: (Turn on lights at 70% brightness → pause for 5 min → 2 more steps). Start settings: State change. |
| [Turn lights on and off · with a wait condition in the routine](automations/lighting/template-light-on-off-with-wait/README.md) | Turn on lights → wait for a condition → Turn off lights (selected steps; 1 other action omitted). Start settings: held for 3 min. Includes condition checks before the actions. |
| [Turn lights on and off · with conditions in the routine](automations/lighting/triggered-light-on-off-with-branches/README.md) | If the configured conditions pass: (Turn off lights); otherwise: (Turn on lights). |

<a id="lighting-scenes"></a>

#### Scenes (1 automation)

| Automation | What happens? |
| --- | --- |
| [Activate a saved scene · with a delay in the routine](automations/lighting/device-scene-on-with-delay/README.md) | Pause for 1 s → Activate a saved scene → pause for 52 s 700 ms (selected steps; 4 other actions omitted). Start settings: Device event. |


</details>

<a id="ventilation"></a>

<details>
<summary><strong>Fans and air purifiers</strong> · 4 automations</summary>

**Jump to:** [Turn on and off (1)](#ventilation-power) · [Set the speed (2)](#ventilation-speed) · [Choose a preset (1)](#ventilation-profiles)

<a id="ventilation-power"></a>

#### Turn on and off (1 automation)

| Automation | What happens? |
| --- | --- |
| [Turn fans on and off · with conditions in the routine](automations/ventilation/scheduled-fan-on-off-with-branches/README.md) | Use the first matching branch: after 03:00:00: Turn on a fan / after 03:30:00: Turn off a fan. Start settings: at 03:00:00 / at 03:30:00. |

<a id="ventilation-speed"></a>

#### Set the speed (2 automations)

| Automation | What happens? |
| --- | --- |
| [Adjust fans](automations/ventilation/event-fan-on-speed/README.md) | Turn on a fan → Set the fan speed to 75% (selected steps; 2 other actions omitted). Start settings: Event. |
| [Adjust fans · with conditions in the routine](automations/ventilation/periodic-fan-on-speed-with-branches/README.md) | Prepare intermediate values → 1 more step (see full flow). Start settings: minutes: 0. Includes condition checks before the actions. |

<a id="ventilation-profiles"></a>

#### Choose a preset (1 automation)

| Automation | What happens? |
| --- | --- |
| [Turn fans on and off and adjust their settings · with a wait condition in the routine](automations/ventilation/state-fan-on-off-preset-with-wait/README.md) | Use the first matching branch: prepare intermediate values → Turn on a fan → 5 more steps / prepare intermediate values → Turn on a fan → 5 more steps; 1 more branch. Start settings: to state: `cleaning`. |


</details>

<a id="cleaning"></a>

<details>
<summary><strong>Robot vacuums</strong> · 8 automations</summary>

**Jump to:** [Start cleaning (5)](#cleaning-start) · [Set suction power (2)](#cleaning-power) · [Clean selected areas (1)](#cleaning-areas)

<a id="cleaning-start"></a>

#### Start cleaning (5 automations)

| Automation | What happens? |
| --- | --- |
| [Start a robot vacuum](automations/cleaning/mixed-vacuum-start/README.md) | Start a robot vacuum → Reset a counter. Start settings: above 2 / at 08:00:00; 1 more trigger in the details. Includes condition checks before the actions. |
| [Start a robot vacuum — Variant A](automations/cleaning/scheduled-vacuum-start-8bec92f6/README.md) | Select a device option; selected option: “Silent” → Start a robot vacuum. Start settings: at 03:00:00. |
| [Start a robot vacuum — Variant B](automations/cleaning/scheduled-vacuum-start-dd1999b3/README.md) | Start a robot vacuum. Start settings: at 09:30:00. |
| [Start a robot vacuum · with conditions in the routine](automations/cleaning/state-vacuum-start-with-branches/README.md) | If state: `not_home`; 1 other check: (if state: `off`: (Send a message; message text: “Keiner zuhause. Es wird sauber gemacht.”; message title: “Staubsauger” → Turn on a stored on/off value → 1 more step)). Start settings: State change. |
| [Start a robot vacuum · with a delay in the routine](automations/cleaning/state-vacuum-start-with-delay/README.md) | Pause for 3 s → Start a robot vacuum (selected steps; 3 other actions omitted). Start settings: State change. Includes condition checks before the actions. |

<a id="cleaning-power"></a>

#### Set suction power (2 automations)

| Automation | What happens? |
| --- | --- |
| [Start a robot vacuum and set its suction power — Variant A](automations/cleaning/scheduled-vacuum-set-fan-speed-start-47446c20/README.md) | Set the suction power; suction/speed setting: “max” → Start a robot vacuum. Start settings: at 09:30:00. |
| [Start a robot vacuum and set its suction power — Variant B](automations/cleaning/scheduled-vacuum-set-fan-speed-start-d5c5adae/README.md) | Set the suction power; suction/speed setting: “20” → Start a robot vacuum. Start settings: at 13:00:00. Includes condition checks before the actions. |

<a id="cleaning-areas"></a>

#### Clean selected areas (1 automation)

| Automation | What happens? |
| --- | --- |
| [Vacuum a selected area](automations/cleaning/device-dreame-vacuum-vacuum-clean-segment/README.md) | Vacuum a selected area; cleaning passes: 1. Start settings: Device event. |


</details>

<a id="media"></a>

<details>
<summary><strong>Music, media and cameras</strong> · 2 automations</summary>

**Jump to:** [Save camera pictures (1)](#media-snapshots) · [Show a live camera view (1)](#media-camera-live)

<a id="media-snapshots"></a>

#### Save camera pictures (1 automation)

| Automation | What happens? |
| --- | --- |
| [Save a camera picture · with a delay in the routine](automations/media/state-camera-snapshot-with-delay/README.md) | Save a camera picture → pause for 1 s (selected steps; 6 other actions omitted). Start settings: from state: `off`; to state: `on`. |

<a id="media-camera-live"></a>

#### Show a live camera view (1 automation)

| Automation | What happens? |
| --- | --- |
| [Control media and cameras · with a delay in the routine](automations/media/device-state-media-playback-play-stream-snapshot-with-delay/README.md) | If state: `off`: (Play media → pause for 2 s 500 ms → 1 more step) → Save a camera picture → pause for 1 s (selected steps; 5 other actions omitted). Start settings: to state: `on` / State change; 1 more trigger in the details. |


</details>

<a id="tasks"></a>

<details>
<summary><strong>Task lists and reminders</strong> · 13 automations</summary>

**Jump to:** [Read task lists (9)](#tasks-read) · [Edit tasks (3)](#tasks-edit) · [Remove tasks (1)](#tasks-remove)

<a id="tasks-read"></a>

#### Read task lists (9 automations)

| Automation | What happens? |
| --- | --- |
| [Read a task list · with conditions in the routine](automations/tasks/device-todo-read-with-branches/README.md) | Read a task list; task status: `needs_action` (selected steps; 4 other actions omitted). Start settings: Device event. |
| [Read a task list · with conditions in the routine — Variant A](automations/tasks/scheduled-todo-read-with-branches-614bee92/README.md) | Read a task list; task status: `needs_action` → prepare intermediate values → if the configured conditions pass: (Run your own script). Start settings: at 06:00:00; weekdays: `wed`. |
| [Read a task list · with conditions in the routine — Variant B](automations/tasks/scheduled-todo-read-with-branches-9416b616/README.md) | Read a task list; task status: `needs_action` → prepare intermediate values → if the configured conditions pass: (Run your own script). Start settings: at 06:00:00; weekdays: `fri`, `mon`. |
| [Read a task list · with conditions in the routine — Variant A](automations/tasks/state-todo-read-with-branches-1d409d5f/README.md) | Read a task list; task status: `needs_action` (selected steps; 3 other actions omitted). Start settings: State change. Includes condition checks before the actions. |
| [Read a task list · with conditions in the routine — Variant B](automations/tasks/state-todo-read-with-branches-20f42e51/README.md) | Read a task list; task status: `needs_action` (selected steps; 3 other actions omitted). Start settings: to state: `unavailable`; held for 2 min. |
| [Read a task list · with conditions in the routine — Variant C](automations/tasks/state-todo-read-with-branches-29774ed7/README.md) | If the configured conditions pass: (Send a message; message text: “Geschirrspüler ist an \!”; message title: “🍽️ Geschirrspüler”) → if the configured conditions pass: (Send a message; message text: “Geschirrspüler ist IDENTIFIER\_104 \!”; message title: “🍽️ Geschirrspüler” → Read a task list; task status: `needs_action` → 2 more steps). Start settings: State change. |
| [Read a task list · with conditions in the routine — Variant D](automations/tasks/state-todo-read-with-branches-2eb2b24e/README.md) | Read a task list; task status: `needs_action` (selected steps; 3 other actions omitted). Start settings: State change. Includes condition checks before the actions. |
| [Read a task list · with a delay in the routine](automations/tasks/state-todo-read-with-delay/README.md) | Increase a counter → pause for 1 s → if above 20: (Read a task list; task status: `needs_action` → prepare intermediate values → 5 more steps). Start settings: from state: `off`; to state: `on`; held for 3 s. Includes condition checks before the actions. |
| [Read a task list · with conditions in the routine](automations/tasks/threshold-state-todo-read-with-branches/README.md) | Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value → Send a message to your own notification destination; message text: “Die Waschmaschine ist IDENTIFIER\_104.”; message title: “Waschmaschine” → 4 more steps. Start settings: above 10; held for 2 min / below 5; held for 20 min; 1 more trigger in the details. |

<a id="tasks-edit"></a>

#### Edit tasks (3 automations)

| Automation | What happens? |
| --- | --- |
| [Read and edit a task list · with conditions in the routine — Variant A](automations/tasks/periodic-todo-read-update-with-branches-9bf67b03/README.md) | Read a task list; task status: `needs_action` → prepare intermediate values → repeat for each list item: prepare intermediate values. Start settings: hours: /1. |
| [Read and edit a task list · with conditions in the routine — Variant B](automations/tasks/periodic-todo-read-update-with-branches-b915c5b1/README.md) | Read a task list → prepare intermediate values → repeat for each list item: prepare intermediate values. Start settings: hours: /1. |
| [Read and edit a task list · with conditions in the routine](automations/tasks/startup-periodic-todo-read-update-with-branches/README.md) | Read a task list; task status: `needs_action` → repeat for each list item: prepare intermediate values. Start settings: minutes: 0 / Home Assistant event. |

<a id="tasks-remove"></a>

#### Remove tasks (1 automation)

| Automation | What happens? |
| --- | --- |
| [Read a task list and remove items · with conditions in the routine](automations/tasks/periodic-todo-read-remove-with-branches/README.md) | Read a task list → repeat for each list item: prepare intermediate values (selected steps; 4 other actions omitted). Start settings: hours: /1. |


</details>

<a id="switches"></a>

<details>
<summary><strong>Switches and sockets</strong> · 15 automations</summary>

**Jump to:** [Turn on (4)](#switches-on) · [Turn off (3)](#switches-off) · [Toggle (4)](#switches-toggle) · [Turn on and off (4)](#switches-on-off)

<a id="switches-on"></a>

#### Turn on (4 automations)

| Automation | What happens? |
| --- | --- |
| [Turn on a switch · with a delay in the routine](automations/switches/mqtt-switch-on-with-delay/README.md) | If state: `off`: (Turn on a switch → pause for 10 s) → check conditions; stop this sequence if false → Run your own script. Start settings: MQTT message. |
| [Turn on a switch](automations/switches/state-switch-on/README.md) | Turn on a switch → Run your own script. Start settings: held for 15 s. Includes condition checks before the actions. |
| [Turn on a switch · with a wait condition in the routine](automations/switches/state-template-switch-on-with-wait/README.md) | Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value → check conditions; stop this sequence if false → 4 more steps. Start settings: held for 8 min / held for 20 s. |
| [Turn on a switch](automations/switches/template-switch-on/README.md) | Turn on a switch. Start settings: held for 5 min. |

<a id="switches-off"></a>

#### Turn off (3 automations)

| Automation | What happens? |
| --- | --- |
| [Turn off a switch · with a wait condition in the routine](automations/switches/state-switch-off-with-wait/README.md) | Wait for a value above 7.999 or 5 other triggers (up to 1 min; continue on timeout) → if state: `on`; held for 3 min; 6 other checks: (Turn off a switch) (selected steps; 2 other actions omitted). Start settings: to state: `unavailable`; held for 1 min. Includes condition checks before the actions. |
| [Turn off a switch](automations/switches/template-switch-off/README.md) | Turn off a switch. Start settings: held for 10 min. |
| [Turn off a switch · with a wait condition in the routine](automations/switches/triggered-switch-off-with-wait/README.md) | Wait for a value below 8 (up to 10 min; continue on timeout) → if the configured conditions pass: (Turn off a switch); otherwise: (Show a notice in Home Assistant; message text: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 …“; message title: “person-Steckdose bleibt an”) (selected steps; 3 other actions omitted). Includes condition checks before the actions. |

<a id="switches-toggle"></a>

#### Toggle (4 automations)

| Automation | What happens? |
| --- | --- |
| [Switch between on and off](automations/switches/device-switch-toggle/README.md) | Switch between on and off. Start settings: Device event. |
| [Switch between on and off](automations/switches/state-switch-toggle/README.md) | Switch between on and off. Start settings: State change. |
| [Switch between on and off — Variant A](automations/switches/triggered-switch-toggle-8229bc4f/README.md) | Switch between on and off. |
| [Switch between on and off — Variant B](automations/switches/triggered-switch-toggle-bb01f12e/README.md) | Switch between on and off. |

<a id="switches-on-off"></a>

#### Turn on and off (4 automations)

| Automation | What happens? |
| --- | --- |
| [Turn switches on and off · with a wait condition in the routine](automations/switches/mixed-switch-on-off-with-wait/README.md) | Run 3 paths in parallel. Start settings: State change / Home Assistant event; 1 more trigger in the details. Includes condition checks before the actions. |
| [Turn switches on and off · with conditions in the routine](automations/switches/state-switch-on-off-with-branches/README.md) | Use the first matching branch: state: `on`: Turn on a switch / state: `off`: Turn off a switch. Start settings: to state: `on` / to state: `off`; held for 5 min. |
| [Turn switches on and off · with a delay in the routine](automations/switches/state-switch-on-off-with-delay/README.md) | Use the first matching branch: state: `on`: Turn on a switch → pause for 3 min → 2 more steps / state: `off`: check conditions; stop this sequence if false → Turn off a switch. Start settings: to state: `on` / to state: `off`; held for 5 min. |
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
| [Use announcements and spoken text](automations/voice/state-voice-announce-speak/README.md) | Run 7 paths in parallel. Start settings: to state: `on`. |


</details>

<a id="notifications"></a>

<details>
<summary><strong>Messages and notices</strong> · 9 automations</summary>

**Jump to:** [Send messages (7)](#notifications-messages) · [Notices in Home Assistant (2)](#notifications-ha-notices)

<a id="notifications-messages"></a>

#### Send messages (7 automations)

| Automation | What happens? |
| --- | --- |
| [Send messages — Variant A](automations/notifications/device-notification-send-48543cff/README.md) | Send a message; message text: “🚪Pass wegen den person auf \!\!”; message title: “Die Haustür ist länger als 5 Minuten variable\_62\!\!\!”. Start settings: held for 5 min. |
| [Send messages — Variant B](automations/notifications/device-notification-send-6646dca6/README.md) | Reset a counter → Run your own script → Send a message; message text: “Windelzähler wurde zurückgesetzt. Ein To‑Do person Leeren des Windeleimers wurde erstellt.”; message title: “Windelzähler”. Start settings: Device event. |
| [Send messages · with a delay in the routine](automations/notifications/device-notification-send-with-delay/README.md) | Repeat until conditions pass: Send a message; message text: “Technickschrank hat keinen Strom”. Start limits: below 5. |
| [Send messages · with conditions in the routine](automations/notifications/startup-periodic-notification-send-with-branches/README.md) | Get a weather forecast → prepare intermediate values → 1 more step (see full flow). Start settings: minutes: 10 / Home Assistant event. Includes condition checks before the actions. |
| [Send messages — Variant A](automations/notifications/state-notification-send-92ff0651/README.md) | Prepare intermediate values → Send a message to your own notification destination; message text: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; message title: “🌧️ Regenalarm · \{\{ variable\_16 \}\}” → Send a message to your own notification destination; message text: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; message title: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”. Start settings: to state: `on`. Includes condition checks before the actions. |
| [Send messages — Variant B](automations/notifications/state-notification-send-f0c37163/README.md) | Send a message; message text: “person wurde aktiviert.”. Start settings: from state: `off`; to state: `on`. |
| [Send messages](automations/notifications/state-scheduled-notification-send/README.md) | Store some text → Send a message to your own notification destination; message text: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; message title: “Restmüll morgen” → Send a message to your own notification destination; message text: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; message title: “Restmüll morgen”. Start settings: at 20:00:00 / to state: `on`. Includes condition checks before the actions. |

<a id="notifications-ha-notices"></a>

#### Notices in Home Assistant (2 automations)

| Automation | What happens? |
| --- | --- |
| [Send messages and show notices — Variant A](automations/notifications/device-notifications-create-notify-4a36cf99/README.md) | Send a message; message text: “Büro Balkontür steht seit mehr als 5 Minuten variable\_62.” → Show a notice in Home Assistant; message text: “Die Balkontür im Büro steht seit über 5 Minuten variable\_62.”; message title: “Balkontür variable\_62”. Start settings: held for 5 min. |
| [Send messages and show notices — Variant B](automations/notifications/device-notifications-create-notify-50bbe8ed/README.md) | Send a message; message text: “🚪Pass wegen den person auf \!\!”; message title: “Die Tür in person Küche ist seit 2 Minuten variable\_62 \!” → Show a notice in Home Assistant; message text: “Die Tür in person Küche ist seit 2 Minuten variable\_62\! Pass auf die person auf\!”; message title: “Tür in person Küche variable\_62”. Start settings: held for 2 min. |


</details>

<a id="helpers"></a>

<details>
<summary><strong>Counters and stored values</strong> · 5 automations</summary>

**Jump to:** [Virtual switches (3)](#helpers-switches) · [Change counters (1)](#helpers-counters) · [Store text (1)](#helpers-text)

<a id="helpers-switches"></a>

#### Virtual switches (3 automations)

| Automation | What happens? |
| --- | --- |
| [Turn off a stored on/off value](automations/helpers/scheduled-input-boolean-off/README.md) | Turn off a stored on/off value. Start settings: at 23:55:00. |
| [Change stored on/off values · with conditions in the routine](automations/helpers/scheduled-input-boolean-on-off-with-branches/README.md) | If after 18:00:00: (Turn on a stored on/off value); otherwise: (Turn off a stored on/off value). Start settings: at 20:00:00 / at 08:00:00. |
| [Change stored on/off values · with conditions in the routine](automations/helpers/state-scheduled-input-boolean-on-off-with-branches/README.md) | Use the first matching branch: Turn on a stored on/off value / Turn off a stored on/off value. Start settings: from state: `off`; to state: `on` / from state: `on`; to state: `off`; 1 more trigger in the details. |

<a id="helpers-counters"></a>

#### Change counters (1 automation)

| Automation | What happens? |
| --- | --- |
| [Increase a counter](automations/helpers/device-counter-increment/README.md) | Increase a counter. Start settings: held for 8 s. |

<a id="helpers-text"></a>

#### Store text (1 automation)

| Automation | What happens? |
| --- | --- |
| [Store some text](automations/helpers/template-input-text-value/README.md) | Store some text. Start settings: held for 3 min. Includes condition checks before the actions. |


</details>

<a id="system"></a>

<details>
<summary><strong>More routines and device actions</strong> · 22 automations</summary>

**Jump to:** [Your own scripts (5)](#system-scripts) · [MQTT messages (3)](#system-mqtt) · [Control other automations (1)](#system-automations) · [Get weather data (1)](#system-weather) · [Maintenance and logs (1)](#system-maintenance) · [Actions to set up (11)](#system-unfinished)

<a id="system-scripts"></a>

#### Your own scripts (5 automations)

| Automation | What happens? |
| --- | --- |
| [Run an existing script](automations/system/event-script-run/README.md) | Run your own script. Start settings: Event. Includes condition checks before the actions. |
| [Run an existing script · with conditions in the routine](automations/system/mqtt-script-on-with-branches/README.md) | If the configured conditions pass: (Start an existing script); otherwise: (Start an existing script). Start settings: MQTT message. |
| [Run an existing script](automations/system/mqtt-script-run/README.md) | Run your own script. Start settings: MQTT message. |
| [Run an existing script](automations/system/startup-periodic-script-run/README.md) | Run your own script. Start settings: minutes: 15 / Home Assistant event. |
| [Run an existing script](automations/system/state-scheduled-script-run/README.md) | Repeat for each list item: check conditions; stop this sequence if false. Start settings: at 10:00:00 / State change. |

<a id="system-mqtt"></a>

#### MQTT messages (3 automations)

| Automation | What happens? |
| --- | --- |
| [Send an MQTT message](automations/system/periodic-mqtt-publish/README.md) | Send an MQTT message. Start settings: minutes: /30. |
| [Send an MQTT message](automations/system/startup-state-mqtt-publish/README.md) | Send an MQTT message. Start settings: State change / Home Assistant event. |
| [Send an MQTT message](automations/system/state-mqtt-publish/README.md) | Send an MQTT message. Start settings: State change. Includes condition checks before the actions. |

<a id="system-automations"></a>

#### Control other automations (1 automation)

| Automation | What happens? |
| --- | --- |
| [Enable and disable other automations · with a delay in the routine](automations/system/device-automation-on-off-with-delay/README.md) | Device action: `turn_off` → Enable another automation → Disable another automation → 2 more steps (see full flow). Start settings: Device event. |

<a id="system-weather"></a>

#### Get weather data (1 automation)

| Automation | What happens? |
| --- | --- |
| [Combine several functions · with a delay in the routine](automations/system/state-periodic-system-custom-action-get-forecasts-with-delay/README.md) | Get a weather forecast → check conditions; stop this sequence if false → prepare intermediate values → 3 more steps (see full flow). Start settings: to state: `on`; held for 30 s / held for 30 s; 1 more trigger in the details. Includes condition checks before the actions. |

<a id="system-maintenance"></a>

#### Maintenance and logs (1 automation)

| Automation | What happens? |
| --- | --- |
| [Combine several functions](automations/system/periodic-system-reload-config-entry-write/README.md) | Write an entry in the system log; log level: `warning`; message text: “person Realtime hängt, lade Integration person. Letztes Update person sensor.example\_09: \{\{ states.sensor.exampl…“ → Reload a device integration. Start settings: minutes: /10. Includes condition checks before the actions. |

<a id="system-unfinished"></a>

#### Actions to set up (11 automations)

| Automation | What happens? |
| --- | --- |
| [Set up your own action — Variant A](automations/system/device-generic-action-07b7476f/README.md) | Action type not available. Start settings: Device event. |
| [Set up your own action — Variant B](automations/system/device-generic-action-2e3d4aa8/README.md) | Action type not available. Start settings: Device event. Includes condition checks before the actions. |
| [Set up your own action — Variant C](automations/system/device-generic-action-384c7903/README.md) | Action type not available. Start settings: Device event. Includes condition checks before the actions. |
| [Set up your own action — Variant D](automations/system/device-generic-action-f0b83fa0/README.md) | Action type not available. Start settings: Device event. |
| [Set up your own action · with conditions in the routine](automations/system/device-generic-action-with-branches/README.md) | If the configured conditions pass: (Device action: `turn_on` → Device action: `turn_on`); otherwise: (Device action: `turn_off` → Device action: `turn_off`). Start settings: Device event. |
| [Set up your own action · with a wait condition in the routine — Variant A](automations/system/device-generic-action-with-wait-1b7f707c/README.md) | If the configured conditions pass: (if below 10: (Device action: `turn_on` → wait for from state: `on`; to state: `off` (up to 1 min; continue on timeout) → 1 more step)). Start settings: Device event. |
| [Set up your own action · with a wait condition in the routine — Variant B](automations/system/device-generic-action-with-wait-9cf7bd31/README.md) | Device action: `turn_on` → wait for a value below 60 → Device action: `turn_off`. Start limits: above 60. |
| [Combine several functions · with conditions in the routine](automations/system/mqtt-system-action-custom-action-with-branches/README.md) | Use the first matching branch: Action type not available; otherwise: Run your own script. Start settings: MQTT message. |
| [Set up your own action · with conditions in the routine](automations/system/periodic-generic-action-with-branches/README.md) | If below 0.2: (Action type not available); otherwise: (Action type not available). Start settings: minutes: 10. |
| [Set up your own action](automations/system/state-generic-action/README.md) | Action type not available. Start settings: State change. |
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
