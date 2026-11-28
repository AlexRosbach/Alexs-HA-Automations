from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import publish_automations as publisher
from privacy_guard import PrivacyError, check_repository, load_yaml


def example_export() -> list[dict]:
    name = "synthetic" + "_private_label"
    return [{"config": {
        "alias": name,
        "id": 123456789,
        "triggers": [{"trigger": "state", "entity_id": "binary_sensor." + name, "to": "on"}],
        "actions": [{"action": "light.turn_on", "target": {"entity_id": "light." + name}}],
        "mode": "single",
    }}]


def snapshot(root: Path) -> dict[Path, bytes]:
    return {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}


class PublisherTests(unittest.TestCase):
    def test_door_control_excluded_before_anonymization_and_checked_after(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"
            records = example_export()
            records += [{"config": {"actions": [{"action": "script.open_front_door"}]}}]
            source.write_text(json.dumps(records))
            output = parent / "public"
            self.assertEqual(publisher.publish(source, output), 1)
            self.assertEqual(len(list(output.rglob("automation.yaml"))), 1)
            before = snapshot(output)
            source.write_text(json.dumps(records[1:]))
            with self.assertRaises(PrivacyError):
                publisher.publish(source, output)
            self.assertEqual(snapshot(output), before)

    def test_cover_that_becomes_ambiguous_after_redaction_is_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"
            records = example_export() + [{"config": {
                "alias": "Window blind control",
                "actions": [{"action": "cover.close_cover", "target": {"device_id": "private-device"}}],
            }}]
            source.write_text(json.dumps(records))
            output = parent / "public"
            self.assertEqual(publisher.publish(source, output), 1)
            self.assertEqual(len(list(output.rglob("automation.yaml"))), 1)

    def test_message_preserved_with_external_private_name_list(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            name = "synthetic" + "person"
            source = parent / "private-input.json"
            source.write_text(json.dumps([{"config": {"triggers": [{"trigger": "time", "at": "18:30:00"}],
                "actions": [{"action": "notify.mobile_app_phone", "data": {"message": name + ", the laundry is finished."}}]}}]))
            names = parent / "private-names.txt"; names.write_text(name + "\n")
            output = parent / "public"
            self.assertEqual(publisher.publish(source, output, names), 1)
            config = load_yaml(next(output.rglob("automation.yaml")).read_text())
            self.assertIn("the laundry is finished", config["actions"][0]["data"]["message"])
            self.assertNotIn(name, repr(config))
            self.assertEqual(config["triggers"][0]["at"], "18:30:00")
            self.assertFalse((output / names.name).exists())

    def test_external_export_creates_named_catalogue_and_is_repeatable(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"
            source.write_text(json.dumps(example_export()))
            output = parent / "public"
            self.assertEqual(publisher.publish(source, output), 1)
            paths = list(output.rglob("automation.yaml"))
            self.assertEqual(len(paths), 1)
            self.assertIn("lighting", paths[0].parts)
            self.assertNotIn("automation-001", str(paths[0]))
            config = load_yaml(paths[0].read_text())
            self.assertEqual(config["triggers"][0]["trigger"], "state")
            self.assertNotIn("synthetic" + "_private_label", paths[0].read_text())
            self.assertEqual({path.name for path in paths[0].parent.iterdir()}, publisher.MANAGED_FILES)
            for name in publisher.ROOT_READMES:
                readme = output / name
                self.assertTrue(readme.is_file())
                readme.write_text(readme.read_text().replace("<!-- catalogue:start -->", "Custom introductory text.\n\n<!-- catalogue:start -->"))
            before = snapshot(output)
            self.assertEqual(publisher.publish(source, output), 1)
            self.assertEqual(before, snapshot(output))
            self.assertEqual(check_repository(output)[:2], (0, 0))

    def test_existing_single_language_catalogue_migrates_without_losing_examples(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"; source.write_text(json.dumps(example_export()))
            output = parent / "public"
            publisher.publish(source, output)
            bilingual = snapshot(output)
            for readme in output.rglob("README.de.md"):
                readme.unlink()
            self.assertEqual(publisher.publish(source, output), 1)
            self.assertEqual(bilingual, snapshot(output))

    def test_invalid_input_does_not_destroy_existing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"
            source.write_text(json.dumps(example_export()))
            output = parent / "public"
            publisher.publish(source, output)
            path = next(output.rglob("automation.yaml"))
            previous = path.read_bytes()
            source.write_text("invalid" + " private source")
            with self.assertRaises(PrivacyError):
                publisher.publish(source, output)
            self.assertEqual(path.read_bytes(), previous)

    def test_unmanaged_output_source_inside_repo_and_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"
            source.write_text(json.dumps(example_export()))
            output = parent / "public"
            unrelated = output / "automations" / "unmanaged"
            unrelated.mkdir(parents=True)
            sentinel = unrelated / "README.md"; sentinel.write_text("keep this document")
            with self.assertRaises(PrivacyError):
                publisher.publish(source, output)
            self.assertEqual(sentinel.read_text(), "keep this document")
            repo = parent / "repo"; repo.mkdir()
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            private = repo / "private-input.json"; private.write_bytes(source.read_bytes())
            with self.assertRaises(PrivacyError):
                publisher.publish(private, repo)
            link = parent / "input-link.json"; link.symlink_to(source)
            with self.assertRaises(PrivacyError):
                publisher.publish(link, parent / "other-output")
            linked_output = parent / "linked-output"; linked_output.mkdir()
            readme_link = linked_output / "README.de.md"; readme_link.symlink_to(sentinel)
            with self.assertRaises(PrivacyError):
                publisher.publish(source, linked_output)
            self.assertTrue(readme_link.is_symlink())
            self.assertEqual(sentinel.read_text(), "keep this document")

    def test_validation_failure_does_not_replace_catalogue(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"; source.write_text(json.dumps(example_export()))
            output = parent / "public"
            publisher.publish(source, output)
            path = next(output.rglob("automation.yaml"))
            before = path.read_bytes()
            with patch.object(publisher, "check_repository", return_value=(1, 0, {"synthetic"})):
                with self.assertRaises(PrivacyError):
                    publisher.publish(source, output)
            self.assertEqual(path.read_bytes(), before)

    def test_rename_failure_restores_all_catalogue_files(self):
        for existing_output in (False, True):
            for component in ("automations", *publisher.ROOT_READMES):
                with self.subTest(existing_output=existing_output, component=component), tempfile.TemporaryDirectory() as directory:
                    parent = Path(directory)
                    source = parent / "private-input.json"; source.write_text(json.dumps(example_export()))
                    output = parent / "public"
                    if existing_output:
                        publisher.publish(source, output)
                    before = snapshot(output)
                    source.write_text(json.dumps(example_export() * 2))
                    actual_replace = publisher.os.replace
                    def fail_candidate(src, dst):
                        if Path(src).parent.name == "candidate" and Path(src).name == component:
                            raise OSError("synthetic promotion failure")
                        actual_replace(src, dst)
                    with patch.object(publisher.os, "replace", side_effect=fail_candidate):
                        with self.assertRaises(PrivacyError):
                            publisher.publish(source, output)
                    self.assertEqual(snapshot(output), before)
                    self.assertEqual(list(parent.glob(".ha-publication-backup-*")), [])


if __name__ == "__main__":
    unittest.main()
