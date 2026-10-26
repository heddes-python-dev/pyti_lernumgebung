import unittest

from pyti_app.level_generator import GRID_SIZE
from pyti_app.level_paths import level_reachable
from pyti_app.levels import LEVELS


class LevelTests(unittest.TestCase):
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
