import unittest
from collections import deque
from contextlib import redirect_stdout
from io import StringIO

from PySide6.QtWidgets import QApplication

from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.level_specs import level_nummer
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter

DELTAS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def shortest_route_count(start, goal, walls):
    distances = {start: 0}
    routes = {start: 1}
    queue = deque([start])
    while queue:
        point = queue.popleft()
        for length in (1, 2):
            for dx, dy in DELTAS:
                neighbor = point[0] + length * dx, point[1] + length * dy
                between = point[0] + dx, point[1] + dy
                if (
                    not 0 <= neighbor[0] < GRID_SIZE
                    or not 0 <= neighbor[1] < GRID_SIZE
                    or neighbor in walls
                    or (length == 2 and between not in walls)
                ):
                    continue
                distance = distances[point] + 1
                if neighbor not in distances:
                    distances[neighbor] = distance
                    routes[neighbor] = routes[point]
                    queue.append(neighbor)
                elif distances[neighbor] == distance:
                    routes[neighbor] += routes[point]
    return routes.get(goal, 0)


def shortest_directions(start, goal, walls):
    parents = {start: None}
    queue = deque([start])
    while queue:
        point = queue.popleft()
        for distance in (1, 2):
            for direction, (dx, dy) in enumerate(DELTAS):
                neighbor = point[0] + distance * dx, point[1] + distance * dy
                between = point[0] + dx, point[1] + dy
                if (
                    0 <= neighbor[0] < GRID_SIZE
                    and 0 <= neighbor[1] < GRID_SIZE
                    and neighbor not in walls
                    and (distance == 1 or between in walls)
                    and neighbor not in parents
                ):
                    parents[neighbor] = point, (direction, distance)
                    queue.append(neighbor)
    if goal not in parents:
        return []
    route = []
    point = goal
    while parents[point] is not None:
        point, action = parents[point]
        route.append(action)
    return list(reversed(route))


def script_for(level, directions):
    commands = []
    facing = level["start_richtung"]
    turns = {1: "turnRight()", 2: "turnAround()", 3: "turnLeft()"}
    for direction, distance in directions:
        difference = (direction - facing) % 4
        if difference:
            commands.append(turns[difference])
        commands.append("jump()" if distance == 2 else "moveForward()")
        facing = direction
    commands.append("pickBeeper()")
    return "\n".join(commands)


class LevelRouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_kurzeste_routen_zaehler(self):
        self.assertEqual(shortest_route_count((0, 0), (2, 0), set()), 1)
        self.assertEqual(shortest_route_count((0, 0), (1, 1), set()), 2)
        self.assertEqual(
            [level_nummer(i) for i in (1, 9, 10, 99, 100)],
            ["0.0.1", "0.0.9", "0.1.0", "0.9.9", "1.0.0"],
        )

    def test_eindeutige_missionen_haben_genau_eine_kurzroute(self):
        terms = ("einzig", "einmalig", "allein", "nur eine", "nur ein", "ausschließlich")
        for name, level in LEVELS.items():
            if not any(term in level["description"].casefold() for term in terms):
                continue
            with self.subTest(level=name):
                start = level["start_x"], level["start_y"]
                goal = tuple(level["goal"]["position"])
                self.assertEqual(
                    shortest_route_count(start, goal, set(map(tuple, level["waende"]))),
                    1,
                )

    def test_alle_standardlevel_mit_dem_interpreter_loesbar(self):
        self.assertEqual(len(LEVELS), 100)
        self.assertEqual(next(iter(LEVELS)), "0.0.1 Der erste Beeper")
        self.assertEqual(list(LEVELS)[-1], "1.0.0 Das große Finale")
        for number, (name, level) in enumerate(LEVELS.items(), 1):
            with self.subTest(level=name):
                start = level["start_x"], level["start_y"]
                goal = tuple(level["goal"]["position"])
                directions = shortest_directions(
                    start, goal, set(map(tuple, level["waende"]))
                )
                self.assertTrue(directions or start == goal)
                script = script_for(level, directions)
                if number > 50:
                    jump_count = int(
                        level["description"].rsplit("Überwinde ", 1)[1].split()[0]
                    )
                    self.assertEqual(script.count("jump()"), jump_count)

                robot = Pyti(grid_size=GRID_SIZE)
                field = SpielfeldManager(grid_size=GRID_SIZE)
                field.lade_level(level, robot)
                interpreter = BefehlsInterpreter(
                    robot, field, max_execution_time=5, action_delay_ms=0
                )
                with redirect_stdout(StringIO()):
                    success = interpreter.interpretiere_und_fuehre_aus(
                        script
                    )
                self.assertTrue(success, interpreter.last_execution_error)
                self.assertTrue(field.ziel_erreicht(robot, level["goal"]))


if __name__ == "__main__":
    unittest.main()
