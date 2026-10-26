"""Erzeugt reproduzierbare perfekte Labyrinthe mit Sprungbarrieren."""

import random
from collections import deque

from .level_generator import GRID_SIZE


def _verbinde(a, b):
    return tuple(sorted((a, b)))


def baue_labyrinth(start, ziel, groesse, seed, sprung_barrieren):
    rng = random.Random(seed)
    zellen = {(x, y) for x in range(groesse) for y in range(groesse)}
    besucht, stapel, kanten = {start}, [start], set()
    while stapel:
        x, y = stapel[-1]
        nachbarn = [
            (x + dx, y + dy)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
        ]
        frei = [punkt for punkt in nachbarn if punkt in zellen - besucht]
        if not frei:
            stapel.pop()
            continue
        nachbar = rng.choice(frei)
        kanten.add(_verbinde(stapel[-1], nachbar))
        besucht.add(nachbar)
        stapel.append(nachbar)

    weg = _zellenweg(start, ziel, kanten, groesse)
    if sprung_barrieren > len(weg):
        raise ValueError("Mehr Sprungbarrieren als Labyrinthdurchgänge.")
    blockiert = {
        weg[i * len(weg) // sprung_barrieren]
        for i in range(sprung_barrieren)
    }
    if len(blockiert) != sprung_barrieren:
        raise ValueError("Sprungbarrieren konnten nicht eindeutig verteilt werden.")
    waende = {
        (x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)
    }
    frei = {(3 * x + 1, 3 * y + 1) for x, y in zellen}
    for a, b in kanten:
        x, y = 3 * a[0] + 1, 3 * a[1] + 1
        dx, dy = b[0] - a[0], b[1] - a[1]
        frei.update(((x + dx, y + dy), (x + 2 * dx, y + 2 * dy)))
    waende.difference_update(frei)
    for a, b in blockiert:
        x, y = 3 * a[0] + 1, 3 * a[1] + 1
        dx, dy = b[0] - a[0], b[1] - a[1]
        waende.add((x + dx, y + dy))
        waende.discard((x + 2 * dx, y + 2 * dy))
    start_xy = (3 * start[0] + 1, 3 * start[1] + 1)
    ziel_xy = (3 * ziel[0] + 1, 3 * ziel[1] + 1)
    return {
        "start_x": start_xy[0],
        "start_y": start_xy[1],
        "start_richtung": 1,
        "waende": sorted(waende),
        "beeper": [ziel_xy],
        "goal": {"type": "collect_beeper", "position": ziel_xy},
    }


def _zellenweg(start, ziel, kanten, groesse):
    anschluss = {
        (x, y): [] for x in range(groesse) for y in range(groesse)
    }
    for a, b in kanten:
        anschluss[a].append(b)
        anschluss[b].append(a)
    queue = deque([start])
    eltern = {start: None}
    while queue:
        zelle = queue.popleft()
        for nachbar in anschluss[zelle]:
            if nachbar not in eltern:
                eltern[nachbar] = zelle
                queue.append(nachbar)
    zellen = []
    zelle = ziel
    while zelle != start:
        vorher = eltern[zelle]
        zellen.append(_verbinde(zelle, vorher))
        zelle = vorher
    return list(reversed(zellen))
