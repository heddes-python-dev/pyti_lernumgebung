"""Graph traversal for level reachability with walking and jumping."""

from collections import deque

from .level_generator import GRID_SIZE


def level_reachable(start, goal, walls):
    visited = {start}
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for distance in (1, 2):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                point = x + distance * dx, y + distance * dy
                between = x + dx, y + dy
                if (
                    0 <= point[0] < GRID_SIZE
                    and 0 <= point[1] < GRID_SIZE
                    and point not in walls
                    and (distance == 1 or between in walls)
                    and point not in visited
                ):
                    if point == goal:
                        return True
                    visited.add(point)
                    queue.append(point)
    return start == goal
