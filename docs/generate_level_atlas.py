"""Generate a printable, verified workbook page for each shipped level."""

import sys
from collections import deque
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS

FOCI = (
    (5, "Anweisungsfolge und erste Drehungen"),
    (15, "Bedingungen, Sensoren und einfache Umwege"),
    (25, "Planen, Schleifen und systematisches Prüfen"),
    (35, "Korridore, Kreuzungen und Fehlerbehandlung"),
    (50, "Komplexe Wege, robuste Schleifen und eigener Lösungsplan"),
)


def route_facts(start, goal, walls):
    distances = {start: 0}
    routes = {start: 1}
    queue = deque([start])
    while queue:
        point = queue.popleft()
        x, y = point
        for neighbor in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                not 0 <= neighbor[0] < GRID_SIZE
                or not 0 <= neighbor[1] < GRID_SIZE
                or neighbor in walls
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

def render():
    lines = [
        "# Anhang A – Levelkarten und Arbeitsheft",
        "",
        "Diese 50 Arbeitsblätter beziehen sich auf die mitgelieferte Levelsammlung.",
        "Koordinaten und Wandzahlen stammen aus den Leveldaten; Mindestwege sind",
        "per Breitensuche auf dem Raster berechnet und zählen nur Bewegungen,",
        "nicht Drehbefehle. Die Anzahl der kürzesten Wege zählt alternative",
        "Bewegungsrouten mit derselben Schrittzahl. Sie ist keine Anzahl aller",
        "möglichen Skripte. Jede Karte ist als eigenständige Druckseite gedacht.",
        "",
    ]
    for number, (name, level) in enumerate(LEVELS.items(), 1):
        if number > 1:
            lines.extend(["", r"\newpage", ""])
        start = level["start_x"], level["start_y"]
        goal = tuple(level["goal"]["position"])
        shortest, routes = route_facts(start, goal, set(map(tuple, level["waende"])))
        mission = level["description"].replace("<br>", " ").strip()
        focus = next(text for maximum, text in FOCI if number <= maximum)
        lines.extend([
            f"## Level {number:02d} – {name}",
            "",
            f"**{mission}**",
            "",
            "| Merkmal | Leveldaten |",
            "|---|---|",
            f"| Start | `{start}` |",
            f"| Startblickrichtung | {('Norden', 'Osten', 'Süden', 'Westen')[level['start_richtung']]} |",
            f"| Ziel | `{goal}` |",
            f"| Wände | {len(level['waende'])} |",
            f"| Kürzester Rasterweg | {shortest} Bewegungen |",
            f"| Kürzeste Bewegungsrouten | {routes} |",
            "",
            f"**Lernfokus:** {focus}.",
            "",
            "### Vor dem Programmieren",
            "",
            "1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.",
            "2. Markiere die Wände und nenne eine mögliche erste Entscheidung.",
            "3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.",
            "",
            "### Mein Lösungsplan",
            "",
            "Welche Teilstrecken oder Entscheidungen wiederholen sich?",
            "",
            "________________________________________________________________________",
            "",
            "Welche Sensoren oder Python-Konstrukte willst du verwenden?",
            "",
            "________________________________________________________________________",
            "",
            "### Test und Rückblick",
            "",
            "Was soll Pyti nach den ersten drei Aktionen tun?",
            "",
            "________________________________________________________________________",
            "",
            "Wo ist dein Programm zuerst anders gelaufen als erwartet?",
            "",
            "________________________________________________________________________",
            "",
            "Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?",
            "",
            "☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?",
            "",
            "________________________________________________________________________",
        ])
    lines.extend([
        "",
        r"\newpage",
        "",
        "## Lehrkraft- und Adminnotizen",
        "",
        "Vor der Ausgabe kann im Admin-Panel die lokale Levelkonfiguration",
        "angepasst werden. Die hier gedruckten Koordinaten beschreiben die",
        "mitgelieferten Standardlevel; nach Änderungen können sie abweichen.",
        "Eine Anpassung der Schwierigkeit kann über die Anzahl und Lage der",
        "Wände erfolgen. Vor dem Speichern muss der Ziel-Beper erreichbar bleiben.",
        "",
        "### Beobachtungsbogen",
        "",
        "| Lernende Person | Level | Beobachtung | Nächster Schritt |",
        "|---|---:|---|---|",
        "|  |  |  |  |",
        "|  |  |  |  |",
        "|  |  |  |  |",
        "|  |  |  |  |",
        "|  |  |  |  |",
        "",
        "### Freie Notizen",
        "",
        "________________________________________________________________________",
        "",
        "________________________________________________________________________",
        "",
        "________________________________________________________________________",
    ])
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    (ROOT / "BENUTZERHANDBUCH_LEVELATLAS.md").write_text(
        render(), encoding="utf-8"
    )
