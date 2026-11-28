"""Describe the surviving, ordered logic in public Home Assistant examples.

Only reviewed vocabulary, known setting types and safe reference identifiers enter
Markdown. Original aliases, service suffixes, formulas and arbitrary prose are
never assumed to describe the automation's purpose.
"""
from __future__ import annotations

import math
import re
from typing import Any

import privacy_guard
from privacy_guard import DOMAINS, ENUMS

LANGUAGES = {"en", "de"}
_REFERENCE = re.compile(r"^(?:[a-z][a-z0-9_]*\.example_\d{2,5}|(?:DEVICE|AREA|FLOOR|LABEL|ENTITY|ID|TAG|ENTRY)_\d{2,5})$")
_TIME = re.compile(r"^(?:[01]?\d|2[0-3]):[0-5]\d(?::[0-5]\d(?:\.\d{1,3})?)?$")
_DURATION = re.compile(r"^\d{1,4}:[0-5]\d(?::[0-5]\d(?:\.\d{1,3})?)?$")
_PATTERN = re.compile(r"^(?:\*|/[1-9]\d?|[0-5]?\d)$")
_MAX_DEPTH = 20


def _t(language: str, en: str, de: str) -> str:
    return de if language == "de" else en


def _missing(language: str) -> str:
    return _t(language, "not available", "nicht erhalten")


def _items(value: Any) -> list[Any]:
    return value if isinstance(value, list) else [] if value is None else [value]


def _number(value: Any) -> str | None:
    if type(value) is str and re.fullmatch(r"-?\d{1,6}(?:\.\d{1,6})?", value):
        return value
    if type(value) not in (int, float) or abs(value) > 10**12 or not math.isfinite(value):
        return None
    return str(value) if type(value) is int else format(value, ".12g")


def _reference(value: Any) -> str | None:
    if type(value) is not str:
        return None
    public_entity = getattr(privacy_guard, "is_public_entity", None)
    if callable(public_entity) and public_entity(value):
        return "`" + value + "`"
    if not _REFERENCE.fullmatch(value):
        return None
    if "." in value and value.split(".", 1)[0] not in DOMAINS:
        return None
    return "`" + value + "`"


def _public_text(value: Any) -> str | None:
    validator = getattr(privacy_guard, "is_public_text", None)
    if type(value) is not str or not callable(validator) or not validator(value):
        return None
    if privacy_guard.PLACEHOLDER.fullmatch(value):
        return None
    # Keep text readable while preventing it from creating links, tables, HTML
    # or formatting in the generated document.
    text = " ".join(value.split()).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"([\\`*_{}\[\]()#!|~])", r"\\\1", text)
    return "“" + text + "”"


def _formula(value: Any) -> str | None:
    if type(value) is not str or not ("{{" in value or "{%" in value or value.lower() in {"true", "false"}):
        return None
    return _public_text(value)


def _references(value: Any, language: str) -> str:
    return ", ".join(_reference(item) or _missing(language) for item in _items(value)) or _missing(language)


def _enum(value: Any, key: str, language: str) -> str:
    if isinstance(value, list):
        return ", ".join(_enum(item, key, language) for item in value) or _missing(language)
    if value is None:
        return _t(language, "unspecified (null)", "ohne Wert (null)")
    if type(value) is str and value in ENUMS.get(key, ()):
        return "`" + value + "`"
    return _missing(language)


def _duration(value: Any, language: str) -> str:
    number = _number(value)
    if number is not None:
        return f"{number} s"
    if type(value) is str and _DURATION.fullmatch(value):
        return value + _t(language, " (time format)", " (Zeitformat)")
    if isinstance(value, dict):
        units = {"days": _t(language, "days", "Tage"), "hours": "h", "minutes": "min", "seconds": "s", "milliseconds": "ms"}
        parts = []
        for key, unit in units.items():
            if key in value:
                number = _number(value[key])
                if number is None:
                    parts.append(f"{unit}: {_missing(language)}")
                elif value[key] != 0:
                    parts.append(f"{number} {unit}")
        if parts:
            return " ".join(parts)
        if any(key in value for key in units):
            return "0 s"
    return _missing(language)


def _time(value: Any, language: str) -> str:
    if isinstance(value, list):
        return ", ".join(_time(item, language) for item in value)
    if type(value) is str and _TIME.fullmatch(value):
        return value
    return _reference(value) or _missing(language)


def _target(node: dict, language: str) -> str:
    mappings = [node]
    for key in ("target", "data", "data_template"):
        if isinstance(node.get(key), dict):
            mappings.append(node[key])
    found = []
    for mapping in mappings:
        for key in ("entity_id", "device_id", "area_id", "floor_id", "label_id", "media_player_entity_id"):
            if key in mapping:
                value = _references(mapping[key], language)
                if value not in found:
                    found.append(value)
    return ", ".join(found)


def _rule_settings(node: dict, language: str, compact: bool = False) -> list[str]:
    """Retained settings do not imply a missing trigger/condition type."""
    parts = []
    if not compact:
        target = _target(node, language)
        if target:
            parts.append(target)
    for key, en, de in (("above", "above", "über"), ("below", "below", "unter")):
        if key in node:
            value = _number(node[key]) or _reference(node[key]) or _missing(language)
            parts.append(f"{_t(language, en, de)} {value}")
    for key, en, de in (("from", "from state", "von Zustand"), ("to", "to state", "zu Zustand"), ("state", "state", "Zustand"), ("not_from", "excluded previous state", "ausgeschlossener vorheriger Zustand"), ("not_to", "excluded new state", "ausgeschlossener neuer Zustand")):
        if key in node:
            parts.append(f"{_t(language, en, de)}: {_enum(node[key], 'state', language)}")
    if "for" in node:
        parts.append(_t(language, "held for", "Dauer") + " " + _duration(node["for"], language))
    for key, en, de in (("at", "at", "um"), ("before", "before", "vor"), ("after", "after", "nach")):
        if key in node:
            value = _enum(node[key], "event", language) if node[key] in ("sunrise", "sunset") else _time(node[key], language)
            parts.append(_t(language, en, de) + " " + value)
    for key, en, de in (("hours", "hours", "Stunden"), ("minutes", "minutes", "Minuten"), ("seconds", "seconds", "Sekunden")):
        if key in node:
            value = node[key]
            rendered = str(value) if type(value) is int and 0 <= value <= 59 else value if type(value) is str and _PATTERN.fullmatch(value) else _missing(language)
            parts.append(f"{_t(language, en, de)}: {rendered}")
    if "weekday" in node:
        parts.append(_t(language, "weekdays", "Wochentage") + ": " + _enum(node["weekday"], "weekday", language))
    for key, en, de in (("before_offset", "before offset", "Versatz davor"), ("after_offset", "after offset", "Versatz danach"), ("offset", "offset", "Versatz")):
        if key in node:
            parts.append(_t(language, en, de) + ": " + _duration(node[key], language))
    for key, en, de in (("event", "event", "Ereignis"), ("type", "device event/action", "Geräteereignis/-aktion")):
        if key in node and not compact:
            parts.append(_t(language, en, de) + ": " + _enum(node[key], key, language))
    for key, en, de in (("attribute", "attribute name", "Attributname"), ("value_template", "formula", "Formel"), ("event_type", "event name", "Ereignisname"), ("topic", "MQTT topic", "MQTT-Thema"), ("payload", "MQTT content", "MQTT-Inhalt")):
        if key in node and not compact:
            formula = _formula(node[key]) if key == "value_template" else None
            parts.append(_t(language, en, de) + ": " + (formula or _missing(language)))
    if "id" in node and not compact:
        parts.append(_t(language, "trigger reference", "Auslöser-Verweis") + ": " + _references(node["id"], language))
    return parts


_TRIGGER_LABELS = {
    "state": ("State change", "Zustandsänderung"), "numeric_state": ("Numeric threshold crossing", "Überschreiten oder Unterschreiten eines Zahlenwerts"),
    "time": ("Scheduled time", "Feste Uhrzeit"), "time_pattern": ("Repeating schedule", "Wiederholter Zeitplan"),
    "sun": ("Sun event", "Sonnenereignis"), "event": ("Event", "Ereignis"), "template": ("Formula becomes true", "Formel wird wahr"),
    "device": ("Device event", "Geräteereignis"), "mqtt": ("MQTT message", "MQTT-Nachricht"), "tag": ("Tag scan", "Tag wird gescannt"),
    "homeassistant": ("Home Assistant event", "Home-Assistant-Ereignis"), "calendar": ("Calendar event", "Kalenderereignis"),
    "zone": ("Zone event", "Zonenereignis"), "webhook": ("Webhook call", "Webhook-Aufruf"), "conversation": ("Voice command", "Sprachbefehl"),
}


def _trigger(node: Any, language: str, compact: bool = False) -> str:
    if not isinstance(node, dict):
        return _t(language, "Trigger definition not available", "Auslöser-Definition nicht erhalten")
    kind = node.get("trigger", node.get("platform"))
    labels = _TRIGGER_LABELS.get(kind) if type(kind) is str else None
    label = _t(language, *labels) if labels else _t(language, "Trigger type missing", "Auslösertyp nicht erhalten")
    parts = _rule_settings(node, language, compact)
    result = label + (": " + "; ".join(parts) if parts else "")
    if node.get("enabled") is False:
        result = _t(language, "Disabled — ", "Deaktiviert — ") + result
    return result


def _condition(node: Any, language: str, depth: int = 0) -> str:
    if depth > _MAX_DEPTH:
        return _t(language, "Further nested conditions; inspect YAML", "Weitere verschachtelte Bedingungen; YAML prüfen")
    if isinstance(node, list):
        if not node:
            return _t(language, "no conditions", "keine Bedingungen")
        return _t(language, "all of", "alle folgenden") + ": " + "; ".join(_condition(item, language, depth + 1) for item in node)
    if not isinstance(node, dict):
        formula = _formula(node)
        return _t(language, "formula: ", "Formel: ") + formula if formula else _t(language, "condition formula not available", "Bedingungsformel nicht erhalten")
    if node.get("enabled") is False:
        active = {key: value for key, value in node.items() if key != "enabled"}
        return _t(language, "disabled check (ignored): ", "deaktivierte Prüfung (übersprungen): ") + _condition(active, language, depth + 1)
    kind = node.get("condition")
    operators = {"and": ("all of", "alle folgenden"), "or": ("at least one of", "mindestens eine der folgenden"), "not": ("none of", "keine der folgenden")}
    labels = {"state": ("state check", "Zustandsprüfung"), "numeric_state": ("number check", "Zahlenprüfung"), "template": ("formula check", "Formelprüfung"), "time": ("time check", "Zeitprüfung"), "sun": ("sun check", "Sonnenprüfung"), "zone": ("zone check", "Zonenprüfung"), "trigger": ("trigger-reference check", "Auslöser-Verweis prüfen"), "device": ("device check", "Geräteprüfung")}
    if type(kind) is str and kind in operators:
        children = _items(node.get("conditions"))
        return _t(language, *operators[kind]) + " [" + "; ".join(_condition(item, language, depth + 1) for item in children) + "]"
    label = _t(language, *labels[kind]) if type(kind) is str and kind in labels else _t(language, "condition type missing", "Bedingungstyp nicht erhalten")
    settings = _rule_settings(node, language)
    if "conditions" in node:
        settings.append(_t(language, "nested tests; connecting rule missing", "verschachtelte Prüfungen; Verknüpfung nicht erhalten") + " [" + "; ".join(_condition(item, language, depth + 1) for item in _items(node["conditions"])) + "]")
    return label + (": " + "; ".join(settings) if settings else "")


_NUMERIC_SETTINGS = {
    "brightness_pct": ("brightness", "Helligkeit", "%"), "brightness": ("brightness level", "Helligkeitswert", "/255"),
    "brightness_step_pct": ("brightness change", "Helligkeitsänderung", "%"), "brightness_step": ("brightness change", "Helligkeitsänderung", ""),
    "transition": ("transition", "Übergang", " s"), "color_temp_kelvin": ("colour temperature", "Farbtemperatur", " K"),
    "color_temp": ("colour temperature", "Farbtemperatur", " mired"), "temperature": ("temperature setting (unit not given)", "Temperaturwert (Einheit nicht angegeben)", ""),
    "target_temp_high": ("upper temperature setting", "oberer Temperaturwert", ""), "target_temp_low": ("lower temperature setting", "unterer Temperaturwert", ""),
    "percentage": ("fan speed", "Lüftergeschwindigkeit", "%"), "humidity": ("humidity", "Luftfeuchtigkeit", "%"),
    "position": ("position", "Position", "%"), "tilt_position": ("tilt position", "Lamellenposition", "%"),
    "volume_level": ("volume (0–1)", "Lautstärke (0–1)", ""), "clean_times": ("cleaning passes", "Reinigungsdurchgänge", ""),
    "qos": ("MQTT quality level", "MQTT-Qualitätsstufe", ""), "ttl": ("message lifetime", "Nachrichtenlebensdauer", " s"),
}
_TEXT_SETTINGS = {
    "temperature": ("temperature setting", "Temperaturwert"), "preset_mode": ("preset", "Profil"), "fan_speed": ("suction/speed setting", "Saug-/Geschwindigkeitsstufe"),
    "value": ("stored value", "gespeicherter Wert"), "option": ("selected option", "gewählte Option"), "message": ("message text", "Nachrichtentext"),
    "title": ("message title", "Nachrichtentitel"), "text": ("text", "Text"), "topic": ("MQTT topic", "MQTT-Thema"),
    "payload": ("MQTT content", "MQTT-Inhalt"), "media_content_id": ("media source", "Medienquelle"), "filename": ("file destination", "Dateiziel"),
    "item": ("task item", "Aufgabeneintrag"), "uid": ("task reference", "Aufgaben-Verweis"), "segments": ("cleaning area identifiers", "Reinigungsbereich-IDs"),
    "timestamp": ("stored time", "gespeicherte Zeit"), "language": ("speech language", "Sprache der Ausgabe"),
}


def _data_parts(node: dict, language: str, compact: bool = False) -> list[str]:
    data = node.get("data", node.get("data_template", {}))
    if not isinstance(data, dict):
        return [_t(language, "action settings not available", "Aktionswerte nicht erhalten")]
    parts = []
    for key, (en, de, suffix) in _NUMERIC_SETTINGS.items():
        if key in data:
            number = _number(data[key])
            if compact and number is None:
                continue
            parts.append(_t(language, en, de) + ": " + (number + suffix if number is not None else _missing(language)))
    for key in ("hvac_mode", "status", "media_content_type", "enqueue", "flash", "level", "format"):
        if key in data:
            labels = {"hvac_mode": ("heating/cooling mode", "Heiz-/Kühlmodus"), "status": ("task status", "Aufgabenstatus"), "media_content_type": ("media type", "Medientyp"), "enqueue": ("playback queue", "Wiedergabewarteschlange"), "flash": ("flashing", "Blinken"), "level": ("log level", "Protokollstufe"), "format": ("stream format", "Stream-Format")}
            if compact and _enum(data[key], key, language) == _missing(language):
                continue
            parts.append(_t(language, *labels[key]) + ": " + _enum(data[key], key, language))
    for key, labels in _TEXT_SETTINGS.items():
        if key in data and key not in _NUMERIC_SETTINGS and (not compact or key in {"message", "title", "text", "preset_mode", "fan_speed", "option"}):
            number = _number(data[key]) if key == "value" and node.get("action", node.get("service")) in ("input_number.set_value", "number.set_value", "counter.set_value") else None
            public_text = _public_text(data[key])
            if compact and not public_text:
                continue
            if compact and public_text and len(public_text) > 120:
                public_text = public_text[:116] + "…“"
            parts.append(_t(language, *labels) + ": " + (number or public_text or _missing(language)))
    for key in ("rgb_color", "rgbw_color", "rgbww_color", "hs_color", "xy_color"):
        if key in data:
            values = data[key]
            numbers = [_number(value) for value in values] if isinstance(values, list) and len(values) <= 5 else []
            rendered = ", ".join(numbers) if numbers and all(number is not None for number in numbers) else _missing(language)
            parts.append(_t(language, "colour values", "Farbwerte") + ": " + rendered)
    for key, en, de in (("retain", "retain MQTT message", "MQTT-Nachricht speichern"), ("preannounce", "announcement tone", "Ankündigungston"), ("stop_actions", "stop affected running actions", "laufende betroffene Aktionen stoppen"), ("skip_condition", "skip the other automation's conditions", "Bedingungen der anderen Automation überspringen"), ("is_volume_muted", "muted", "stumm"), ("dry_run", "simulation only", "nur Simulation")):
        if key in data and not compact:
            value = _t(language, "yes", "ja") if data[key] is True else _t(language, "no", "nein") if data[key] is False else _missing(language)
            parts.append(_t(language, en, de) + ": " + value)
    if "answers" in data and not compact:
        parts.append(_t(language, "answer choices", "Antwortmöglichkeiten") + ": " + str(len(_items(data["answers"]))) + _t(language, "; answer phrases not available", "; Antworttexte nicht erhalten"))
    if "media" in data and not compact:
        parts.append(_t(language, "media selection not available", "Medienauswahl nicht erhalten"))
    return parts


def _service_text(node: dict, language: str, compact: bool = False) -> str:
    from catalogue import ACTION_LABELS_DE, ACTION_LABELS_EN
    labels = ACTION_LABELS_DE if language == "de" else ACTION_LABELS_EN
    service = node.get("action", node.get("service"))
    concept = service if type(service) is str and service in labels else None
    if concept is None and type(service) is str and "." in service:
        domain = service.split(".", 1)[0]
        if domain in {"script", "notify", "rest_command"}:
            concept = domain + ".call"
    if concept:
        result = labels[concept]
    elif "type" in node and type(node["type"]) is str and node["type"] in ENUMS["type"]:
        result = _t(language, "Device action", "Geräteaktion") + ": " + _enum(node["type"], "type", language)
    else:
        result = _t(language, "Action type not available", "Aktionstyp nicht erhalten")
    target = _target(node, language)
    if not compact and target:
        result += " — " + target
    direct_reference = _reference(service) if concept and concept.endswith(".call") else None
    if direct_reference and not compact:
        result += " — " + direct_reference
    parts = _data_parts(node, language, compact)
    if parts:
        result += "; " + "; ".join(parts)
    if node.get("continue_on_error") is True and not compact:
        result += _t(language, "; configured to continue after supported action errors", "; Fortsetzung nach unterstützten Aktionsfehlern eingestellt")
    if "response_variable" in node and not compact:
        result += _t(language, "; save the returned result for later steps", "; Rückgabe für spätere Schritte speichern")
    return result


def _timeout(node: dict, language: str) -> str:
    if "timeout" not in node:
        return _t(language, "No timeout is configured.", "Keine Zeitgrenze eingestellt.")
    duration = _duration(node["timeout"], language)
    if node.get("continue_on_timeout") is False:
        continuation = _t(language, "Stop this sequence when the timeout expires.", "Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.")
    elif node.get("continue_on_timeout", True) is True:
        continuation = _t(language, "Continue with the next step when the timeout expires.", "Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.")
    else:
        continuation = _t(language, "The timeout continuation setting is not available.", "Die Einstellung zur Fortsetzung nach Ablauf ist nicht erhalten.")
    return _t(language, "Time limit: ", "Zeitgrenze: ") + duration + ". " + continuation


def _step_lines(node: Any, language: str, depth: int = 0) -> list[str]:
    if depth > _MAX_DEPTH:
        return [_t(language, "Further nested steps; inspect YAML.", "Weitere verschachtelte Schritte; YAML prüfen.")]
    if not isinstance(node, dict):
        return [_t(language, "Step definition not available.", "Schritt-Definition nicht erhalten.")]
    lines = []
    if "if" in node:
        lines = [_t(language, "If ", "Wenn ") + _condition(node["if"], language) + ":", "", _t(language, "**Then:**", "**Dann:**"), ""]
        lines += [line for line in _sequence(node.get("then"), language, depth + 1)]
        if "else" in node:
            lines += ["", _t(language, "**Otherwise:**", "**Sonst:**"), ""]
            lines += [line for line in _sequence(node["else"], language, depth + 1)]
    elif "choose" in node:
        lines = [_t(language, "Use the first matching branch; later branches in this choice are skipped.", "Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.")]
        for index, branch in enumerate(_items(node["choose"]), 1):
            branch = branch if isinstance(branch, dict) else {}
            lines += ["", _t(language, f"**Branch {index}:** ", f"**Zweig {index}:** ") + _condition(branch.get("conditions"), language), ""]
            lines += [line for line in _sequence(branch.get("sequence"), language, depth + 1)]
        if "default" in node:
            lines += ["", _t(language, "**If no branch matches:**", "**Wenn kein Zweig passt:**"), ""]
            lines += [line for line in _sequence(node["default"], language, depth + 1)]
        else:
            lines += ["", _t(language, "No default branch is configured.", "Kein Standardzweig eingestellt.")]
    elif "parallel" in node:
        lines = [_t(language, "Start these paths in parallel. Their execution order is not guaranteed.", "Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.")]
        for index, branch in enumerate(_items(node["parallel"]), 1):
            sequence = branch.get("sequence", [branch]) if isinstance(branch, dict) else branch
            lines += ["", _t(language, f"**Parallel path {index}:**", f"**Paralleler Pfad {index}:**"), ""]
            lines += [line for line in _sequence(sequence, language, depth + 1)]
    elif "repeat" in node:
        repeat = node["repeat"] if isinstance(node["repeat"], dict) else {}
        if "count" in repeat:
            title = _t(language, "Repeat count: ", "Anzahl Wiederholungen: ") + (_number(repeat["count"]) or _missing(language))
        elif "for_each" in repeat:
            count = str(len(repeat["for_each"])) if isinstance(repeat["for_each"], list) else _missing(language)
            title = _t(language, "Repeat for each list item; item count: ", "Für jeden Listeneintrag wiederholen; Anzahl Einträge: ") + count
        elif "while" in repeat:
            title = _t(language, "Check before each pass; repeat while ", "Vor jedem Durchlauf prüfen; wiederholen, solange ") + _condition(repeat["while"], language)
        elif "until" in repeat:
            title = _t(language, "Run at least once, then repeat until ", "Mindestens einmal ausführen, danach wiederholen, bis ") + _condition(repeat["until"], language)
        else:
            title = _t(language, "Repeat rule not available", "Wiederholungsregel nicht erhalten")
        lines = [title + ".", ""] + [line for line in _sequence(repeat.get("sequence"), language, depth + 1)]
    elif "wait_for_trigger" in node:
        lines = [_t(language, "Wait for one of these triggers:", "Auf einen dieser Auslöser warten:")]
        lines += ["", *["- " + _trigger(trigger, language) for trigger in _items(node["wait_for_trigger"])], "", _timeout(node, language)]
    elif "wait_template" in node:
        formula = _formula(node["wait_template"])
        label = _t(language, "Wait until this formula is true: ", "Warten, bis diese Formel wahr ist: ") + formula + "." if formula else _t(language, "Wait until a formula is true; the formula is not available.", "Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.")
        lines = [label, "", _timeout(node, language)]
    elif "delay" in node:
        lines = [_t(language, "Pause for ", "Warten für ") + _duration(node["delay"], language) + "."]
    elif "condition" in node:
        lines = [_t(language, "Check ", "Prüfen: ") + _condition(node, language) + _t(language, ". If false, stop the current sequence here.", ". Falls falsch, den aktuellen Ablauf hier stoppen.")]
    elif "variables" in node:
        values = node["variables"]
        count = len(values) if isinstance(values, dict) else None
        lines = [_t(language, f"Prepare {count} intermediate values; their contents/formulas are not described.", f"{count} Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.") if count is not None else _t(language, "Intermediate values not available.", "Zwischenwerte nicht erhalten.")]
    elif "stop" in node:
        lines = [_t(language, "Stop this run", "Diesen Durchlauf stoppen") + (_t(language, " with an error", " mit einem Fehler") if node.get("error") is True else "") + "."]
    elif "sequence" in node:
        lines = [_t(language, "Run these steps in order:", "Diese Schritte nacheinander ausführen:"), ""] + [line for line in _sequence(node["sequence"], language, depth + 1)]
    else:
        lines = [_service_text(node, language) + "."]
    if node.get("enabled") is False:
        lines[0] = _t(language, "**Disabled step:** ", "**Deaktivierter Schritt:** ") + lines[0]
    return lines


def _sequence(value: Any, language: str, depth: int = 0) -> list[str]:
    nodes = _items(value)
    if not nodes:
        return [_t(language, "No steps configured.", "Keine Schritte eingestellt.")]
    lines = []
    for index, node in enumerate(nodes, 1):
        step = _step_lines(node, language, depth)
        if lines:
            lines.append("")
        lines.append(f"{index}. " + step[0])
        lines.extend(" " * len(f"{index}. ") + line if line.strip() else "" for line in step[1:])
    return lines


def _mode(config: dict, language: str) -> str:
    mode = config.get("mode", "single")
    descriptions = {
        "single": ("If it triggers again while running, the new run is not started.", "Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf."),
        "restart": ("A new trigger stops the current run and starts it again, provided the automation's conditions pass.", "Ein neuer Auslöser stoppt den laufenden Durchlauf und startet neu, sofern die Bedingungen der Automation erfüllt sind."),
        "queued": ("New runs wait in a queue and run in arrival order. They join the queue only if the automation's conditions pass at trigger time.", "Neue Durchläufe warten in einer Warteschlange und laufen in Eingangsreihenfolge. Sie werden nur eingereiht, wenn die Bedingungen beim Auslösen erfüllt sind."),
        "parallel": ("Each new trigger can start an independent run alongside existing runs.", "Jeder neue Auslöser kann einen eigenen Durchlauf neben bereits laufenden Durchläufen starten."),
    }
    if type(mode) is not str or mode not in descriptions:
        return _t(language, "Run mode not available.", "Ausführungsmodus nicht erhalten.")
    text = "`" + mode + "`: " + _t(language, *descriptions[mode])
    if mode in {"queued", "parallel"}:
        maximum = _number(config.get("max", 10)) or _missing(language)
        text += _t(language, " Limit for running and queued runs: ", " Grenze für laufende und wartende Durchläufe: ") + maximum + "."
    if config.get("initial_state") is False:
        text += _t(language, " The automation is initially disabled.", " Die Automation ist anfangs deaktiviert.")
    return text


def render_details(config: dict, language: str = "en") -> str:
    """Return bilingual Markdown grounded in the retained configuration."""
    if language not in LANGUAGES or not isinstance(config, dict):
        raise ValueError("Unsupported language or automation configuration")
    triggers = _items(config.get("triggers", config.get("trigger")))
    lines = ["## " + _t(language, "What starts it?", "Wann startet sie?"), ""]
    if triggers:
        if len(triggers) > 1:
            lines += [_t(language, "Any enabled trigger below can start a run.", "Jeder aktivierte Auslöser unten kann einen Durchlauf starten."), ""]
        lines += [f"- **{index}.** " + _trigger(trigger, language) for index, trigger in enumerate(triggers, 1)]
    else:
        lines += [_t(language, "No trigger definition is included in this file.", "Diese Datei enthält keine Auslöser-Definition.")]
    lines += ["", "## " + _t(language, "What must be true first?", "Was muss vorher erfüllt sein?"), ""]
    conditions = config.get("conditions", config.get("condition", []))
    if not conditions:
        lines += [_t(language, "No top-level conditions are configured. Checks inside the steps still apply.", "Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.")]
    else:
        lines += [_t(language, "Before the actions run: ", "Bevor die Aktionen starten: ") + _condition(conditions, language) + "."]
    lines += ["", "## " + _t(language, "Actual flow", "Konkreter Ablauf"), ""]
    if "use_blueprint" in config:
        lines += [_t(language, "This file refers to a blueprint. The blueprint's internal steps are not included here; its actual behaviour cannot be reconstructed from this file alone.", "Diese Datei verweist auf einen Blueprint. Dessen interne Schritte fehlen hier; das tatsächliche Verhalten lässt sich aus dieser Datei allein nicht rekonstruieren."), ""]
    if "variables" in config:
        lines += [_t(language, "The automation also prepares intermediate values; their contents/formulas are not described.", "Die Automation bereitet außerdem Zwischenwerte vor; ihre Inhalte/Formeln sind nicht beschrieben."), ""]
    lines += _sequence(config.get("actions", config.get("action", [])), language)
    lines += ["", "## " + _t(language, "If it triggers again", "Wenn sie erneut ausgelöst wird"), "", _mode(config, language), ""]
    lines += [_t(language, "Repeated entity references connect the same device or value across these steps. Names such as `sensor.example_01` are placeholders; neutral descriptive names may also be retained. Settings marked “not available” cannot be recovered from this example.", "Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen."), ""]
    lines += [_t(language, "Behaviour reference: [action sequences](https://www.home-assistant.io/docs/automation/building-blocks/) · [waits and timeouts](https://www.home-assistant.io/building-blocks/wait_template/) · [run modes](https://www.home-assistant.io/docs/automation/modes/).", "Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/)."), ""]
    return "\n".join(lines)


def _summary_duration(value: Any, language: str) -> str:
    if type(value) is str and _DURATION.fullmatch(value):
        values = value.split(":")
        hours, minutes = int(values[0]), int(values[1])
        seconds = float(values[2]) if len(values) > 2 else 0
        parts = [f"{amount:g} {unit}" for amount, unit in ((hours, "h"), (minutes, "min"), (seconds, "s")) if amount]
        return " ".join(parts) or "0 s"
    return _duration(value, language)


def _summary_settings(node: dict, language: str) -> list[str]:
    """Keep useful retained values; missing-value diagnostics stay in details."""
    parts = [part for part in _rule_settings(node, language, True)
             if _missing(language) not in part and "(null)" not in part]
    if "for" in node:
        parts = [part.replace(_duration(node["for"], language), _summary_duration(node["for"], language)) for part in parts]
    return parts


def _condition_brief(value: Any, language: str) -> str:
    conditions = _items(value)
    first = conditions[0] if conditions and isinstance(conditions[0], dict) else {}
    settings = _summary_settings(first, language)
    result = "; ".join(settings) or _t(language, "the configured conditions pass", "die eingestellten Bedingungen erfüllt sind")
    if len(conditions) > 1 and settings:
        count = len(conditions) - 1
        result += _t(language, f"; {count} other check" + ("s" if count != 1 else ""), f"; {count} weitere Prüfung" + ("en" if count != 1 else ""))
    return result


def _summary_action(node: dict, language: str) -> str:
    """Put a common action and its useful value in one readable phrase."""
    service = node.get("action", node.get("service"))
    data = node.get("data", node.get("data_template", {}))
    if not isinstance(data, dict):
        return _service_text(node, language, compact=True)
    phrases = {
        "climate.set_temperature": ("temperature", "Set the temperature to {value}", "Temperatur auf {value} setzen"),
        "fan.set_percentage": ("percentage", "Set the fan speed to {value}%", "Lüftergeschwindigkeit auf {value} % setzen"),
        "media_player.volume_set": ("volume_level", "Set the volume to {value} (0–1)", "Lautstärke auf {value} setzen (0–1)"),
        "input_number.set_value": ("value", "Store the number {value}", "Zahlenwert {value} speichern"),
        "counter.set_value": ("value", "Set a counter to {value}", "Zähler auf {value} setzen"),
    }
    if type(service) is str and service in phrases:
        key, english, german = phrases[service]
        value = _number(data.get(key))
        if value is not None:
            remaining = dict(data)
            remaining.pop(key, None)
            extras = _data_parts({**node, "data": remaining}, language, compact=True)
            extras = [part for part in extras if _missing(language) not in part]
            return _t(language, english, german).format(value=value) + ("; " + "; ".join(extras) if extras else "")
    if service == "light.turn_on" and (value := _number(data.get("brightness_pct"))) is not None:
        remaining = dict(data)
        remaining.pop("brightness_pct", None)
        extras = [part for part in _data_parts({**node, "data": remaining}, language, compact=True) if _missing(language) not in part]
        label = _t(language, f"Turn on lights at {value}% brightness", f"Licht mit {value} % Helligkeit einschalten")
        return label + ("; " + "; ".join(extras) if extras else "")
    return _service_text(node, language, compact=True)


def _branch_preview(value: Any, language: str, depth: int) -> str:
    sequence = _items(value)
    result = " → ".join(_brief_step(step, language, depth + 1) for step in sequence[:2]) or _t(language, "no steps", "keine Schritte")
    if len(sequence) > 2:
        count = len(sequence) - 2
        result += _t(language, f" → {count} more step" + ("s" if count != 1 else ""), f" → {count} " + ("weiterer Schritt" if count == 1 else "weitere Schritte"))
    return result


def _brief_step(node: Any, language: str, depth: int = 0) -> str:
    if not isinstance(node, dict) or depth > 2:
        return _t(language, "further nested steps", "weitere verschachtelte Schritte")
    if node.get("enabled") is False:
        active = {key: value for key, value in node.items() if key != "enabled"}
        return _t(language, "disabled: ", "deaktiviert: ") + _brief_step(active, language, depth)
    if "choose" in node:
        branches = _items(node["choose"])
        previews = []
        for branch in branches[:2]:
            if isinstance(branch, dict):
                conditions = _items(branch.get("conditions"))
                settings = _summary_settings(conditions[0], language) if conditions and isinstance(conditions[0], dict) else []
                steps = _branch_preview(branch.get("sequence"), language, depth)
                previews.append(("; ".join(settings) + ": " if settings else "") + steps)
        result = _t(language, "use the first matching branch: ", "den ersten passenden Zweig ausführen: ") + " / ".join(previews)
        if len(branches) > 2:
            count = len(branches) - 2
            result += _t(language, f"; {count} more " + ("branch" if count == 1 else "branches"), f"; {count} " + ("weiterer Zweig" if count == 1 else "weitere Zweige"))
        if "default" in node:
            result += _t(language, "; otherwise: ", "; sonst: ") + _branch_preview(node["default"], language, depth)
        return result
    if "if" in node:
        result = _t(language, "if ", "wenn ") + _condition_brief(node["if"], language) + ": (" + _branch_preview(node.get("then"), language, depth) + ")"
        if node.get("else"):
            result += _t(language, "; otherwise: (", "; sonst: (") + _branch_preview(node["else"], language, depth) + ")"
        return result
    if "wait_for_trigger" in node or "wait_template" in node:
        triggers = _items(node.get("wait_for_trigger"))
        first = triggers[0] if triggers and isinstance(triggers[0], dict) else {}
        settings = _summary_settings(first, language)
        limits = [part for part in settings if part.startswith(("above ", "below ", "über ", "unter "))]
        if limits:
            description = _t(language, "a value ", "einen Wert ") + _t(language, " and ", " und ").join(limits)
            if len(triggers) > 1:
                count = len(triggers) - 1
                description += _t(language, f" or {count} other trigger" + ("s" if count != 1 else ""), f" oder {count} weitere" + ("n Auslöser" if count == 1 else " Auslöser"))
            text = _t(language, "wait for ", "warten auf ") + description
        elif settings:
            text = _t(language, "wait for ", "warten auf ") + "; ".join(settings)
            if len(triggers) > 1:
                text += _t(language, " or another configured trigger", " oder einen anderen eingestellten Auslöser")
        elif len(triggers) > 1:
            text = _t(language, f"wait for one of {len(triggers)} triggers", f"auf einen von {len(triggers)} Auslösern warten")
        else:
            text = _t(language, "wait for a condition" if "wait_template" in node else "wait for another trigger", "auf eine Bedingung warten" if "wait_template" in node else "auf einen weiteren Auslöser warten")
        if "timeout" in node:
            behavior = _t(language, "stop on timeout", "bei Ablauf stoppen") if node.get("continue_on_timeout") is False else _t(language, "continue on timeout", "bei Ablauf weiter") if node.get("continue_on_timeout", True) is True else _t(language, "timeout behaviour unavailable", "Verhalten bei Ablauf nicht erhalten")
            duration = _summary_duration(node["timeout"], language)
            limit = _t(language, "up to ", "bis zu ") + duration + "; " if _missing(language) not in duration else ""
            text += " (" + limit + behavior + ")"
        return text
    if "delay" in node:
        return _t(language, "pause for ", "warten für ") + _summary_duration(node["delay"], language)
    if "parallel" in node:
        return _t(language, f"run {len(_items(node['parallel']))} paths in parallel", f"{len(_items(node['parallel']))} Pfade parallel ausführen")
    if "repeat" in node:
        repeat = node["repeat"] if isinstance(node["repeat"], dict) else {}
        sequence = _items(repeat.get("sequence"))
        rule = _t(language, "repeat", "wiederholen")
        if "count" in repeat:
            rule += " " + (_number(repeat["count"]) or _missing(language)) + _t(language, " times", "-mal")
        elif "until" in repeat:
            rule += _t(language, " until conditions pass", " bis Bedingungen erfüllt sind")
        elif "while" in repeat:
            rule += _t(language, " while conditions pass", " solange Bedingungen erfüllt sind")
        elif "for_each" in repeat:
            rule += _t(language, " for each list item", " für jeden Listeneintrag")
        return rule + (": " + _brief_step(sequence[0], language, depth + 1) if sequence else "")
    if "variables" in node:
        return _t(language, "prepare intermediate values", "Zwischenwerte vorbereiten")
    if "condition" in node:
        return _t(language, "check conditions; stop this sequence if false", "Bedingungen prüfen; bei falsch diesen Ablauf stoppen")
    if "stop" in node:
        return _t(language, "stop this run", "Durchlauf stoppen")
    if "sequence" in node:
        return _t(language, "run a nested sequence", "verschachtelten Ablauf ausführen")
    return _summary_action(node, language)


def _contains_domain(value: Any, domains: set[str], depth: int = 0) -> bool:
    if depth > _MAX_DEPTH:
        return False
    if isinstance(value, dict):
        service = value.get("action", value.get("service"))
        if type(service) is str and service.split(".", 1)[0] in domains:
            return True
        return any(_contains_domain(child, domains, depth + 1) for child in value.values())
    if isinstance(value, list):
        return any(_contains_domain(child, domains, depth + 1) for child in value)
    return False


def _summary_start(config: dict, language: str) -> str:
    """Mention retained start settings without repeating redaction diagnostics."""
    starts = []
    limits_only = True
    for trigger in _items(config.get("triggers", config.get("trigger"))):
        if not isinstance(trigger, dict) or trigger.get("enabled") is False:
            continue
        settings = _summary_settings(trigger, language)
        kind = trigger.get("trigger", trigger.get("platform"))
        if settings:
            limits_only = limits_only and all(part.startswith(("above ", "below ", "über ", "unter ")) for part in settings)
            starts.append("; ".join(settings))
        elif type(kind) is str and kind in _TRIGGER_LABELS:
            labels = _TRIGGER_LABELS[kind]
            event = trigger.get("event")
            if kind == "sun" and event in {"sunrise", "sunset"}:
                starts.append(_t(language, "sunrise" if event == "sunrise" else "sunset", "Sonnenaufgang" if event == "sunrise" else "Sonnenuntergang"))
            else:
                starts.append(_t(language, *labels))
            limits_only = False
    if not starts:
        return ""
    distinct = list(dict.fromkeys(starts))
    label = _t(language, "Start limits: ", "Startgrenzen: ") if limits_only else _t(language, "Start settings: ", "Starteinstellungen: ")
    result = label + " / ".join(distinct[:2])
    if len(distinct) > 2:
        count = len(distinct) - 2
        result += _t(language, f"; {count} more trigger" + ("s" if count != 1 else "") + " in the details", f"; {count} " + ("weiterer Auslöser" if count == 1 else "weitere Auslöser") + " in den Details")
    return result + "."


def summarize(config: dict, metadata: dict | None = None, language: str = "en") -> str:
    """Lead with concrete retained actions; keep redaction details on the page."""
    if language not in LANGUAGES or not isinstance(config, dict):
        raise ValueError("Unsupported language or automation configuration")
    actions = _items(config.get("actions", config.get("action")))
    if not actions:
        return _t(language, "Blueprint logic is external." if "use_blueprint" in config else "No action steps included.", "Blueprint-Logik liegt außerhalb der Datei." if "use_blueprint" in config else "Keine Aktionsschritte enthalten.")
    selected = actions
    if len(actions) > 3 and isinstance(metadata, dict):
        from catalogue import CATEGORIES
        category = metadata.get("category")
        domains = CATEGORIES[category][1] if type(category) is str and category in CATEGORIES else set()
        if domains:
            relevant = [action for action in actions if _contains_domain(action, domains) or isinstance(action, dict) and any(key in action for key in ("delay", "wait_for_trigger", "wait_template"))]
            if relevant and len(relevant) < len(actions):
                selected = relevant
    parts = []
    for action in selected[:3]:
        part = _brief_step(action, language)
        if parts and sum(map(len, parts)) + len(part) > 500:
            break
        parts.append(part)
    result = " → ".join(parts)
    result = result[:1].upper() + result[1:]
    if selected is not actions:
        omitted = len(actions) - len(parts)
        result += _t(language, f" (selected steps; {omitted} other action" + ("s" if omitted != 1 else "") + " omitted)", f" (ausgewählte Schritte; {omitted} weitere Aktion" + ("en" if omitted != 1 else "") + " ausgelassen)")
    elif len(actions) > len(parts):
        remaining = len(actions) - len(parts)
        result += _t(language, f" → {remaining} more step" + ("s" if remaining != 1 else "") + " (see full flow)", f" → {remaining} " + ("weiterer Schritt" if remaining == 1 else "weitere Schritte") + " (siehe Ablauf)")
    result += "."
    start = _summary_start(config, language)
    if start:
        result += " " + start
    if config.get("conditions", config.get("condition")):
        result += _t(language, " Includes condition checks before the actions.", " Vor den Aktionen werden Bedingungen geprüft.")
    return result
