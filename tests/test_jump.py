import os
import unittest
from contextlib import redirect_stdout
from io import StringIO

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.admin_store import AdminStore
from pyti_app.field_manager import SpielfeldManager
from pyti_app.robot import Pyti, PytiWandKollisionError
from pyti_app.script_runtime import BefehlsInterpreter


class JumpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def make_game(self, walls=(), beepers=((2, 1),), goal=(2, 1)):
        level = {
            "start_x": 0,
            "start_y": 1,
            "start_richtung": 1,
            "waende": list(walls),
            "beeper": list(beepers),
            "goal": {"type": "collect_beeper", "position": goal},
        }
        robot = Pyti(grid_size=5)
        field = SpielfeldManager(grid_size=5)
        field.lade_level(level, robot)
        return robot, field, level, BefehlsInterpreter(robot, field, action_delay_ms=0)

    def test_jump_ueberspringt_ein_wandfeld_und_loest_ziel(self):
        robot, field, level, interpreter = self.make_game(walls=((1, 1),))
        with redirect_stdout(StringIO()):
            self.assertTrue(
                interpreter.interpretiere_und_fuehre_aus("jump()\npickBeeper()")
            )
        self.assertEqual((robot.x, robot.y), (2, 1))
        self.assertTrue(field.ziel_erreicht(robot, level["goal"]))
        AdminStore.validate_level(level | {"description": "Sprungtest"})

    def test_jump_ohne_wand_im_zwischenfeld_wird_abgewiesen(self):
        robot, _field, _level, interpreter = self.make_game()
        with self.assertRaises(PytiWandKollisionError):
            interpreter.aktion_ausfuehren("jump")
        self.assertEqual((robot.x, robot.y), (0, 1))

    def test_jump_mit_blockiertem_landeplatz_bewegt_pyti_nicht(self):
        robot, _field, _level, interpreter = self.make_game(walls=((1, 1), (2, 1)))
        with self.assertRaises(PytiWandKollisionError):
            interpreter.aktion_ausfuehren("jump")
        self.assertEqual((robot.x, robot.y), (0, 1))

    def test_jump_ueber_den_spielfeldrand_wird_abgewiesen(self):
        robot, _field, _level, interpreter = self.make_game(walls=((4, 1),))
        robot.x = 3
        robot.y = 1
        with self.assertRaises(PytiWandKollisionError):
            interpreter.aktion_ausfuehren("jump")
        self.assertEqual((robot.x, robot.y), (3, 1))


if __name__ == "__main__":
    unittest.main()
