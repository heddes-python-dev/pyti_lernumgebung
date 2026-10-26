"""Shortest walking and jumping route counts for the printable level atlas."""

from collections import deque

from pyti_app.level_generator import GRID_SIZE


def route_facts(start, goal, walls):
    distances = {start: 0}
    routes = {start: 1}
    queue = deque([start])
    while queue:
        x, y = point = queue.popleft()
        for distance in (1, 2):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = x + distance * dx, y + distance * dy
                between = x + dx, y + dy
                if (
                    not 0 <= neighbor[0] < GRID_SIZE
                    or not 0 <= neighbor[1] < GRID_SIZE
                    or neighbor in walls
                    or (distance == 2 and between not in walls)
                ):
                    continue
                candidate = distances[point] + 1
                if neighbor not in distances:
                    distances[neighbor] = candidate
                    routes[neighbor] = routes[point]
                    queue.append(neighbor)
                elif distances[neighbor] == candidate:
                    routes[neighbor] += routes[point]
    return distances.get(goal), routes.get(goal, 0)
