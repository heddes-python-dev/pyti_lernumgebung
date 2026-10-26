"""Deterministische Generatoren für Levelpfade und Hindernisse."""

GRID_SIZE = 15


def grundpfad(start, ziel, variante):
    pfad = set()

    def abschnitt(von, nach):
        x, y = von
        pfad.add((x, y))
        dx = 1 if nach[0] >= x else -1
        while x != nach[0]:
            x += dx
            pfad.add((x, y))
        dy = 1 if nach[1] >= y else -1
        while y != nach[1]:
            y += dy
            pfad.add((x, y))

    if variante < 2:
        abschnitt(start, ziel)
    else:
        rand_x = GRID_SIZE - 2 if start[0] <= GRID_SIZE // 2 else 1
        rand_y = GRID_SIZE - 2 if start[1] <= GRID_SIZE // 2 else 1
        umweg = (rand_x, rand_y)
        abschnitt(start, umweg)
        abschnitt(umweg, ziel)
    return pfad


def waende_fuer(start, ziel, anzahl, variante):
    pfad = grundpfad(start, ziel, variante)
    kandidaten = []

    def l_pfad(vertikal_zuerst):
        x, y = start
        route = {(x, y)}
        if vertikal_zuerst:
            dy = 1 if ziel[1] >= y else -1
            while y != ziel[1]:
                y += dy
                route.add((x, y))
            dx = 1 if ziel[0] >= x else -1
            while x != ziel[0]:
                x += dx
                route.add((x, y))
        else:
            dx = 1 if ziel[0] >= x else -1
            while x != ziel[0]:
                x += dx
                route.add((x, y))
            dy = 1 if ziel[1] >= y else -1
            while y != ziel[1]:
                y += dy
                route.add((x, y))
        return route

    direkte_wege = l_pfad(False) | l_pfad(True)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if (x, y) in pfad:
                continue
            streifen = (x + variante) % 3 == 0
            schachbrett = (x + y + variante) % 2 == 0
            ring = max(abs(x - 7), abs(y - 7)) in (
                3 + variante % 3,
                5 + variante % 2,
            )
            if streifen or (variante >= 3 and schachbrett) or (
                variante >= 6 and ring
            ):
                kandidaten.append((x, y))

    kandidaten.sort(key=lambda punkt: (
        0 if punkt in direkte_wege - pfad else 1,
        (punkt[0] * 7 + punkt[1] * 11 + variante * 13) % 97,
        punkt[1],
        punkt[0],
    ))
    return kandidaten[:anzahl]


def baue_level(start, ziel, anzahl_waende, variante, mission):
    return {
        "start_x": start[0],
        "start_y": start[1],
        "start_richtung": 1,
        "waende": waende_fuer(start, ziel, anzahl_waende, variante),
        "beeper": [ziel],
        "goal": {"type": "collect_beeper", "position": ziel},
        "description": (
            f"Mission: {mission} Ziel: Erreiche den Beeper bei {ziel} und hebe ihn auf."
        ),
    }
