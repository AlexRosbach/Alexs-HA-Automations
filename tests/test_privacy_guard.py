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

    def test_unknown_fields_and_local_attachment_paths_are_redacted_idempotently(self):
        name = private_word()
        source = {
            "actions": [{
                "data": {
                    name: "private free text",
                    "filename": "/config/www/" + name + ".jpg",
                    "url": "/local/" + name + ".jpg",
                },
            }],
        }
        result = guard.Anonymizer().automation(source)
        data = result["actions"][0]["data"]
        self.assertNotIn(name, repr(result))
        self.assertEqual(data["filename"], "REPLACE_WITH_YOUR_OWN_VALUE")
        self.assertEqual(data["url"], "REPLACE_WITH_YOUR_OWN_VALUE")
        self.assertIn("REPLACE_WITH_YOUR_OWN_TEXT", data.values())
        self.assertEqual(guard.Anonymizer().automation(result), result)

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
        auto.reserve({"entity_id": ["light.example_01", "light.lamp"], "variables": {"variable_01": 1}})
        self.assertEqual(auto.entity("light." + private_word()), "light.example_02")
        self.assertEqual(auto.placeholder("variable", private_word()), "variable_02")
        self.assertEqual(auto.entity("light." + private_word()), "light.example_02")

    def test_retains_readable_entities_messages_schedule_and_template_logic(self):
        config = {
            "triggers": [{"trigger": "time", "at": "18:30:00"}],
            "conditions": [{"condition": "template", "value_template": "{{ states('sensor.laundry_power') | float(0) < 5 }}"}],
            "actions": [{"action": "notify.mobile_app_phone", "data": {"message": "The laundry is finished. You can empty the washing machine.", "title": "Laundry finished"}},
                        {"action": "light.turn_on", "target": {"entity_id": "light.kitchen_ceiling"}}],
            "mode": "single",
        }
        result = guard.Anonymizer().automation(config)
        self.assertEqual(result["triggers"], config["triggers"])
        self.assertEqual(result["mode"], config["mode"])
        self.assertEqual(result["conditions"][0]["value_template"], "{{ states('sensor.example_01') | float(0) < 5 }}")
        self.assertEqual(result["actions"][1]["target"]["entity_id"], "light.example_01")
        self.assertEqual(result["actions"][0]["data"]["message"], config["actions"][0]["data"]["message"])
        self.assertTrue(guard.is_public_text(config["actions"][0]["data"]["message"]))

    def test_private_entity_parts_and_phone_models_removed_without_losing_message(self):
        name = "syntheticperson"
        model = "fold" + "_8"
        entity = "sensor." + name + "_" + model + "_battery"
        config = {
            "triggers": [{"trigger": "numeric_state", "entity_id": entity, "below": 20}],
            "conditions": [{"condition": "template", "value_template": "{{ states('" + entity + "') | float(0) < 20 }}"}],
            "actions": [{"action": "notify.mobile_app_" + name + "_" + model, "data": {"message": name + ", the " + model + " battery is low. Please charge it."}}],
        }
        result = guard.Anonymizer().automation(config)
        rendered = repr(result)
        self.assertNotIn(name, rendered)
        self.assertNotIn(model, rendered)
        self.assertIn("battery is low. Please charge it.", rendered)
        public_entity = result["triggers"][0]["entity_id"]
        self.assertTrue(guard.is_public_entity(public_entity))
        self.assertIn(public_entity, result["conditions"][0]["value_template"])
        self.assertEqual(guard.Anonymizer().automation(result), result)

    def test_variable_references_and_private_recipient_remain_consistent(self):
        name = private_word()
        source = {"variables": {name: 5}, "actions": [{"action": "notify.notify", "data": {
            "message": "Reading: {{ " + name + " }}", "target": 123456789,
        }}]}
        result = guard.Anonymizer().automation(source)
        variable = next(iter(result["variables"]))
        self.assertEqual(result["variables"][variable], 5)
        self.assertIn(variable, result["actions"][0]["data"]["message"])
        self.assertNotIn(name, repr(result))
        self.assertNotIn("123456789", repr(result))
        self.assertEqual(guard.Anonymizer().automation(result), result)

    def test_explicit_private_terms_and_credentials_are_redacted_in_normal_text(self):
        name = private_word()
        token = "gh" + "p_" + "a" * 36
        message = "Hi " + name + ", cleaning is finished. " + token
        result = guard.Anonymizer(private_terms=(name,)).value({"message": message})
        self.assertIn("cleaning is finished", result["message"])
        self.assertNotIn(name, result["message"])
        self.assertNotIn(token, result["message"])
        self.assertTrue(guard.is_public_text(result["message"]))

    def test_dotted_template_entities_use_the_same_anonymous_reference(self):
        private_entity = "sensor." + private_word() + "_power"
        expression = "{{ states." + private_entity + ".state | float(0) > 5 }}"
        self.assertFalse(guard.is_public_text(expression))
        source = {
            "triggers": [{"trigger": "state", "entity_id": private_entity}],
            "conditions": [{"condition": "template", "value_template": expression}],
            "actions": [{"action": "notify.notify", "data": {"message": "{{ states('" + private_entity + "') }}"}}],
        }
        result = guard.Anonymizer().automation(source)
        public_entity = result["triggers"][0]["entity_id"]
        self.assertNotEqual(public_entity, private_entity)
        self.assertEqual(result["conditions"][0]["value_template"], "{{ states." + public_entity + ".state | float(0) > 5 }}")
        self.assertEqual(result["actions"][0]["data"]["message"], "{{ states('" + public_entity + "') }}")
        only_expression = guard.Anonymizer().value({"value_template": expression})
        self.assertNotIn(private_word(), only_expression["value_template"])
        self.assertIn(".state | float(0) > 5", only_expression["value_template"])
        self.assertEqual(guard.Anonymizer().automation(result), result)

    def test_device_and_area_ids_are_replaced_in_literals_before_their_declarations(self):
        device, area = private_word() + "_device", private_word() + "_area"
        expression = "{{ device_attr('" + device + "', 'name') and area_name('" + area + "') }}"
        source = {
            "conditions": [{"condition": "template", "value_template": expression}],
            "actions": [{"domain": "light", "type": "turn_on", "device_id": device},
                        {"action": "light.turn_on", "target": {"area_id": area}}],
        }
        result = guard.Anonymizer().automation(source)
        public_device = result["actions"][0]["device_id"]
        public_area = result["actions"][1]["target"]["area_id"]
        self.assertNotEqual(public_device, device)
        self.assertNotEqual(public_area, area)
        self.assertEqual(result["conditions"][0]["value_template"],
                         "{{ device_attr('" + public_device + "', 'name') and area_name('" + public_area + "') }}")
        self.assertNotIn(private_word(), repr(result))

    def test_person_names_do_not_leak_or_change_jinja_filters(self):
        source = {
            "triggers": [{"trigger": "state", "entity_id": "person.max"}],
            "conditions": [{"condition": "template", "value_template": "{{ [1, 5] | max == 5 }}"}],
            "actions": [{"action": "notify.notify", "data": {
                "message": "Hi Max, {{ [1, 5] | max }}; {{ 'Max can check the laundry' }}; {{ states('sensor.max') }}",
            }}],
        }
        result = guard.Anonymizer().automation(source)
        self.assertEqual(result["triggers"][0]["entity_id"], "person.example_01")
        self.assertEqual(result["conditions"], source["conditions"])
        message = result["actions"][0]["data"]["message"]
        self.assertIn("Hi person, {{ [1, 5] | max }}", message)
        self.assertIn("{{ 'person can check the laundry' }}", message)
        self.assertIn("{{ states('sensor.example_01') }}", message)
        self.assertNotIn("person.max", repr(result))
        self.assertEqual(guard.Anonymizer().automation(result), result)

    def test_public_entities_in_formulas_are_reserved_against_name_collisions(self):
        private_entity = "sensor." + private_word()
        source = {
            "triggers": [{"trigger": "state", "entity_id": private_entity}],
            "conditions": [{"condition": "template", "value_template": "{{ states('sensor.value') != states.sensor.value_02.state }}"}],
            "actions": [{"action": "notify.notify", "data": {"message": "{{ states('" + private_entity + "') }}"}}],
        }
        result = guard.Anonymizer().automation(source)
        public_entity = result["triggers"][0]["entity_id"]
        self.assertEqual(public_entity, "sensor.example_01")
        self.assertEqual(result["conditions"][0]["value_template"], "{{ states('sensor.example_02') != states.sensor.example_03.state }}")
        self.assertIn(public_entity, result["actions"][0]["data"]["message"])

    def test_private_custom_service_cannot_become_a_different_builtin_action(self):
        custom = "script." + private_word() + "_turn_on"
        source = {"actions": [{"action": custom}, {"action": "script.turn_on", "target": {"entity_id": custom}}]}
        result = guard.Anonymizer().automation(source)
        public_custom = result["actions"][0]["action"]
        self.assertNotIn(public_custom, guard.PUBLIC_SERVICES)
        self.assertEqual(result["actions"][1]["action"], "script.turn_on")
        self.assertEqual(result["actions"][1]["target"]["entity_id"], public_custom)
        self.assertTrue(guard.is_public_entity(public_custom))

    def test_safe_string_variables_keep_their_values_and_numeric_private_names_do_not(self):
        private_variable = "phone_" + "01632" + "960123"
        source = {
            "variables": {"laundry_message": "Laundry finished", private_variable: 1},
            "actions": [{"action": "notify.notify", "data": {"message": "{{ laundry_message }}: {{ " + private_variable + " }}"}}],
        }
        result = guard.Anonymizer().automation(source)
        self.assertEqual(result["variables"]["laundry_message"], "Laundry finished")
        public_variable = next(name for name in result["variables"] if name != "laundry_message")
        self.assertNotEqual(public_variable, private_variable)
        self.assertEqual(result["variables"][public_variable], 1)
        self.assertEqual(result["actions"][0]["data"]["message"], "{{ laundry_message }}: {{ " + public_variable + " }}")
        self.assertNotIn(private_variable, repr(result))
        self.assertEqual(guard.Anonymizer().automation(result), result)

    def test_batch_reservation_avoids_later_id_and_variable_placeholder_collisions(self):
        first = {
            "variables": {private_word(): 1},
            "triggers": [{"trigger": "state", "entity_id": "sensor.power", "id": private_word()}],
            "actions": [{"if": [{"condition": "trigger", "id": private_word()}], "then": []}],
        }
        second = {
            "variables": {"variable_01": 2},
            "triggers": [{"trigger": "state", "entity_id": "sensor.temperature", "id": "IDENTIFIER_01"}],
            "actions": [],
        }
        auto = guard.Anonymizer()
        auto.reserve(first)
        auto.reserve(second)
        public_first, public_second = auto.automation(first), auto.automation(second)
        first_id = public_first["triggers"][0]["id"]
        second_id = public_second["triggers"][0]["id"]
        self.assertNotEqual(first_id, second_id)
        self.assertEqual(second_id, "IDENTIFIER_01")
        self.assertEqual(public_first["actions"][0]["if"][0]["id"], first_id)
        self.assertEqual(public_second["variables"], {"variable_01": 2})
        self.assertNotIn("variable_01", public_first["variables"])
        combined = guard.Anonymizer().automation({"variables": {private_word(): 1, "variable_01": 2}, "actions": []})
        self.assertEqual(set(combined["variables"].values()), {1, 2})

    def test_template_literal_delimiters_and_escaped_quotes_are_preserved(self):
        expression = "{{ 'literal }} text' ~ 'it\\'s finished' }}"
        self.assertEqual(guard.Anonymizer().value({"message": expression})["message"], expression)

    def test_renamed_variables_do_not_rename_filters_tests_or_attributes(self):
        source = {
            "variables": {"sum": 2, "synthetic_private": 3},
            "conditions": [
                {"condition": "template", "value_template": "{{ sum + ([1, 2] | sum) + trigger.synthetic_private + synthetic_private }}"},
                {"condition": "template", "value_template": "{{ value is synthetic_private or value is not synthetic_private or trigger . synthetic_private == synthetic_private }}"},
            ],
        }
        result = guard.Anonymizer().automation(source)
        renamed = {value: name for name, value in result["variables"].items()}
        self.assertNotEqual(renamed[2], "sum")
        self.assertNotEqual(renamed[3], "synthetic_private")
        self.assertEqual(result["conditions"][0]["value_template"],
                         "{{ " + renamed[2] + " + ([1, 2] | sum) + trigger.synthetic_private + " + renamed[3] + " }}")
        self.assertEqual(result["conditions"][1]["value_template"],
                         "{{ value is synthetic_private or value is not synthetic_private or trigger . synthetic_private == " + renamed[3] + " }}")

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
    def test_local_phone_numbers_are_removed_without_changing_dates_or_measurements(self):
        number = "01632" + " 960123"
        international = "+44 " + "1632 960123"
        original = "Call " + number + " or " + international + " after the laundry finishes."
        public, findings = guard.sanitize_text(original)
        self.assertNotIn(number, public)
        self.assertNotIn(international, public)
        self.assertIn("after the laundry finishes", public)
        self.assertIn("phone-number", findings)
        safe = "Date 01-02-2026; time 01:02:03; value 0.123456789; sensor.temperature_123"
        self.assertEqual(guard.sanitize_text(safe), (safe, set()))

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
