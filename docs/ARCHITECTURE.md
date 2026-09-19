# Architektur

## Ueberblick

Pyti ist eine kleine Desktop-Anwendung mit PySide6. `main.py` verbindet die UI mit dem Spielfeld, dem Roboter und dem Befehlsinterpreter. Die Anwendung arbeitet bewusst ohne Webserver und ohne externe Datenbank.

Der aktuelle Versionsstand steht in `VERSION`; die Release-Aenderungen werden
im `CHANGELOG.md` gepflegt. Version 1.1.0 enthaelt die gestufte Levelsammlung,
die Zielpruefung, das optionale Beispiele-Fenster und die Unterstuetzung von
Pyti-Befehlen innerhalb eigener Klassen und Funktionen.

## Komponenten

### `main.py`

- Erstellt die Qt-Anwendung.
- Laedt `game_window.ui` ueber einen Pfad relativ zur Quelldatei.
- Baut die responsive Hauptansicht aus Spielfeldspalte und Seitenleiste auf.
- Verbindet Levelauswahl und Startbutton mit der Spiellogik.

### `playing_field.py`

- Verwaltet das 15x15-Raster.
- Zeichnet Raster, Pyti, Waende und Beeper in einer `QGraphicsScene`.
- Prueft Rand- und Wandkollisionen.
- Verarbeitet Mausklicks zum Platzieren und Entfernen von Beepern.

### `pyti.py`

- Enthaelt die Bewegungs- und Drehlogik.
- Verwaltet die Blickrichtung und das Beeper-Inventar.
- Loest bei Randkollisionen `PytiWandKollisionError` aus.

### `commands.py`

- Stellt die Lernbefehle im Skriptkontext bereit.
- Aktualisiert die Darstellung nach jeder Aktion.
- Gibt bei erfolgreicher Ausfuehrung `True`, bei Fehlern `False` zurueck.
- Verwendet eine kurze Qt-Ereignisschleife zwischen Aktionen, damit Animationen sichtbar bleiben.

### `EXAMPLES.md`

- Enthält optionale Beispielprogramme vom Einstieg bis zur objektorientierten Programmierung.
- Wird nur auf Nachfrage über den Button `Beispiele` in einem separaten Dialog angezeigt.
- Der Dialog liest die Datei relativ zu `main.py`; fehlt die Datei, bleibt die Anwendung startfähig.

### `level.py`

Level werden als Python-Dictionary beschrieben. Ein Level besitzt Startposition,
Startblickrichtung, Wände, Ziel-Beeper, eine Mission und ein maschinenlesbares
Ziel. Die Leveldatei erzeugt die Wandmuster so, dass ein Grundpfad zum Ziel frei
bleibt und die Wandanzahl mit der Levelnummer wächst.

```python
"Beispiel": {
    "start_x": 0,
    "start_y": 0,
    "start_richtung": 1,
    "waende": [(2, 1)],
    "beeper": [(4, 0)],
    "goal": {"type": "collect_beeper", "position": (4, 0)},
    "description": "Mission: Umgehe die Wand. Ziel: Erreiche den Beeper und hebe ihn auf."
}
```

Die Anwendung prüft nach erfolgreicher Skriptausführung, ob Pyti am Ziel steht
und den Ziel-Beeper aufgenommen hat.

Richtungen sind numerisch kodiert:

- `0`: Norden
- `1`: Osten
- `2`: Sueden
- `3`: Westen

## Layout

Die UI-Datei liefert nur das Grundfenster mit Spielfeldplatzhalter und Startbutton. `main.py` ersetzt den Platzhalter durch `SpielfeldView` und erstellt die Seitenleiste programmatisch. Qt-Layouts sorgen dafuer, dass der Editor den verfuegbaren Platz erhaelt, ohne Hilfe, Levelauswahl oder Startbutton zu ueberdecken.

## Erweiterungspunkte

- Neue Level in `level.py` ergaenzen.
- Neue Pyti-Aktionen in `commands.py` registrieren.
- Neue Sensoren in `commands.py` und `playing_field.py` implementieren.
- Eine sichere Ausfuehrungsumgebung fuer nicht vertrauenswuerdigen Code integrieren, falls Skripte aus externen Quellen akzeptiert werden sollen. Die aktuelle `exec()`-Ausfuehrung ist keine Sandbox.
