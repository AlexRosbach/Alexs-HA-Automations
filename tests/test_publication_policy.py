"""Door-control exclusion, source inspection and safe whole-example removal."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import publication_policy as policy
from catalogue import build_metadata, render_alias, render_description
from privacy_guard import Anonymizer, dump_yaml


def example(action: str, entity: str) -> dict:
    return {
        "triggers": [{"trigger": "state", "entity_id": "binary_sensor.example_01", "to": "on"}],
        "conditions": [],
        "actions": [{"action": action, "target": {"entity_id": entity}}],
        "mode": "single",
    }


def managed_example(root: Path, config: dict) -> Path:
    config = copy.deepcopy(config)
    metadata = build_metadata(config)
    folder = root / "automations" / metadata["category"] / metadata["slug"]
    folder.mkdir(parents=True)
    config["alias"] = render_alias(metadata)
    config["description"] = render_description(metadata)
    (folder / "automation.yaml").write_text(dump_yaml(config))
    (folder / "metadata.json").write_text(json.dumps(metadata))
    (folder / "README.md").write_text("An example.\n")
    (folder / "README.de.md").write_text("Ein Beispiel.\n")
    return folder


def snapshot(root: Path) -> dict[Path, bytes]:
    return {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file() and not path.is_symlink()}


class PublicationPolicyTests(unittest.TestCase):
    def test_nested_lock_and_device_actions_are_blocked(self) -> None:
        for action in [
            {"action": "lock.unlock", "target": {"entity_id": "lock.example_01"}},
            {"domain": "lock", "type": "open", "device_id": "DEVICE_01"},
            {"action": "homeassistant.turn_on", "target": {"entity_id": "lock.example_01"}},
        ]:
            config = {"actions": [{"choose": [{"conditions": [], "sequence": [{"if": [], "then": [{"parallel": [{"sequence": [action]}]}]}]}]}]}
            with self.subTest(action=action):
                self.assertIn("lock-control", policy.forbidden_reasons(config))

    def test_door_contact_triggers_and_waits_do_not_ban_lighting_or_notifications(self) -> None:
        config = {
            "alias": "Front door contact notification and entrance light",
            "triggers": [{"trigger": "state", "entity_id": "binary_sensor.front_door", "to": "on"}],
            "conditions": [{"condition": "state", "entity_id": "lock.front_door", "state": "unlocked"}],
            "actions": [
                {"action": "light.turn_on", "target": {"entity_id": "light.front_door"}},
                {"wait_for_trigger": [{"trigger": "state", "entity_id": "lock.front_door"}]},
                {"action": "notify.send_message", "data": {"message": "The door opened"}},
            ],
        }
        self.assertEqual(policy.forbidden_reasons(config), set())

    def test_named_custom_door_controls_are_found_before_anonymization(self) -> None:
        for service in ("script.open_front_door", "script.HaustuerOeffnen", "rest_command.open_gate", "esphome.garage_unlock"):
            with self.subTest(service=service):
                self.assertIn("door-control", policy.forbidden_reasons({"actions": [{"action": service}]}))
        cases = [
            {"actions": [{"action": "switch.turn_on", "target": {"entity_id": "switch.garagentor"}}]},
            {"actions": [{"action": "button.press", "alias": "Tür öffnen", "target": {"entity_id": "button.example_01"}}]},
            {"actions": [{"action": "remote.send_command", "data": {"command": "open_garage_door"}}]},
            {"actions": [{"action": "script.turn_on", "target": {"entity_id": "script.gate_opener"}}]},
        ]
        for config in cases:
            self.assertIn("door-control", policy.forbidden_reasons(config))

    def test_keywords_are_words_not_fragments_and_neutral_covers_are_distinguished(self) -> None:
        self.assertEqual(policy.forbidden_reasons(example("switch.turn_on", "switch.outdoor_lights")), set())
        self.assertEqual(policy.forbidden_reasons(example("button.press", "button.doorbell_chime")), set())
        self.assertEqual(policy.forbidden_reasons(example("cover.close_cover", "cover.window_blind")), set())
        self.assertIn("unreviewed-cover-control", policy.forbidden_reasons(example("cover.close_cover", "cover.example_01")))
        garage = example("cover.close_cover", "cover.garage_door")
        garage["alias"] = "Roller shutter control"
        self.assertIn("door-control", policy.forbidden_reasons(garage))

    def test_lock_and_unknown_cover_stay_blocked_after_anonymization(self) -> None:
        for config in [example("lock.open", "lock.front_door"), example("cover.close_cover", "cover.example_01")]:
            anonymizer = Anonymizer()
            anonymizer.reserve(config)
            self.assertTrue(policy.forbidden_reasons(anonymizer.automation(config)))
        source = {"actions": [{"action": "script.open_front_door"}]}
        self.assertIn("door-control", policy.forbidden_reasons(source))

    def test_cover_control_becomes_ambiguous_after_full_entity_redaction(self) -> None:
        source = example("cover.close_cover", "cover.synthetic_private_label")
        source["alias"] = "Window blind control"
        anonymizer = Anonymizer()
        anonymizer.reserve(source)
        published = anonymizer.automation(source)
        self.assertEqual(published["actions"][0]["target"]["entity_id"], "cover.example_01")
        self.assertIn("unreviewed-cover-control", policy.forbidden_reasons(published))

    def test_blueprint_actuator_inputs_are_inspected(self) -> None:
        self.assertIn("lock-control", policy.forbidden_reasons({"use_blueprint": {"input": {"target": "lock.example_01"}}}))
        self.assertIn("door-control", policy.forbidden_reasons({"use_blueprint": {"input": {"door_opener": "button.example_01"}}}))
        self.assertEqual(policy.forbidden_reasons({"use_blueprint": {"input": {"door_contact": "binary_sensor.example_01", "light_target": "light.example_01"}}}), set())

    def test_fix_removes_whole_mixed_example_and_preserves_allowed_ones(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            mixed = example("lock.open", "lock.example_01")
            mixed["actions"].append({"action": "light.turn_on", "target": {"entity_id": "light.example_01"}})
            forbidden = managed_example(root, mixed)
            allowed = managed_example(root, example("light.turn_off", "light.example_02"))
            before = snapshot(allowed)
            result = policy.policy_check(root)
            self.assertEqual((result.checked, result.blocked, result.removed), (2, 1, 0))
            self.assertTrue(forbidden.is_dir())
            fixed = policy.policy_check(root, fix=True)
            self.assertEqual(fixed.removed, 1)
            self.assertFalse(forbidden.exists())
            self.assertEqual(snapshot(allowed), before)
            self.assertEqual(policy.policy_check(root).blocked, 0)

    def test_invalid_later_example_prevents_any_removal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            managed_example(root, example("lock.open", "lock.example_01"))
            invalid = managed_example(root, example("light.turn_on", "light.example_01"))
            (invalid / "automation.yaml").write_text("actions: [invalid\n")
            before = snapshot(root)
            with self.assertRaises(policy.PolicyError):
                policy.policy_check(root, fix=True)
            self.assertEqual(snapshot(root), before)

    def test_unmanaged_files_and_symlinks_prevent_removal(self) -> None:
        for kind in ("extra-file", "symlink"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as directory:
                root = Path(directory) / "repo"
                folder = managed_example(root, example("lock.open", "lock.example_01"))
                if kind == "extra-file":
                    (folder / "personal-notes.txt").write_text("Keep this file")
                else:
                    outside = root.parent / "outside.txt"
                    outside.write_text("Keep this file")
                    (folder / "README.de.md").unlink()
                    (folder / "README.de.md").symlink_to(outside)
                before = snapshot(root)
                with self.assertRaises(policy.PolicyError):
                    policy.policy_check(root, fix=True)
                self.assertTrue(folder.is_dir())
                self.assertEqual(snapshot(root), before)

    def test_partial_move_failure_restores_every_example(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            managed_example(root, example("lock.open", "lock.example_01"))
            second = managed_example(root, example("lock.unlock", "lock.example_02"))
            before = snapshot(root)
            actual_replace = policy.os.replace
            def fail_second(source, destination):
                if Path(source) == second:
                    raise OSError("Synthetic move failure")
                actual_replace(source, destination)
            with patch.object(policy.os, "replace", side_effect=fail_second):
                with self.assertRaises(policy.PolicyError):
                    policy.policy_check(root, fix=True)
            self.assertEqual(snapshot(root), before)
            self.assertEqual(list(root.parent.glob(".ha-policy-removal-*")), [])

    def test_all_excluded_examples_can_leave_an_empty_clean_catalogue(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            managed_example(root, example("lock.open", "lock.example_01"))
            self.assertEqual(policy.policy_check(root, fix=True).removed, 1)
            self.assertEqual(policy.policy_check(root).checked, 0)

    def test_cli_reports_only_counts_and_fixed_categories(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = managed_example(root, example("lock.open", "lock.example_01"))
            path = folder / "automation.yaml"
            private_label = "synthetic_private_label"
            path.write_text(path.read_text() + f"private_note: {private_label}\n")
            command = [sys.executable, str(Path(policy.__file__)), "--check", "--root", str(root)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("lock-control: 1", result.stdout)
            self.assertNotIn(private_label, result.stdout + result.stderr)
            self.assertNotIn(str(root), result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
