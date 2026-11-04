import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pyti_app.admin_backup import (
    create_backup, export_backup, import_backup, restore_backup, validate_backup,
)
from pyti_app.admin_store import AdminStore, DEFAULT_SETTINGS
from pyti_app.custom_levels import EigeneLevelSpeicher
from pyti_app.level_creator_data import LevelEntwurfSpeicher, neuer_entwurf
from pyti_app.levels import LEVELS


class AdminBackupTests(unittest.TestCase):
    def test_backup_validates_and_restores_all_admin_data(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            admin = AdminStore(root / "admin.json")
            custom = EigeneLevelSpeicher(root / "custom.json")
            drafts = LevelEntwurfSpeicher(root / "drafts.json")
            levels = dict(LEVELS)
            levels["0.0.1 Der erste Beeper"] = dict(
                levels["0.0.1 Der erste Beeper"]
            )
            levels["0.0.1 Der erste Beeper"]["description"] = "Gesichert"
            custom_levels = {
                "Eigenes Level: Test": dict(LEVELS["0.0.1 Der erste Beeper"])
            }
            levels.update(custom_levels)
            data = create_backup(
                {"max_execution_time": 20, "action_delay_ms": 100},
                levels, [{"name": "Vorlage", "code": "turnLeft()"}],
                custom_levels, [neuer_entwurf("Entwurf")],
            )
            backup_path = root / "export.json"
            export_backup(backup_path, data)
            self.assertEqual(import_backup(backup_path), json.loads(
                json.dumps(data)
            ))
            restore_backup(data, admin, custom, drafts)
            settings, restored_levels, scripts = admin.load({
                **LEVELS, **custom_levels,
            })
            self.assertEqual(settings["max_execution_time"], 20)
            self.assertEqual(
                restored_levels["0.0.1 Der erste Beeper"]["description"],
                "Gesichert",
            )
            self.assertEqual(scripts[0]["name"], "Vorlage")
            self.assertEqual(
                custom.laden(), json.loads(json.dumps(custom_levels))
            )
            self.assertEqual(drafts.laden()[0]["name"], "Entwurf")
            self.assertEqual(validate_backup(data), data)

    def test_invalid_backup_is_rejected_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            admin = AdminStore(root / "admin.json")
            custom = EigeneLevelSpeicher(root / "custom.json")
            drafts = LevelEntwurfSpeicher(root / "drafts.json")
            admin.path.write_text("unchanged", encoding="utf-8")
            invalid = {
                "format": "pyti-admin-backup", "version": 1,
                "settings": DEFAULT_SETTINGS, "levels": {},
                "scripts": [], "custom_levels": {}, "drafts": [],
            }
            with self.assertRaises(ValueError):
                restore_backup(invalid, admin, custom, drafts)
            self.assertEqual(admin.path.read_text(encoding="utf-8"), "unchanged")

    def test_failed_restore_rolls_back_existing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            admin = AdminStore(root / "admin.json")
            custom = EigeneLevelSpeicher(root / "custom.json")
            drafts = LevelEntwurfSpeicher(root / "drafts.json")
            admin.path.write_text("previous admin", encoding="utf-8")
            custom.path.write_text("previous custom", encoding="utf-8")
            drafts.path.write_text("previous drafts", encoding="utf-8")
            data = create_backup(
                DEFAULT_SETTINGS, LEVELS, [], {}, [neuer_entwurf()]
            )
            with patch.object(drafts, "speichern", side_effect=OSError("disk")):
                with self.assertRaisesRegex(OSError, "disk"):
                    restore_backup(data, admin, custom, drafts)
            self.assertEqual(admin.path.read_text(encoding="utf-8"), "previous admin")
            self.assertEqual(custom.path.read_text(encoding="utf-8"), "previous custom")
            self.assertEqual(drafts.path.read_text(encoding="utf-8"), "previous drafts")


if __name__ == "__main__":
    unittest.main()
