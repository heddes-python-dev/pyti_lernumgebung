import os
import tempfile
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.admin_scripts_tab import ScriptsTab
from pyti_app.admin_store import AdminStore
from pyti_app.field_manager import SpielfeldManager
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter


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
            self.assertEqual(len(levels), 100)
            self.assertIn("nicht geladen", store.load_error)

    def test_ladefehler_verschwindet_nach_gueltigem_oder_fehlendem_config(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "admin.json"
            store = AdminStore(path)
            path.write_text("{kaputt", encoding="utf-8")
            store.load(LEVELS)
            self.assertTrue(store.load_error)
            settings, levels, scripts = store.load(LEVELS)
            store.save(settings, levels, scripts)
            store.load(LEVELS)
            self.assertEqual(store.load_error, "")

            path.write_text("{kaputt", encoding="utf-8")
            store.load(LEVELS)
            self.assertTrue(store.load_error)
            path.unlink()
            store.load(LEVELS)
            self.assertEqual(store.load_error, "")

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

if __name__ == "__main__":
    unittest.main()
