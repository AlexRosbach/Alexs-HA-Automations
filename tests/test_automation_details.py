from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from automation_details import render_details, summarize

MISSING = "REPLACE_WITH_YOUR_OWN_TEXT"


def switch_cycle() -> dict:
    return {
        "triggers": [{"trigger": MISSING, "entity_id": "sensor.example_01", "above": 10}],
        "conditions": [],
        "actions": [
            {"action": "switch.turn_on", "target": {"entity_id": "switch.example_01"}},
            {"wait_for_trigger": [{"trigger": MISSING, "entity_id": "sensor.example_01", "below": 5}], "timeout": {"minutes": 60}},
            {"action": "switch.turn_off", "target": {"entity_id": "switch.example_01"}},
        ],
        "mode": "restart",
    }


class AutomationDetailsTests(unittest.TestCase):
    def test_retained_thresholds_wait_and_order_without_inventing_trigger_type(self):
        config = switch_cycle()
        original = copy.deepcopy(config)
        for language, on, wait, off, missing in (
            ("en", "Turn on a switch", "Wait for one", "Turn off a switch", "Trigger type missing"),
            ("de", "Einen Schalter einschalten", "Auf einen dieser", "Einen Schalter ausschalten", "Auslösertyp nicht erhalten"),
        ):
            with self.subTest(language=language):
                detail = render_details(config, language)
                summary = summarize(config, language=language)
                self.assertLess(detail.index(on), detail.index(wait))
                self.assertLess(detail.index(wait), detail.index(off))
                self.assertIn("60 min", detail)
                self.assertIn("10", summary)
                self.assertIn("5", summary)
                self.assertIn("60 min", summary)
                self.assertIn(missing, detail)
                self.assertNotIn(missing, summary)
                self.assertTrue(summary.startswith(on))
                self.assertEqual(detail.count("`switch.example_01`"), 2)
                self.assertIn("   - ", detail)
                self.assertNotIn("switch.turn_on", detail)
                self.assertNotIn("Numeric threshold crossing", detail)
                self.assertFalse(any(line.endswith(" ") for line in detail.splitlines()))
        self.assertEqual(config, original)

    def test_timeout_stopping_and_default_continuation_are_distinguished(self):
        config = switch_cycle()
        continued = render_details(config)
        config["actions"][1]["continue_on_timeout"] = False
        stopped = render_details(config)
        self.assertIn("Continue with the next step when the timeout expires", continued)
        self.assertIn("Stop this sequence when the timeout expires", stopped)
        self.assertIn("stop on timeout", summarize(config))
        del config["actions"][1]["timeout"]
        self.assertIn("No timeout is configured", render_details(config))

    def test_nested_choices_repeats_and_parallel_paths_are_preserved(self):
        unknown_group = {"condition": MISSING, "conditions": [
            {"condition": MISSING, "above": 7}, {"condition": MISSING, "below": 3},
        ]}
        config = {"conditions": [unknown_group], "actions": [{"parallel": [
            {"sequence": [{"choose": [
                {"conditions": [{"condition": MISSING, "above": 7}], "sequence": [
                    {"if": [{"condition": "state", "entity_id": "binary_sensor.example_01", "state": "on"}],
                     "then": [{"action": "light.turn_on", "data": {"brightness_pct": 70}}],
                     "else": [{"delay": {"minutes": 5}}, {"action": "light.turn_off"}]},
                ]},
                {"conditions": [{"condition": MISSING, "below": 3}], "sequence": [{"stop": MISSING}]},
            ], "default": [{"action": "notify.notify", "data": {"message": MISSING}}]}]},
            {"sequence": [{"repeat": {"until": [{"condition": "state", "state": "off"}], "sequence": [
                {"action": "switch.turn_off"}, {"delay": {"seconds": 10}},
            ]}}]},
        ]}], "mode": "parallel", "max": 5}
        detail = render_details(config)
        self.assertIn("connecting rule missing", detail)
        self.assertIn("first matching branch", detail)
        self.assertIn("If no branch matches", detail)
        self.assertIn("Parallel path 1", detail)
        self.assertIn("Parallel path 2", detail)
        self.assertIn("Run at least once", detail)
        self.assertIn("brightness: 70%", detail)
        self.assertIn("Pause for 5 min", detail)
        self.assertLess(detail.index("Parallel path 1"), detail.index("Parallel path 2"))
        self.assertIn("Limit for running and queued runs: 5", detail)
        self.assertNotIn(MISSING, detail)

    def test_private_identifiers_and_payloads_are_not_repeated(self):
        private_label = "private" + "_owner"
        private_address = "sample" + "@private.test"
        config = {
            "alias": private_label, "description": private_label,
            "triggers": [{"trigger": "event", "event_type": private_label, "event_data": {"person": private_label}}],
            "conditions": [{"condition": "template", "value_template": private_label}],
            "actions": [
                {"action": "notify.mobile_app_" + private_label, "target": {"entity_id": "sensor." + private_label}, "data": {"message": private_address, "title": private_address}},
                {"action": "light.turn_on", "target": {"entity_id": "light.living_room"}, "data": {"brightness_pct": 70}},
                {"action": "notify.notify", "data": {"message": "The laundry is ready. **Check** the machine."}},
            ],
        }
        for language in ("en", "de"):
            with self.subTest(language=language):
                text = render_details(config, language)
                self.assertNotIn(private_label, text)
                self.assertNotIn(private_address, text)
                self.assertNotIn("mobile_app", text)
                self.assertIn("light.living_room", text)
                self.assertIn("The laundry is ready.", text)
                self.assertIn(r"\*\*Check\*\*", text)
                self.assertNotIn(private_label, summarize(config, language=language))

    def test_long_climate_sequence_summary_keeps_primary_values_and_wait(self):
        config = {"actions": [
            {"action": "input_boolean.turn_on"}, {"action": "light.turn_on"},
            {"action": "switch.turn_off"}, {"action": "media_player.volume_set", "data": {"volume_level": 0.2}},
            {"action": "climate.set_temperature", "data": {"temperature": 24}},
            {"wait_for_trigger": [{"trigger": MISSING}], "timeout": {"hours": 3}},
            {"action": "light.turn_off"},
            {"action": "climate.set_temperature", "data": {"temperature": 21}},
        ]}
        for language in ("en", "de"):
            summary = summarize(config, {"category": "climate"}, language)
            self.assertIn("24", summary)
            self.assertIn("21", summary)
            self.assertIn("3 h", summary)
            self.assertLess(summary.index("24"), summary.index("3 h"))
            self.assertLess(summary.index("3 h"), summary.index("21"))
            self.assertIn("omitted" if language == "en" else "ausgelassen", summary)
            self.assertNotIn("°C", summary)

    def test_summaries_lead_with_actions_and_keep_only_useful_start_settings(self):
        config = {
            "triggers": [{"trigger": MISSING, "from": MISSING, "to": MISSING}],
            "actions": [{"action": "light.turn_on", "data": {"brightness_pct": 5}},
                        {"delay": {"minutes": 5}}, {"action": "light.turn_off"}],
        }
        for language, start, missing in (("en", "Turn on lights at 5%", "not available"),
                                         ("de", "Licht mit 5 %", "nicht erhalten")):
            summary = summarize(config, language=language)
            self.assertTrue(summary.startswith(start))
            self.assertIn("5 min", summary)
            self.assertNotIn(missing, summary)
            self.assertIn(missing, render_details(config, language))
        config["triggers"] = [{"trigger": "time", "at": "12:30"},
                              {"trigger": "state", "for": {"minutes": 30}}]
        for language in ("en", "de"):
            summary = summarize(config, language=language)
            self.assertIn("12:30", summary)
            self.assertIn("30 min", summary)
            self.assertLess(summary.index("5 min"), summary.index("12:30"))
        config["actions"] = [{"action": "climate.set_preset_mode", "data": {"preset_mode": "eco"}},
                             {"action": "notify.notify", "data": {"message": "The laundry is ready."}}]
        for language in ("en", "de"):
            summary = summarize(config, language=language)
            self.assertIn("eco", summary)
            self.assertIn("The laundry is ready.", summary)

    def test_disabled_steps_and_external_blueprint_are_explicit(self):
        config = {"triggers": [{"trigger": "time", "at": "12:30", "enabled": False}],
                  "use_blueprint": {"path": "private" + "/blueprint.yaml"},
                  "actions": [{"action": "light.turn_on", "enabled": False}], "initial_state": False}
        text = render_details(config)
        self.assertIn("Disabled —", text)
        self.assertIn("Disabled step", text)
        self.assertIn("blueprint's internal steps are not included", text)
        self.assertIn("initially disabled", text)
        self.assertNotIn("private/blueprint.yaml", text)


if __name__ == "__main__":
    unittest.main()
