"""Generate a printable, verified workbook page for each shipped level."""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pyti_app.levels import LEVELS
from level_atlas_routes import route_facts

FOCI = (
    (5, "Anweisungsfolge und erste Drehungen"),
    (15, "Bedingungen, Sensoren und einfache Umwege"),
    (25, "Planen, Schleifen und systematisches Prüfen"),
    (35, "Korridore, Kreuzungen und Fehlerbehandlung"),
    (50, "Komplexe Wege, robuste Schleifen und eigener Lösungsplan"),
    (60, "Erste Sprünge und kleine Labyrinthe"),
    (70, "Mehrere Sprungstellen und verschachtelte Korridore"),
    (80, "Komplexe Kammerlabyrinthe und Sensorplanung"),
    (90, "Dichte Labyrinthe und lange Sprungfolgen"),
    (100, "Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen"),
)


def render():
    lines = [
        "# Anhang A – Levelkarten und Arbeitsheft",
        "",
        "Diese 100 Arbeitsblätter beziehen sich auf die Standardlevel.",
        "Koordinaten und Wandzahlen stammen aus den Leveldaten; Mindestwege sind",
        "per Breitensuche auf dem Raster berechnet. Ein Schritt ist entweder",
        "Gehen oder ein Sprung über genau ein Feld; Drehungen zählen nicht.",
        "Ein Sprung ist nur über eine Wand möglich und landet auf einem freien Feld.",
        "Die Zahl kürzester Wege zählt alternative Aktionsrouten, nicht Skripte.",
        "Sie zählt keine Anzahl aller möglichen Programme. Jede Karte ist",
        "eine eigene Druckseite.",
        "",
    ]
    for number, (name, level) in enumerate(LEVELS.items(), 1):
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
            f"| Kürzester Weg (Gehen/Springen) | {shortest} Aktionen |",
            f"| Kürzeste Aktionsrouten | {routes} |",
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
