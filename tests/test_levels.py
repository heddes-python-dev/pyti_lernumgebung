import unittest
from collections import deque

from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS


class LevelTests(unittest.TestCase):
    def test_alle_50_level_haben_gueltige_erreichbare_ziele(self):
        self.assertEqual(len(LEVELS), 50)
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

                visited = {start}
                queue = deque([start])
                while queue:
                    x, y = queue.popleft()
                    neighbors = (
                        (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)
                    )
                    for point in neighbors:
                        px, py = point
                        if (
                            0 <= px < GRID_SIZE and 0 <= py < GRID_SIZE
                            and point not in walls and point not in visited
                        ):
                            visited.add(point)
                            queue.append(point)
                self.assertIn(goal, visited)


if __name__ == "__main__":
    unittest.main()
