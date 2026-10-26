import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.field_manager import SpielfeldManager
from pyti_app.robot import NORD, OST, SÜD, WEST, Pyti, PytiWandKollisionError
from pyti_app.script_runtime import BefehlsInterpreter


class BewegungUndDrehungTests(unittest.TestCase):
    def test_bewegung_in_alle_himmelsrichtungen(self):
        for direction, expected in {
            NORD: (2, 1), OST: (3, 2), SÜD: (2, 3), WEST: (1, 2)
        }.items():
            with self.subTest(direction=direction):
                robot = Pyti(x=2, y=2, richtung=direction)
                robot.vor()
                self.assertEqual((robot.x, robot.y), expected)

    def test_links_und_rechts_drehen(self):
        robot = Pyti(richtung=NORD)
        robot.links_drehen()
        self.assertEqual(robot.richtung, WEST)
        robot.rechts_drehen()
        self.assertEqual(robot.richtung, NORD)

    def test_randkollision_laesst_position_unveraendert(self):
        robot = Pyti(x=0, y=0, richtung=NORD)
        with self.assertRaises(PytiWandKollisionError):
            robot.vor()
        self.assertEqual((robot.x, robot.y), (0, 0))


class SpielfeldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.field = SpielfeldManager()
        self.robot = Pyti(x=5, y=5, richtung=OST)

    def test_wand_und_rand_blockieren_weg(self):
        self.field.wand_koordinaten.add((6, 5))
        self.assertFalse(self.field.ist_weg_frei(self.robot))
        self.assertFalse(self.field.toggle_beeper(6, 5))
        self.assertNotIn((6, 5), self.field.beeper_koordinaten)
        self.field.beeper_koordinaten.add((6, 5))
        self.assertFalse(self.field.beeper_voraus_pruefen(self.robot))
        self.robot.x = 14
        self.field.wand_koordinaten.clear()
        self.assertFalse(self.field.ist_weg_frei(self.robot))

    def test_wand_toggle_aktualisiert_spielfeld_und_schuetzt_objekte(self):
        level = {
            "start_x": 5, "start_y": 5, "beeper": [(2, 2)],
            "goal": {"position": (3, 3)},
        }
        self.field.lade_level(level, self.robot)
        self.assertTrue(self.field.toggle_wand(6, 5))
        self.assertIn((6, 5), self.field.wand_koordinaten)
        self.assertFalse(self.field.ist_weg_frei(self.robot))
        self.assertTrue(self.field.toggle_wand(6, 5))
        self.assertNotIn((6, 5), self.field.wand_koordinaten)
        for position in ((5, 5), (2, 2), (3, 3), (-1, 4), (15, 4)):
            with self.subTest(position=position):
                self.assertFalse(self.field.toggle_wand(*position))

    def test_sensoren_pruefen_freie_richtungen_und_beeper(self):
        self.field.wand_koordinaten.update({(6, 5), (5, 4)})
        self.field.beeper_koordinaten.add((6, 5))
        self.assertFalse(self.field.ist_weg_frei(self.robot, "vorne"))
        self.assertFalse(self.field.ist_weg_frei(self.robot, "links"))
        self.assertTrue(self.field.ist_weg_frei(self.robot, "rechts"))
        self.assertFalse(self.field.beeper_voraus_pruefen(self.robot))
        self.field.wand_koordinaten.remove((6, 5))
        self.assertTrue(self.field.beeper_voraus_pruefen(self.robot))
        self.robot.richtung = NORD
        self.assertFalse(self.field.beeper_voraus_pruefen(self.robot))

    def test_beeper_aufnehmen_und_ablegen(self):
        level = {
            "start_x": 2, "start_y": 2, "beeper": [(2, 2)],
            "goal": {"type": "collect_beeper", "position": (2, 2)},
        }
        self.field.lade_level(level, self.robot)
        self.robot.pick_beeper(self.field)
        self.assertEqual(self.robot.beeper_im_inventar, 1)
        self.robot.drop_beeper(self.field)
        self.assertEqual(self.robot.beeper_im_inventar, 0)
        self.assertTrue(self.field.hat_beeper(2, 2))

    def test_zielzaehlt_nur_solange_ziel_beeper_im_inventar_ist(self):
        goal = {"type": "collect_beeper", "position": (2, 2)}
        level = {
            "start_x": 2, "start_y": 2, "beeper": [(2, 2), (3, 2)],
            "goal": goal,
        }
        self.field.lade_level(level, self.robot)
        self.robot.x, self.robot.y = 3, 2
        self.robot.pick_beeper(self.field)
        self.robot.x, self.robot.y = 2, 2
        self.assertFalse(self.field.ziel_erreicht(self.robot, goal))
        self.robot.pick_beeper(self.field)
        self.assertTrue(self.field.ziel_erreicht(self.robot, goal))
        self.robot.drop_beeper(self.field)
        self.assertFalse(self.field.ziel_erreicht(self.robot, goal))

    def test_normale_beeper_ablegen_erhaelt_ziel_beeper_im_inventar(self):
        goal = {"type": "collect_beeper", "position": (1, 0)}
        level = {
            "start_x": 0, "start_y": 0, "start_richtung": OST,
            "beeper": [(1, 0), (2, 0)], "goal": goal,
        }
        self.field.lade_level(level, self.robot)
        interpreter = BefehlsInterpreter(self.robot, self.field)
        interpreter.aktion_ausfuehren("moveForward")
        interpreter.aktion_ausfuehren("pickBeeper")
        interpreter.aktion_ausfuehren("moveForward")
        interpreter.aktion_ausfuehren("pickBeeper")
        interpreter.aktion_ausfuehren("dropBeeper")
        interpreter.aktion_ausfuehren("turnAround")
        interpreter.aktion_ausfuehren("moveForward")
        self.assertEqual(self.robot.beeper_im_inventar, 1)
        self.assertTrue(self.field.ziel_erreicht(self.robot, goal))

    def test_levelwechsel_setzt_inventar_zurueck(self):
        level = {
            "start_x": 2, "start_y": 2, "beeper": [(2, 2)],
            "goal": {"type": "collect_beeper", "position": (2, 2)},
        }
        self.field.lade_level(level, self.robot)
        self.robot.pick_beeper(self.field)
        self.field.lade_level(level, self.robot)
        self.assertEqual(self.robot.beeper_im_inventar, 0)
        self.assertEqual(self.robot.ziel_beeper_im_inventar, 0)


if __name__ == "__main__":
    unittest.main()
