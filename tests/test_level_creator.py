import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QPointF, Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication

from pyti_app.level_creator_data import (
    LevelEntwurfSpeicher,
    export_code,
    neuer_entwurf,
)
from pyti_app.level_creator_dialog import LevelCreatorDialog
from pyti_app.level_creator_view import CELL_SIZE
from pyti_app.custom_levels import EigeneLevelSpeicher
from pyti_app.level_catalog import register_custom_level
from pyti_app.levels import LEVELS
from pyti_app.admin_checks import _check_levels
from pyti_app.admin_store import AdminStore
from PySide6.QtWidgets import QListWidget


class LevelCreatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_entwuerfe_bleiben_erhalten_und_export_ist_python(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "drafts.json"
            custom_store = EigeneLevelSpeicher(Path(directory) / "custom.json")
            registered = {}

            def register(name, level):
                return register_custom_level(
                    registered, level_list, name, level, custom_store
                )

            level_list = QListWidget()
            dialog = LevelCreatorDialog(path, register, lambda: registered.keys())
            dialog.name.setText("Test-Level")
            dialog.mission.setText("Teste die Kreuzung")
            dialog.show()
            self.app.processEvents()
            view = dialog.view

            def click_cell(button, x, y):
                point = view.mapFromScene(
                    QPointF((x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE)
                )
                QTest.mouseClick(view.viewport(), button, pos=point)
                self.app.processEvents()

            dialog.mode.setCurrentIndex(0)
            click_cell(Qt.RightButton, 4, 4)
            dialog.mode.setCurrentIndex(1)
            click_cell(Qt.LeftButton, 3, 3)
            click_cell(Qt.LeftButton, 1, 0)
            self.assertIn("muss auf dem Zielfeld bleiben", dialog.status.text())
            dialog.mode.setCurrentIndex(2)
            click_cell(Qt.LeftButton, 2, 2)
            dialog.direction.setCurrentIndex(2)
            dialog.mode.setCurrentIndex(3)
            click_cell(Qt.LeftButton, 5, 5)

            draft = LevelEntwurfSpeicher(path).laden()[0]
            self.assertEqual(draft["name"], "Test-Level")
            self.assertEqual(draft["level"]["start_x"], 2)
            self.assertEqual(draft["level"]["start_y"], 2)
            self.assertEqual(draft["level"]["start_richtung"], 2)
            self.assertEqual(draft["level"]["goal"]["position"], [5, 5])
            self.assertIn((4, 4), map(tuple, draft["level"]["waende"]))
            self.assertIn((3, 3), map(tuple, draft["level"]["beeper"]))
            code = export_code(draft["name"], draft)
            namespace = {"LEVELS": {}}
            exec(compile(code, "exported-level.py", "exec"), namespace)
            self.assertIn("Test-Level", namespace["LEVELS"])
            self.assertIn([5, 5], namespace["LEVELS"]["Test-Level"]["beeper"])
            dialog.register_button.click()
            key = "Eigenes Level: Test-Level"
            self.assertIn(key, registered)
            self.assertIn(key, [level_list.item(i).text() for i in range(level_list.count())])
            restored = custom_store.laden()
            self.assertIn(key, restored)
            defaults = {**LEVELS, **restored}
            with tempfile.TemporaryDirectory() as config_dir:
                _, loaded_levels, _ = AdminStore(
                    Path(config_dir) / "admin.json"
                ).load(defaults)
            self.assertIn(key, loaded_levels)
            _check_levels(loaded_levels)
            export_path = Path(directory) / "test_level.py"
            with patch(
                "pyti_app.level_creator_actions.QFileDialog.getSaveFileName",
                return_value=(str(export_path), "Python-Dateien (*.py)"),
            ):
                dialog._export()
            self.assertIn("LEVELS.update", export_path.read_text(encoding="utf-8"))
            compile(export_path.read_text(encoding="utf-8"), str(export_path), "exec")
            dialog.close()

    def test_neue_entwuerfe_sind_separat_gespeichert(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "drafts.json"
            dialog = LevelCreatorDialog(path, lambda *_: "", lambda: ())
            dialog.new_button.click()
            self.assertEqual(dialog.draft_list.count(), 2)
            dialog.name.setText("Zweiter Entwurf")
            drafts = LevelEntwurfSpeicher(path).laden()
            self.assertEqual(len(drafts), 2)
            self.assertEqual(drafts[1]["name"], "Zweiter Entwurf")
            dialog.delete_button.click()
            self.assertEqual(len(LevelEntwurfSpeicher(path).laden()), 1)
            dialog.close()

    def test_defekter_entwurf_wird_nicht_still_ueberschrieben(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "drafts.json"
            path.write_text("{broken", encoding="utf-8")
            dialog = LevelCreatorDialog(path, lambda *_: "", lambda: ())
            self.assertFalse(dialog.persist_enabled)
            self.assertIn("Datei bleibt erhalten", dialog.status.text())
            dialog.name.setText("Neuer Text")
            self.assertEqual(path.read_text(encoding="utf-8"), "{broken")
            dialog.close()


if __name__ == "__main__":
    unittest.main()
