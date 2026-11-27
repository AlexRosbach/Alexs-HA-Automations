"""Synthetic privacy regressions; no real source values belong in fixtures."""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import privacy_guard as guard
from catalogue import write_catalogue


def private_word() -> str:
    return "synthetic" + "_private_label"


class AnonymizerTests(unittest.TestCase):
    def test_custom_services_entity_keys_numeric_secrets_and_variables(self):
        name = private_word()
        raw = {
            "alias": name,
            "id": 123456789,
            "trigger": [{"platform": "state", "entity_id": "sensor." + name}],
            "variables": {name: {"climate." + name: name}},
            "actions": [
                {"action": "notify.mobile_app_" + name, "data": {"message": name}},
                {"action": "script." + name, "data": {"token": 123456789, "latitude": 50.1234}},
                {"action": "light.turn_on", "target": {"entity_id": "light." + name}},
            ],
            "mode": name,
        }
        auto = guard.Anonymizer()
        result = auto.automation(raw)
        self.assertNotIn(name, repr(result))
        self.assertNotIn("123456789", repr(result))
        self.assertNotIn("50.1234", repr(result))
        self.assertNotIn("id", result)
        self.assertEqual(result["actions"][2]["action"], "light.turn_on")
        self.assertEqual(result["trigger"][0]["platform"], "state")
        self.assertEqual(result["actions"][1]["data"]["token"], "REPLACE_WITH_YOUR_OWN_SECRET")
        self.assertEqual(auto.automation(result), result)

    def test_preserves_schema_enums_quantities_and_reference_equivalence(self):
        raw = {
            "triggers": [{"trigger": "state", "entity_id": "binary_sensor." + private_word(), "to": "on"}],
            "conditions": [{"condition": "state", "entity_id": "binary_sensor." + private_word(), "state": "on"}],
            "actions": [{"delay": {"seconds": 12}}, {"action": "light.turn_on", "data": {"brightness_pct": 65}}],
            "mode": "restart", "enabled": False,
        }
        result = guard.Anonymizer().automation(raw)
        self.assertEqual(result["triggers"][0]["entity_id"], result["conditions"][0]["entity_id"])
        self.assertEqual(result["triggers"][0]["to"], "on")
        self.assertEqual(result["actions"][0]["delay"]["seconds"], 12)
        self.assertEqual(result["actions"][1]["data"]["brightness_pct"], 65)
        self.assertEqual(result["mode"], "restart")
        self.assertIs(result["enabled"], False)

    def test_placeholder_vocabulary_does_not_allow_private_names(self):
        raw = {"target": {"entity_id": private_word().upper() + "_01"}, "action": private_word() + ".example_01"}
        result = guard.Anonymizer().value(raw)
        self.assertNotIn(private_word(), repr(result).lower())
        self.assertNotEqual(result["target"]["entity_id"], raw["target"]["entity_id"])

    def test_reserved_placeholders_do_not_collide(self):
        auto = guard.Anonymizer()
        auto.reserve({"entity_id": "light.example_01", "variables": {"variable_01": 1}})
        self.assertEqual(auto.entity("light." + private_word()), "light.example_02")
        self.assertEqual(auto.placeholder("variable", private_word()), "variable_02")
        self.assertEqual(auto.entity("light." + private_word()), "light.example_02")

    def test_secret_tags_preserved_with_neutral_names(self):
        raw = guard.load_yaml("token: !secret " + private_word() + "\n")
        result = guard.Anonymizer().value(raw)
        self.assertIsInstance(result["token"], guard.SecretReference)
        rendered = guard.dump_yaml(result)
        self.assertIn("!secret", rendered)
        self.assertNotIn(private_word(), rendered)
        self.assertEqual(guard.load_yaml(rendered), result)
        self.assertEqual(guard.Anonymizer().value(result), result)

    def test_invalid_tags_duplicates_cycles_fail_without_values(self):
        for text in ["value: !include " + private_word(), "mode: single\nmode: restart\n"]:
            with self.assertRaises(guard.PrivacyError) as caught:
                guard.load_yaml(text)
            self.assertNotIn(private_word(), str(caught.exception))
        cycle = []; cycle.append(cycle)
        with self.assertRaises(guard.PrivacyError):
            guard.Anonymizer().value(cycle)


class TextGuardTests(unittest.TestCase):
    def test_high_confidence_identifiers_and_weak_credentials(self):
        address = ".".join(("10", "42", "23", "7"))
        email = private_word() + "@" + "private" + ".invalid"
        ipv6 = ":".join(("fd42", "abcd", "1234", "", "5"))
        original = "\n".join(["password: " + private_word(), "chat_id: " + str(123456789), address, email, ipv6])
        public, findings = guard.sanitize_text(original)
        self.assertNotIn(private_word(), public)
        self.assertNotIn(address, public)
        self.assertNotIn(email, public)
        self.assertNotIn(ipv6, public)
        self.assertGreaterEqual(len(findings), 3)
        self.assertFalse(guard.sanitize_text(public)[1])

    def test_provider_tokens_and_private_keys_are_removed(self):
        token = "gh" + "p_" + "a" * 36
        key = "-" * 5 + "BEGIN PRIVATE KEY" + "-" * 5 + "\n" + private_word() + "\n" + "-" * 5 + "END PRIVATE KEY" + "-" * 5
        rendered, found = guard.sanitize_text(token + "\n" + key)
        self.assertNotIn(token, rendered)
        self.assertNotIn(private_word(), rendered)
        self.assertEqual(found, {"provider-token", "private-key"})

    def test_public_documentation_and_code_expressions_are_not_corrupted(self):
        text = "https://developers.home-assistant.io/\nhttps://github.com/actions/checkout\nhttps://example.invalid\n192.0.2.1\n2001:db8::1\n"
        self.assertEqual(guard.sanitize_text(text), (text, set()))
        code = "original = 'password: ' + 'test-' + 'private-value\\n'\n"
        self.assertEqual(guard.sanitize_text(code, structured=False), (code, set()))
        self.assertEqual(guard.sanitize_text("token: ${{ secrets.GITHUB_TOKEN }}\n")[1], set())


class RepositoryGuardTests(unittest.TestCase):
    def test_generated_labels_preserved_comments_removed_and_fix_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = {"triggers": [{"trigger": "state", "entity_id": "sensor.example_01"}], "actions": [{"action": "light.turn_on"}], "mode": "single"}
            write_catalogue(root, [{"config": raw, "trigger_types": ["state"]}])
            path = next(root.rglob("automation.yaml"))
            alias = guard.load_yaml(path.read_text())["alias"]
            path.write_text(path.read_text() + "# " + private_word() + "\n")
            self.assertEqual(guard.check_repository(root)[0], 1)
            self.assertEqual(guard.check_repository(root, fix=True)[:2], (1, 0))
            self.assertEqual(guard.load_yaml(path.read_text())["alias"], alias)
            self.assertNotIn(private_word(), path.read_text())
            self.assertEqual(guard.check_repository(root)[:2], (0, 0))

    def test_unknown_private_files_prevent_partial_fix(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bad = "password: " + private_word() + "\n"
            (root / "sample.yaml").write_text(bad)
            (root / "secrets.yaml").write_text(bad)
            changed, unresolved, categories = guard.check_repository(root, fix=True)
            self.assertEqual((changed, unresolved), (1, 1))
            self.assertIn("private-input-file", categories)
            self.assertEqual((root / "sample.yaml").read_text(), bad)

    def test_symlink_and_binary_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"; root.mkdir()
            private = Path(directory) / "private.txt"; private.write_text(private_word())
            (root / "shortcut.md").symlink_to(private)
            with self.assertRaises(guard.PrivacyError):
                guard.check_repository(root, fix=True)
            (root / "shortcut.md").unlink()
            (root / "image.bin").write_bytes(b"\x00\xff")
            self.assertEqual(guard.check_repository(root, fix=True)[1], 1)

    def test_nested_snapshot_is_not_hidden_by_parent_gitignore(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".gitignore").write_text("snapshot/\n")
            snapshot = root / "snapshot"; snapshot.mkdir()
            (snapshot / "sample.yaml").write_text("password: " + private_word() + "\n")
            self.assertEqual(guard.check_repository(snapshot)[0], 1)

    def test_tracked_dependency_named_directory_is_not_exempt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            target = root / "node_modules"; target.mkdir()
            (target / "sample.yaml").write_text("password: " + private_word() + "\n")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            self.assertEqual(guard.check_repository(root)[0], 1)


if __name__ == "__main__":
    unittest.main()
