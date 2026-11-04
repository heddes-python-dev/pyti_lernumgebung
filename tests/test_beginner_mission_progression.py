import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.beginner_mission_data import erstelle_erste_mission
from pyti_app.field_manager import SpielfeldManager
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter


class MissionsfortschrittTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_level_0_0_1_bis_0_1_0_haben_ausfuehrbare_missionsloesungen(self):
        for name, level in LEVELS.items():
            nummer = tuple(map(int, name.split(" ", 1)[0].split(".")))
            if not ((0, 0, 1) <= nummer <= (0, 1, 0)):
                continue
            with self.subTest(level=name):
                mission = erstelle_erste_mission(level)
                self.assertIsNotNone(mission)
                self.assertEqual(mission.starter_code, mission.loesung_code)
                self.assertEqual(
                    sum(
                        zeile.startswith("# Fuege hier ")
                        for zeile in mission.luecken_code.splitlines()
                    ),
                    1,
                )
                compile(mission.starter_code, "<mission-sample>", "exec")
                compile(mission.luecken_code, "<mission-gap>", "exec")
                robot = Pyti()
                field = SpielfeldManager()
                field.lade_level(level, robot)
                interpreter = BefehlsInterpreter(
                    robot, field, action_delay_ms=0
                )

                self.assertTrue(
                    interpreter.interpretiere_und_fuehre_aus(
                        mission.loesung_code
                    )
                )
                self.assertTrue(field.ziel_erreicht(robot, level["goal"]))


if __name__ == "__main__":
    unittest.main()
