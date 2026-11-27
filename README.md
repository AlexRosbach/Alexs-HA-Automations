# Home Assistant automation examples

A categorized catalogue of configurable Home Assistant examples, with descriptive names, generated documentation and automated privacy checks.

These are public templates. The earlier export replaced many trigger values, conditions and expressions with placeholders. The examples therefore need local configuration and, in some cases, reconstruction before Home Assistant can run them.

## Find and use an example

1. Choose a category in the [automation catalogue](#automation-catalogue) below.
2. Open the example's README to see its identifiable behavior and setup requirements.
3. Configure its YAML locally: replace example entities and placeholders, restore missing expressions, and use your own `secrets.yaml` for credentials.
4. Validate the completed configuration in Home Assistant and test with a non-critical device before enabling it.

## Naming and structure

Every example lives at `automations/<category>/<trigger>-<target>-<action>[-<qualifier>]/` and contains:

- `automation.yaml` — the configurable example.
- `README.md` — purpose, trigger, setup and privacy notes.
- `metadata.json` — reviewed generic action and trigger concepts used to generate its name and documentation.

For example, `switches/threshold-switch-on-off-with-wait/` describes a switch cycle triggered by a numeric threshold with an intermediate wait. Names use lowercase English words separated by hyphens; no person, room or installation names appear in them.

When several examples have the same identifiable behavior, their descriptive name ends with a short stable fingerprint. This preserves every example without inventing a purpose that the anonymized export no longer records. The original export order is not used as the automation's name.

## Maintain the catalogue

Install the repository's Python dependencies, then generate or verify all catalogue documentation:

```sh
python -m pip install -r requirements-dev.txt
python scripts/catalogue.py --write
python scripts/catalogue.py --check
```

The table below and each example README are generated from validated metadata. Edit the public concepts in `metadata.json` together with the corresponding YAML, then regenerate. Keep names consistent with the [documentation guide](how-to/document-an-automation.md).

- [Security and privacy pipeline](how-to/security-and-privacy.md) — local checks, automatic cleanup and the limits of cleanup after publication.
- [Document an automation](how-to/document-an-automation.md) — naming, metadata and publishing requirements.
- [Agent checklist](how-to/agent-documentation-checklist.md) — the required publishing workflow.

Never commit original exports, personal configuration, credentials, registries or Home Assistant backups. Automated detection covers known patterns and explicit policy; it cannot guarantee recognition of every private detail in arbitrary prose.

<!-- catalogue:start -->

<a id="automation-catalogue"></a>

## Automation catalogue (136 examples)

Choose a category, then open an example's documentation. Every name describes only behavior identifiable in the public export.

[Climate (18)](#climate) | [Lighting (29)](#lighting) | [Ventilation (4)](#ventilation) | [Cleaning (8)](#cleaning) | [Covers (3)](#covers) | [Media and cameras (2)](#media) | [Access (2)](#access) | [Tasks and reminders (13)](#tasks) | [Switches (16)](#switches) | [Voice (1)](#voice) | [Notifications (11)](#notifications) | [Helpers (6)](#helpers) | [System and scripts (23)](#system)

<a id="climate"></a>

### Climate

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Climate: temperature — device trigger · with branches (54a60709)](automations/climate/device-climate-temperature-with-branches-54a60709/README.md) | Device trigger | `climate.set_temperature` |
| [Climate: temperature — device trigger · with branches (c104c302)](automations/climate/device-climate-temperature-with-branches-c104c302/README.md) | Device trigger | `climate.set_temperature` |
| [Climate: temperature — state change, scheduled time, repeating schedule · with branches](automations/climate/mixed-climate-temperature-with-branches/README.md) | State change, Scheduled time, Repeating schedule | `climate.set_temperature`, `input_boolean.turn_off` |
| [Climate: temperature — state change, template condition, scheduled time · with wait (a3321799)](automations/climate/mixed-climate-temperature-with-wait-a3321799/README.md) | State change, Template condition, Scheduled time | `climate.set_temperature`, `input_text.set_value` |
| [Climate: temperature — state change, template condition, scheduled time · with wait (f1451717)](automations/climate/mixed-climate-temperature-with-wait-f1451717/README.md) | State change, Template condition, Scheduled time | `climate.set_temperature`, `input_boolean.turn_off`, `input_text.set_value` |
| [Climate: temperature — state change, template condition, scheduled time · with wait (fc1f1012)](automations/climate/mixed-climate-temperature-with-wait-fc1f1012/README.md) | State change, Template condition, Scheduled time | `climate.set_temperature`, `input_text.set_value` |
| [Climate: temperature — scheduled time · with branches (47c2e215)](automations/climate/scheduled-climate-temperature-with-branches-47c2e215/README.md) | Scheduled time | `climate.set_temperature` |
| [Climate: temperature — scheduled time · with branches (5aaa8edc)](automations/climate/scheduled-climate-temperature-with-branches-5aaa8edc/README.md) | Scheduled time | `climate.set_temperature`, `input_boolean.turn_on`, `input_number.set_value`, `input_text.set_value` |
| [Climate: mode, temperature — state change · with branches (049416bb)](automations/climate/state-climate-mode-temperature-with-branches-049416bb/README.md) | State change | `climate.set_hvac_mode`, `climate.set_temperature` |
| [Climate: mode, temperature — state change · with branches (104d0276)](automations/climate/state-climate-mode-temperature-with-branches-104d0276/README.md) | State change | `climate.set_hvac_mode`, `climate.set_temperature` |
| [Climate: mode, temperature — state change · with branches (6016b2ee)](automations/climate/state-climate-mode-temperature-with-branches-6016b2ee/README.md) | State change | `climate.set_hvac_mode`, `climate.set_temperature` |
| [Climate: mode, temperature — state change · with branches (75cb761b)](automations/climate/state-climate-mode-temperature-with-branches-75cb761b/README.md) | State change | `climate.set_hvac_mode`, `climate.set_temperature` |
| [Climate: temperature — state change · with wait](automations/climate/state-climate-temperature-with-wait/README.md) | State change | `automation.turn_off`, `automation.turn_on`, `climate.set_temperature`, `input_boolean.turn_off`, `input_boolean.turn_on`, `light.turn_on`, `media_player.media_pause`, `media_player.play_media`, `media_player.volume_set`, `switch.turn_off` |
| [Climate: mode, preset, temperature — state change, repeating schedule · with wait (3b582a19)](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-3b582a19/README.md) | State change, Repeating schedule | `climate.set_hvac_mode`, `climate.set_preset_mode`, `climate.set_temperature`, `input_text.set_value` |
| [Climate: mode, preset, temperature — state change, repeating schedule · with wait (6037647c)](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-6037647c/README.md) | State change, Repeating schedule | `climate.set_hvac_mode`, `climate.set_preset_mode`, `climate.set_temperature`, `input_text.set_value` |
| [Climate: mode, preset, temperature — state change, repeating schedule · with wait (b8c21183)](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-b8c21183/README.md) | State change, Repeating schedule | `climate.set_hvac_mode`, `climate.set_preset_mode`, `climate.set_temperature`, `input_text.set_value` |
| [Climate: mode, preset, temperature — state change, repeating schedule · with wait (d46bf28e)](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-d46bf28e/README.md) | State change, Repeating schedule | `climate.set_hvac_mode`, `climate.set_preset_mode`, `climate.set_temperature`, `input_text.set_value` |
| [Climate: mode, preset, temperature — state change, repeating schedule · with wait (f9d2161c)](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-f9d2161c/README.md) | State change, Repeating schedule | `climate.set_hvac_mode`, `climate.set_preset_mode`, `climate.set_temperature`, `input_text.set_value` |

<a id="lighting"></a>

### Lighting

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Light: on, off — device trigger · with branches (1c0d2b3a)](automations/lighting/device-light-on-off-with-branches-1c0d2b3a/README.md) | Device trigger | `light.turn_off`, `light.turn_on` |
| [Light: on, off — device trigger · with branches (5d21fa0b)](automations/lighting/device-light-on-off-with-branches-5d21fa0b/README.md) | Device trigger | `fan.turn_off`, `fan.turn_on`, `light.turn_off`, `light.turn_on`, `script.custom_action` |
| [Light: on, off — device trigger · with branches (6fe09721)](automations/lighting/device-light-on-off-with-branches-6fe09721/README.md) | Device trigger | `light.turn_off`, `light.turn_on` |
| [Light: on, off — device trigger · with branches (c0980148)](automations/lighting/device-light-on-off-with-branches-c0980148/README.md) | Device trigger | `light.turn_off`, `light.turn_on` |
| [Light: on, off — device trigger · with branches (fc5d4c73)](automations/lighting/device-light-on-off-with-branches-fc5d4c73/README.md) | Device trigger | `light.turn_off`, `light.turn_on` |
| [Light: toggle — device trigger (3c5800f8)](automations/lighting/device-light-toggle-3c5800f8/README.md) | Device trigger | `light.toggle` |
| [Light: toggle — device trigger (835102aa)](automations/lighting/device-light-toggle-835102aa/README.md) | Device trigger | `light.toggle` |
| [Light: toggle — device trigger (8feb4762)](automations/lighting/device-light-toggle-8feb4762/README.md) | Device trigger | `light.toggle` |
| [Light: toggle — device trigger (f2e96056)](automations/lighting/device-light-toggle-f2e96056/README.md) | Device trigger | `light.toggle` |
| [Scene: on — device trigger · with delay](automations/lighting/device-scene-on-with-delay/README.md) | Device trigger | `media_player.media_play_pause`, `media_player.play_media`, `media_player.volume_set`, `scene.turn_on` |
| [Light: on, off — mqtt message · with branches](automations/lighting/mqtt-light-on-off-with-branches/README.md) | MQTT message | `light.turn_off`, `light.turn_on`, `script.custom_action`, `script.turn_on`, `switch.turn_on` |
| [Light: off — scheduled time](automations/lighting/scheduled-light-off/README.md) | Scheduled time | `light.turn_off`, `switch.turn_off` |
| [Light: off — state change (22ac0c06)](automations/lighting/state-light-off-22ac0c06/README.md) | State change | `light.turn_off` |
| [Light: off — state change (7cb13cdd)](automations/lighting/state-light-off-7cb13cdd/README.md) | State change | `light.turn_off` |
| [Light: off — state change · with wait (4dccd971)](automations/lighting/state-light-off-with-wait-4dccd971/README.md) | State change | `light.turn_off`, `notify.custom_action`, `switch.turn_off` |
| [Light: off — state change · with wait (6fcc8f29)](automations/lighting/state-light-off-with-wait-6fcc8f29/README.md) | State change | `light.turn_off`, `notify.custom_action`, `script.custom_action` |
| [Light: off — state change · with wait (b05993d4)](automations/lighting/state-light-off-with-wait-b05993d4/README.md) | State change | `light.turn_off`, `notify.custom_action`, `script.custom_action`, `switch.turn_off` |
| [Light: off — state change · with wait (b5e8441e)](automations/lighting/state-light-off-with-wait-b5e8441e/README.md) | State change | `input_datetime.set_datetime`, `light.turn_off`, `script.custom_action` |
| [Light: on, off — state change · with branches (26b32a95)](automations/lighting/state-light-on-off-with-branches-26b32a95/README.md) | State change | `light.turn_off`, `light.turn_on` |
| [Light: on, off — state change · with branches (a4561b61)](automations/lighting/state-light-on-off-with-branches-a4561b61/README.md) | State change | `light.turn_off`, `light.turn_on` |
| [Light: on, off — state change · with branches (af2a0600)](automations/lighting/state-light-on-off-with-branches-af2a0600/README.md) | State change | `light.turn_off`, `light.turn_on`, `switch.turn_off`, `switch.turn_on` |
| [Light: on, off — state change · with wait (bacb991b)](automations/lighting/state-light-on-off-with-wait-bacb991b/README.md) | State change | `light.turn_off`, `light.turn_on` |
| [Light: on, off — state change · with wait (c1ab88d4)](automations/lighting/state-light-on-off-with-wait-c1ab88d4/README.md) | State change | `light.turn_off`, `light.turn_on`, `notify.custom_action`, `switch.turn_on` |
| [Light: on, toggle — state change · with branches](automations/lighting/state-light-on-toggle-with-branches/README.md) | State change | `light.toggle`, `light.turn_on` |
| [Light: on — state change · with delay](automations/lighting/state-light-on-with-delay/README.md) | State change | `light.turn_on`, `switch.turn_off`, `switch.turn_on` |
| [Light: on — state change · with wait](automations/lighting/state-light-on-with-wait/README.md) | State change | `light.turn_on` |
| [Light: on, off — template condition · with wait](automations/lighting/template-light-on-off-with-wait/README.md) | Template condition | `light.turn_off`, `light.turn_on` |
| [Light: on, off — trigger needs configuration · with branches](automations/lighting/triggered-light-on-off-with-branches/README.md) | Trigger needs configuration | `light.turn_off`, `light.turn_on` |
| [Light: toggle — trigger needs configuration](automations/lighting/triggered-light-toggle/README.md) | Trigger needs configuration | `light.toggle` |

<a id="ventilation"></a>

### Ventilation

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Fan: on, speed — event](automations/ventilation/event-fan-on-speed/README.md) | Event | `fan.set_percentage`, `fan.turn_on`, `notify.custom_action` |
| [Fan: on, speed — repeating schedule · with branches](automations/ventilation/periodic-fan-on-speed-with-branches/README.md) | Repeating schedule | `fan.set_percentage`, `fan.turn_on`, `notify.custom_action` |
| [Fan: on, off — scheduled time · with branches](automations/ventilation/scheduled-fan-on-off-with-branches/README.md) | Scheduled time | `fan.turn_off`, `fan.turn_on` |
| [Fan: on, off, preset — state change · with wait](automations/ventilation/state-fan-on-off-preset-with-wait/README.md) | State change | `fan.set_preset_mode`, `fan.turn_off`, `fan.turn_on`, `notify.custom_action`, `notify.notify` |

<a id="cleaning"></a>

### Cleaning

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Vacuum: segment cleaning — device trigger](automations/cleaning/device-dreame-vacuum-vacuum-clean-segment/README.md) | Device trigger | `dreame_vacuum.vacuum_clean_segment` |
| [Vacuum: start — numeric threshold, state change, scheduled time](automations/cleaning/mixed-vacuum-start/README.md) | Numeric threshold, State change, Scheduled time | `counter.reset`, `vacuum.start` |
| [Vacuum: speed, start — scheduled time (9e5f40a9)](automations/cleaning/scheduled-vacuum-set-fan-speed-start-9e5f40a9/README.md) | Scheduled time | `vacuum.set_fan_speed`, `vacuum.start` |
| [Vacuum: speed, start — scheduled time (e5d9d1cc)](automations/cleaning/scheduled-vacuum-set-fan-speed-start-e5d9d1cc/README.md) | Scheduled time | `vacuum.set_fan_speed`, `vacuum.start` |
| [Vacuum: start — scheduled time (7aa7e1d7)](automations/cleaning/scheduled-vacuum-start-7aa7e1d7/README.md) | Scheduled time | `vacuum.start` |
| [Vacuum: start — scheduled time (bc976c84)](automations/cleaning/scheduled-vacuum-start-bc976c84/README.md) | Scheduled time | `select.select_option`, `vacuum.start` |
| [Vacuum: start — state change · with branches](automations/cleaning/state-vacuum-start-with-branches/README.md) | State change | `input_boolean.turn_on`, `notify.notify`, `vacuum.start` |
| [Vacuum: start — state change · with delay](automations/cleaning/state-vacuum-start-with-delay/README.md) | State change | `notify.custom_action`, `select.select_option`, `vacuum.start` |

<a id="covers"></a>

### Covers

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Cover: close, open — device trigger · with branches](automations/covers/device-cover-close-open-with-branches/README.md) | Device trigger | `cover.close_cover`, `cover.open_cover` |
| [Cover: close, open — numeric threshold · with branches](automations/covers/threshold-cover-close-open-with-branches/README.md) | Numeric threshold | `cover.close_cover`, `cover.open_cover`, `input_boolean.turn_off`, `input_boolean.turn_on`, `switch.turn_on` |
| [Cover: close — numeric threshold, template condition · with branches](automations/covers/threshold-template-cover-close-with-branches/README.md) | Numeric threshold, Template condition | `cover.close_cover`, `notify.custom_action`, `notify.send_message`, `switch.turn_on` |

<a id="media"></a>

### Media and cameras

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Media and cameras control — device trigger, state change · with delay](automations/media/device-state-media-playback-play-stream-snapshot-with-delay/README.md) | Device trigger, State change | `camera.play_stream`, `camera.snapshot`, `input_boolean.turn_on`, `media_player.play_media`, `notify.custom_action` |
| [Camera: snapshot — state change · with delay](automations/media/state-camera-snapshot-with-delay/README.md) | State change | `camera.snapshot`, `notify.custom_action`, `notify.send_message`, `script.custom_action`, `todo.get_items` |

<a id="access"></a>

### Access

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Lock: open — state change · with wait](automations/access/state-lock-open-with-wait/README.md) | State change | `button.press`, `lock.open`, `notify.custom_action`, `script.custom_action` |
| [Lock: open — state change, tag scan](automations/access/state-tag-lock-open/README.md) | State change, Tag scan | `button.press`, `lock.open` |

<a id="tasks"></a>

### Tasks and reminders

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Task list: read tasks — device trigger · with branches](automations/tasks/device-todo-read-with-branches/README.md) | Device trigger | `notify.custom_action`, `script.custom_action`, `todo.get_items` |
| [Task list: read tasks, remove tasks — repeating schedule · with branches](automations/tasks/periodic-todo-read-remove-with-branches/README.md) | Repeating schedule | `script.custom_action`, `todo.get_items`, `todo.remove_item` |
| [Task list: read tasks, update tasks — repeating schedule · with branches (67bcce5a)](automations/tasks/periodic-todo-read-update-with-branches-67bcce5a/README.md) | Repeating schedule | `script.custom_action`, `todo.get_items`, `todo.update_item` |
| [Task list: read tasks, update tasks — repeating schedule · with branches (79a8b952)](automations/tasks/periodic-todo-read-update-with-branches-79a8b952/README.md) | Repeating schedule | `script.custom_action`, `todo.get_items`, `todo.update_item` |
| [Task list: read tasks, update tasks — repeating schedule · with branches (a6071dba)](automations/tasks/periodic-todo-read-update-with-branches-a6071dba/README.md) | Repeating schedule | `script.custom_action`, `todo.get_items`, `todo.update_item` |
| [Task list: read tasks — scheduled time · with branches (42ac304c)](automations/tasks/scheduled-todo-read-with-branches-42ac304c/README.md) | Scheduled time | `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — scheduled time · with branches (8247970e)](automations/tasks/scheduled-todo-read-with-branches-8247970e/README.md) | Scheduled time | `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — state change · with branches (433b7d45)](automations/tasks/state-todo-read-with-branches-433b7d45/README.md) | State change | `notify.notify`, `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — state change · with branches (46a1dac1)](automations/tasks/state-todo-read-with-branches-46a1dac1/README.md) | State change | `notify.notify`, `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — state change · with branches (ad85ca77)](automations/tasks/state-todo-read-with-branches-ad85ca77/README.md) | State change | `notify.notify`, `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — state change · with branches (c96c1391)](automations/tasks/state-todo-read-with-branches-c96c1391/README.md) | State change | `notify.notify`, `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — state change · with delay](automations/tasks/state-todo-read-with-delay/README.md) | State change | `counter.increment`, `counter.reset`, `notify.custom_action`, `notify.send_message`, `script.custom_action`, `todo.get_items` |
| [Task list: read tasks — numeric threshold, state change · with branches](automations/tasks/threshold-state-todo-read-with-branches/README.md) | Numeric threshold, State change | `input_boolean.turn_off`, `input_boolean.turn_on`, `notify.custom_action`, `script.custom_action`, `todo.get_items` |

<a id="switches"></a>

### Switches

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Switch: toggle — device trigger](automations/switches/device-switch-toggle/README.md) | Device trigger | `switch.toggle` |
| [Switch: on — mqtt message · with delay](automations/switches/mqtt-switch-on-with-delay/README.md) | MQTT message | `switch.turn_on` |
| [Switch: on, off — state change, repeating schedule · with wait](automations/switches/state-periodic-switch-on-off-with-wait/README.md) | State change, Repeating schedule | `button.press`, `switch.turn_off`, `switch.turn_on` |
| [Switch: off — state change · with wait](automations/switches/state-switch-off-with-wait/README.md) | State change | `switch.turn_off` |
| [Switch: on — state change](automations/switches/state-switch-on/README.md) | State change | `script.custom_action`, `switch.turn_on` |
| [Switch: on, off — state change · with branches](automations/switches/state-switch-on-off-with-branches/README.md) | State change | `switch.turn_off`, `switch.turn_on` |
| [Switch: on, off — state change · with delay (91d3deba)](automations/switches/state-switch-on-off-with-delay-91d3deba/README.md) | State change | `switch.turn_off`, `switch.turn_on` |
| [Switch: on, off — state change · with delay (d9a93573)](automations/switches/state-switch-on-off-with-delay-d9a93573/README.md) | State change | `switch.turn_off`, `switch.turn_on` |
| [Switch: toggle — state change](automations/switches/state-switch-toggle/README.md) | State change | `switch.toggle` |
| [Switch: on — state change, template condition · with wait](automations/switches/state-template-switch-on-with-wait/README.md) | State change, Template condition | `assist_satellite.ask_question`, `input_boolean.turn_off`, `input_boolean.turn_on`, `switch.turn_on` |
| [Switch: off — template condition](automations/switches/template-switch-off/README.md) | Template condition | `switch.turn_off` |
| [Switch: on — template condition](automations/switches/template-switch-on/README.md) | Template condition | `switch.turn_on` |
| [Switch: on, off — numeric threshold · with wait](automations/switches/threshold-switch-on-off-with-wait/README.md) | Numeric threshold | `switch.turn_off`, `switch.turn_on` |
| [Switch: off — trigger needs configuration · with wait](automations/switches/triggered-switch-off-with-wait/README.md) | Trigger needs configuration | `persistent_notification.create`, `rest_command.custom_action`, `switch.turn_off` |
| [Switch: toggle — trigger needs configuration (24cc2d6e)](automations/switches/triggered-switch-toggle-24cc2d6e/README.md) | Trigger needs configuration | `switch.toggle` |
| [Switch: toggle — trigger needs configuration (c9419015)](automations/switches/triggered-switch-toggle-c9419015/README.md) | Trigger needs configuration | `switch.toggle` |

<a id="voice"></a>

### Voice

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Voice control — state change](automations/voice/state-voice-announce-speak/README.md) | State change | `assist_satellite.announce`, `notify.custom_action`, `persistent_notification.create`, `tts.speak` |

<a id="notifications"></a>

### Notifications

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Notification: send — device trigger (4fffe63e)](automations/notifications/device-notification-send-4fffe63e/README.md) | Device trigger | `counter.reset`, `notify.notify`, `script.custom_action` |
| [Notification: send — device trigger (6b699d26)](automations/notifications/device-notification-send-6b699d26/README.md) | Device trigger | `automation.trigger`, `mqtt.publish`, `notify.custom_action` |
| [Notification: send — device trigger (8e742eeb)](automations/notifications/device-notification-send-8e742eeb/README.md) | Device trigger | `notify.notify` |
| [Notification: send — device trigger · with delay](automations/notifications/device-notification-send-with-delay/README.md) | Device trigger | `notify.notify` |
| [Notifications control — device trigger (42c8182d)](automations/notifications/device-notifications-create-notify-42c8182d/README.md) | Device trigger | `notify.notify`, `persistent_notification.create` |
| [Notifications control — device trigger (713dfa68)](automations/notifications/device-notifications-create-notify-713dfa68/README.md) | Device trigger | `notify.notify`, `persistent_notification.create` |
| [Notification: send — repeating schedule · with branches](automations/notifications/periodic-notification-send-with-branches/README.md) | Repeating schedule | `notify.custom_action`, `weather.get_forecasts` |
| [Notification: send — state change (0989a580)](automations/notifications/state-notification-send-0989a580/README.md) | State change | `input_button.press`, `notify.send_message` |
| [Notification: send — state change (3e58df61)](automations/notifications/state-notification-send-3e58df61/README.md) | State change | `notify.notify` |
| [Notification: send — state change (a0e2d0da)](automations/notifications/state-notification-send-a0e2d0da/README.md) | State change | `notify.custom_action` |
| [Notification: send — state change, scheduled time](automations/notifications/state-scheduled-notification-send/README.md) | State change, Scheduled time | `input_text.set_value`, `notify.custom_action` |

<a id="helpers"></a>

### Helpers

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Counter: increment — device trigger](automations/helpers/device-counter-increment/README.md) | Device trigger | `counter.increment` |
| [Input boolean: off — scheduled time](automations/helpers/scheduled-input-boolean-off/README.md) | Scheduled time | `input_boolean.turn_off` |
| [Input boolean: on, off — scheduled time · with branches](automations/helpers/scheduled-input-boolean-on-off-with-branches/README.md) | Scheduled time | `input_boolean.turn_off`, `input_boolean.turn_on` |
| [Input boolean: on, off — state change · with delay](automations/helpers/state-input-boolean-on-off-with-delay/README.md) | State change | `button.press`, `input_boolean.turn_off`, `input_boolean.turn_on` |
| [Input boolean: on, off — state change, scheduled time · with branches](automations/helpers/state-scheduled-input-boolean-on-off-with-branches/README.md) | State change, Scheduled time | `input_boolean.turn_off`, `input_boolean.turn_on` |
| [Input text: value — template condition](automations/helpers/template-input-text-value/README.md) | Template condition | `input_text.set_value` |

<a id="system"></a>

### System and scripts

| Automation | Trigger | Actions |
| --- | --- | --- |
| [Automation: on, off — device trigger · with delay](automations/system/device-automation-on-off-with-delay/README.md) | Device trigger | `automation.turn_off`, `automation.turn_on` |
| [Configurable: action — device trigger (15407118)](automations/system/device-generic-action-15407118/README.md) | Device trigger | `generic.action` |
| [Configurable: action — device trigger (15407118-a)](automations/system/device-generic-action-15407118-a/README.md) | Device trigger | `generic.action` |
| [Configurable: action — device trigger (ddc77372)](automations/system/device-generic-action-ddc77372/README.md) | Device trigger | `generic.action` |
| [Configurable: action — device trigger (f594a0ff)](automations/system/device-generic-action-f594a0ff/README.md) | Device trigger | `generic.action` |
| [Configurable: action — device trigger · with branches](automations/system/device-generic-action-with-branches/README.md) | Device trigger | `generic.action` |
| [Configurable: action — device trigger · with wait (31e6d1d6)](automations/system/device-generic-action-with-wait-31e6d1d6/README.md) | Device trigger | `generic.action` |
| [Configurable: action — device trigger · with wait (4ebede39)](automations/system/device-generic-action-with-wait-4ebede39/README.md) | Device trigger | `generic.action` |
| [Script: run — event](automations/system/event-script-run/README.md) | Event | `script.custom_action` |
| [Script: on — mqtt message · with branches](automations/system/mqtt-script-on-with-branches/README.md) | MQTT message | `script.turn_on` |
| [Script: run — mqtt message](automations/system/mqtt-script-run/README.md) | MQTT message | `script.custom_action` |
| [Script: run — mqtt message · with branches](automations/system/mqtt-script-run-with-branches/README.md) | MQTT message | `script.custom_action` |
| [Configurable: action — repeating schedule · with branches](automations/system/periodic-generic-action-with-branches/README.md) | Repeating schedule | `generic.action` |
| [Mqtt: publish — repeating schedule](automations/system/periodic-mqtt-publish/README.md) | Repeating schedule | `mqtt.publish` |
| [Script: run — repeating schedule](automations/system/periodic-script-run/README.md) | Repeating schedule | `script.custom_action` |
| [System and scripts control — repeating schedule](automations/system/periodic-system-reload-config-entry-write/README.md) | Repeating schedule | `homeassistant.reload_config_entry`, `system_log.write` |
| [Configurable: action — state change](automations/system/state-generic-action/README.md) | State change | `generic.action` |
| [Mqtt: publish — state change (03a56ab8)](automations/system/state-mqtt-publish-03a56ab8/README.md) | State change | `mqtt.publish` |
| [Mqtt: publish — state change (4d55a0f6)](automations/system/state-mqtt-publish-4d55a0f6/README.md) | State change | `mqtt.publish` |
| [System and scripts control — state change, repeating schedule · with delay](automations/system/state-periodic-system-custom-action-get-forecasts-with-delay/README.md) | State change, Repeating schedule | `script.custom_action`, `weather.get_forecasts` |
| [Script: run — state change, scheduled time](automations/system/state-scheduled-script-run/README.md) | State change, Scheduled time | `script.custom_action` |
| [System and scripts control — state change · with delay](automations/system/state-system-press-select-option-with-delay/README.md) | State change | `button.press`, `select.select_option` |
| [Configurable: action — trigger needs configuration](automations/system/triggered-generic-action/README.md) | Trigger needs configuration | `generic.action` |

<!-- catalogue:end -->
