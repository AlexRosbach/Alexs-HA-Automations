#!/usr/bin/env python3
"""Fail-closed checks and deterministic anonymization for public HA examples.

This is deliberately a publication policy, not a general natural-language PII
classifier. Unknown automation strings become explicit placeholders; code and
documentation receive conservative, high-confidence text checks. Gitleaks adds
credential-provider detection. No finding ever includes the matched value.
"""
from __future__ import annotations

import argparse
import ipaddress
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any
from urllib.parse import urlsplit

import yaml


class PrivacyError(ValueError):
    """Only fixed, non-sensitive messages may be supplied to this exception."""


class SecretReference(str):
    pass


class PublicLoader(yaml.SafeLoader):
    pass


class PublicDumper(yaml.SafeDumper):
    pass


def _mapping(loader: PublicLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            if key in result:
                raise PrivacyError("Duplicate YAML mapping key")
            result[key] = loader.construct_object(value_node, deep=deep)
        except TypeError:
            raise PrivacyError("Unsupported YAML mapping key") from None
    return result


PublicLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)
PublicLoader.add_constructor("!secret", lambda loader, node: SecretReference(loader.construct_scalar(node)))
PublicDumper.add_representer(SecretReference, lambda dumper, value: dumper.represent_scalar("!secret", str(value)))


def load_yaml(text: str) -> Any:
    try:
        return yaml.load(text, Loader=PublicLoader)
    except (yaml.YAMLError, RecursionError, ValueError, TypeError):
        raise PrivacyError("Invalid or unsupported YAML; source details suppressed") from None


def dump_yaml(value: Any) -> str:
    return yaml.dump(value, Dumper=PublicDumper, allow_unicode=True, sort_keys=False)


DOMAINS = frozenset("""alarm_control_panel assist_satellite automation binary_sensor
    button calendar camera climate conversation counter cover device_tracker fan
    homeassistant humidifier input_boolean input_button input_datetime input_number
    input_select input_text light lock media_player mqtt notify number persistent_notification
    person remote rest_command scene script select sensor siren sun switch system_log
    timer todo tts update vacuum valve wake_on_lan water_heater weather zone
    dreame_vacuum zha zwave_js hassio logbook recorder frontend shell_command
    event text stt image image_processing schedule tag template websocket_api""".split())

# Explicit pairs: a name-shaped service is not automatically a public service.
SERVICE_NAMES = {
    "light": "turn_on turn_off toggle",
    "switch": "turn_on turn_off toggle",
    "input_boolean": "turn_on turn_off toggle",
    "automation": "trigger turn_on turn_off toggle reload",
    "script": "turn_on turn_off toggle reload",
    "scene": "turn_on apply reload",
    "counter": "increment decrement reset set_value configure",
    "notify": "notify send_message",
    "persistent_notification": "create dismiss dismiss_all",
    "mqtt": "publish reload",
    "todo": "get_items add_item update_item remove_item remove_completed_items",
    "button": "press",
    "input_button": "press",
    "lock": "lock unlock open",
    "vacuum": "start pause stop return_to_base locate clean_spot set_fan_speed send_command",
    "dreame_vacuum": "vacuum_clean_segment",
    "climate": "set_temperature set_hvac_mode set_preset_mode set_fan_mode set_swing_mode turn_on turn_off toggle",
    "cover": "open_cover close_cover stop_cover toggle set_cover_position open_cover_tilt close_cover_tilt stop_cover_tilt set_cover_tilt_position",
    "media_player": "turn_on turn_off toggle volume_set volume_up volume_down volume_mute play_media media_play media_pause media_play_pause media_stop media_next_track media_previous_track select_source shuffle_set repeat_set join unjoin clear_playlist",
    "fan": "turn_on turn_off toggle set_percentage set_preset_mode set_direction oscillate increase_speed decrease_speed",
    "homeassistant": "turn_on turn_off toggle restart stop check_config reload_config_entry reload_all update_entity",
    "system_log": "write clear",
    "camera": "snapshot record play_stream turn_on turn_off enable_motion_detection disable_motion_detection",
    "weather": "get_forecasts",
    "select": "select_option select_first select_last select_next select_previous",
    "input_select": "select_option select_first select_last select_next select_previous set_options",
    "assist_satellite": "announce start_conversation ask_question",
    "input_text": "set_value reload",
    "input_number": "set_value increment decrement reload",
    "input_datetime": "set_datetime reload",
    "number": "set_value",
    "tts": "speak clear_cache",
    "timer": "start pause cancel finish change reload",
    "alarm_control_panel": "alarm_arm_away alarm_arm_home alarm_arm_night alarm_arm_vacation alarm_disarm alarm_trigger",
    "calendar": "get_events create_event",
    "conversation": "process",
    "remote": "turn_on turn_off toggle send_command learn_command delete_command",
    "update": "install skip clear_skipped",
    "logbook": "log",
}
PUBLIC_SERVICES = frozenset(f"{domain}.{name}" for domain, names in SERVICE_NAMES.items() for name in names.split())

SCHEMA_KEYS = frozenset("""triggers trigger platform conditions condition actions action
    service target entity_id entity source_entity_id device_id area_id floor_id label_id
    config_entry_id entry_id user_id person_id id ids tag_id notification_id context
    domain type subtype data data_template metadata mode alias description enabled
    initial_state max max_exceeded continue_on_error continue_on_timeout response_variable
    variables repeat for_each sequence choose default if then else until while count
    parallel wait_for_trigger wait_template timeout delay for hours minutes seconds
    milliseconds days above below at before after before_offset after_offset to from
    not_to not_from state attribute value_template match event event_type event_data
    weekday value title message text payload topic qos retain evaluate_payload
    brightness brightness_pct brightness_step brightness_step_pct transition rgb_color
    rgbw_color rgbww_color hs_color xy_color color_temp color_temp_kelvin color_name
    flash effect temperature target_temp_high target_temp_low hvac_mode fan_mode
    preset_mode swing_mode humidity percentage fan_speed clean_times segments
    position tilt_position volume_level is_volume_muted shuffle source media
    media_content_id media_content_type media_class children_media_class navigateIds
    browse_entity_id media_player_entity_id media_player enqueue extra supported_features
    status uid summary item options option path input use_blueprint sensor
    datetime date time timestamp duration stop stop_actions skip_condition trace
    stored_traces filename attachment url thumbnail content-type hide-thumbnail format
    tag persistent ttl priority preannounce answers sentences question_media_id language
    notification_id level logger error prefilter dry_run request_time threshold
    service_data event_data_template message_data code password token api_key secret
    access_token refresh_token client_secret webhook_id authorization latitude longitude
    elevation mac ip host hostname ssid bssid port username email phone chat_id
    answer memory events day cache announce offset transition_length response_variable
    max_exceeded action_yes action_no""".split())

ENUMS = {
    "mode": frozenset("single restart queued parallel".split()),
    "trigger": frozenset("state numeric_state time time_pattern sun event template device mqtt webhook homeassistant zone geo_location tag calendar conversation persistent_notification".split()),
    "platform": frozenset("state numeric_state time time_pattern sun event template device mqtt webhook homeassistant zone geo_location tag calendar conversation persistent_notification".split()),
    "condition": frozenset("and or not state numeric_state template time sun zone trigger device".split()),
    "domain": DOMAINS,
    "state": frozenset("on off open closed opening closing locked unlocked home not_home unavailable unknown idle active paused playing stopped charging docked cleaning returning problem ok heat cool auto dry fan_only heat_cool".split()),
    "to": frozenset("on off open closed opening closing locked unlocked home not_home unavailable unknown idle active paused playing stopped charging docked cleaning returning heat cool auto dry fan_only heat_cool".split()),
    "from": frozenset("on off open closed opening closing locked unlocked home not_home unavailable unknown idle active paused playing stopped charging docked cleaning returning heat cool auto dry fan_only heat_cool".split()),
    "event": frozenset("sunrise sunset start shutdown".split()),
    "hvac_mode": frozenset("off heat cool heat_cool auto dry fan_only".split()),
    "match": frozenset(("all", "any")),
    "status": frozenset(("needs_action", "completed")),
    "max_exceeded": frozenset(("silent", "warning", "error", "info", "debug")),
    "level": frozenset(("critical", "fatal", "error", "warning", "warn", "info", "debug", "notset")),
    "weekday": frozenset("mon tue wed thu fri sat sun".split()),
    "format": frozenset(("hls", "dash")),
    "media_content_type": frozenset("music video image movie episode playlist channel url app channels cast directory".split()),
    "media_class": frozenset("music video image movie episode playlist channel app directory".split()),
    "children_media_class": frozenset("music video image movie episode playlist channel app directory".split()),
    "flash": frozenset(("short", "long")),
    "enqueue": frozenset(("add", "next", "play", "replace")),
    "type": frozenset("is_on is_off turned_on turned_off pressed not_opened opened closed motion no_motion occupied not_occupied illuminance temperature humidity battery power energy turn_on turn_off toggle lock unlock open close stop restart double_press single_press long_press short_press remote_button_short_press remote_button_long_press remote_button_short_release remote_button_long_release".split()),
}
NUMERIC_KEYS = frozenset("""hours minutes seconds milliseconds days above below timeout delay
    brightness brightness_pct brightness_step brightness_step_pct transition color_temp
    color_temp_kelvin temperature target_temp_high target_temp_low percentage clean_times
    position tilt_position volume_level qos ttl max count stored_traces humidity threshold
    duration transition_length""".split())
BOOL_KEYS = frozenset("""enabled initial_state continue_on_error continue_on_timeout retain
    evaluate_payload stop_actions skip_condition persistent preannounce shuffle
    is_volume_muted dry_run cache announce""".split())
SECRET_KEY = re.compile(r"(?:password|passwd|token|secret|api[_-]?key|authorization|access[_-]?key|private[_-]?key|webhook|credential|pin[_-]?code|^code$)", re.I)
DIRECT_ID_KEY = re.compile(r"(?:^|_)(?:id|ids)$|^(?:latitude|longitude|elevation|mac|ip|host|hostname|ssid|bssid|username|email|phone|chat_id)$", re.I)
ENTITY = re.compile(r"^([a-z][a-z0-9_]*)\.([a-z0-9_]+)$")
PLACEHOLDER_KINDS = frozenset("DEVICE AREA FLOOR LABEL IDENTIFIER ENTITY ID MEDIA_CONTENT BROWSE_ENTITY TAG ENTRY NOTIFICATION MEDIA_PLAYER_ENTITY QUESTION_MEDIA".split())
PLACEHOLDER = re.compile(
    r"^(?:REPLACE_WITH_YOUR_OWN_(?:SECRET|TEXT|VALUE)|(?:"
    + "|".join(sorted(PLACEHOLDER_KINDS))
    + r"|variable|field|example_secret)_\d{2,5}|(?:"
    + "|".join(sorted(DOMAINS | {"entity"}))
    + r")\.example_\d{2,5})$"
)
TIME_PATTERN = re.compile(r"^(?:\*|/[1-9][0-9]?|[0-5]?[0-9])$")


class Anonymizer:
    """Shared per-publication mappings preserve cross-example references."""

    def __init__(self) -> None:
        self.mapping: dict[tuple[str, str], str] = {}
        self.reserved: dict[str, set[str]] = {}
        self.active: set[int] = set()
        self._reserved_objects: set[int] = set()

    def reserve(self, value: Any, depth: int = 0) -> None:
        if depth > 80:
            raise PrivacyError("Automation nesting is too deep")
        if isinstance(value, (dict, list)):
            if id(value) in self._reserved_objects:
                return
            self._reserved_objects.add(id(value))
        if isinstance(value, str) and PLACEHOLDER.fullmatch(value):
            group = value.rsplit("_", 1)[0]
            self.reserved.setdefault(group, set()).add(value)
        elif isinstance(value, dict):
            for k, v in value.items():
                self.reserve(k, depth + 1)
                self.reserve(v, depth + 1)
        elif isinstance(value, list):
            for item in value:
                self.reserve(item, depth + 1)

    def placeholder(self, kind: str, value: Any) -> str:
        if isinstance(value, str) and PLACEHOLDER.fullmatch(value):
            return value
        lookup = (kind, repr(value))
        if lookup not in self.mapping:
            reserved = self.reserved.setdefault(kind, set())
            n = 1
            while f"{kind}_{n:02d}" in reserved:
                n += 1
            replacement = f"{kind}_{n:02d}"
            reserved.add(replacement)
            self.mapping[lookup] = replacement
        return self.mapping[lookup]

    def entity(self, value: str) -> str:
        match = ENTITY.fullmatch(value)
        domain = match.group(1) if match and match.group(1) in DOMAINS else "entity"
        return self.placeholder(f"{domain}.example", value)

    def key(self, value: Any, context: str = "") -> str:
        if isinstance(value, str) and ENTITY.fullmatch(value):
            return self.entity(value)
        if isinstance(value, str) and PLACEHOLDER.fullmatch(value):
            return value
        if context == "variables":
            return self.placeholder("variable", value)
        if isinstance(value, str) and value in SCHEMA_KEYS:
            return value
        return self.placeholder("field", value)

    def value(self, value: Any, key: str = "", depth: int = 0) -> Any:
        if depth > 80:
            raise PrivacyError("Automation nesting is too deep")
        # Sensitive numeric, boolean and list values must be handled before type checks.
        if SECRET_KEY.search(key) and key not in {"trigger", "platform"}:
            return SecretReference(self.placeholder("example_secret", str(value))) if isinstance(value, SecretReference) else "REPLACE_WITH_YOUR_OWN_SECRET"
        if isinstance(value, SecretReference):
            return SecretReference(self.placeholder("example_secret", str(value)))
        if isinstance(value, (dict, list)):
            marker = id(value)
            if marker in self.active:
                raise PrivacyError("Recursive YAML aliases are not supported")
            self.active.add(marker)
            try:
                if isinstance(value, list):
                    return [self.value(v, key, depth + 1) for v in value]
                result = {}
                for k, v in value.items():
                    public_key = self.key(k, key)
                    if public_key in result:
                        raise PrivacyError("Anonymization would create duplicate mapping keys")
                    result[public_key] = self.value(v, str(k), depth + 1)
                return result
            finally:
                self.active.remove(marker)
        if value is None:
            return None
        if isinstance(value, str) and PLACEHOLDER.fullmatch(value):
            return value
        if key in {"entity_id", "entity", "source_entity_id", "browse_entity_id", "media_player_entity_id"}:
            return self.entity(value) if isinstance(value, str) and ENTITY.fullmatch(value) else self.placeholder("ENTITY", value)
        if DIRECT_ID_KEY.search(key):
            kind = {"device_id": "DEVICE", "area_id": "AREA", "floor_id": "FLOOR", "label_id": "LABEL", "id": "IDENTIFIER"}.get(key, "IDENTIFIER")
            return self.placeholder(kind, value)
        if key == "response_variable":
            return self.placeholder("variable", value)
        if isinstance(value, bool):
            return value if key in BOOL_KEYS else "REPLACE_WITH_YOUR_OWN_VALUE"
        if isinstance(value, (int, float)):
            return value if key in NUMERIC_KEYS and math.isfinite(value) and abs(value) <= 1000000 else "REPLACE_WITH_YOUR_OWN_VALUE"
        if not isinstance(value, str):
            return "REPLACE_WITH_YOUR_OWN_VALUE"
        if key in {"action", "service"}:
            return value if value in PUBLIC_SERVICES else self.entity(value)
        if key in ENUMS and value in ENUMS[key]:
            return value
        if key in {"hours", "minutes", "seconds"} and TIME_PATTERN.fullmatch(value):
            return value
        if key in {"delay", "timeout", "for"} and re.fullmatch(r"\d{1,2}:\d{2}:\d{2}(?:\.\d{1,3})?", value):
            return value
        if key in NUMERIC_KEYS and re.fullmatch(r"-?\d{1,6}(?:\.\d{1,6})?", value):
            return value
        return "REPLACE_WITH_YOUR_OWN_TEXT"

    def automation(self, config: dict[str, Any], labels: tuple[str, str] | None = None) -> dict[str, Any]:
        if not isinstance(config, dict):
            raise PrivacyError("An automation must be a mapping")
        result = self.value({k: v for k, v in config.items() if k not in {"id", "alias", "description"}})
        if labels:
            result["alias"], result["description"] = labels
        else:
            result["alias"] = "REPLACE_WITH_YOUR_OWN_TEXT"
            result["description"] = "REPLACE_WITH_YOUR_OWN_TEXT"
        return result


# Text findings have category-only diagnostics. Examples use reserved domains.
EMAIL_RE = re.compile(r"(?<![\w.])[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
IPV4_RE = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")
IPV6_RE = re.compile(r"(?<![\w:])(?:[0-9A-Fa-f]{0,4}:){2,}[0-9A-Fa-f:.]*(?:%[A-Za-z0-9_-]+)?(?![\w:])")
MAC_RE = re.compile(r"(?i)(?<![\w:])(?:[0-9a-f]{2}:){5}[0-9a-f]{2}(?![\w:])")
INTERNAL_HOST_RE = re.compile(r"(?i)\b(?:[a-z0-9][a-z0-9-]*\.)+(?:local|lan|internal|home|corp)(?![a-z0-9_.-])")
URL_RE = re.compile(r"(?i)\b(?:https?|wss?|ftp)://[^\s<>\"'`\)\]}]+")
TOKEN_RE = re.compile(r"(?<!\w)(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|cfut_[A-Za-z0-9_-]{15,}|sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{20,}|AIza[0-9A-Za-z_-]{30,})(?!\w)")
PRIVATE_KEY_RE = re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----.*?-----END (?:[A-Z ]+ )?PRIVATE KEY-----", re.S)
JWT_RE = re.compile(r"(?<![\w-])eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}(?![\w-])")
ASSIGNMENT_KEYS = r"password|passwd|api_key|access_token|refresh_token|client_secret|auth_token|authorization|private_key|webhook_id|token|phone|chat_id|latitude|longitude|ssid|hostname"
ASSIGNMENT_RE = re.compile(r"(?im)(?P<prefix>\b(?:" + ASSIGNMENT_KEYS + r")\b[\"']?\s*[:=]\s*)(?P<quote>[\"'])(?P<value>[^\n\r\"']+)(?P=quote)(?=[ \t]*(?:[,}\)\n\r#]|$))")
BARE_ASSIGNMENT_RE = re.compile(r"(?im)(?P<prefix>\b(?:" + ASSIGNMENT_KEYS + r")\b[\"']?\s*[:=]\s*)(?P<value>[^\s#,'\"{}\[\]]+)(?P<ending>\s*(?:[,}]|#|$))")
PUBLIC_HOSTS = frozenset("""github.com api.github.com raw.githubusercontent.com docs.github.com
    www.github.com github.blog home-assistant.io www.home-assistant.io developers.home-assistant.io
    community.home-assistant.io alerts.home-assistant.io pypi.org files.pythonhosted.org
    python.org www.python.org docs.python.org pre-commit.com www.shellcheck.net
    results.pre-commit.ci example.com example.org example.net example.invalid localhost""".split())
PUBLIC_MAIL_DOMAINS = frozenset(("example.com", "example.org", "example.net", "example.invalid", "users.noreply.github.com"))


def _safe_assignment(value: str) -> bool:
    return bool(PLACEHOLDER.fullmatch(value) or value.startswith(("${", "{{", "!secret ")) or value in {"", "example", "changeme", "redacted"})


def sanitize_text(text: str, *, structured: bool = True) -> tuple[str, set[str]]:
    categories: set[str] = set()

    def replace(pattern: re.Pattern, kind: str, replacement: str, allowed=lambda match: False) -> None:
        nonlocal text
        def callback(match: re.Match) -> str:
            if allowed(match):
                return match.group(0)
            categories.add(kind)
            return replacement
        text = pattern.sub(callback, text)

    replace(PRIVATE_KEY_RE, "private-key", "REPLACE_WITH_YOUR_OWN_SECRET")
    replace(TOKEN_RE, "provider-token", "REPLACE_WITH_YOUR_OWN_SECRET")
    replace(JWT_RE, "jwt", "REPLACE_WITH_YOUR_OWN_SECRET")
    def public_url(match: re.Match) -> bool:
        try:
            value = urlsplit(match.group(0))
            return (value.hostname or "").lower() in PUBLIC_HOSTS and value.username is None and value.password is None
        except ValueError:
            return False
    replace(URL_RE, "private-endpoint", "https://example.invalid", public_url)
    replace(EMAIL_RE, "email-address", "person@example.invalid", lambda m: m.group(0).rsplit("@", 1)[1].lower() in PUBLIC_MAIL_DOMAINS)

    def safe_ip(match: re.Match) -> bool:
        try:
            address = ipaddress.ip_address(match.group(0))
        except ValueError:
            return True
        return address.is_loopback or address.is_unspecified or any(address in ipaddress.ip_network(n) for n in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24"))

    replace(IPV4_RE, "ip-address", "192.0.2.1", safe_ip)
    def safe_ipv6(match: re.Match) -> bool:
        try:
            address = ipaddress.ip_address(match.group(0).split("%", 1)[0])
        except ValueError:
            return True
        return address.is_loopback or address.is_unspecified or address in ipaddress.ip_network("2001:db8::/32")
    replace(IPV6_RE, "ip-address", "2001:db8::1", safe_ipv6)
    replace(MAC_RE, "mac-address", "00:00:00:00:00:00", lambda m: m.group(0) == "00:00:00:00:00:00")
    replace(INTERNAL_HOST_RE, "internal-hostname", "example.invalid")
    def assignment(match: re.Match) -> str:
        if _safe_assignment(match.group("value")):
            return match.group(0)
        categories.add("credential-assignment")
        return match.group("prefix") + match.group("quote") + "REPLACE_WITH_YOUR_OWN_SECRET" + match.group("quote")
    text = ASSIGNMENT_RE.sub(assignment, text)
    if structured:
        def bare_assignment(match: re.Match) -> str:
            value = match.group("value")
            if _safe_assignment(value) or value in {"null", "None", "true", "false"}:
                return match.group(0)
            categories.add("credential-or-private-assignment")
            return match.group("prefix") + '"REPLACE_WITH_YOUR_OWN_SECRET"' + match.group("ending")
        text = BARE_ASSIGNMENT_RE.sub(bare_assignment, text)
    return text, categories


FORBIDDEN_FILE = re.compile(r"(?i)(?:^|/)(?:secrets\.ya?ml|\.env(?:\.(?!example$)[^/]+)?|\.storage(?:/.*)?|[^/]+\.(?:db|sqlite3?|pem|key|p12|pfx)|(?:[^/]*(?:backup|export)[^/]*)\.(?:json|zip|tar|gz)|automations\.ya?ml)$")
SKIP_DIRS = frozenset((".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".ruff_cache", "node_modules"))
MAX_FILE_BYTES = 2 * 1024 * 1024


def safe_paths(root: Path) -> list[Path]:
    if root.is_symlink():
        raise PrivacyError("Repository root must not be a symlink")
    root = root.resolve()
    probe = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    git_root = probe.returncode == 0 and Path(probe.stdout.strip()).resolve() == root
    result = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"], capture_output=True) if git_root else None
    if result is not None and result.returncode == 0:
        names = sorted(set(os.fsdecode(name) for name in result.stdout.split(b"\0") if name))
        paths = [root / name for name in names]
    else:
        paths = sorted(root.rglob("*"))
    selected = []
    for path in paths:
        relative = path.relative_to(root)
        # Git excludes untracked caches. Tracked or staged content is never
        # exempt merely because its directory resembles a dependency/cache.
        if ".git" in relative.parts:
            continue
        # Checking every ancestor also rejects directory symlink escapes.
        if any(parent.is_symlink() for parent in (path, *path.parents) if parent != root.parent):
            raise PrivacyError("Symlinks are not permitted in publication inputs")
        if path.is_file():
            if not path.resolve().is_relative_to(root):
                raise PrivacyError("File is outside the repository root")
            selected.append(path)
    return selected


def _atomic_write(path: Path, text: str) -> None:
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=".privacy-", delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
            temporary.chmod(path.stat().st_mode & 0o777)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def _public_labels(path: Path) -> tuple[str, str] | None:
    metadata = path.with_name("metadata.json")
    if not metadata.exists():
        return None
    if metadata.is_symlink():
        raise PrivacyError("Metadata symlinks are not permitted")
    try:
        import json
        from catalogue import validate_metadata, render_alias, render_description
        record = validate_metadata(json.loads(metadata.read_text(encoding="utf-8")))
        return render_alias(record), render_description(record)
    except (ImportError, ValueError, TypeError, KeyError, OSError):
        raise PrivacyError("Invalid public catalogue metadata") from None


def check_repository(root: Path, *, fix: bool = False) -> tuple[int, int, set[str]]:
    if root.is_symlink():
        raise PrivacyError("Repository root must not be a symlink")
    root = root.resolve()
    paths = safe_paths(root)
    source: dict[Path, str] = {}
    configurations: dict[Path, dict] = {}
    replacements: dict[Path, str] = {}
    categories: set[str] = set()
    unresolved = 0
    anonymizer = Anonymizer()
    for path in paths:
        relative = path.relative_to(root)
        if FORBIDDEN_FILE.search(relative.as_posix()):
            categories.add("private-input-file")
            unresolved += 1
            continue
        if path.stat().st_size > MAX_FILE_BYTES:
            categories.add("oversized-unreviewed-file")
            unresolved += 1
            continue
        try:
            text = path.read_text(encoding="utf-8")
            if "\0" in text:
                raise UnicodeError
        except (UnicodeError, OSError):
            categories.add("binary-or-unreadable-file")
            unresolved += 1
            continue
        source[path] = text
        if relative.parts[0] == "automations" and path.name in {"automation.yaml", "automation.yml"}:
            try:
                config = load_yaml(text)
                if not isinstance(config, dict):
                    raise PrivacyError("An automation must be a mapping")
                anonymizer.reserve(config)
                configurations[path] = config
            except (PrivacyError, RecursionError):
                categories.add("invalid-automation-yaml")
                unresolved += 1
    for path, text in source.items():
        if path in configurations:
            try:
                public = anonymizer.automation(configurations[path], labels=_public_labels(path))
                replacement = dump_yaml(public)
                # Canonical output drops all comments, including personal prose
                # that a heuristic name detector cannot reliably recognize.
                _, text_categories = sanitize_text(text)
                if replacement != text or text_categories:
                    categories.add("automation-private-value")
                    categories.update(text_categories)
                    replacements[path] = replacement
            except (PrivacyError, ValueError, TypeError, RecursionError):
                categories.add("unsafe-automation-structure")
                unresolved += 1
        else:
            replacement, findings = sanitize_text(text, structured=path.suffix.lower() in {".yaml", ".yml", ".json", ".toml", ".ini", ".cfg", ".md", ".txt"})
            if findings:
                categories.update(findings)
                replacements[path] = replacement
    # Fail atomically: do not apply a subset when unsafe/binary inputs remain.
    if fix and not unresolved:
        for path, text in replacements.items():
            _atomic_write(path, text)
    return len(replacements), unresolved, categories


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--fix", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        changed, unresolved, categories = check_repository(args.root, fix=args.fix)
    except (PrivacyError, OSError, ValueError):
        print("Privacy check could not safely inspect the repository. Input details suppressed.", file=sys.stderr)
        return 2
    if unresolved or (changed and not args.fix):
        print(f"Privacy check failed: {changed} file(s) need sanitization; {unresolved} input(s) need manual review.")
        print("Finding categories: " + ", ".join(sorted(categories)))
        return 1
    print(f"Privacy check passed; {changed} file(s) sanitized." if args.fix else "Privacy check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
