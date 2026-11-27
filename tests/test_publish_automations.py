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


class PublisherTests(unittest.TestCase):
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
            before = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
            self.assertEqual(publisher.publish(source, output), 1)
            after = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
            self.assertEqual(before, after)
            self.assertEqual(check_repository(output)[:2], (0, 0))

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

    def test_rename_failure_restores_previous_catalogue(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            source = parent / "private-input.json"; source.write_text(json.dumps(example_export()))
            output = parent / "public"
            publisher.publish(source, output)
            path = next(output.rglob("automation.yaml"))
            before = path.read_bytes()
            actual_replace = publisher.os.replace
            def fail_candidate(src, dst):
                if Path(src).parent.name == "candidate" and Path(src).name == "automations":
                    raise OSError("synthetic promotion failure")
                actual_replace(src, dst)
            with patch.object(publisher.os, "replace", side_effect=fail_candidate):
                with self.assertRaises(PrivacyError):
                    publisher.publish(source, output)
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
