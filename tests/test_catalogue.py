"""Catalogue contracts: privacy-safe names, completeness and reproducibility."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import catalogue
from privacy_guard import SecretReference, dump_yaml, load_yaml


def example() -> dict:
    return {
        "triggers": [{"trigger": "numeric_state", "entity_id": "sensor.example_01", "above": 10}],
        "conditions": [],
        "actions": [
            {"action": "switch.turn_on", "target": {"entity_id": "switch.example_01"}},
            {"wait_for_trigger": [{"trigger": "numeric_state", "entity_id": "sensor.example_01", "below": 5}]},
            {"action": "switch.turn_off", "target": {"entity_id": "switch.example_01"}},
        ],
        "mode": "restart",
    }


class CatalogueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "README.md").write_text(f"# Examples\n\n{catalogue.START}\n{catalogue.END}\n")

    def publish(self, configs: list[dict] | None = None) -> list[Path]:
        return catalogue.write_catalogue(self.root, [{"config": c} for c in (configs or [example()])])

    def test_names_communicate_behavior(self) -> None:
        [folder] = self.publish()
        self.assertEqual(folder.relative_to(self.root).as_posix(), "automations/switches/threshold-switch-on-off-with-wait")
        metadata = json.loads((folder / "metadata.json").read_text())
        self.assertEqual(metadata["trigger_types"], ["numeric_state"])
        self.assertEqual(metadata["action_count"], 3)
        self.assertIn("Switch: on, off", catalogue.render_alias(metadata))

    def test_every_indistinguishable_example_is_preserved(self) -> None:
        folders = self.publish([example(), example(), example()])
        self.assertEqual(len(folders), 3)
        self.assertEqual(len({p.name for p in folders}), 3)
        self.assertTrue(all("threshold-switch-on-off-with-wait-" in p.name for p in folders))
        self.assertEqual(len(catalogue.load_entries(self.root)), 3)
        self.assertIn("3 examples", (self.root / "README.md").read_text())

    def test_titles_distinguish_waits_from_delays(self) -> None:
        waiting = example()
        delayed = copy.deepcopy(waiting)
        delayed["actions"][1] = {"delay": {"seconds": 10}}
        wait_title = catalogue.render_alias(catalogue.build_metadata(waiting))
        delay_title = catalogue.render_alias(catalogue.build_metadata(delayed))
        self.assertIn("with wait", wait_title)
        self.assertIn("with delay", delay_title)
        self.assertNotEqual(wait_title, delay_title)

    def test_new_output_includes_root_readme_and_index(self) -> None:
        (self.root / "README.md").unlink()
        [folder] = self.publish()
        text = (self.root / "README.md").read_text()
        self.assertIn("Automation catalogue (1 example)", text)
        self.assertIn(folder.relative_to(self.root).as_posix() + "/README.md", text)
        self.assertTrue(catalogue.update_readme(self.root, check=True))

    def test_custom_private_labels_never_enter_metadata_or_docs(self) -> None:
        config = example()
        private = "private_recipient_label"
        config["alias"] = private
        config["actions"] = [{"action": "notify.mobile_app_" + private}]
        [folder] = self.publish([config])
        for path in [folder / "metadata.json", folder / "README.md", self.root / "README.md"]:
            self.assertNotIn(private, path.read_text())
        self.assertNotIn(private, folder.as_posix())
        self.assertEqual(load_yaml((folder / "automation.yaml").read_text())["alias"], "Notification: send — numeric threshold")

    def test_generation_is_idempotent_and_detects_stale_docs(self) -> None:
        [folder] = self.publish()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertTrue(catalogue.update_readme(self.root, check=True))
        self.assertTrue(catalogue.update_readme(self.root))
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        (folder / "README.md").write_text("stale documentation\n")
        self.assertFalse(catalogue.update_readme(self.root, check=True))
        self.assertFalse(catalogue.update_readme(self.root))
        self.assertTrue(catalogue.update_readme(self.root, check=True))

    def test_malformed_metadata_fails_without_private_value_in_error(self) -> None:
        metadata = catalogue.build_metadata(example())
        for key, value in [("category", []), ("actions", ["notify.private_name"]), ("variant", "abcdef12-privateperson"), ("slug", "../../escape")]:
            broken = copy.deepcopy(metadata)
            broken[key] = value
            with self.subTest(key=key), self.assertRaises(catalogue.CatalogueError) as error:
                catalogue.validate_metadata(broken)
            self.assertNotIn(str(value), str(error.exception))

    def test_symlinked_example_is_rejected(self) -> None:
        [folder] = self.publish()
        path = folder / "automation.yaml"
        original = path.read_text()
        outside = self.root / "outside.yaml"
        outside.write_text(original)
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaises(catalogue.CatalogueError):
            catalogue.update_readme(self.root)
        self.assertEqual(outside.read_text(), original)

    def test_stale_action_metadata_is_rejected(self) -> None:
        [folder] = self.publish()
        path = folder / "automation.yaml"
        config = load_yaml(path.read_text())
        config["actions"].append({"action": "notify.notify"})
        path.write_text(dump_yaml(config))
        with self.assertRaises(catalogue.CatalogueError):
            catalogue.load_entries(self.root)

    def test_existing_catalogue_is_never_overwritten(self) -> None:
        self.publish()
        with self.assertRaises(catalogue.CatalogueError):
            self.publish()
        self.assertEqual(len(catalogue.load_entries(self.root)), 1)

    def test_secret_reference_roundtrips(self) -> None:
        config = example()
        config["actions"].append({"action": "notify.notify", "data": {"message": SecretReference("example_secret_01")}})
        [folder] = self.publish([config])
        parsed = load_yaml((folder / "automation.yaml").read_text())
        self.assertIsInstance(parsed["actions"][-1]["data"]["message"], SecretReference)
        self.assertEqual(len(catalogue.load_entries(self.root)), 1)

    def test_root_marker_errors_are_not_silently_overwritten(self) -> None:
        self.publish()
        (self.root / "README.md").write_text("README without markers\n")
        with self.assertRaises(catalogue.CatalogueError):
            catalogue.update_readme(self.root)


if __name__ == "__main__":
    unittest.main()
