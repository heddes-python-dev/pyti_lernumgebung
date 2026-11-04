"""Erstellt sichere Vorlagen für den tatsächlich ausgewählten Level."""

from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class ErsteMissionDaten:
    beschreibung: str
    starter_code: str
    luecken_code: str
    loesung_code: str
    hinweise: tuple[str, str, str]


RICHTUNGEN = {
    0: ((0, -1), "nach oben"),
    1: ((1, 0), "nach rechts"),
    2: ((0, 1), "nach unten"),
    3: ((-1, 0), "nach links"),
}


def erstelle_erste_mission(level):
    start = (level["start_x"], level["start_y"])
    richtung, richtungstext = RICHTUNGEN[level["start_richtung"]]
    ziel = tuple(level["goal"]["position"])
    weg = _kuerzester_weg(start, level["start_richtung"], ziel, level["waende"])
    if weg is None:
        return None

    weg_ohne_waende = _kuerzester_weg(
        start, level["start_richtung"], ziel, []
    )
    wandhinweis = (
        "Achte auf die Wand im direkten Weg."
        if len(weg) > len(weg_ohne_waende)
        else "Prüfe Startblickrichtung und freie Felder."
    )
    loesung_zeilen = weg + ["pickBeeper()"]
    starter_code = "\n".join(loesung_zeilen) + "\n"
    dreh_index = next(
        (index for index, befehl in enumerate(weg) if befehl.startswith("turn")),
        None,
    )
    if dreh_index is not None:
        fehlende_aktion = weg[dreh_index]
        luecken_zeilen = list(weg)
        luecken_zeilen[dreh_index] = (
            "# Fuege hier " + fehlende_aktion + " ein."
        )
        luecken_zeilen.append("pickBeeper()")
    elif len(weg) > 1:
        fehlende_aktion = weg[-1]
        luecken_zeilen = weg[:-1] + [
            "# Fuege hier " + fehlende_aktion + " ein.",
            "pickBeeper()",
        ]
    else:
        fehlende_aktion = "pickBeeper()"
        luecken_zeilen = weg + [
            "# Fuege hier " + fehlende_aktion + " ein."
        ]
    luecken_code = "\n".join(luecken_zeilen) + "\n"

    bewegungen = weg.count("moveForward()")
    drehungen = len(weg) - bewegungen
    bewegungstext = "Bewegungsschritt" if bewegungen == 1 else "Bewegungsschritte"
    drehungstext = "Drehung" if drehungen == 1 else "Drehungen"
    hinweise = (
        f"Pyti startet und schaut {richtungstext}. {wandhinweis}",
        f"Die Route braucht {bewegungen} {bewegungstext} und "
        f"{drehungen} {drehungstext}.",
        f"Die fehlende Aktion ist {fehlende_aktion}.",
    )
    feld = "Befehl" if len(weg) == 1 else "Befehle"
    beschreibung = (
        f"Pyti schaut {richtungstext}. "
        f"Ein kürzester sicherer Weg zum Beeper braucht {len(weg)} {feld} "
        f"({bewegungen} {bewegungstext} und {drehungen} {drehungstext}). "
        "Das vollständige Beispiel enthält auch pickBeeper(). "
        + (
            "In der Lückenvorlage fehlt ein Richtungswechsel."
            if dreh_index is not None
            else "In der Lückenvorlage fehlt nur der letzte Wegbefehl."
            if len(weg) > 1
            else "In der Lückenvorlage fehlt nur pickBeeper()."
        )
    )
    return ErsteMissionDaten(
        beschreibung=beschreibung,
        starter_code=starter_code,
        luecken_code=luecken_code,
        loesung_code=starter_code,
        hinweise=hinweise,
    )


def _kuerzester_weg(start, richtung, ziel, waende):
    deltas = ((0, -1), (1, 0), (0, 1), (-1, 0))
    walls = {tuple(wand) for wand in waende}
    anfang = (*start, richtung)
    queue = deque([anfang])
    vorherige = {anfang: None}
    befehle = {}
    ende = None
    while queue:
        x, y, blick = queue.popleft()
        if (x, y) == ziel:
            ende = (x, y, blick)
            break
        dx, dy = deltas[blick]
        nachbarn = (
            ((x, y, (blick - 1) % 4), "turnLeft()"),
            ((x, y, (blick + 1) % 4), "turnRight()"),
            ((x + dx, y + dy, blick), "moveForward()"),
        )
        for zustand, befehl in nachbarn:
            nx, ny, _ = zustand
            if (
                not 0 <= nx < 15 or not 0 <= ny < 15
                or (befehl == "moveForward()" and (nx, ny) in walls)
                or zustand in vorherige
            ):
                continue
            vorherige[zustand] = (x, y, blick)
            befehle[zustand] = befehl
            queue.append(zustand)
    if ende is None:
        return None
    weg = []
    while vorherige[ende] is not None:
        weg.append(befehle[ende])
        ende = vorherige[ende]
    return list(reversed(weg))
