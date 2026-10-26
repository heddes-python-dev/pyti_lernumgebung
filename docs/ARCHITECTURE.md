# Architektur

## Ueberblick

Pyti ist eine Desktop-Anwendung mit PySide6. `main.py` ist der Einstiegspunkt;
die Implementierung ist in kleine Module unter `pyti_app/` gegliedert. Jede
Python-Datei bleibt unter 150 Zeilen. Die Anwendung arbeitet ohne Webserver
und externe Datenbank.

Der aktuelle Versionsstand steht in `VERSION`; die Release-Aenderungen werden
im `CHANGELOG.md` gepflegt. Version 1.2.0 ergaenzt Version 1.1.0 um die
Modularisierung, automatisierte Verhaltenstests, abbrechbare Skriptausfuehrung,
ein lokales Admin-Panel, interaktive Spielfeldbearbeitung und Level-Neustart.

## Komponenten

### Anwendung und Oberfläche

- `pyti_app/application.py` erstellt Qt-Objekte und verbindet Module.
- `pyti_app/ui_builder.py` lädt `game_window.ui` und baut die Widgets.
- `pyti_app/app_controller.py` steuert Levelwechsel, Level-Neustart, Start,
  Stopp und UI-Status.
- `pyti_app/admin_panel.py` bündelt lokale Statusprüfungen, Einstellungen,
  Levelverwaltung und Beispielskripte.
- `pyti_app/admin_store.py` validiert und speichert Admin-Daten als JSON im
  Benutzer-Konfigurationsordner.
- Die Root-Module `main.py`, `commands.py`, `playing_field.py`, `pyti.py`,
  `level.py`, `editor.py` und `highlighter.py` erhalten kurze
  Kompatibilitätsimporte.

### Spiellogik und Level

- `pyti_app/robot.py` enthält Bewegung, Blickrichtung und Beeper-Inventar.
- `pyti_app/field_manager.py` verwaltet Weltzustand, Sensoren und Zielprüfung.
- `pyti_app/field_rendering.py` zeichnet Raster, Wände, Pyti und Beeper.
- `pyti_app/field_view.py` verarbeitet Linksklicks zum Bearbeiten von Beepern
  und Rechtsklicks zum Setzen und Entfernen von Wänden.
- `pyti_app/level_creator_dialog.py` verwaltet den eigenständigen Creator;
  `level_creator_view.py` verarbeitet Werkzeugklicks und
  `level_creator_data.py` speichert validierte Entwürfe und erzeugt den
  optionalen Python-Export. `custom_levels.py` persistiert registrierte
  Level als validiertes JSON im Benutzer-Konfigurationsordner;
  `level_catalog.py` ergänzt sie zur Laufzeit in der Levelauswahl.
- `pyti_app/level_specs.py` speichert Missionsdaten; `level_generator.py`
  erzeugt Wandmuster und `levels.py` baut daraus die Levelsammlung.

### Skriptausführung und Editor

- `pyti_app/script_runtime.py` registriert Pyti-Befehle und führt Lernskripte
  mit einem Zeitlimit aus.
- `pyti_app/script_worker.py` führt Skripte im `QThread` aus und leitet
  Spielfeldzugriffe per Qt-Signal in den GUI-Thread.
- `pyti_app/admin_checks.py` prüft Imports, Spiellogik, Level-Erreichbarkeit
  und UI-Elemente ohne den aktuellen Spielzustand zu verändern.
- `pyti_app/editor.py` und `highlighter.py` implementieren Editor und
  Python-Syntax-Highlighting.

### `EXAMPLES.md`

- Enthält optionale Beispielprogramme vom Einstieg bis zur objektorientierten Programmierung.
- Wird nur auf Nachfrage über den Button `Beispiele` in einem separaten Dialog angezeigt.
- Der Dialog liest die Datei relativ zu `main.py`; fehlt die Datei, bleibt die Anwendung startfähig.

### Leveldefinitionen

Level werden aus den Spezifikationen in `pyti_app/level_specs.py` erzeugt. Ein
Level besitzt Startposition,
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

Die Anwendung prüft nach erfolgreicher Skriptausführung, ob Pyti am Ziel steht,
den Ziel-Beeper tatsächlich aufgenommen hat und ihn noch im Inventar trägt.

Richtungen sind numerisch kodiert:

- `0`: Norden
- `1`: Osten
- `2`: Sueden
- `3`: Westen

## Layout

Die UI-Datei liefert das Grundfenster. `pyti_app/ui_builder.py` setzt
Spielfeldansicht und Seitenleiste programmatisch zusammen. Qt-Layouts sorgen
dafuer, dass der Editor den verfuegbaren Platz erhaelt.

## Erweiterungspunkte

- Neue Level in `pyti_app/level_specs.py` ergaenzen.
- Neue Pyti-Aktionen in `pyti_app/script_runtime.py` registrieren.
- Neue Sensoren in `pyti_app/script_runtime.py` und
  `pyti_app/field_manager.py` implementieren.
- Eine sichere Ausfuehrungsumgebung fuer nicht vertrauenswuerdigen Code integrieren, falls Skripte aus externen Quellen akzeptiert werden sollen. Die aktuelle `exec()`-Ausfuehrung ist keine Sandbox.
