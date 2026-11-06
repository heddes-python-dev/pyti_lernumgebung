import json
import tempfile
import unittest
from pathlib import Path

from pyti_app.progress_store import ProgressStore


class ProgressStoreTests(unittest.TestCase):
    def test_completed_and_active_levels_survive_reload(self):
        with tempfile.TemporaryDirectory() as directory:
            store = ProgressStore(Path(directory) / "progress.json")
            store.save({"Level B", "Level A"}, "Level B")
            completed, active = store.load()
            self.assertEqual(completed, {"Level A", "Level B"})
            self.assertEqual(active, "Level B")

    def test_invalid_progress_is_reported_and_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "progress.json"
            path.write_text("{broken", encoding="utf-8")
            store = ProgressStore(path)
            with self.assertRaises(ValueError):
                store.load()
            self.assertIn("nicht geladen", store.load_error)
            with self.assertRaisesRegex(ValueError, "nicht überschrieben"):
                store.save(set(), "")
            self.assertEqual(path.read_text(encoding="utf-8"), "{broken")

    def test_unknown_progress_version_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "progress.json"
            path.write_text(json.dumps({"version": 2}), encoding="utf-8")
            with self.assertRaises(ValueError):
                ProgressStore(path).load()


if __name__ == "__main__":
    unittest.main()
