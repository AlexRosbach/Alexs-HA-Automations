#!/usr/bin/env python3
"""Name public examples and maintain their documentation from finite metadata.

No original aliases, entity names or arbitrary service names enter the catalogue.
The metadata deliberately has no free-text fields: titles and summaries are
rendered from a reviewed vocabulary, not copied from a private installation.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

START = "<!-- catalogue:start -->"
END = "<!-- catalogue:end -->"
TRIGGERS = {
    "state": ("state", "State change"),
    "numeric_state": ("threshold", "Numeric threshold"),
    "time": ("scheduled", "Scheduled time"),
    "time_pattern": ("periodic", "Repeating schedule"),
    "sun": ("sun", "Sun event"),
    "event": ("event", "Event"),
    "template": ("template", "Template condition"),
    "device": ("device", "Device trigger"),
    "tag": ("tag", "Tag scan"),
    "mqtt": ("mqtt", "MQTT message"),
    "homeassistant": ("startup", "Home Assistant event"),
    "webhook": ("webhook", "Webhook"),
    "calendar": ("calendar", "Calendar event"),
    "zone": ("zone", "Zone event"),
    "conversation": ("voice", "Conversation"),
    "unknown": ("triggered", "Trigger needs configuration"),
}
TRIGGER_HINTS = {
    "state changes": "state", "numeric thresholds": "numeric_state",
    "a scheduled time": "time", "a repeating schedule": "time_pattern",
    "sun events": "sun", "Home Assistant events": "event",
    "a template condition": "template",
}
# These are catalogue concepts. *.call represents an anonymized custom service,
# not an executable Home Assistant action name.
ACTION_VERBS = {
    "automation": {"trigger", "turn_on", "turn_off", "toggle"},
    "assist_satellite": {"ask_question", "announce"},
    "button": {"press"}, "camera": {"snapshot", "play_stream"},
    "climate": {"set_temperature", "set_hvac_mode", "set_preset_mode", "turn_on", "turn_off"},
    "counter": {"reset", "increment", "decrement", "set_value"},
    "cover": {"open_cover", "close_cover", "stop_cover", "set_cover_position"},
    "dreame_vacuum": {"vacuum_clean_segment"},
    "fan": {"turn_on", "turn_off", "set_percentage", "set_preset_mode", "toggle"},
    "homeassistant": {"reload_config_entry", "turn_on", "turn_off", "toggle"},
    "input_boolean": {"turn_on", "turn_off", "toggle"},
    "input_button": {"press"}, "input_datetime": {"set_datetime"},
    "input_number": {"set_value"}, "input_text": {"set_value"},
    "light": {"turn_on", "turn_off", "toggle"},
    "lock": {"open", "lock", "unlock"},
    "media_player": {"volume_set", "play_media", "media_play_pause", "media_pause", "media_play", "turn_on", "turn_off"},
    "mqtt": {"publish"}, "notify": {"notify", "send_message", "call"},
    "persistent_notification": {"create", "dismiss"},
    "rest_command": {"call"}, "scene": {"turn_on"},
    "script": {"turn_on", "turn_off", "toggle", "call"},
    "select": {"select_option"}, "system_log": {"write"},
    "switch": {"turn_on", "turn_off", "toggle"},
    "todo": {"get_items", "add_item", "update_item", "remove_item", "remove_completed_items"},
    "tts": {"speak"}, "vacuum": {"start", "stop", "pause", "return_to_base", "set_fan_speed"},
    "weather": {"get_forecasts"}, "generic": {"action"},
}
ALLOWED_ACTIONS = {f"{domain}.{verb}" for domain, verbs in ACTION_VERBS.items() for verb in verbs}
FEATURES = {"conditions", "branches", "wait", "delay", "repeat", "parallel", "blueprint", "variables"}
CATEGORIES = {
    "climate": ("Climate", {"climate"}),
    "lighting": ("Lighting", {"light", "scene"}),
    "ventilation": ("Ventilation", {"fan"}),
    "cleaning": ("Cleaning", {"vacuum", "dreame_vacuum"}),
    "covers": ("Covers", {"cover"}),
    "media": ("Media and cameras", {"media_player", "camera"}),
    "access": ("Access", {"lock"}),
    "tasks": ("Tasks and reminders", {"todo"}),
    "switches": ("Switches", {"switch"}),
    "voice": ("Voice", {"assist_satellite", "tts"}),
    "notifications": ("Notifications", {"notify", "persistent_notification"}),
    "helpers": ("Helpers", {"counter", "input_boolean", "input_button", "input_datetime", "input_number", "input_text"}),
    "system": ("System and scripts", set()),
}
VERB_LABELS = {
    "turn_on": "on", "turn_off": "off", "turn_on+turn_off": "on and off",
    "turn_off+turn_on": "on and off", "toggle": "toggle", "set_temperature": "temperature",
    "set_hvac_mode": "mode", "set_preset_mode": "preset", "set_percentage": "speed",
    "open_cover": "open", "close_cover": "close", "open": "open",
    "volume_set": "volume", "play_media": "playback", "media_play_pause": "play or pause",
    "media_pause": "pause", "notify": "notification", "send_message": "message",
    "call": "custom action", "create": "notification", "get_items": "read tasks",
    "update_item": "update tasks", "remove_item": "remove tasks", "vacuum_clean_segment": "segment cleaning",
    "set_fan_speed": "speed", "set_value": "value", "set_datetime": "date and time",
    "ask_question": "question", "reload_config_entry": "reload integration",
    "get_forecasts": "forecast", "play_stream": "stream", "select_option": "selection",
    "write": "log entry", "action": "action",
}
DOMAIN_LABELS = {
    "light": "Light", "scene": "Scene", "climate": "Climate", "fan": "Fan",
    "vacuum": "Vacuum", "dreame_vacuum": "Vacuum", "cover": "Cover", "media_player": "Media",
    "camera": "Camera", "lock": "Lock", "todo": "Task list", "switch": "Switch",
    "notify": "Notification", "persistent_notification": "Persistent", "script": "Script",
    "rest_command": "REST", "assist_satellite": "Voice", "tts": "Speech",
    "generic": "Configurable", "homeassistant": "Home Assistant",
}
# Reader-facing language stays separate from canonical identifiers and YAML
# aliases. Changing a translation must never rename an automation or its files.
CATEGORIES_DE = {
    "climate": "Heizung und Raumklima",
    "lighting": "Licht",
    "ventilation": "Lüfter und Luftreiniger",
    "cleaning": "Saugroboter",
    "covers": "Rollläden und Abdeckungen",
    "media": "Musik, Medien und Kameras",
    "access": "Schlösser und Zutritt",
    "tasks": "Aufgabenlisten und Erinnerungen",
    "switches": "Schalter und Steckdosen",
    "voice": "Sprache und Durchsagen",
    "notifications": "Nachrichten und Hinweise",
    "helpers": "Zähler und gespeicherte Werte",
    "system": "Weitere Abläufe und Geräteaktionen",
}
SUBCATEGORIES_DE = {
    "climate": {
        "temperature": "Temperatur einstellen", "modes": "Heiz- und Kühlmodus",
        "profiles": "Heiz- und Klimaprofile", "power": "Ein- und Ausschalten",
    },
    "lighting": {
        "on": "Einschalten", "off": "Ausschalten", "toggle": "Umschalten",
        "on-off": "Ein- und Ausschalten", "scenes": "Szenen",
    },
    "ventilation": {
        "power": "Ein- und Ausschalten", "speed": "Geschwindigkeit einstellen",
        "profiles": "Betriebsprofile auswählen",
    },
    "cleaning": {
        "start": "Starten", "power": "Saugleistung einstellen",
        "areas": "Bestimmte Bereiche reinigen", "pause-stop": "Pausieren und stoppen",
        "charging": "Zur Ladestation schicken",
    },
    "covers": {
        "open": "Öffnen", "close": "Schließen", "open-close": "Öffnen und schließen",
        "position": "Position einstellen", "stop": "Bewegung stoppen",
    },
    "media": {
        "snapshots": "Kamerabilder speichern", "camera-live": "Kamerabild live anzeigen",
        "playback": "Medien wiedergeben und steuern",
    },
    "access": {
        "open": "Schloss öffnen", "lock": "Verriegeln", "unlock": "Entriegeln",
        "lock-unlock": "Verriegeln und entriegeln",
    },
    "tasks": {
        "read": "Aufgabenlisten abfragen", "add": "Aufgaben hinzufügen",
        "edit": "Einträge bearbeiten", "remove": "Einträge entfernen",
    },
    "switches": {
        "on": "Einschalten", "off": "Ausschalten", "toggle": "Umschalten",
        "on-off": "Ein- und Ausschalten",
    },
    "voice": {"announcements": "Durchsagen und Vorlesen", "questions": "Fragen per Sprache stellen"},
    "notifications": {
        "messages": "Nachrichten versenden", "ha-notices": "Hinweise in Home Assistant",
    },
    "helpers": {
        "switches": "Virtuelle Schalter", "counters": "Zähler verändern",
        "text": "Texte speichern", "numbers": "Zahlen speichern",
        "datetime": "Datum und Uhrzeit speichern", "buttons": "Virtuelle Tasten",
    },
    "system": {
        "scripts": "Eigene Skripte", "device-controls": "Gerätefunktionen und Tasten",
        "mqtt": "MQTT-Nachrichten", "automations": "Andere Automationen schalten",
        "weather": "Wetterdaten abrufen", "maintenance": "Wartung und Protokolle",
        "web-requests": "Vorbereitete Web-Anfragen", "unfinished": "Noch einzurichtende Aktionen",
        "other": "Weitere Funktionen",
    },
}
TRIGGERS_DE = {
    "state": "Wenn sich ein Wert oder Zustand ändert",
    "numeric_state": "Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet",
    "time": "Zu einer eingestellten Uhrzeit",
    "time_pattern": "In einem regelmäßig wiederholten Zeitabstand",
    "sun": "Rund um Sonnenaufgang oder Sonnenuntergang",
    "event": "Wenn ein festgelegtes Ereignis eintritt",
    "template": "Wenn eine selbst festgelegte Bedingung zutrifft",
    "device": "Wenn ein Gerät ein Ereignis meldet",
    "tag": "Wenn ein Tag gescannt wird",
    "mqtt": "Wenn eine MQTT-Nachricht ankommt",
    "homeassistant": "Bei einem Ereignis von Home Assistant",
    "webhook": "Wenn ein eingerichteter Webhook aufgerufen wird",
    "calendar": "Bei einem Ereignis im Kalender",
    "zone": "Wenn sich der Aufenthalt in einer Zone ändert",
    "conversation": "Bei einem eingerichteten Sprachbefehl",
    "unknown": "Der Auslöser muss noch eingerichtet werden",
}
TRIGGER_REQUIREMENTS_DE = {
    "numeric_state": "Einen passenden Sensor oder anderen Zahlenwert in Home Assistant und die gewünschte Messwertgrenze.",
    "state": "Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.",
    "device": "Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.",
}
ACTION_LABELS_DE = {
    "automation.trigger": "Eine andere Automation starten",
    "automation.turn_on": "Eine andere Automation aktivieren",
    "automation.turn_off": "Eine andere Automation deaktivieren",
    "automation.toggle": "Eine andere Automation umschalten",
    "assist_satellite.ask_question": "Eine Frage per Sprache stellen",
    "assist_satellite.announce": "Eine Durchsage abspielen",
    "button.press": "Eine Gerätefunktion per Tastendruck auslösen",
    "camera.snapshot": "Ein Kamerabild speichern",
    "camera.play_stream": "Ein Kamerabild live anzeigen",
    "climate.set_temperature": "Die gewünschte Raumtemperatur einstellen",
    "climate.set_hvac_mode": "Den Heiz- oder Kühlbetrieb einstellen",
    "climate.set_preset_mode": "Ein Heiz- oder Klimaprofil auswählen",
    "climate.turn_on": "Heizung oder Klimaanlage einschalten",
    "climate.turn_off": "Heizung oder Klimaanlage ausschalten",
    "counter.reset": "Einen Zähler zurücksetzen",
    "counter.increment": "Einen Zähler erhöhen",
    "counter.decrement": "Einen Zähler verringern",
    "counter.set_value": "Einen Zählerwert festlegen",
    "cover.open_cover": "Eine Abdeckung öffnen",
    "cover.close_cover": "Eine Abdeckung schließen",
    "cover.stop_cover": "Eine fahrende Abdeckung stoppen",
    "cover.set_cover_position": "Die Position einer Abdeckung einstellen",
    "dreame_vacuum.vacuum_clean_segment": "Einen ausgewählten Bereich saugen lassen",
    "fan.turn_on": "Einen Lüfter einschalten",
    "fan.turn_off": "Einen Lüfter ausschalten",
    "fan.set_percentage": "Die Lüftergeschwindigkeit einstellen",
    "fan.set_preset_mode": "Ein Lüfterprofil auswählen",
    "fan.toggle": "Einen Lüfter umschalten",
    "homeassistant.reload_config_entry": "Eine Geräteanbindung neu laden",
    "homeassistant.turn_on": "Ein Gerät einschalten",
    "homeassistant.turn_off": "Ein Gerät ausschalten",
    "homeassistant.toggle": "Ein Gerät umschalten",
    "input_boolean.turn_on": "Einen gespeicherten Ein/Aus-Wert einschalten",
    "input_boolean.turn_off": "Einen gespeicherten Ein/Aus-Wert ausschalten",
    "input_boolean.toggle": "Einen gespeicherten Ein/Aus-Wert umschalten",
    "input_button.press": "Eine eingerichtete Schaltfläche auslösen",
    "input_datetime.set_datetime": "Ein Datum oder eine Uhrzeit speichern",
    "input_number.set_value": "Einen Zahlenwert speichern",
    "input_text.set_value": "Einen Textwert speichern",
    "light.turn_on": "Licht einschalten",
    "light.turn_off": "Licht ausschalten",
    "light.toggle": "Licht zwischen Ein und Aus umschalten",
    "lock.open": "Ein Schloss öffnen",
    "lock.lock": "Ein Schloss verriegeln",
    "lock.unlock": "Ein Schloss entriegeln",
    "media_player.volume_set": "Die Lautstärke einstellen",
    "media_player.play_media": "Medien abspielen",
    "media_player.media_play_pause": "Die Wiedergabe starten oder pausieren",
    "media_player.media_pause": "Die Wiedergabe pausieren",
    "media_player.media_play": "Die Wiedergabe fortsetzen",
    "media_player.turn_on": "Ein Abspielgerät einschalten",
    "media_player.turn_off": "Ein Abspielgerät ausschalten",
    "mqtt.publish": "Eine MQTT-Nachricht senden",
    "notify.notify": "Eine Nachricht senden",
    "notify.send_message": "Eine Nachricht senden",
    "notify.call": "Eine Nachricht an ein eigenes Ziel senden",
    "persistent_notification.create": "Einen Hinweis in Home Assistant anzeigen",
    "persistent_notification.dismiss": "Einen Hinweis in Home Assistant entfernen",
    "rest_command.call": "Eine vorbereitete Web-Anfrage ausführen",
    "scene.turn_on": "Eine gespeicherte Szene aktivieren",
    "script.turn_on": "Ein vorhandenes Skript starten",
    "script.turn_off": "Ein laufendes Skript stoppen",
    "script.toggle": "Ein Skript starten oder stoppen",
    "script.call": "Ein eigenes Skript ausführen",
    "select.select_option": "Eine Geräteoption auswählen",
    "system_log.write": "Einen Eintrag ins Systemprotokoll schreiben",
    "switch.turn_on": "Einen Schalter einschalten",
    "switch.turn_off": "Einen Schalter ausschalten",
    "switch.toggle": "Einen Schalter zwischen Ein und Aus umschalten",
    "todo.get_items": "Eine Aufgabenliste abfragen",
    "todo.add_item": "Eine Aufgabe hinzufügen",
    "todo.update_item": "Einen Eintrag in einer Aufgabenliste ändern",
    "todo.remove_item": "Einen Eintrag aus einer Aufgabenliste entfernen",
    "todo.remove_completed_items": "Erledigte Aufgaben entfernen",
    "tts.speak": "Einen Text vorlesen lassen",
    "vacuum.start": "Einen Saugroboter starten",
    "vacuum.stop": "Einen Saugroboter stoppen",
    "vacuum.pause": "Einen Saugroboter pausieren",
    "vacuum.return_to_base": "Einen Saugroboter zur Ladestation schicken",
    "vacuum.set_fan_speed": "Die Saugleistung einstellen",
    "weather.get_forecasts": "Eine Wettervorhersage abrufen",
    "generic.action": "Eine noch offene Aktion ergänzen",
}
REQUIREMENTS_DE = {
    "automation": "Die anderen Automationen, die du damit starten oder schalten möchtest.",
    "assist_satellite": "Ein in Home Assistant eingerichtetes Sprachgerät.",
    "button": "Eine Gerätefunktion, die Home Assistant als Taste bereitstellt.",
    "camera": "Eine eingebundene Kamera mit der benötigten Bild- oder Videofunktion.",
    "climate": "Ein eingebundenes Thermostat oder eine Klimaanlage.",
    "counter": "Einen Zähler-Helfer in Home Assistant.",
    "cover": "Ein passendes Gerät, zum Beispiel einen Rollladen oder ein Rollo.",
    "dreame_vacuum": "Einen passenden Saugroboter mit eingerichteten Reinigungsbereichen.",
    "fan": "Einen Lüfter oder Luftreiniger, den Home Assistant steuern kann.",
    "homeassistant": "Die Geräteanbindung oder Geräte, auf die sich die Aktion beziehen soll.",
    "input_boolean": "Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.",
    "input_button": "Eine als Helfer eingerichtete Schaltfläche in Home Assistant.",
    "input_datetime": "Einen Helfer, der ein Datum oder eine Uhrzeit speichert.",
    "input_number": "Einen Helfer, der einen Zahlenwert speichert.",
    "input_text": "Einen Helfer, der einen Textwert speichert.",
    "light": "Lampen, die Home Assistant steuern kann.",
    "lock": "Ein Schloss, das Home Assistant steuern kann.",
    "media_player": "Ein eingebundenes Abspielgerät, zum Beispiel einen Lautsprecher.",
    "mqtt": "Eine eingerichtete MQTT-Anbindung für den Nachrichtenaustausch zwischen Geräten.",
    "notify": "Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.",
    "persistent_notification": "Home Assistant für die Anzeige der Hinweise.",
    "rest_command": "Eine vorbereitete Web-Anfrage, die in Home Assistant als REST-Befehl eingerichtet ist.",
    "scene": "Eine gespeicherte Szene mit den gewünschten Geräteeinstellungen.",
    "script": "Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.",
    "select": "Ein Gerät mit einer in Home Assistant auswählbaren Option.",
    "system_log": "Home Assistant für die Protokolleinträge.",
    "switch": "Einen Schalter oder eine schaltbare Steckdose in Home Assistant.",
    "todo": "Eine in Home Assistant eingerichtete Aufgabenliste.",
    "tts": "Eine eingerichtete Sprachausgabe und ein passendes Abspielgerät.",
    "vacuum": "Einen in Home Assistant eingebundenen Saugroboter.",
    "weather": "Eine Wetteranbindung, die Vorhersagen bereitstellt.",
    "generic": "Die Geräte und die Aktion, die du selbst ergänzen möchtest.",
}
CATEGORIES_EN = {
    "climate": "Heating and cooling", "lighting": "Lights",
    "ventilation": "Fans and air purifiers", "cleaning": "Robot vacuums",
    "covers": "Blinds and covers", "media": "Music, media and cameras",
    "access": "Locks and access", "tasks": "Task lists and reminders",
    "switches": "Switches and sockets", "voice": "Voice and announcements",
    "notifications": "Messages and notices", "helpers": "Counters and stored values",
    "system": "More routines and device actions",
}
SUBCATEGORIES_EN = {
    "climate": {
        "temperature": "Set the temperature", "modes": "Heating and cooling modes",
        "profiles": "Heating and cooling presets", "power": "Turn on and off",
    },
    "lighting": {
        "on": "Turn on", "off": "Turn off", "toggle": "Toggle",
        "on-off": "Turn on and off", "scenes": "Scenes",
    },
    "ventilation": {
        "power": "Turn on and off", "speed": "Set the speed", "profiles": "Choose a preset",
    },
    "cleaning": {
        "start": "Start cleaning", "power": "Set suction power", "areas": "Clean selected areas",
        "pause-stop": "Pause and stop", "charging": "Return to the dock",
    },
    "covers": {
        "open": "Open", "close": "Close", "open-close": "Open and close",
        "position": "Set the position", "stop": "Stop movement",
    },
    "media": {
        "snapshots": "Save camera pictures", "camera-live": "Show a live camera view",
        "playback": "Play and control media",
    },
    "access": {
        "open": "Open a lock", "lock": "Lock", "unlock": "Unlock", "lock-unlock": "Lock and unlock",
    },
    "tasks": {
        "read": "Read task lists", "add": "Add tasks", "edit": "Edit tasks", "remove": "Remove tasks",
    },
    "switches": {"on": "Turn on", "off": "Turn off", "toggle": "Toggle", "on-off": "Turn on and off"},
    "voice": {"announcements": "Announcements and spoken text", "questions": "Ask spoken questions"},
    "notifications": {"messages": "Send messages", "ha-notices": "Notices in Home Assistant"},
    "helpers": {
        "switches": "Virtual switches", "counters": "Change counters", "text": "Store text",
        "numbers": "Store numbers", "datetime": "Store dates and times", "buttons": "Virtual buttons",
    },
    "system": {
        "scripts": "Your own scripts", "device-controls": "Device functions and buttons",
        "mqtt": "MQTT messages", "automations": "Control other automations",
        "weather": "Get weather data", "maintenance": "Maintenance and logs",
        "web-requests": "Configured web requests", "unfinished": "Actions to set up", "other": "Other functions",
    },
}
TRIGGERS_EN = {
    "state": "When a value or state changes",
    "numeric_state": "When a reading crosses a chosen limit",
    "time": "At a chosen time",
    "time_pattern": "At a regularly repeating time interval",
    "sun": "Around sunrise or sunset",
    "event": "When a chosen event occurs",
    "template": "When a condition you define becomes true",
    "device": "When a device reports an event",
    "tag": "When a tag is scanned",
    "mqtt": "When an MQTT message arrives",
    "homeassistant": "When a Home Assistant event occurs",
    "webhook": "When a configured webhook is called",
    "calendar": "When a calendar event occurs",
    "zone": "When presence in a zone changes",
    "conversation": "When a configured voice command is spoken",
    "unknown": "The trigger still needs to be set up",
}
TRIGGER_REQUIREMENTS_EN = {
    "numeric_state": "A suitable sensor or other number in Home Assistant, and the limit you want to use.",
    "state": "A value or state whose change should start the routine, for example from a device, sensor or helper.",
    "device": "A connected device that provides a suitable event as a trigger.",
}
ACTION_LABELS_EN = {
    "automation.trigger": "Start another automation",
    "automation.turn_on": "Enable another automation",
    "automation.turn_off": "Disable another automation",
    "automation.toggle": "Toggle another automation",
    "assist_satellite.ask_question": "Ask a spoken question",
    "assist_satellite.announce": "Play an announcement",
    "button.press": "Run a device function by pressing a button",
    "camera.snapshot": "Save a camera picture",
    "camera.play_stream": "Show a live camera view",
    "climate.set_temperature": "Set the desired room temperature",
    "climate.set_hvac_mode": "Set the heating or cooling mode",
    "climate.set_preset_mode": "Choose a heating or cooling preset",
    "climate.turn_on": "Turn on heating or air conditioning",
    "climate.turn_off": "Turn off heating or air conditioning",
    "counter.reset": "Reset a counter",
    "counter.increment": "Increase a counter",
    "counter.decrement": "Decrease a counter",
    "counter.set_value": "Set a counter value",
    "cover.open_cover": "Open a blind or cover",
    "cover.close_cover": "Close a blind or cover",
    "cover.stop_cover": "Stop a moving blind or cover",
    "cover.set_cover_position": "Set the position of a blind or cover",
    "dreame_vacuum.vacuum_clean_segment": "Vacuum a selected area",
    "fan.turn_on": "Turn on a fan",
    "fan.turn_off": "Turn off a fan",
    "fan.set_percentage": "Set the fan speed",
    "fan.set_preset_mode": "Choose a fan preset",
    "fan.toggle": "Toggle a fan",
    "homeassistant.reload_config_entry": "Reload a device integration",
    "homeassistant.turn_on": "Turn on a device",
    "homeassistant.turn_off": "Turn off a device",
    "homeassistant.toggle": "Toggle a device",
    "input_boolean.turn_on": "Turn on a stored on/off value",
    "input_boolean.turn_off": "Turn off a stored on/off value",
    "input_boolean.toggle": "Toggle a stored on/off value",
    "input_button.press": "Press a configured virtual button",
    "input_datetime.set_datetime": "Store a date or time",
    "input_number.set_value": "Store a number",
    "input_text.set_value": "Store some text",
    "light.turn_on": "Turn on lights",
    "light.turn_off": "Turn off lights",
    "light.toggle": "Switch lights between on and off",
    "lock.open": "Open a lock",
    "lock.lock": "Lock a lock",
    "lock.unlock": "Unlock a lock",
    "media_player.volume_set": "Set the volume",
    "media_player.play_media": "Play media",
    "media_player.media_play_pause": "Play or pause media",
    "media_player.media_pause": "Pause media",
    "media_player.media_play": "Resume media playback",
    "media_player.turn_on": "Turn on a media player",
    "media_player.turn_off": "Turn off a media player",
    "mqtt.publish": "Send an MQTT message",
    "notify.notify": "Send a message",
    "notify.send_message": "Send a message",
    "notify.call": "Send a message to your own notification destination",
    "persistent_notification.create": "Show a notice in Home Assistant",
    "persistent_notification.dismiss": "Remove a notice from Home Assistant",
    "rest_command.call": "Run a configured web request",
    "scene.turn_on": "Activate a saved scene",
    "script.turn_on": "Start an existing script",
    "script.turn_off": "Stop a running script",
    "script.toggle": "Start or stop a script",
    "script.call": "Run your own script",
    "select.select_option": "Select a device option",
    "system_log.write": "Write an entry in the system log",
    "switch.turn_on": "Turn on a switch",
    "switch.turn_off": "Turn off a switch",
    "switch.toggle": "Switch between on and off",
    "todo.get_items": "Read a task list",
    "todo.add_item": "Add a task",
    "todo.update_item": "Update an item in a task list",
    "todo.remove_item": "Remove an item from a task list",
    "todo.remove_completed_items": "Remove completed tasks",
    "tts.speak": "Read text aloud",
    "vacuum.start": "Start a robot vacuum",
    "vacuum.stop": "Stop a robot vacuum",
    "vacuum.pause": "Pause a robot vacuum",
    "vacuum.return_to_base": "Send a robot vacuum back to its dock",
    "vacuum.set_fan_speed": "Set the suction power",
    "weather.get_forecasts": "Get a weather forecast",
    "generic.action": "Fill in an unfinished action",
}
REQUIREMENTS_EN = {
    "automation": "The other automations you want to start or control.",
    "assist_satellite": "A voice device set up in Home Assistant.",
    "button": "A device function that Home Assistant provides as a button.",
    "camera": "A connected camera with the picture or video function you need.",
    "climate": "A connected thermostat or air conditioner.",
    "counter": "A counter helper in Home Assistant.",
    "cover": "A suitable device, such as a roller shutter or blind.",
    "dreame_vacuum": "A suitable robot vacuum with cleaning areas set up.",
    "fan": "A fan or air purifier that Home Assistant can control.",
    "homeassistant": "The device integration or devices you want the action to use.",
    "input_boolean": "A toggle helper: an on/off value stored in Home Assistant.",
    "input_button": "A button set up as a helper in Home Assistant.",
    "input_datetime": "A helper that stores a date or time.",
    "input_number": "A helper that stores a number.",
    "input_text": "A helper that stores text.",
    "light": "Lights that Home Assistant can control.",
    "lock": "A lock that Home Assistant can control.",
    "media_player": "A connected media player, such as a speaker.",
    "mqtt": "An MQTT integration set up to exchange messages between devices.",
    "notify": "A configured notification destination, such as the Home Assistant app.",
    "persistent_notification": "Home Assistant to display the notices.",
    "rest_command": "A web request configured as a REST command in Home Assistant.",
    "scene": "A saved scene with your chosen device settings.",
    "script": "An existing Home Assistant script: a saved sequence of actions.",
    "select": "A device with an option you can select in Home Assistant.",
    "system_log": "Home Assistant to record the log entries.",
    "switch": "A switch or smart socket in Home Assistant.",
    "todo": "A task list set up in Home Assistant.",
    "tts": "Text-to-speech set up with a suitable media player.",
    "vacuum": "A robot vacuum connected to Home Assistant.",
    "weather": "A weather integration that provides forecasts.",
    "generic": "The devices and action you want to add yourself.",
}
LANGUAGES = {
    "en": {"readme": "README.md", "guide": "get-started.md", "categories": CATEGORIES_EN,
           "subcategories": SUBCATEGORIES_EN, "triggers": TRIGGERS_EN,
           "trigger_requirements": TRIGGER_REQUIREMENTS_EN, "actions": ACTION_LABELS_EN,
           "requirements": REQUIREMENTS_EN},
    "de": {"readme": "README.de.md", "guide": "get-started.de.md", "categories": CATEGORIES_DE,
           "subcategories": SUBCATEGORIES_DE, "triggers": TRIGGERS_DE,
           "trigger_requirements": TRIGGER_REQUIREMENTS_DE, "actions": ACTION_LABELS_DE,
           "requirements": REQUIREMENTS_DE},
}

METADATA_KEYS = {"schema_version", "category", "slug", "trigger_types", "actions", "features", "trigger_count", "action_count", "variant"}
SLUG_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


class CatalogueError(ValueError):
    """An error whose message must not include private source values."""


def _items(value: Any) -> list[Any]:
    return value if isinstance(value, list) else [value] if value is not None else []


def infer_trigger_types(config: dict[str, Any], hint_text: str = "") -> list[str]:
    found = {kind for text, kind in TRIGGER_HINTS.items() if text in hint_text}
    for item in _items(config.get("triggers", config.get("trigger"))):
        if not isinstance(item, dict):
            continue
        kind = item.get("trigger", item.get("platform"))
        if isinstance(kind, str) and kind in TRIGGERS:
            found.add(kind)
        elif "device_id" in item:
            found.add("device")
        elif "tag_id" in item:
            found.add("tag")
        elif "topic" in item:
            found.add("mqtt")
    return sorted(found or {"unknown"})


def action_ids(config: dict[str, Any]) -> list[str]:
    found: set[str] = set()
    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"action", "service"} and isinstance(child, str) and "." in child:
                    domain = child.split(".", 1)[0]
                    if child in ALLOWED_ACTIONS:
                        found.add(child)
                    elif domain in {"notify", "script", "rest_command"}:
                        found.add(f"{domain}.call")
                    else:
                        found.add("generic.action")
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(config.get("actions", config.get("action", [])))
    return sorted(found or {"generic.action"})


def _features(config: dict[str, Any]) -> list[str]:
    found: set[str] = set()
    key_features = {"choose": "branches", "if": "branches", "wait_for_trigger": "wait", "wait_template": "wait", "delay": "delay", "repeat": "repeat", "parallel": "parallel", "use_blueprint": "blueprint", "variables": "variables"}
    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in key_features:
                    found.add(key_features[key])
                if key in {"condition", "conditions"} and child:
                    found.add("conditions")
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(config)
    return sorted(found)


def _category(actions: list[str]) -> str:
    domains = {action.split(".", 1)[0] for action in actions}
    for category, (_, matches) in CATEGORIES.items():
        if domains & matches:
            return category
    return "system"


def _primary_actions(metadata: dict[str, Any]) -> list[str]:
    domains = CATEGORIES[metadata["category"]][1]
    found = [a for a in metadata["actions"] if a.split(".")[0] in domains]
    return found or metadata["actions"]


def _slug_base(metadata: dict[str, Any]) -> str:
    triggers = metadata["trigger_types"]
    start = "mixed" if len(triggers) > 2 else "-".join(TRIGGERS[t][0] for t in triggers)
    primary = _primary_actions(metadata)
    domains = sorted({a.split(".")[0] for a in primary})
    domain = domains[0] if len(domains) == 1 else metadata["category"]
    verbs = sorted({a.split(".")[1] for a in primary}, key=lambda v: ({"turn_on": 0, "turn_off": 1}.get(v, 2), v))
    short = {"turn_on": "on", "turn_off": "off", "set_temperature": "temperature", "set_hvac_mode": "mode", "set_preset_mode": "preset", "set_percentage": "speed", "open_cover": "open", "close_cover": "close", "media_play_pause": "play-pause", "media_pause": "pause", "play_media": "playback", "volume_set": "volume", "send_message": "message", "get_items": "read", "update_item": "update", "remove_item": "remove", "call": "custom-action", "set_value": "value"}
    if domain == "notify":
        domain, short["call"], short["notify"], short["send_message"] = "notification", "send", "send", "send"
    elif domain in {"script", "rest_command"}:
        short["call"] = "run"
    verbs_text = "-".join(dict.fromkeys(short.get(v, v.replace("_", "-")) for v in verbs)) if len(verbs) <= 3 else "control"
    features = metadata["features"]
    qualifier = "-with-wait" if "wait" in features else "-with-delay" if "delay" in features else "-with-branches" if "branches" in features else ""
    return f"{start}-{domain.replace('_', '-')}-{verbs_text}{qualifier}"


def build_metadata(config: dict[str, Any], trigger_types: list[str] | None = None) -> dict[str, Any]:
    if not isinstance(config, dict):
        raise CatalogueError("Automation configuration must be a mapping.")
    hints = trigger_types if trigger_types is not None else infer_trigger_types(config)
    if not isinstance(hints, list) or not hints or any(not isinstance(t, str) or t not in TRIGGERS for t in hints):
        raise CatalogueError("Invalid trigger metadata.")
    actions = action_ids(config)
    metadata = {
        "schema_version": 1, "category": _category(actions), "slug": "",
        "trigger_types": sorted(set(hints)), "actions": actions, "features": _features(config),
        "trigger_count": len(_items(config.get("triggers", config.get("trigger")))),
        "action_count": len(_items(config.get("actions", config.get("action")))),
        "variant": "",
    }
    metadata["slug"] = _slug_base(metadata)
    return validate_metadata(metadata)


def validate_metadata(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != METADATA_KEYS:
        raise CatalogueError("Invalid catalogue metadata fields.")
    if type(value["schema_version"]) is not int or value["schema_version"] != 1 or not isinstance(value["category"], str) or value["category"] not in CATEGORIES:
        raise CatalogueError("Invalid catalogue metadata version or category.")
    for key, allowed in (("trigger_types", set(TRIGGERS)), ("actions", ALLOWED_ACTIONS), ("features", FEATURES)):
        items = value[key]
        if not isinstance(items, list) or any(not isinstance(item, str) or item not in allowed for item in items):
            raise CatalogueError("Unknown catalogue metadata vocabulary.")
        if items != sorted(set(items)) or (key != "features" and not items):
            raise CatalogueError("Catalogue lists must be sorted, unique and complete.")
    for key in ("trigger_count", "action_count"):
        if type(value[key]) is not int or not 0 <= value[key] <= 10000:
            raise CatalogueError("Invalid catalogue step count.")
    variant = value["variant"]
    if not isinstance(variant, str) or (variant and not re.fullmatch(r"[a-f0-9]{8}(?:-[a-z]{1,2})?", variant)):
        raise CatalogueError("Invalid catalogue variant fingerprint.")
    if value["category"] != _category(value["actions"]):
        raise CatalogueError("Category does not match the public action concepts.")
    expected = _slug_base(value) + (f"-{variant}" if variant else "")
    if not isinstance(value["slug"], str) or value["slug"] != expected or len(expected) > 180 or not SLUG_RE.fullmatch(expected):
        raise CatalogueError("Invalid descriptive automation name.")
    return value


def render_alias(metadata: dict[str, Any]) -> str:
    validate_metadata(metadata)
    primary = _primary_actions(metadata)
    domains = sorted({a.split(".")[0] for a in primary})
    if len(domains) == 1:
        domain = domains[0]
        verbs = sorted({a.split(".")[1] for a in primary}, key=lambda v: ({"turn_on": 0, "turn_off": 1}.get(v, 2), v))
        noun = DOMAIN_LABELS.get(domain, domain.replace("_", " ").capitalize())
        verb_text = "send" if domain == "notify" else ", ".join("run" if v == "call" else VERB_LABELS.get(v, v.replace("_", " ")) for v in verbs)
        purpose = f"{noun}: {verb_text}"
    else:
        purpose = f"{CATEGORIES[metadata['category']][0]} control"
    trigger = ", ".join(TRIGGERS[t][1].lower() for t in metadata["trigger_types"])
    features = metadata["features"]
    qualifier = "with wait" if "wait" in features else "with delay" if "delay" in features else "with branches" if "branches" in features else ""
    return f"{purpose} — {trigger}" + (f" · {qualifier}" if qualifier else "") + (f" ({metadata['variant']})" if metadata["variant"] else "")


def render_description(metadata: dict[str, Any]) -> str:
    validate_metadata(metadata)
    actions = ", ".join(a.replace(".call", ".custom_action") for a in metadata["actions"])
    return f"Public template using {actions}. Configure all placeholders and restore missing trigger or template details before use."


def subcategory(metadata: dict[str, Any], language: str = "en") -> tuple[str, str]:
    """Assign exactly one task-based subgroup from reviewed action concepts."""
    validate_metadata(metadata)
    category = metadata["category"]
    actions = set(_primary_actions(metadata))
    all_actions = set(metadata["actions"])
    if category in {"lighting", "switches"}:
        domain = "light" if category == "lighting" else "switch"
        if category == "lighting" and "scene.turn_on" in actions:
            key = "scenes"
        elif {f"{domain}.turn_on", f"{domain}.turn_off"} <= actions:
            key = "on-off"
        elif f"{domain}.toggle" in actions:
            key = "toggle"
        elif f"{domain}.turn_on" in actions:
            key = "on"
        else:
            key = "off"
    elif category == "climate":
        key = "profiles" if "climate.set_preset_mode" in actions else "modes" if "climate.set_hvac_mode" in actions else "temperature" if "climate.set_temperature" in actions else "power"
    elif category == "ventilation":
        key = "profiles" if "fan.set_preset_mode" in actions else "speed" if "fan.set_percentage" in actions else "power"
    elif category == "cleaning":
        key = "areas" if "dreame_vacuum.vacuum_clean_segment" in actions else "power" if "vacuum.set_fan_speed" in actions else "start" if "vacuum.start" in actions else "charging" if "vacuum.return_to_base" in actions else "pause-stop"
    elif category == "covers":
        key = "open-close" if {"cover.open_cover", "cover.close_cover"} <= actions else "position" if "cover.set_cover_position" in actions else "open" if "cover.open_cover" in actions else "close" if "cover.close_cover" in actions else "stop"
    elif category == "media":
        key = "camera-live" if "camera.play_stream" in actions else "snapshots" if actions == {"camera.snapshot"} else "playback"
    elif category == "access":
        key = "open" if "lock.open" in actions else "lock-unlock" if {"lock.lock", "lock.unlock"} <= actions else "lock" if "lock.lock" in actions else "unlock"
    elif category == "tasks":
        key = "remove" if actions & {"todo.remove_item", "todo.remove_completed_items"} else "edit" if "todo.update_item" in actions else "add" if "todo.add_item" in actions else "read"
    elif category == "voice":
        key = "questions" if "assist_satellite.ask_question" in actions else "announcements"
    elif category == "notifications":
        key = "ha-notices" if any(a.startswith("persistent_notification.") for a in actions) else "messages"
    elif category == "helpers":
        domains = {a.split(".", 1)[0] for a in actions}
        key = "counters" if "counter" in domains else "switches" if "input_boolean" in domains else "text" if "input_text" in domains else "numbers" if "input_number" in domains else "datetime" if "input_datetime" in domains else "buttons"
    else:
        domains = {a.split(".", 1)[0] for a in all_actions}
        if "generic.action" in all_actions:
            key = "unfinished"
        elif "weather.get_forecasts" in all_actions:
            key = "weather"
        elif "mqtt.publish" in all_actions:
            key = "mqtt"
        elif "homeassistant.reload_config_entry" in all_actions or "system_log" in domains:
            key = "maintenance"
        elif "automation" in domains:
            key = "automations"
        elif domains & {"button", "select"}:
            key = "device-controls"
        elif "script" in domains:
            key = "scripts"
        elif "rest_command" in domains:
            key = "web-requests"
        else:
            key = "other"
    return key, _language(language)["subcategories"][category][key]


def _group_entries(entries: list[tuple[Path, dict[str, Any]]]) -> dict[str, dict[str, list[tuple[Path, dict[str, Any]]]]]:
    groups: dict[str, dict[str, list[tuple[Path, dict[str, Any]]]]] = {}
    for entry in entries:
        _, metadata = entry
        key, _ = subcategory(metadata)
        groups.setdefault(metadata["category"], {}).setdefault(key, []).append(entry)
    return groups


def _language(language: str) -> dict[str, Any]:
    if language not in LANGUAGES:
        raise CatalogueError("Unsupported documentation language.")
    return LANGUAGES[language]


def _action_groups(actions: list[str], language: str = "en") -> list[str]:
    """Describe action capabilities without asserting order or missing causes."""
    vocabulary = _language(language)
    def text(english: str, german: str) -> str:
        return german if language == "de" else english

    groups: dict[str, set[str]] = {}
    for action in actions:
        domain, verb = action.split(".", 1)
        groups.setdefault(domain, set()).add(verb)
    labels: list[str] = []
    for domain, verbs in groups.items():
        label = ""
        if domain in {"light", "switch", "fan", "input_boolean", "homeassistant"} and {"turn_on", "turn_off"} <= verbs:
            both = {
                "light": text("Turn lights on and off", "Licht ein- und ausschalten"),
                "switch": text("Turn switches on and off", "Schalter ein- und ausschalten"),
                "fan": text("Turn fans on and off", "Lüfter ein- und ausschalten"),
                "input_boolean": text("Change stored on/off values", "Gespeicherte Ein/Aus-Werte ändern"),
                "homeassistant": text("Turn devices on and off", "Geräte ein- und ausschalten"),
            }
            label = both[domain]
            if domain == "fan" and verbs - {"turn_on", "turn_off"}:
                label = text("Turn fans on and off and adjust their settings", "Lüfter ein- und ausschalten sowie einstellen")
            elif "toggle" in verbs:
                label = {
                    "light": text("Control lights", "Licht schalten"),
                    "switch": text("Control switches", "Schalter steuern"),
                    "fan": text("Control fans", "Lüfter schalten"),
                    "input_boolean": text("Change stored on/off values", "Gespeicherte Ein/Aus-Werte ändern"),
                    "homeassistant": text("Control devices", "Geräte schalten"),
                }[domain]
        elif domain == "light" and verbs == {"turn_on", "toggle"}:
            label = text("Turn on or toggle lights", "Licht einschalten oder umschalten")
        elif domain == "climate" and len(verbs) > 1:
            label = text("Adjust heating or air conditioning", "Heizung oder Klimaanlage einstellen")
        elif domain == "cover" and verbs == {"open_cover", "close_cover"}:
            label = text("Open and close a blind or cover", "Eine Abdeckung öffnen und schließen")
        elif domain == "notify":
            label = text("Send messages", "Nachrichten senden")
        elif domain == "todo" and {"get_items", "update_item"} == verbs:
            label = text("Read and edit a task list", "Eine Aufgabenliste lesen und bearbeiten")
        elif domain == "todo" and {"get_items", "remove_item"} == verbs:
            label = text("Read a task list and remove items", "Eine Aufgabenliste lesen und Einträge entfernen")
        elif domain == "script" and verbs <= {"call", "turn_on"}:
            label = text("Run an existing script", "Ein vorhandenes Skript ausführen")
        elif domain == "script" and len(verbs) > 1:
            label = text("Start or stop your own scripts", "Eigene Skripte starten oder stoppen")
        elif domain == "media_player" and len(verbs) > 1:
            label = text("Control media playback", "Die Medienwiedergabe steuern")
        elif domain == "vacuum" and verbs == {"start", "set_fan_speed"}:
            label = text("Start a robot vacuum and set its suction power", "Einen Saugroboter starten und die Saugleistung einstellen")
        elif domain == "automation" and verbs == {"turn_on", "turn_off"}:
            label = text("Enable and disable other automations", "Andere Automationen aktivieren und deaktivieren")
        if label:
            labels.append(label)
        else:
            labels.extend(vocabulary["actions"].get(f"{domain}.{verb}", text("Set up another action", "Eine weitere Aktion einrichten")) for verb in sorted(verbs))
    return list(dict.fromkeys(labels))


def _qualifier(metadata: dict[str, Any], language: str = "en") -> str:
    features = metadata["features"]
    # A delay can belong to a secondary action. Never call the primary action
    # "delayed" merely because a delay exists somewhere in the configuration.
    if "wait" in features:
        return "mit Wartebedingung im Ablauf" if language == "de" else "with a wait condition in the routine"
    if "delay" in features:
        return "mit Wartezeit im Ablauf" if language == "de" else "with a delay in the routine"
    if "branches" in features:
        return "mit Bedingungen im Ablauf" if language == "de" else "with conditions in the routine"
    return ""


def render_public_title(metadata: dict[str, Any], language: str = "en") -> str:
    """Beginner-facing title; does not affect canonical YAML aliases."""
    validate_metadata(metadata)
    vocabulary = _language(language)
    labels = _action_groups(_primary_actions(metadata), language)
    if len(labels) == 1:
        title = labels[0]
    else:
        combinations = {
            "climate": ("Control heating or air conditioning", "Heizung oder Klimaanlage steuern"),
            "lighting": ("Control lights and scenes", "Licht und Szenen steuern"),
            "ventilation": ("Adjust fans", "Lüfter einstellen"),
            "cleaning": ("Control a robot vacuum", "Einen Saugroboter steuern"),
            "covers": ("Control a blind or cover", "Eine Abdeckung steuern"),
            "media": ("Control media and cameras", "Medien und Kameras steuern"),
            "access": ("Control a lock", "Ein Schloss steuern"),
            "tasks": ("Edit a task list", "Eine Aufgabenliste bearbeiten"),
            "switches": ("Control switches", "Schalter steuern"),
            "voice": ("Use announcements and spoken text", "Durchsagen und Sprachausgabe nutzen"),
            "notifications": ("Send messages and show notices", "Nachrichten und Hinweise ausgeben"),
            "helpers": ("Change stored values", "Gespeicherte Werte ändern"),
            "system": ("Combine several functions", "Mehrere Funktionen verbinden"),
        }
        title = combinations[metadata["category"]][language == "de"]
    if title == vocabulary["actions"]["generic.action"]:
        title = "Eigene Aktion einrichten" if language == "de" else "Set up your own action"
    qualifier = _qualifier(metadata, language)
    return title + (f" · {qualifier}" if qualifier else "")


def _visible_variants(entries: list[tuple[Path, dict[str, Any]]], language: str = "en") -> dict[str, str]:
    _language(language)
    groups: dict[tuple[str, str, str, tuple[str, ...]], list[dict[str, Any]]] = {}
    for _, metadata in entries:
        # Group by the same English presentation in both languages so a variant
        # keeps its letter when a reader switches language.
        key = (metadata["category"], subcategory(metadata)[0], render_public_title(metadata), tuple(metadata["trigger_types"]))
        groups.setdefault(key, []).append(metadata)
    label = "Variante" if language == "de" else "Variant"
    return {metadata["slug"]: f"{label} {_letters(number).upper()}"
            for group in groups.values() if len(group) > 1
            for number, metadata in enumerate(sorted(group, key=lambda item: item["slug"]))}


def render_example_readme(metadata: dict[str, Any], variant_label: str = "", language: str = "en", config: dict[str, Any] | None = None) -> str:
    vocabulary = _language(language)
    title = render_public_title(metadata, language) + (f" — {variant_label}" if variant_label else "")
    category = metadata["category"]
    subcategory_key, subcategory_label = subcategory(metadata, language)
    readme, guide = vocabulary["readme"], vocabulary["guide"]
    breadcrumb = f"[{vocabulary['categories'][category]}](../../../{readme}#{category}) → [{subcategory_label}](../../../{readme}#{category}-{subcategory_key})"
    actions = _action_groups(metadata["actions"], language)
    lead = "Diese Automation verbindet folgende Funktionen:" if language == "de" else "This automation combines these functions:"
    purpose = actions[0] + "." if len(actions) == 1 else lead + "\n\n" + "\n".join(f"- {label}." for label in actions)
    if "generic.action" in metadata["actions"]:
        purpose += "\n\n" + ("Die konkrete Aktion ist im Export nicht mehr vollständig erkennbar. Du musst die fehlenden Schritte selbst ergänzen." if language == "de" else "The original export no longer shows the full action. You need to add the missing steps yourself.")
    triggers = "\n".join(f"- {vocabulary['triggers'][kind]}." for kind in metadata["trigger_types"])
    if config is not None:
        from automation_details import render_details, summarize
        purpose = summarize(config, metadata, language)
        behavior = render_details(config, language).rstrip()
    elif language == "de":
        behavior = "## Wann startet sie?\n\n" + triggers + "\n\nDie genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest."
    else:
        behavior = "## What starts it?\n\n" + triggers + "\n\nYou choose the exact devices, values and conditions when setting it up."
    domains = sorted({action.split(".", 1)[0] for action in metadata["actions"]})
    default_requirement = "Die passende Gerätefunktion in Home Assistant." if language == "de" else "The matching device function in Home Assistant."
    requirement_items = [vocabulary["requirements"].get(domain, default_requirement) for domain in domains]
    requirement_items += [vocabulary["trigger_requirements"][kind] for kind in metadata["trigger_types"] if kind in vocabulary["trigger_requirements"]]
    requirements = "\n".join(f"- {item}" for item in dict.fromkeys(requirement_items))
    if language == "de":
        return f"""# {title}

[English](README.md) · **Deutsch**

{breadcrumb}

[Alle Automationen ansehen](../../../{readme}#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/{guide})

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

{purpose}

{behavior}

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

{requirements}

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/{guide}).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
"""
    return f"""# {title}

**English** · [Deutsch](README.de.md)

{breadcrumb}

[Browse all automations](../../../{readme}#automation-catalogue) · [Set up step by step](../../../how-to/{guide})

An anonymized Home Assistant example, shared for inspiration.

This is an anonymized copy. Replace the placeholders and restore any missing logic before using it in your own setup.

## What does this example do?

{purpose}

{behavior}

## What do I need?

Home Assistant and these devices or features:

{requirements}

## What do I need to change?

1. Open the [YAML example](automation.yaml) and follow the [step-by-step guide](../../../how-to/{guide}).
2. Replace the placeholders with your devices, destinations and chosen settings. Values such as `example_…` or `REPLACE_…` are not a finished configuration.
3. Fill in missing triggers, conditions and formulas. Some of these details were removed during the original export. Changing device names alone is then not enough.
4. Check the finished automation in Home Assistant and first test its actions manually with a device that is safe to experiment with.
5. Then test a real start using the trigger you configured. This also checks the conditions and the complete routine.

Keep your login details and your finished personal configuration private.
"""


def _safe_root(root: Path) -> Path:
    root = Path(root).absolute()
    if root.is_symlink() or any(p.is_symlink() for p in root.parents):
        raise CatalogueError("Symlinked output paths are not supported.")
    return root


def _safe_file(path: Path) -> None:
    if path.is_symlink() or any(p.is_symlink() for p in path.parents):
        raise CatalogueError("Symlinked catalogue paths are not supported.")


def _write(path: Path, text: str) -> None:
    _safe_file(path)
    path.write_text(text, encoding="utf-8")


def _fingerprint(config: Any) -> str:
    from privacy_guard import SCHEMA_KEYS

    # Fingerprint public structure, not private text or custom dictionary keys.
    def shape(value: Any) -> Any:
        if isinstance(value, dict):
            pairs = [(str(key) if isinstance(key, str) and key in SCHEMA_KEYS else "custom_key", shape(child)) for key, child in value.items() if key not in {"alias", "description", "id"}]
            return sorted(pairs, key=lambda pair: json.dumps(pair, sort_keys=True))
        if isinstance(value, list):
            return [shape(child) for child in value]
        if isinstance(value, str):
            if value in ALLOWED_ACTIONS or re.fullmatch(r"(?:[a-z_]+\.)?example_[0-9]+|[A-Z_]+_[0-9]+|REPLACE_[A-Z_]+", value):
                return value
            return "text"
        return value
    return hashlib.sha256(json.dumps(shape(config), sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:8]


def _letters(number: int) -> str:
    result = ""
    while True:
        number, remainder = divmod(number, 26)
        result = chr(97 + remainder) + result
        if not number:
            return result
        number -= 1


def write_catalogue(root: Path, examples: list[dict[str, Any]]) -> list[Path]:
    """Write an empty staging catalogue from sanitized configs and trigger hints.

    examples = [{'config': mapping, 'trigger_types': ['state', ...]}, ...]
    The caller owns privacy sanitization and atomic promotion of this staging
    directory. Existing automations are never removed or overwritten here.
    """
    from privacy_guard import dump_yaml

    root = _safe_root(root)
    target = root / "automations"
    _safe_file(target)
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        raise CatalogueError("Catalogue output must be empty; use a staging directory.")
    planned: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for example in examples:
        if not isinstance(example, dict) or "config" not in example or set(example) - {"config", "trigger_types"}:
            raise CatalogueError("Invalid catalogue example input.")
        config = copy.deepcopy(example["config"])
        metadata = build_metadata(config, example.get("trigger_types"))
        planned.append((config, metadata))
    names = Counter((m["category"], m["slug"]) for _, m in planned)
    used: set[tuple[str, str]] = set()
    for config, metadata in planned:
        base_slug = metadata["slug"]
        if names[(metadata["category"], base_slug)] > 1:
            fingerprint = _fingerprint(config)
            metadata["variant"] = fingerprint
            metadata["slug"] = f"{base_slug}-{fingerprint}"
            duplicate = 0
            while (metadata["category"], metadata["slug"]) in used:
                if duplicate >= 702:
                    raise CatalogueError("Too many indistinguishable variants; review the input.")
                metadata["variant"] = f"{fingerprint}-{_letters(duplicate)}"
                metadata["slug"] = f"{base_slug}-{metadata['variant']}"
                duplicate += 1
        used.add((metadata["category"], metadata["slug"]))
        validate_metadata(metadata)
    target.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for config, metadata in planned:
        folder = target / metadata["category"] / metadata["slug"]
        _safe_file(folder)
        folder.mkdir(parents=True)
        config.pop("id", None)
        config["alias"] = render_alias(metadata)
        config["description"] = render_description(metadata)
        _write(folder / "automation.yaml", dump_yaml(config))
        _write(folder / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
        for language, vocabulary in LANGUAGES.items():
            _write(folder / vocabulary["readme"], render_example_readme(metadata, language=language, config=config))
        outputs.append(folder)
    for language, vocabulary in LANGUAGES.items():
        readme = root / vocabulary["readme"]
        _safe_file(readme)
        if not readme.exists():
            _write(readme, _new_root_readme(language))
    update_readme(root)
    return outputs


def load_entries(root: Path, allow_missing_translations: bool = False) -> list[tuple[Path, dict[str, Any]]]:
    from privacy_guard import load_yaml

    root = _safe_root(root)
    target = root / "automations"
    _safe_file(target)
    if not target.is_dir():
        raise CatalogueError("Automation catalogue is missing.")
    entries: list[tuple[Path, dict[str, Any]]] = []
    seen: set[str] = set()
    for category in sorted(target.iterdir()):
        _safe_file(category)
        if not category.is_dir() or category.name not in CATEGORIES:
            raise CatalogueError("Unexpected automation category or path.")
        for folder in sorted(category.iterdir()):
            _safe_file(folder)
            if not folder.is_dir():
                raise CatalogueError("Unexpected file in an automation category.")
            required = {"README.md", "README.de.md", "automation.yaml", "metadata.json"}
            children = list(folder.iterdir())
            present = {p.name for p in children}
            allowed = [required]
            if allow_missing_translations:
                allowed.append(required - {"README.de.md"})
            if present not in allowed:
                raise CatalogueError("Each example requires YAML, metadata and both language README files only.")
            for child in children:
                _safe_file(child)
                if not child.is_file():
                    raise CatalogueError("Unexpected directory inside an automation example.")
            try:
                metadata = validate_metadata(json.loads((folder / "metadata.json").read_text(encoding="utf-8")))
                config = load_yaml((folder / "automation.yaml").read_text(encoding="utf-8"))
            except (ValueError, TypeError, OSError, yaml.YAMLError) as exc:
                raise CatalogueError("An example has invalid YAML or metadata.") from None
            if folder.name != metadata["slug"] or category.name != metadata["category"]:
                raise CatalogueError("An example path does not follow its metadata name.")
            if not isinstance(config, dict) or config.get("alias") != render_alias(metadata) or config.get("description") != render_description(metadata):
                raise CatalogueError("An example alias or description does not match its metadata.")
            current = build_metadata(config, metadata["trigger_types"])
            if any(metadata[k] != current[k] for k in ("category", "actions", "features", "trigger_count", "action_count")):
                raise CatalogueError("An example's public behavior metadata is outdated.")
            if folder.name in seen:
                raise CatalogueError("Duplicate automation names are not allowed.")
            seen.add(folder.name)
            entries.append((folder, metadata))
    if not entries:
        raise CatalogueError("The catalogue must contain at least one example.")
    return entries


def _read_example_config(folder: Path) -> dict[str, Any]:
    from privacy_guard import load_yaml

    path = folder / "automation.yaml"
    _safe_file(path)
    try:
        config = load_yaml(path.read_text(encoding="utf-8"))
    except (ValueError, TypeError, OSError, yaml.YAMLError):
        raise CatalogueError("An example has invalid YAML.") from None
    if not isinstance(config, dict):
        raise CatalogueError("An example must contain an automation mapping.")
    return config


def _new_root_readme(language: str) -> str:
    _language(language)
    if language == "de":
        return ("# Alex' Home-Assistant-Automationen\n\n[English](README.md) · **Deutsch**\n\n"
                "Automationen aus meinem Home-Assistant-Setup, als Anregung für dein eigenes Zuhause. "
                "Wähle unten einen Bereich und öffne ein Beispiel. Dort steht, welche Geräte du brauchst "
                "und was du anpassen musst. Die geteilten Kopien sind anonymisiert, enthalten Platzhalter "
                "und sind noch nicht direkt einsatzbereit. Deine Zugangsdaten und persönliche Konfiguration "
                "bleiben bei dir.\n\n"
                f"{START}\n{END}\n")
    return ("# Alex's Home Assistant Automations\n\n**English** · [Deutsch](README.de.md)\n\n"
            "Automations from my Home Assistant setup, shared to inspire ideas for your own home. "
            "Choose a category below and open an example to see which devices you need and what "
            "to change. These shared copies are anonymized, contain placeholders and are not ready "
            "to use as they are. Keep your login details and personal configuration private.\n\n"
            f"{START}\n{END}\n")


def render_index(root: Path, entries: list[tuple[Path, dict[str, Any]]], language: str = "en", configs: dict[Path, dict[str, Any]] | None = None) -> str:
    from automation_details import summarize

    vocabulary = _language(language)
    def text(english: str, german: str) -> str:
        return german if language == "de" else english
    def count_label(count: int) -> str:
        return text("automation", "Automation") if count == 1 else text("automations", "Automationen")

    groups = _group_entries(entries)
    subgroup_count = sum(len(subgroups) for subgroups in groups.values())
    title = text("Shared automations", "Automationen im Überblick")
    intro = text(
        f"The shared automations are grouped into **{len(groups)} categories and {subgroup_count} subcategories** based on what they do.",
        f"Die geteilten Automationen sind in **{len(groups)} Bereiche und {subgroup_count} Unterbereiche** nach ihrer erkennbaren Funktion aufgeteilt.",
    )
    instructions = text(
        "Choose a category below and expand it. The links inside take you straight to the task you want. Then open an example to see what it does and how you could adapt it to your home.",
        "Wähle unten einen Bereich und klappe ihn auf. Die Sprunglinks darin führen direkt zum gewünschten Unterbereich. Öffne anschließend ein Beispiel: Dort steht, was es macht und wie du es an dein Zuhause anpassen kannst.",
    )
    variant_note = text(
        "Some routines have several variants. The letters help you tell them apart; they refer to different configurations, not particular rooms or devices.",
        "Manche Abläufe gibt es in mehreren Varianten. Die Buchstaben helfen beim Unterscheiden; sie stehen für unterschiedliche Konfigurationen, nicht für bestimmte Räume oder Geräte.",
    )
    lines = [START, "", '<a id="automation-catalogue"></a>', "", f"## {title} ({len(entries)} {count_label(len(entries))})", "", intro, "", instructions, "", variant_note, "", text("| Category | Automations | Subcategories |", "| Bereich | Automationen | Unterbereiche |"), "| --- | ---: | --- |"]
    variants = _visible_variants(entries, language)
    for category in CATEGORIES:
        subgroups = groups.get(category, {})
        if not subgroups:
            continue
        total = sum(len(items) for items in subgroups.values())
        labels = " · ".join(label for key, label in vocabulary["subcategories"][category].items() if key in subgroups)
        lines.append(f"| [{vocabulary['categories'][category]}](#{category}) | {total} | {labels} |")
    lines.append("")
    for category in CATEGORIES:
        subgroups = groups.get(category, {})
        if not subgroups:
            continue
        total = sum(len(items) for items in subgroups.values())
        lines += [f'<a id="{category}"></a>', "", "<details>", f"<summary><strong>{vocabulary['categories'][category]}</strong> · {total} {count_label(total)}</summary>", ""]
        jumps = " · ".join(f"[{label} ({len(subgroups[key])})](#{category}-{key})" for key, label in vocabulary["subcategories"][category].items() if key in subgroups)
        jump_label = text("Jump to", "Direkt zu")
        lines += [f"**{jump_label}:** {jumps}", ""]
        for key, label in vocabulary["subcategories"][category].items():
            subset = subgroups.get(key, [])
            if not subset:
                continue
            lines += [f'<a id="{category}-{key}"></a>', "", f"#### {label} ({len(subset)} {count_label(len(subset))})", "", text("| Automation | What happens? |", "| Automation | Was passiert? |"), "| --- | --- |"]
            for folder, metadata in subset:
                title = render_public_title(metadata, language)
                if metadata["slug"] in variants:
                    title += " — " + variants[metadata["slug"]]
                title = title.replace("|", "\\|")
                link = folder.relative_to(root).as_posix() + "/" + vocabulary["readme"]
                config = configs[folder] if configs is not None else _read_example_config(folder)
                summary = summarize(config, metadata, language).replace("|", "\\|").replace("\n", " ")
                lines.append(f"| [{title}]({link}) | {summary} |")
            lines.append("")
        lines += ["", "</details>", ""]
    lines += [END, ""]
    return "\n".join(lines)


def update_readme(root: Path, check: bool = False) -> bool:
    root = _safe_root(root)
    entries = load_entries(root, allow_missing_translations=not check)
    configs = {folder: _read_example_config(folder) for folder, _ in entries}
    pending: list[tuple[Path, str]] = []
    for language, vocabulary in LANGUAGES.items():
        readme = root / vocabulary["readme"]
        _safe_file(readme)
        try:
            original = readme.read_text(encoding="utf-8")
        except FileNotFoundError:
            if language == "en" or check:
                raise CatalogueError("Repository README is missing.") from None
            original = _new_root_readme(language)
        if original.count(START) != 1 or original.count(END) != 1 or original.index(START) > original.index(END):
            raise CatalogueError("README needs exactly one ordered catalogue marker pair.")
        start, end = original.index(START), original.index(END) + len(END)
        generated = original[:start] + render_index(root, entries, language, configs).rstrip() + original[end:]
        if generated != original or not readme.exists():
            pending.append((readme, generated))
        variants = _visible_variants(entries, language)
        for folder, metadata in entries:
            path = folder / vocabulary["readme"]
            expected = render_example_readme(metadata, variants.get(metadata["slug"], ""), language, configs[folder])
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                pending.append((path, expected))
    if not check:
        for path, content in pending:
            _write(path, content)
    return not pending


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        unchanged = update_readme(args.root, check=args.check)
    except (CatalogueError, OSError):
        print("Catalogue validation failed. Check the naming, metadata and required files locally.", file=sys.stderr)
        return 1
    if args.check and not unchanged:
        print("Generated documentation is outdated. Run python scripts/catalogue.py --write.", file=sys.stderr)
        return 1
    print("Catalogue names, metadata and generated documentation are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
