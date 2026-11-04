import os
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.app_controller import PytiController
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class MissionsStatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.widgets = baue_ui(
            Path(__file__).resolve().parents[1], LEVELS.keys()
        )
        self.robot = Pyti(grid_size=GRID_SIZE)
        self.field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(self.robot, self.field)
        self.controller = PytiController(
            self.widgets, dict(LEVELS), self.robot, self.field, interpreter,
            SkriptBruecke(interpreter),
        )

    def tearDown(self):
        self.widgets.window.close()

    def test_erfolgreicher_lauf_behaelt_code_und_meldet_offenes_levelziel(self):
        code = "moveForward()\n"
        self.widgets.editor.setPlainText(code)
        self.controller.active = True
        self.controller.previous_enabled = []

        self.controller._on_script_finished(True, False)

        self.assertEqual(self.widgets.editor.toPlainText(), code)
        self.assertIn("Ziel noch nicht erreicht", self.widgets.status.text())

    def test_erfolgreiches_levelziel_wird_bestaetigt_und_code_bleibt_erhalten(self):
        code = "pickBeeper()\n"
        self.widgets.editor.setPlainText(code)
        self.robot.x, self.robot.y = 4, 0
        self.robot.ziel_beeper_im_inventar = 1
        self.field.beeper_koordinaten.remove((4, 0))
        self.controller.active = True
        self.controller.previous_enabled = []

        self.controller._on_script_finished(True, False)

        self.assertEqual(self.widgets.editor.toPlainText(), code)
        self.assertIn("Ziel erreicht", self.widgets.status.text())
        self.assertIn("Geschafft!", self.widgets.mission.text())


if __name__ == "__main__":
    unittest.main()
