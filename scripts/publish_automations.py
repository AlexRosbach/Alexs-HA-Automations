#!/usr/bin/env python3
"""Build a privacy-safe Home Assistant automation example catalogue.

The source export is deliberately kept outside this repository. This tool only
writes synthetic, documented examples and fails if it encounters a value that
looks like a secret or a direct identifier it cannot replace safely.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

# Keep only values whose schema is an intentionally finite Home Assistant enum.
# Everything else is a placeholder, even when it looks harmless: room labels,
# variable names, messages and custom event names routinely identify a home.
SAFE_STRING_KEYS = {"mode"}
SERVICE_RE = re.compile(r"^[a-z_]+\.[a-z_]+$")
ENTITY_RE = re.compile(r"^[a-z_]+\.[a-z0-9_]+$")
ID_KEY_RE = re.compile(r"(?:^|_)(?:id|ids|device_id|area_id|floor_id|config_entry_id)$")
SECRET_KEY_RE = re.compile(r"(?:token|password|secret|api_key|webhook|authorization|access_key)", re.I)
URL_RE = re.compile(r"(?:https?://|wss?://|@[\w.-]+\.[a-z]{2,})", re.I)
HEX_RE = re.compile(r"\b(?:[0-9a-f]{8,}|[0-9a-f]{2}(?::[0-9a-f]{2}){5})\b", re.I)


class Anonymizer:
    def __init__(self) -> None:
        self.entities: dict[str, str] = {}
        self.opaque: dict[tuple[str, str], str] = {}
        self.counts: Counter[str] = Counter()

    def entity(self, value: str) -> str:
        if value not in self.entities:
            domain = value.split(".", 1)[0] if "." in value else "entity"
            self.counts[f"entity:{domain}"] += 1
            self.entities[value] = f"{domain}.example_{self.counts[f'entity:{domain}']:02d}"
        return self.entities[value]

    def opaque_value(self, kind: str, value: str) -> str:
        key = (kind, value)
        if key not in self.opaque:
            self.counts[kind] += 1
            self.opaque[key] = f"{kind.upper()}_{self.counts[kind]:02d}"
        return self.opaque[key]

    def value(self, value: Any, key: str = "") -> Any:
        if isinstance(value, dict):
            return {k: self.value(v, str(k)) for k, v in value.items()}
        if isinstance(value, list):
            return [self.value(v, key) for v in value]
        if not isinstance(value, str):
            return value
        if SECRET_KEY_RE.search(key):
            return "REPLACE_WITH_YOUR_OWN_SECRET"
        if key in {"entity_id", "entity", "source_entity_id"}:
            return self.entity(value) if ENTITY_RE.match(value) else self.opaque_value("entity", value)
        if key in {"service", "action"} and SERVICE_RE.match(value):
            return value
        if ID_KEY_RE.search(key):
            return self.opaque_value(key.replace("_id", "") or "identifier", value)
        if URL_RE.search(value) or HEX_RE.search(value):
            return "REPLACE_WITH_YOUR_OWN_VALUE"
        if key in SAFE_STRING_KEYS:
            return value
        # Labels, messages, aliases, template strings and device names are never
        # copied verbatim: even harmless-looking words can identify a household.
        return "REPLACE_WITH_YOUR_OWN_TEXT"


def readable_summary(source: dict[str, Any]) -> tuple[str, str]:
    """Describe behavior by HA concepts only; never reuse labels or IDs."""
    triggers = source.get("triggers", source.get("trigger", []))
    actions = source.get("actions", source.get("action", []))
    trigger_count = len(triggers) if isinstance(triggers, list) else 1
    action_count = len(actions) if isinstance(actions, list) else 1
    trigger_items = triggers if isinstance(triggers, list) else [triggers]
    labels = {
        "state": "state changes",
        "numeric_state": "numeric thresholds",
        "time": "a scheduled time",
        "time_pattern": "a repeating schedule",
        "sun": "sun events",
        "event": "Home Assistant events",
        "template": "a template condition",
    }
    trigger_kinds = []
    for item in trigger_items:
        if isinstance(item, dict):
            kind = item.get("trigger", item.get("platform"))
            if kind in labels and labels[kind] not in trigger_kinds:
                trigger_kinds.append(labels[kind])
    action_domains: set[str] = set()
    def find_services(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"action", "service"} and isinstance(child, str) and SERVICE_RE.match(child):
                    action_domains.add(child.split(".", 1)[0])
                find_services(child)
        elif isinstance(value, list):
            for child in value:
                find_services(child)
    find_services(actions)
    starts = ", ".join(trigger_kinds) if trigger_kinds else "one or more Home Assistant triggers"
    services = ", ".join(f"`{domain}`" for domain in sorted(action_domains)) or "generic Home Assistant actions"
    return (
        f"This example starts from {starts} and runs {action_count} action step(s) across the {services} domain(s).",
        f"It contains {trigger_count} trigger(s). Device, room, person, and free-text details were removed deliberately. Replace every `example_…` and `REPLACE_…` value with entities and text from your own installation.",
    )


def make_readme(number: int, source: dict[str, Any]) -> str:
    purpose, use = readable_summary(source)
    return f"""# Automation {number:03d}

## What it does

{purpose}

## How to use it

{use}

1. Copy `automation.yaml` into Home Assistant (UI YAML editor or your automation package).
        2. Replace every `example_…`, `REPLACE_…`, `DEVICE_…`, and `AREA_…` placeholder.
3. Validate the YAML, reload automations, and test with a safe device first.

## Privacy and safety

This example was anonymized before publication. It intentionally contains no original entity IDs, device IDs, areas, user names, addresses, URLs, tokens, webhooks, or notification targets. Review every placeholder before enabling it.
"""


def assert_public_safe(root: Path) -> None:
    forbidden = re.compile(r"(?:[0-9a-f]{8,}|(?:[0-9a-f]{2}:){5}[0-9a-f]{2}|https?://)", re.I)
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in {".yaml", ".yml", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if forbidden.search(text):
            raise RuntimeError(f"Potential identifier or URL remains in {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    raw = json.loads(args.source.read_text(encoding="utf-8"))
    if not isinstance(raw, list) or not raw:
        raise SystemExit("Source must be a non-empty JSON list")
    auto = Anonymizer()
    target = args.output / "automations"
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for number, item in enumerate(raw, 1):
        config = copy.deepcopy(item["config"])
        config.pop("id", None)
        config.pop("alias", None)
        config.pop("description", None)
        public = auto.value(config)
        public["alias"] = f"Automation {number:03d} – reusable example"
        public["description"] = "Anonymized public example. Replace all placeholders before use."
        folder = target / f"automation-{number:03d}"
        folder.mkdir()
        (folder / "automation.yaml").write_text(yaml.safe_dump(public, allow_unicode=True, sort_keys=False), encoding="utf-8")
        (folder / "README.md").write_text(make_readme(number, config), encoding="utf-8")
    assert_public_safe(target)
    print(f"Created {len(raw)} anonymized examples in {target}")


if __name__ == "__main__":
    main()
