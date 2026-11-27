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


def subcategory(metadata: dict[str, Any]) -> tuple[str, str]:
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
    return key, SUBCATEGORIES_DE[category][key]


def _group_entries(entries: list[tuple[Path, dict[str, Any]]]) -> dict[str, dict[str, list[tuple[Path, dict[str, Any]]]]]:
    groups: dict[str, dict[str, list[tuple[Path, dict[str, Any]]]]] = {}
    for entry in entries:
        _, metadata = entry
        key, _ = subcategory(metadata)
        groups.setdefault(metadata["category"], {}).setdefault(key, []).append(entry)
    return groups


def _action_groups_de(actions: list[str]) -> list[str]:
    """Describe action capabilities without asserting order or missing causes."""
    groups: dict[str, set[str]] = {}
    for action in actions:
        domain, verb = action.split(".", 1)
        groups.setdefault(domain, set()).add(verb)
    labels: list[str] = []
    for domain, verbs in groups.items():
        label = ""
        if domain in {"light", "switch", "fan", "input_boolean", "homeassistant"} and {"turn_on", "turn_off"} <= verbs:
            both = {"light": "Licht ein- und ausschalten", "switch": "Schalter ein- und ausschalten", "fan": "Lüfter ein- und ausschalten", "input_boolean": "Gespeicherte Ein/Aus-Werte ändern", "homeassistant": "Geräte ein- und ausschalten"}
            label = both[domain]
            if domain == "fan" and verbs - {"turn_on", "turn_off"}:
                label = "Lüfter ein- und ausschalten sowie einstellen"
            elif "toggle" in verbs:
                label = {"light": "Licht schalten", "switch": "Schalter steuern", "fan": "Lüfter schalten", "input_boolean": "Gespeicherte Ein/Aus-Werte ändern", "homeassistant": "Geräte schalten"}[domain]
        elif domain == "light" and verbs == {"turn_on", "toggle"}:
            label = "Licht einschalten oder umschalten"
        elif domain == "climate" and len(verbs) > 1:
            label = "Heizung oder Klimaanlage einstellen"
        elif domain == "cover" and verbs == {"open_cover", "close_cover"}:
            label = "Eine Abdeckung öffnen und schließen"
        elif domain == "notify":
            label = "Nachrichten senden"
        elif domain == "todo" and {"get_items", "update_item"} == verbs:
            label = "Eine Aufgabenliste lesen und bearbeiten"
        elif domain == "todo" and {"get_items", "remove_item"} == verbs:
            label = "Eine Aufgabenliste lesen und Einträge entfernen"
        elif domain == "script" and verbs <= {"call", "turn_on"}:
            label = "Ein vorhandenes Skript ausführen"
        elif domain == "script" and len(verbs) > 1:
            label = "Eigene Skripte starten oder stoppen"
        elif domain == "media_player" and len(verbs) > 1:
            label = "Die Medienwiedergabe steuern"
        elif domain == "vacuum" and verbs == {"start", "set_fan_speed"}:
            label = "Einen Saugroboter starten und die Saugleistung einstellen"
        elif domain == "automation" and verbs == {"turn_on", "turn_off"}:
            label = "Andere Automationen aktivieren und deaktivieren"
        if label:
            labels.append(label)
        else:
            labels.extend(ACTION_LABELS_DE.get(f"{domain}.{verb}", "Eine weitere Aktion einrichten") for verb in sorted(verbs))
    return list(dict.fromkeys(labels))


def _qualifier_de(metadata: dict[str, Any]) -> str:
    features = metadata["features"]
    # A delay can belong to a secondary action. Never call the primary action
    # "delayed" merely because a delay exists somewhere in the configuration.
    if "wait" in features:
        return "mit Wartebedingung im Ablauf"
    if "delay" in features:
        return "mit Wartezeit im Ablauf"
    if "branches" in features:
        return "mit Bedingungen im Ablauf"
    return ""


def render_public_title(metadata: dict[str, Any]) -> str:
    """Beginner-facing German title; does not affect canonical YAML aliases."""
    validate_metadata(metadata)
    labels = _action_groups_de(_primary_actions(metadata))
    if len(labels) == 1:
        title = labels[0]
    else:
        combinations = {
            "climate": "Heizung oder Klimaanlage steuern",
            "lighting": "Licht und Szenen steuern",
            "ventilation": "Lüfter einstellen",
            "cleaning": "Einen Saugroboter steuern",
            "covers": "Eine Abdeckung steuern",
            "media": "Medien und Kameras steuern",
            "access": "Ein Schloss steuern",
            "tasks": "Eine Aufgabenliste bearbeiten",
            "switches": "Schalter steuern",
            "voice": "Durchsagen und Sprachausgabe nutzen",
            "notifications": "Nachrichten und Hinweise ausgeben",
            "helpers": "Gespeicherte Werte ändern",
            "system": "Mehrere Funktionen verbinden",
        }
        title = combinations[metadata["category"]]
    if title == "Eine noch offene Aktion ergänzen":
        title = "Eigene Aktion einrichten"
    qualifier = _qualifier_de(metadata)
    return title + (f" · {qualifier}" if qualifier else "")


def _visible_variants(entries: list[tuple[Path, dict[str, Any]]]) -> dict[str, str]:
    groups: dict[tuple[str, str, str, tuple[str, ...]], list[dict[str, Any]]] = {}
    for _, metadata in entries:
        key = (metadata["category"], subcategory(metadata)[0], render_public_title(metadata), tuple(metadata["trigger_types"]))
        groups.setdefault(key, []).append(metadata)
    return {metadata["slug"]: f"Variante {_letters(number).upper()}"
            for group in groups.values() if len(group) > 1
            for number, metadata in enumerate(sorted(group, key=lambda item: item["slug"]))}


def render_example_readme(metadata: dict[str, Any], variant_label: str = "") -> str:
    title = render_public_title(metadata) + (f" — {variant_label}" if variant_label else "")
    category = metadata["category"]
    subcategory_key, subcategory_label = subcategory(metadata)
    breadcrumb = f"[{CATEGORIES_DE[category]}](../../../README.md#{category}) → [{subcategory_label}](../../../README.md#{category}-{subcategory_key})"
    actions = _action_groups_de(metadata["actions"])
    purpose = actions[0] + "." if len(actions) == 1 else "Die Vorlage verbindet folgende Funktionen:\n\n" + "\n".join(f"- {label}." for label in actions)
    if "generic.action" in metadata["actions"]:
        purpose += "\n\nDie konkrete Aktion ist im Export nicht mehr vollständig erkennbar. Du musst die fehlenden Schritte selbst ergänzen."
    triggers = "\n".join(f"- {TRIGGERS_DE[kind]}." for kind in metadata["trigger_types"])
    domains = sorted({action.split(".", 1)[0] for action in metadata["actions"]})
    requirement_items = [REQUIREMENTS_DE.get(domain, "Die passende Gerätefunktion in Home Assistant.") for domain in domains]
    requirement_items += [TRIGGER_REQUIREMENTS_DE[kind] for kind in metadata["trigger_types"] if kind in TRIGGER_REQUIREMENTS_DE]
    requirements = "\n".join(f"- {item}" for item in dict.fromkeys(requirement_items))
    return f"""# {title}

{breadcrumb}

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

{purpose}

## Wann startet sie?

{triggers}

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

{requirements}

## Was muss ich anpassen?

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
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
        _write(folder / "README.md", render_example_readme(metadata))
        outputs.append(folder)
    readme = root / "README.md"
    _safe_file(readme)
    if not readme.exists():
        _write(readme, "# Automationen für Home Assistant\n\n"
               "Vorlagen zum Anpassen an dein Zuhause. Wähle unten einen Bereich und öffne "
               "eine Vorlage. Dort steht, welche Geräte du brauchst und was du einrichten musst. "
               "Die Beispiele enthalten Platzhalter und sind noch nicht direkt einsatzbereit. "
               "Deine Zugangsdaten und persönliche Konfiguration bleiben bei dir.\n\n"
               f"{START}\n{END}\n")
    update_readme(root)
    return outputs


def load_entries(root: Path) -> list[tuple[Path, dict[str, Any]]]:
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
            required = {"README.md", "automation.yaml", "metadata.json"}
            children = list(folder.iterdir())
            if {p.name for p in children} != required:
                raise CatalogueError("Each example requires YAML, metadata and README files only.")
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


def render_index(root: Path, entries: list[tuple[Path, dict[str, Any]]]) -> str:
    count_label = "Vorlage" if len(entries) == 1 else "Vorlagen"
    groups = _group_entries(entries)
    subgroup_count = sum(len(subgroups) for subgroups in groups.values())
    lines = [START, "", '<a id="automation-catalogue"></a>', "", f"## Automationen im Überblick ({len(entries)} {count_label})", "", f"Die Vorlagen sind in **{len(groups)} Bereiche und {subgroup_count} Unterbereiche** nach ihrer erkennbaren Funktion aufgeteilt.", "", "Wähle unten einen Bereich und klappe ihn auf. Die Sprunglinks darin führen direkt zum gewünschten Unterbereich. Öffne anschließend eine Vorlage: Dort steht, was du brauchst und was du anpassen musst.", "", "Manche Abläufe gibt es in mehreren Varianten. Die Buchstaben helfen beim Unterscheiden; sie stehen für unterschiedliche Konfigurationen, nicht für bestimmte Räume oder Geräte.", "", "| Bereich | Vorlagen | Unterbereiche |", "| --- | ---: | --- |"]
    variants = _visible_variants(entries)
    for category in CATEGORIES:
        subgroups = groups.get(category, {})
        if not subgroups:
            continue
        total = sum(len(items) for items in subgroups.values())
        labels = " · ".join(label for key, label in SUBCATEGORIES_DE[category].items() if key in subgroups)
        lines.append(f"| [{CATEGORIES_DE[category]}](#{category}) | {total} | {labels} |")
    lines.append("")
    for category in CATEGORIES:
        subgroups = groups.get(category, {})
        if not subgroups:
            continue
        total = sum(len(items) for items in subgroups.values())
        item_label = "Vorlage" if total == 1 else "Vorlagen"
        lines += [f'<a id="{category}"></a>', "", "<details>", f"<summary><strong>{CATEGORIES_DE[category]}</strong> · {total} {item_label}</summary>", ""]
        jumps = " · ".join(f"[{label} ({len(subgroups[key])})](#{category}-{key})" for key, label in SUBCATEGORIES_DE[category].items() if key in subgroups)
        lines += [f"**Direkt zu:** {jumps}", ""]
        for key, label in SUBCATEGORIES_DE[category].items():
            subset = subgroups.get(key, [])
            if not subset:
                continue
            label_count = "Vorlage" if len(subset) == 1 else "Vorlagen"
            lines += [f'<a id="{category}-{key}"></a>', "", f"#### {label} ({len(subset)} {label_count})", "", "| Vorlage | Wann startet sie? |", "| --- | --- |"]
            for folder, metadata in subset:
                title = render_public_title(metadata)
                if metadata["slug"] in variants:
                    title += " — " + variants[metadata["slug"]]
                title = title.replace("|", "\\|")
                link = folder.relative_to(root).as_posix() + "/README.md"
                triggers = "; ".join(TRIGGERS_DE[kind] for kind in metadata["trigger_types"])
                lines.append(f"| [{title}]({link}) | {triggers} |")
            lines.append("")
        lines += ["", "</details>", ""]
    lines += [END, ""]
    return "\n".join(lines)


def update_readme(root: Path, check: bool = False) -> bool:
    root = _safe_root(root)
    entries = load_entries(root)
    readme = root / "README.md"
    _safe_file(readme)
    try:
        original = readme.read_text(encoding="utf-8")
    except OSError:
        raise CatalogueError("Repository README is missing.") from None
    if original.count(START) != 1 or original.count(END) != 1 or original.index(START) > original.index(END):
        raise CatalogueError("README needs exactly one ordered catalogue marker pair.")
    start, end = original.index(START), original.index(END) + len(END)
    generated = original[:start] + render_index(root, entries).rstrip() + original[end:]
    pending: list[tuple[Path, str]] = []
    if generated != original:
        pending.append((readme, generated))
    variants = _visible_variants(entries)
    for folder, metadata in entries:
        path = folder / "README.md"
        expected = render_example_readme(metadata, variants.get(metadata["slug"], ""))
        if path.read_text(encoding="utf-8") != expected:
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
