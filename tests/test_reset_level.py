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


class LevelResetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_button_laadet_levelzustand_neu_und_behaelt_skript(self):
        widgets = baue_ui(Path(__file__).resolve().parents[1], LEVELS.keys())
        robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(robot, field)
        controller = PytiController(
            widgets, dict(LEVELS), robot, field, interpreter,
            SkriptBruecke(interpreter),
        )
        current = widgets.level_liste.currentItem().text()
        original = LEVELS[current]
        widgets.editor.setPlainText("moveForward()")
        robot.x, robot.y, robot.richtung = 8, 8, 2
        robot.beeper_im_inventar = 2
        field.wand_koordinaten.add((8, 7))
        field.beeper_koordinaten.clear()

        widgets.reset_button.click()

        self.assertEqual((robot.x, robot.y), (original["start_x"], original["start_y"]))
        self.assertEqual(robot.richtung, original.get("start_richtung", 1))
        self.assertEqual(robot.beeper_im_inventar, 0)
        self.assertEqual(field.wand_koordinaten, set(map(tuple, original["waende"])))
        self.assertEqual(field.beeper_koordinaten, set(map(tuple, original["beeper"])))
        self.assertEqual(widgets.editor.toPlainText(), "moveForward()")
        self.assertEqual(widgets.status.text(), "Level neu gestartet.")
        self.assertFalse(controller.active)
        widgets.window.close()


if __name__ == "__main__":
    unittest.main()
