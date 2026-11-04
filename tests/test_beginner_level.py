import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.field_manager import SpielfeldManager
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter


class FirstMissionLevelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_first_level_matches_the_guided_mission(self):
        level = LEVELS["0.0.1 Der erste Beeper"]
        robot = Pyti()
        field = SpielfeldManager()
        field.lade_level(level, robot)
        interpreter = BefehlsInterpreter(robot, field, action_delay_ms=0)

        self.assertEqual((robot.x, robot.y), (0, 0))
        self.assertEqual(robot.richtung, 1)
        self.assertEqual(field.beeper_koordinaten, {(4, 0)})
        self.assertEqual(field.wand_koordinaten, set())

        for expected_x in (1, 2, 3):
            interpreter.aktion_ausfuehren("moveForward")
            self.assertEqual((robot.x, robot.y), (expected_x, 0))
        self.assertFalse(field.ziel_erreicht(robot, level["goal"]))

        interpreter.aktion_ausfuehren("moveForward")
        self.assertEqual((robot.x, robot.y), (4, 0))
        self.assertFalse(field.ziel_erreicht(robot, level["goal"]))
        interpreter.aktion_ausfuehren("pickBeeper")
        self.assertTrue(field.ziel_erreicht(robot, level["goal"]))


if __name__ == "__main__":
    unittest.main()
