import unittest

from pyti_app.level_generator import GRID_SIZE
from pyti_app.beginner_mission_data import _kuerzester_weg
from pyti_app.level_paths import level_reachable
from pyti_app.levels import LEVELS


class LevelTests(unittest.TestCase):
    def test_hindernismissionen_erfordern_einen_umweg(self):
        anspruchswoerter = (
            "umgeh", "blockier", "hindern", "barriere", "wand",
            "korridor", "labyrinth", "kammer", "slalom", "spiral",
            "durchgang", "öffnung", "schleuse", "raster", "gasse",
            "abzweig", "gang", "sackgasse", "schlang", "kreuzung",
            "ringmauer", "innenhof", "irr",
        )
        for name, level in list(LEVELS.items())[:50]:
            mission = level["description"].split("Ziel:")[0].casefold()
            if not any(wort in mission for wort in anspruchswoerter):
                continue
            start = level["start_x"], level["start_y"]
            goal = tuple(level["goal"]["position"])
            route = _kuerzester_weg(
                start, level["start_richtung"], goal, level["waende"]
            )
            freie_route = _kuerzester_weg(
                start, level["start_richtung"], goal, []
            )
            with self.subTest(level=name):
                self.assertGreater(len(route), len(freie_route))

    def test_level_eine_wand_versperrt_den_geraden_weg(self):
        level = LEVELS["0.0.3 Eine Wand"]
        start = level["start_x"], level["start_y"]
        goal = tuple(level["goal"]["position"])
        route = _kuerzester_weg(
            start, level["start_richtung"], goal, level["waende"]
        )
        freie_route = _kuerzester_weg(start, level["start_richtung"], goal, [])

        self.assertEqual(level["waende"], [(2, 2)])
        self.assertGreater(len(route), len(freie_route))

    def test_alle_100_level_haben_gueltige_erreichbare_ziele(self):
        self.assertEqual(len(LEVELS), 100)
        layouts = set()
        for name, level in LEVELS.items():
            with self.subTest(level=name):
                start = (level["start_x"], level["start_y"])
                goal = tuple(level["goal"]["position"])
                walls = set(level["waende"])
                points = (start, goal, *walls, *level["beeper"])
                for x, y in points:
                    self.assertTrue(0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE)
                self.assertNotIn(start, walls)
                self.assertNotIn(goal, walls)
                self.assertIn(goal, level["beeper"])
                layouts.add(tuple(sorted(walls)))

                self.assertTrue(level_reachable(start, goal, walls))
        self.assertEqual(len(layouts), 100)

if __name__ == "__main__":
    unittest.main()
