import os
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QPushButton, QTextBrowser

from pyti_app.app_controller import PytiController
from pyti_app.beginner_mission import zeige_erste_mission
from pyti_app.beginner_mission_data import erstelle_erste_mission
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class MissionsauswahlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.widgets = baue_ui(
            Path(__file__).resolve().parents[1], LEVELS.keys()
        )
        self.robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(self.robot, field)
        self.controller = PytiController(
            self.widgets, dict(LEVELS), self.robot, field, interpreter,
            SkriptBruecke(interpreter),
        )
        self.widgets.level_liste.setCurrentRow(1)

    def tearDown(self):
        self.widgets.window.close()

    def test_dialog_nutzt_das_ausgewaehlte_level_0_0_2(self):
        expected = erstelle_erste_mission(LEVELS["0.0.2 Der erste Dreh"])
        self.widgets.editor.clear()

        def simuliere_dialog(dialog):
            self.assertEqual(
                dialog.windowTitle(), "Erste Mission: 0.0.2 Der erste Dreh"
            )
            text = dialog.findChild(QTextBrowser).toPlainText()
            self.assertIn("1 Drehung", text)
            buttons = {
                button.text(): button
                for button in dialog.findChildren(QPushButton)
            }
            solution = buttons["Lösung laden"]
            hints = buttons["Tipp anzeigen"]
            self.assertFalse(solution.isEnabled())
            hints.click()
            hints.click()
            self.assertFalse(solution.isEnabled())
            hints.click()
            self.assertTrue(solution.isEnabled())
            solution.click()

        with patch(
            "pyti_app.beginner_mission.QDialog.exec",
            new=simuliere_dialog,
        ):
            zeige_erste_mission(self.widgets.window, self.widgets, LEVELS)

        self.assertEqual(self.widgets.level_liste.currentRow(), 1)
        self.assertEqual(
            self.widgets.editor.toPlainText(), expected.loesung_code
        )
        self.assertIn("turnLeft()", expected.loesung_code)
        self.assertEqual((self.robot.x, self.robot.y), (0, 4))


if __name__ == "__main__":
    unittest.main()
