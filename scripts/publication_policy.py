#!/usr/bin/env python3
"""Exclude door-control automations from the published catalogue.

Run source checks before anonymization: removing identifying names also removes
clues about what custom switches and scripts control. Run the same policy again
on the cleaned output. Unknown cover actuators require review because an opaque
cover identifier could refer to a garage door. Door-contact sensors used to
trigger lighting or notifications are not door-control actions.

Fix mode removes complete managed examples, never individual action steps, and
does not rewrite Git history. Logs contain only fixed policy categories/counts.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from typing import Any
import unicodedata

import yaml


REASON_CODES = frozenset({"lock-control", "door-control", "unreviewed-cover-control"})
ACTUATOR_DOMAINS = frozenset({
    "switch", "button", "script", "remote", "cover", "rest_command",
    "shell_command", "input_button", "scene", "automation",
})
READ_ONLY_DOMAINS = frozenset({
    "notify", "persistent_notification", "tts", "logbook", "system_log",
    "light", "sensor", "binary_sensor", "event",
})
DOOR_WORD = re.compile(
    r"(?:doors?|gates?|gateopener|gatecontrol|garage|garages|garagen|garagedoor|garageopener|"
    r"(?:front|back|side|entry|entrance|garage)?door(?:s|opener|lock|control)?|"
    r"(?:haus|eingangs|wohnungs|garten|hinter|seiten)?tuer(?:en|oeffner|steuerung|antrieb|schloss)?|"
    r"(?:garten|einfahrts|hof|garagen)?tor(?:e|oeffner|antrieb|steuerung)?)"
)
NEUTRAL_COVER_WORDS = frozenset({
    "blind", "blinds", "shutter", "shutters", "window", "windows",
    "rollladen", "rolllaeden", "rolladen", "rollaeden", "jalousie",
    "jalousien", "raffstore", "raffstores", "fenster",
})
CONTROL_WORDS = frozenset({
    "open", "close", "unlock", "lock", "opener", "operate", "control",
    "oeffnen", "oeffner", "schliessen", "entriegeln", "verriegeln", "antrieb",
})
ENTITY_REFERENCE = re.compile(r"^([a-z][a-z0-9_]*)\.[a-z0-9_]+$")
MAX_FILE_BYTES = 4 * 1024 * 1024


class PolicyError(ValueError):
    """Policy error whose message never includes source text or private paths."""


@dataclass(frozen=True)
class PolicyResult:
    checked: int
    blocked: int
    removed: int
    reason_counts: dict[str, int]


def _strings(value: Any) -> list[str]:
    result: list[str] = []
    pending = [value]
    visited = 0
    while pending:
        visited += 1
        if visited > 10000:
            raise PolicyError("Policy input is too complex to inspect safely")
        item = pending.pop()
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, list):
            pending.extend(item)
        elif isinstance(item, dict):
            pending.extend(item.values())
    return result


def _words(values: list[str]) -> set[str]:
    text = " ".join(values)
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text).lower()
    text = text.translate(str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}))
    text = unicodedata.normalize("NFKD", text)
    return set(re.findall(r"[a-z0-9]+", text))


def _door_hint(values: list[str]) -> bool:
    return any(DOOR_WORD.fullmatch(word) for word in _words(values))


def forbidden_reasons(config: dict[str, Any]) -> set[str]:
    """Return fixed policy reasons for source or anonymized automation content.

    Trigger and condition entities do not count as actuators. Aliases only give
    context to actual control actions, so an automation describing a door sensor
    can still turn on a light or send a notification.
    """
    if not isinstance(config, dict):
        raise PolicyError("Automation input must be a mapping")
    reasons: set[str] = set()
    visited = 0
    active: set[int] = set()

    def inspect_action(node: dict[str, Any], labels: list[str]) -> None:
        services = [node[key] for key in ("action", "service") if isinstance(node.get(key), str)]
        domains = {service.split(".", 1)[0] for service in services if "." in service}
        if isinstance(node.get("domain"), str):
            domains.add(node["domain"])
        selectors = _strings(node.get("entity_id"))
        if isinstance(node.get("target"), dict):
            selectors += _strings(node["target"].get("entity_id"))
        commands: list[str] = []
        for data_key in ("data", "service_data"):
            data = node.get(data_key)
            if isinstance(data, dict):
                selectors += _strings(data.get("entity_id"))
                commands += _strings(data.get("command")) + _strings(data.get("commands"))
        target_domains = {match.group(1) for value in selectors if (match := ENTITY_REFERENCE.fullmatch(value))}
        if "lock" in domains or "lock" in target_domains:
            reasons.add("lock-control")
        context = labels + services + selectors + commands
        door = _door_hint(context)
        if "cover" in domains or "cover" in target_domains:
            if door:
                reasons.add("door-control")
            elif not (_words(context) & NEUTRAL_COVER_WORDS):
                reasons.add("unreviewed-cover-control")
        actuator = bool((domains | target_domains) & ACTUATOR_DOMAINS)
        actuator |= any(service in {"homeassistant.turn_on", "homeassistant.turn_off", "homeassistant.toggle"} for service in services)
        # Custom integration services can operate an opener too; never classify
        # messages or lights as actuators just because their alias mentions a door.
        custom_control = bool(domains - READ_ONLY_DOMAINS) and bool(_words(services + commands) & CONTROL_WORDS)
        if door and (actuator or custom_control):
            reasons.add("door-control")

    def walk(node: Any, labels: list[str], depth: int = 0) -> None:
        nonlocal visited
        visited += 1
        if visited > 100000 or depth > 100:
            raise PolicyError("Policy input is too complex to inspect safely")
        if not isinstance(node, (dict, list)):
            return
        identity = id(node)
        if identity in active:
            raise PolicyError("Recursive policy input is not supported")
        active.add(identity)
        try:
            if isinstance(node, list):
                for child in node:
                    walk(child, labels, depth + 1)
                return
            local_labels = labels + _strings(node.get("alias")) + _strings(node.get("description"))
            inspect_action(node, local_labels)
            for key in ("actions", "action", "sequence", "then", "else", "default", "parallel"):
                if isinstance(node.get(key), (dict, list)):
                    walk(node[key], local_labels, depth + 1)
            if isinstance(node.get("choose"), list):
                for branch in node["choose"]:
                    if isinstance(branch, dict):
                        walk(branch, local_labels, depth + 1)
            if isinstance(node.get("repeat"), dict):
                walk(node["repeat"].get("sequence"), local_labels, depth + 1)
        finally:
            active.remove(identity)

    labels = _strings(config.get("alias")) + _strings(config.get("description"))
    for key in ("actions", "action"):
        walk(config.get(key), labels)
    blueprint = config.get("use_blueprint")
    if isinstance(blueprint, dict) and isinstance(blueprint.get("input"), dict):
        # Blueprint inputs may name actuators even though their action sequence
        # lives outside the exported automation.
        for key, value in blueprint["input"].items():
            references = [item for item in _strings(value) if ENTITY_REFERENCE.fullmatch(item)]
            if references:
                inspect_action({"entity_id": references}, labels + ([key] if isinstance(key, str) else []))
    return reasons


def _safe_path(path: Path) -> None:
    if any(part.is_symlink() for part in (path, *path.parents)) or ".git" in path.parts:
        raise PolicyError("Publication paths must not contain symlinks or Git metadata")


def _managed_examples(root: Path) -> list[tuple[Path, dict[str, Any]]]:
    from catalogue import CATEGORIES, validate_metadata
    from privacy_guard import load_yaml

    _safe_path(root)
    target = root / "automations"
    _safe_path(target)
    if not root.is_dir() or not target.is_dir():
        raise PolicyError("A managed automation catalogue is required")
    result = []
    required = {"automation.yaml", "metadata.json", "README.md"}
    for category in sorted(target.iterdir()):
        _safe_path(category)
        if not category.is_dir() or category.name not in CATEGORIES:
            raise PolicyError("Unexpected catalogue category")
        for folder in sorted(category.iterdir()):
            _safe_path(folder)
            if not folder.is_dir():
                raise PolicyError("Unexpected catalogue entry")
            children = list(folder.iterdir())
            if {child.name for child in children} not in (required, required | {"README.de.md"}):
                raise PolicyError("Managed examples must not contain unrelated files")
            for child in children:
                _safe_path(child)
                if not child.is_file() or child.stat().st_size > MAX_FILE_BYTES:
                    raise PolicyError("Managed example files must be bounded regular files")
            try:
                metadata = validate_metadata(json.loads((folder / "metadata.json").read_text(encoding="utf-8")))
                config = load_yaml((folder / "automation.yaml").read_text(encoding="utf-8"))
            except (ValueError, TypeError, OSError, yaml.YAMLError):
                raise PolicyError("Invalid managed example; no files were removed") from None
            if metadata["category"] != category.name or metadata["slug"] != folder.name or not isinstance(config, dict):
                raise PolicyError("Managed example identity is invalid")
            result.append((folder, config))
    return result


def _remove_examples(root: Path, folders: list[Path]) -> None:
    backup = Path(tempfile.mkdtemp(prefix=".ha-policy-removal-", dir=root.parent))
    moved: list[tuple[Path, Path]] = []
    complete = False
    try:
        for folder in folders:
            destination = backup / folder.relative_to(root / "automations")
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(folder, destination)
            moved.append((folder, destination))
        complete = True
    except OSError:
        try:
            for original, destination in reversed(moved):
                os.replace(destination, original)
        except OSError:
            raise PolicyError("Policy rollback failed; previous examples retained in a local backup") from None
        complete = True
        raise PolicyError("Could not remove excluded examples; previous catalogue restored") from None
    finally:
        if complete:
            shutil.rmtree(backup)
    for category in {folder.parent for folder in folders}:
        if not any(category.iterdir()):
            category.rmdir()


def policy_check(root: Path, fix: bool = False) -> PolicyResult:
    """Validate all examples before optionally removing complete blocked ones."""
    root = Path(root).absolute()
    entries = _managed_examples(root)
    blocked: list[Path] = []
    counts: Counter[str] = Counter()
    for folder, config in entries:
        reasons = forbidden_reasons(config)
        if reasons:
            blocked.append(folder)
            counts.update(reasons)
    if fix and blocked:
        _remove_examples(root, blocked)
    return PolicyResult(len(entries), len(blocked), len(blocked) if fix else 0, dict(sorted(counts.items())))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--fix", action="store_true")
    args = parser.parse_args()
    try:
        result = policy_check(args.root, fix=args.fix)
    except (PolicyError, OSError, ValueError, TypeError, RecursionError):
        print("Publication policy failed safely; validate the managed catalogue locally. Source details suppressed.", file=sys.stderr)
        return 1
    print(f"Publication policy: checked {result.checked}; blocked {result.blocked}; removed {result.removed}.")
    for reason, count in result.reason_counts.items():
        print(f"{reason}: {count}")
    return 1 if args.check and result.blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
