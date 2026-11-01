import os
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QMessageBox, QListWidget

from pyti_app.admin_panel import AdminPanel
from pyti_app.admin_store import AdminStore
from pyti_app.app_controller import PytiController
from pyti_app.custom_levels import EigeneLevelSpeicher
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_catalog import delete_custom_level, register_custom_level
from pyti_app.level_creator_data import neuer_entwurf
from pyti_app.level_creator_dialog import LevelCreatorDialog
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class LevelDeletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_admin_deletes_custom_level_and_preserves_standard_levels(self):
        widgets = baue_ui(Path.cwd(), LEVELS.keys())
        robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(robot, field)
        controller = PytiController(
            widgets, dict(LEVELS), robot, field, interpreter,
            SkriptBruecke(interpreter),
        )
        with tempfile.TemporaryDirectory() as directory:
            store = AdminStore(Path(directory) / "admin.json")
            custom_store = EigeneLevelSpeicher(
                Path(directory) / "custom_levels.json"
            )
            name = "Eigenes Level: Test"
            level = deepcopy(next(iter(LEVELS.values())))
            custom_store.speichern("Test", level)
            controller.levels[name] = level
            widgets.level_liste.addItem(name)
            settings, levels, scripts = store.load(controller.levels)
            controller.levels.update(levels)
            panel = AdminPanel(
                store, controller, settings, scripts, "1.2.0",
                custom_level_store=custom_store,
            )
            self.assertFalse(panel.levels.delete_button.isEnabled())
            row = next(
                index for index in range(panel.levels.level_list.count())
                if panel.levels.level_list.item(index).text() == name
            )
            panel.levels.level_list.setCurrentRow(row)
            self.assertTrue(panel.levels.delete_button.isEnabled())
            with patch(
                "pyti_app.admin_panel.QMessageBox.question",
                return_value=QMessageBox.Yes,
            ):
                panel._confirm_delete_level()
            self.assertIn(name, custom_store.laden())
            panel.save()
            self.assertNotIn(name, controller.levels)
            self.assertNotIn(name, custom_store.laden())
            self.assertFalse(any(
                widgets.level_liste.item(index).text() == name
                for index in range(widgets.level_liste.count())
            ))
            _settings, loaded, _scripts = store.load(LEVELS)
            self.assertNotIn(name, loaded)
            panel.close()
        widgets.window.close()

    def test_creator_deletes_registered_custom_level(self):
        with tempfile.TemporaryDirectory() as directory:
            custom_store = EigeneLevelSpeicher(
                Path(directory) / "custom_levels.json"
            )
            registered = {}
            level_list = QListWidget()

            def register(name, level):
                return register_custom_level(
                    registered, level_list, name, level, custom_store
                )

            dialog = LevelCreatorDialog(
                Path(directory) / "drafts.json",
                register,
                lambda: registered.keys(),
                delete_level=lambda key: delete_custom_level(
                    registered, level_list, key, custom_store
                ),
            )
            key = register(
                "Test",
                neuer_entwurf()["level"] | {"description": "Teste das Level."},
            )
            dialog._refresh_registered_levels(key)
            self.assertTrue(dialog.delete_saved_button.isEnabled())
            with patch(
                "pyti_app.level_creator_actions.QMessageBox.question",
                return_value=QMessageBox.Yes,
            ):
                dialog._delete_registered_level()
            self.assertNotIn(key, registered)
            self.assertNotIn(key, custom_store.laden())
            self.assertEqual(dialog.saved_level_list.count(), 0)
            self.assertEqual(level_list.count(), 0)
            dialog.close()


if __name__ == "__main__":
    unittest.main()
