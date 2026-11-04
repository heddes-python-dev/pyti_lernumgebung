import unittest

from pyti_app.beginner_mission_data import erstelle_erste_mission
from pyti_app.levels import LEVELS


class ErsteMissionDatenTests(unittest.TestCase):
    def test_standardlevel_vorlagen_sind_passend_und_ausfuehrbar(self):
        mission = erstelle_erste_mission(
            LEVELS["0.0.1 Der erste Beeper"]
        )

        compile(mission.luecken_code, "<test-gap-template>", "exec")
        self.assertEqual(mission.starter_code.count("moveForward()"), 4)
        self.assertEqual(mission.loesung_code.count("moveForward()"), 4)
        self.assertIn("pickBeeper()", mission.loesung_code)
        self.assertEqual(mission.starter_code, mission.loesung_code)
        self.assertEqual(len(mission.hinweise), 3)

    def test_nachbar_beeper_mission_bietet_keinen_zusaetzlichen_schritt_an(self):
        level = dict(LEVELS["0.0.1 Der erste Beeper"])
        level.update(
            start_x=0,
            start_y=14,
            start_richtung=1,
            beeper=[(1, 14)],
            waende=[],
            goal={"type": "collect_beeper", "position": (1, 14)},
        )

        mission = erstelle_erste_mission(level)

        self.assertEqual(
            mission.starter_code, "moveForward()\npickBeeper()\n"
        )
        self.assertIn("pickBeeper()", mission.luecken_code)
        self.assertEqual(
            mission.loesung_code, "moveForward()\npickBeeper()\n"
        )
        self.assertNotIn("moveForward()\nmoveForward()", mission.loesung_code)
        compile(mission.luecken_code, "<test-neighbor-gap>", "exec")

    def test_mission_wird_ohne_geraden_freien_weg_nicht_generiert(self):
        level = dict(LEVELS["0.0.1 Der erste Beeper"])
        level["waende"] = [(1, 0), (0, 1)]

        self.assertIsNone(erstelle_erste_mission(level))

    def test_lueckenvorlage_laesst_beim_langen_weg_die_drehung_offen(self):
        mission = erstelle_erste_mission(
            LEVELS["0.0.9 Zwei lange Abschnitte"]
        )

        self.assertIn("# Fuege hier turnRight() ein.", mission.luecken_code)
        self.assertEqual(mission.luecken_code.count("pickBeeper()"), 1)
        compile(mission.luecken_code, "<test-turn-gap>", "exec")


if __name__ == "__main__":
    unittest.main()
