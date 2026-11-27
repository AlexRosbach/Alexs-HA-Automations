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


def _summary(metadata: dict[str, Any]) -> str:
    actions = ", ".join(f"`{action.replace('.call', '.custom_action')}`" for action in metadata["actions"])
    return f"Uses {actions}; {metadata['action_count']} top-level action step(s)."


def render_example_readme(metadata: dict[str, Any]) -> str:
    title = render_alias(metadata)
    triggers = ", ".join(TRIGGERS[t][1] for t in metadata["trigger_types"])
    features = ", ".join(metadata["features"]) or "none identified"
    variant = "\nThis name includes a stable fingerprint because another example has the same identifiable purpose. The fingerprint distinguishes configurations; it does not describe a different household or room.\n" if metadata["variant"] else ""
    return f"""# {title}

## What it does

{_summary(metadata)}

- **Category:** {CATEGORIES[metadata['category']][0]}
- **Triggers:** {triggers} ({metadata['trigger_count']} configured trigger block(s))
- **Structure:** {features}

The title describes only the behavior still identifiable in this exported template. Original trigger values, expressions and labels may already have been replaced during the earlier export. They cannot be recovered from this file. Custom action labels in this documentation describe anonymized actions, not literal service names to copy.
{variant}
## How to use it

1. Read [the catalogue](../../../README.md) and [the setup guide](../../../how-to/document-an-automation.md).
2. Inspect [`automation.yaml`](automation.yaml). Reconstruct missing trigger, condition and template expressions; replacing entity IDs alone may not be enough.
3. Replace every `example_…`, `REPLACE_…`, `DEVICE_…`, `AREA_…` and other placeholder with your own local configuration. Keep credentials in your own Home Assistant `secrets.yaml`.
4. Validate the completed configuration with Home Assistant. Test it manually with a non-critical device before enabling it.

## Privacy and safety

This is a configurable example, not a ready-to-run backup. Do not commit your local credentials, identifiers, recipient names, internal addresses or completed personal configuration. Run the repository's [security checks](../../../how-to/security-and-privacy.md) before publishing changes.

The public title and summary are generated from [`metadata.json`](metadata.json), which accepts only reviewed generic concepts.
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
        _write(readme, "# Home Assistant automation examples\n\n"
               "Configurable public templates with descriptive names. Open an example's README, "
               "configure every placeholder locally and validate it in Home Assistant before use. "
               "Keep personal configuration and credentials outside this catalogue.\n\n"
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
    count_label = "example" if len(entries) == 1 else "examples"
    lines = [START, "", '<a id="automation-catalogue"></a>', "", f"## Automation catalogue ({len(entries)} {count_label})", "", "Choose a category, then open an example's documentation. Every name describes only behavior identifiable in the public export.", ""]
    counts = Counter(m["category"] for _, m in entries)
    lines += [" | ".join(f"[{CATEGORIES[c][0]} ({counts[c]})](#{c})" for c in CATEGORIES if counts[c]), ""]
    for category, (label, _) in CATEGORIES.items():
        subset = [(p, m) for p, m in entries if m["category"] == category]
        if not subset:
            continue
        lines += [f'<a id="{category}"></a>', "", f"### {label}", "", "| Automation | Trigger | Actions |", "| --- | --- | --- |"]
        for folder, metadata in subset:
            title = render_alias(metadata).replace("|", "\\|")
            link = folder.relative_to(root).as_posix() + "/README.md"
            triggers = ", ".join(TRIGGERS[t][1] for t in metadata["trigger_types"])
            actions = ", ".join(f"`{a.replace('.call', '.custom_action')}`" for a in metadata["actions"])
            lines.append(f"| [{title}]({link}) | {triggers} | {actions} |")
        lines.append("")
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
    for folder, metadata in entries:
        path = folder / "README.md"
        expected = render_example_readme(metadata)
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
