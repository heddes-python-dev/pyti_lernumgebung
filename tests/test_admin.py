import os
import tempfile
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.admin_checks import pruefe_system
from pyti_app.admin_panel import AdminPanel
from pyti_app.admin_scripts_tab import ScriptsTab
from pyti_app.admin_store import AdminStore
from pyti_app.app_controller import PytiController
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class AdminPanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_config_wird_gespeichert_und_validiert(self):
        with tempfile.TemporaryDirectory() as directory:
            store = AdminStore(Path(directory) / "admin.json")
            settings, levels, scripts = store.load(LEVELS)
            settings["max_execution_time"] = 12
            levels["0.0.1 Der erste Beeper"]["description"] = "Geändert"
            scripts[0]["name"] = "Eigene Vorlage"
            store.save(settings, levels, scripts)
            loaded_settings, loaded_levels, loaded_scripts = store.load(LEVELS)
            self.assertEqual(loaded_settings["max_execution_time"], 12)
            self.assertEqual(
                loaded_levels["0.0.1 Der erste Beeper"]["description"], "Geändert"
            )
            self.assertEqual(loaded_scripts[0]["name"], "Eigene Vorlage")
            broken = dict(loaded_levels["0.0.1 Der erste Beeper"])
            broken["waende"] = [[4, 0]]
            with self.assertRaisesRegex(ValueError, "Wänden"):
                AdminStore.validate_level(broken)

    def test_beschaedigte_config_wird_im_status_erkennbar(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "admin.json"
            path.write_text("{kaputt", encoding="utf-8")
            store = AdminStore(path)
            settings, levels, _scripts = store.load(LEVELS)
            self.assertEqual(settings["max_execution_time"], 30)
            self.assertEqual(len(levels), 50)
            self.assertIn("nicht geladen", store.load_error)

    def test_beispielvorlagen_koennen_geloescht_und_ausgewaehlt_werden(self):
        tab = ScriptsTab([
            {"name": "Alt", "code": "x = 1"},
            {"name": "Bleibt", "code": "turnLeft()"},
        ])
        tab.delete_current()
        self.assertEqual(tab.values(), [{"name": "Bleibt", "code": "turnLeft()"}])
        tab.load_selected()

    def test_letzter_skriptfehler_wird_fuer_statusanzeige_erfasst(self):
        interpreter = BefehlsInterpreter(Pyti(), SpielfeldManager())
        self.assertFalse(interpreter.interpretiere_und_fuehre_aus(
            "if True print('Fehler')"
        ))
        last_error = interpreter.last_execution_error
        self.assertIn("SyntaxError", last_error)
        self.assertTrue(interpreter.interpretiere_und_fuehre_aus("x = 1"))
        self.assertEqual(interpreter.last_execution_error, last_error)

    def test_admin_ui_speichert_aenderungen_und_zeigt_systemstatus(self):
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
            settings, levels, scripts = store.load(controller.levels)
            controller.levels.update(levels)
            panel = AdminPanel(store, controller, settings, scripts, "1.2.0")
            panel.settings.timeout.setValue(12)
            panel.settings.delay.setValue(50)
            panel.levels.description.setPlainText("Admin-Text")
            panel.levels.walls.set_coordinates(
                panel.levels.walls.coordinates() + [[3, 1]]
            )
            panel.levels.beepers.set_coordinates(
                panel.levels.beepers.coordinates() + [[3, 0]]
            )
            panel.scripts.name.setText("Meine Vorlage")
            panel.scripts.code.setPlainText("turnRight()")
            panel.save()
            self.assertEqual(interpreter.max_execution_time, 12)
            self.assertEqual(interpreter.action_delay_ms, 50)
            self.assertEqual(
                controller.levels["0.0.1 Der erste Beeper"]["description"],
                "Admin-Text",
            )
            self.assertIn(
                [3, 1], controller.levels["0.0.1 Der erste Beeper"]["waende"]
            )
            self.assertIn(
                [3, 0], controller.levels["0.0.1 Der erste Beeper"]["beeper"]
            )
            self.assertEqual(panel.scripts.values()[0]["name"], "Meine Vorlage")
            reopened = AdminPanel(
                store, controller, controller.admin_settings,
                controller.admin_scripts, "1.2.0",
            )
            self.assertEqual(reopened.settings.timeout.value(), 12)
            statuses = pruefe_system(
                controller.levels, widgets, interpreter
            )
            self.assertTrue(
                all(status == "OK" for status, _, _ in statuses), repr(statuses)
            )
        widgets.window.close()


if __name__ == "__main__":
    unittest.main()
