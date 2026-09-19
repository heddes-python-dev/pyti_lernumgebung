"""Leveldefinitionen mit ansteigendem Schwierigkeitsgrad.

Die Wandfelder blockieren komplette Spielfeldzellen. Jeder Level behält deshalb
einen berechneten Grundpfad vom Start zum Ziel frei. Zusätzliche Wände formen
mit wachsender Levelnummer Barrieren, Korridore und am Ende ein Labyrinth.
"""


GRID_SIZE = 15


def _grundpfad(start, ziel, variante):
    """Erzeugt mit wachsender Variante einen längeren sicheren Grundpfad."""
    pfad = set()

    def abschnitt(von, nach):
        x, y = von
        pfad.add((x, y))
        schritt_x = 1 if nach[0] >= x else -1
        while x != nach[0]:
            x += schritt_x
            pfad.add((x, y))
        schritt_y = 1 if nach[1] >= y else -1
        while y != nach[1]:
            y += schritt_y
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


def _waende_fuer(start, ziel, anzahl, variante):
    """Wählt Wände aus mehreren Mustern, ohne den Grundpfad zu blockieren."""
    pfad = _grundpfad(start, ziel, variante)
    kandidaten = []

    def l_pfad(vertikal_zuerst):
        x, y = start
        route = {(x, y)}
        if vertikal_zuerst:
            schritt_y = 1 if ziel[1] >= y else -1
            while y != ziel[1]:
                y += schritt_y
                route.add((x, y))
            schritt_x = 1 if ziel[0] >= x else -1
            while x != ziel[0]:
                x += schritt_x
                route.add((x, y))
        else:
            schritt_x = 1 if ziel[0] >= x else -1
            while x != ziel[0]:
                x += schritt_x
                route.add((x, y))
            schritt_y = 1 if ziel[1] >= y else -1
            while y != ziel[1]:
                y += schritt_y
                route.add((x, y))
        return route

    direkte_wege = l_pfad(False) | l_pfad(True)

    # Wechselnde Streifen erzeugen zunächst Barrieren und später Korridore.
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if (x, y) in pfad:
                continue
            streifen = (x + variante) % 3 == 0
            schachbrett = (x + y + variante) % 2 == 0
            ring = max(abs(x - 7), abs(y - 7)) in (3 + variante % 3, 5 + variante % 2)
            if streifen or (variante >= 3 and schachbrett) or (variante >= 6 and ring):
                kandidaten.append((x, y))

    # Die direkte Route wird zuerst blockiert. Die Auswahl bleibt dabei
    # deterministisch und wird nur einmal beim Import der Level berechnet.
    kandidaten.sort(key=lambda punkt: (
        0 if punkt in direkte_wege - pfad else 1,
        (punkt[0] * 7 + punkt[1] * 11 + variante * 13) % 97,
        punkt[1],
        punkt[0],
    ))
    return kandidaten[:anzahl]


def _level(name, start, ziel, anzahl_waende, variante, mission):
    return {
        "start_x": start[0],
        "start_y": start[1],
        "start_richtung": 1,
        "waende": _waende_fuer(start, ziel, anzahl_waende, variante),
        "beeper": [ziel],
        "goal": {"type": "collect_beeper", "position": ziel},
        "description": f"Mission: {mission} Ziel: Erreiche den Beeper bei {ziel} und hebe ihn auf.",
    }


_level_specs = [
    ("Der erste Beeper", (0, 0), (4, 0), 0, "Gehe geradeaus und lerne moveForward()."),
    ("Der erste Dreh", (0, 4), (4, 1), 1, "Verbinde Geradeauslaufen mit einer ersten Drehung."),
    ("Eine Wand", (0, 2), (5, 2), 2, "Umgehe die einzelne Blockade."),
    ("Zwei Richtungen", (1, 1), (6, 4), 3, "Wechsle zwischen horizontalem und vertikalem Weg."),
    ("Die Ecke", (0, 5), (5, 0), 4, "Finde den Weg um die Eckbarriere."),
    ("Kleine Treppe", (0, 8), (6, 3), 5, "Folge dem Verlauf der Treppenwände."),
    ("Zickzack", (0, 0), (7, 4), 6, "Schlängle dich durch die versetzten Wände."),
    ("Die Gasse", (0, 6), (8, 6), 7, "Suche den Eingang zur freien Gasse."),
    ("Sackgasse", (1, 1), (8, 7), 8, "Erkenne die Sackgasse und nimm den Umweg."),
    ("Der Tunnel", (0, 5), (9, 5), 9, "Bleibe im schmalen Korridor auf Kurs."),
    ("Kreuzung", (2, 2), (9, 8), 10, "Wähle an mehreren Kreuzungen den richtigen Weg."),
    ("Umweg nach Norden", (0, 9), (8, 1), 11, "Umgehe die Barrieren und arbeite nach Norden."),
    ("Umweg nach Süden", (8, 0), (2, 10), 12, "Plane einen sicheren Weg nach Süden."),
    ("Das Karree", (2, 2), (10, 2), 13, "Umkreise den blockierten Innenbereich."),
    ("Das Kreuz", (4, 4), (0, 0), 14, "Entkomme aus dem Kreuzungsbereich und erreiche den Beeper."),
    ("Doppelter Korridor", (0, 2), (11, 8), 15, "Navigiere durch zwei hintereinanderliegende Korridore."),
    ("Die Spirale", (1, 1), (10, 10), 16, "Folge dem spiralförmigen Wandmuster nach innen."),
    ("Das Tor", (5, 12), (5, 1), 17, "Finde die einzige günstige Durchfahrt durch die Barriere."),
    ("Wand-Slalom", (0, 10), (12, 4), 18, "Weiche den versetzten Wänden im Slalom aus."),
    ("Das L-Labyrinth", (1, 10), (12, 1), 19, "Umgehe zwei lange L-förmige Hindernisse."),
    ("Drei Kammern", (0, 0), (12, 8), 20, "Durchquere drei getrennte Wandbereiche."),
    ("Der Haken", (2, 2), (1, 12), 21, "Finde den Ausgang aus dem hakenförmigen Aufbau."),
    ("Diagonale", (0, 12), (12, 0), 22, "Arbeite dich an der diagonalen Wandstruktur vorbei."),
    ("Die Schleife", (1, 1), (13, 11), 23, "Verlasse die Schleife und halte auf das Ziel zu."),
    ("Korridor-Netz", (0, 7), (13, 7), 24, "Wähle im Korridornetz die passende Abzweigung."),
    ("Der Innenhof", (7, 13), (7, 1), 25, "Durchquere den Innenhof ohne an einer Wand zu enden."),
    ("Vier Abzweigungen", (0, 0), (13, 13), 26, "Prüfe an jeder Abzweigung die freie Richtung."),
    ("Das Fenster", (2, 12), (12, 2), 27, "Nutze die Öffnungen im Fenster-Muster."),
    ("Schlangengänge", (0, 1), (13, 12), 28, "Folge den geschwungenen Gängen bis zum Ausgang."),
    ("Die Ringmauer", (1, 7), (13, 7), 29, "Finde die Lücke in der Ringmauer."),
    ("Doppelschleuse", (0, 13), (13, 0), 30, "Passiere zwei Schleusen mit jeweils einer Öffnung."),
    ("Das Raster", (1, 1), (13, 13), 31, "Überquere das dichte Raster Schritt für Schritt."),
    ("Labyrinth Bronze", (0, 0), (13, 9), 32, "Finde den einzigen langen Weg durch das Labyrinth."),
    ("Labyrinth Silber", (2, 12), (12, 2), 34, "Nutze Sensoren, um Sackgassen zu erkennen."),
    ("Labyrinth Nord", (7, 13), (7, 0), 36, "Steige durch mehrere verschachtelte Korridore nach Norden."),
    ("Labyrinth Süd", (7, 0), (7, 13), 38, "Finde den Ausgang am anderen Ende des Labyrinths."),
    ("Das Irrgarten-Herz", (0, 7), (7, 7), 40, "Erreiche das Zentrum des großen Irrgartens."),
    ("Verlorene Kreuzung", (14, 14), (1, 1), 42, "Orientiere dich in einem dichten Kreuzungsnetz."),
    ("Die lange Schleife", (0, 14), (14, 0), 44, "Durchlaufe die lange Schleife ohne Abkürzung."),
    ("Labyrinth Gold", (1, 13), (13, 1), 46, "Finde im komplexen Muster den sicheren Zielkorridor."),
    ("Das große Labyrinth", (0, 0), (14, 14), 48, "Löse das vollständige Labyrinth mit Sensoren und Schleifen."),
    ("Meisterprüfung", (14, 14), (0, 0), 50, "Bewältige alle zuvor geübten Navigationsmuster."),
    ("Der letzte Korridor", (0, 7), (14, 7), 52, "Finde den versteckten Durchgang durch das Endspiel."),
    ("Vier Tore", (7, 14), (7, 0), 54, "Öffne gedanklich die vier Tore des Labyrinths."),
    ("Das Wendewerk", (0, 0), (14, 10), 56, "Plane viele Drehungen, ohne eine Sackgasse zu übersehen."),
    ("Die Tiefen", (14, 0), (0, 14), 58, "Dringe bis in die tiefste Kammer vor."),
    ("Labyrinth Diamant", (1, 1), (13, 13), 60, "Finde den Zielweg durch das nahezu vollständige Raster."),
    ("Der Endspurt", (0, 13), (14, 1), 62, "Halte trotz dichter Wände die Orientierung."),
    ("Meisterlabyrinth", (14, 14), (0, 0), 64, "Löse das anspruchsvollste bisherige Labyrinth."),
    ("Das große Finale", (0, 0), (14, 14), 66, "Finde den Weg zum letzten Beeper und beende die Lernstrecke."),
]


LEVELS = {
    f"0.0.{nummer} {name}": _level(
        name,
        start,
        ziel,
        anzahl_waende,
        nummer // 5,
        mission,
    )
    for nummer, (name, start, ziel, anzahl_waende, mission) in enumerate(_level_specs, 1)
}