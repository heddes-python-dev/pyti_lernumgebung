# Pyti Lernumgebung

Aktuelle Version: **1.1.0**

Eine lokale Lernumgebung fuer Python und algorithmisches Denken. In einer grafischen PySide6-Anwendung programmiert man den Roboter Pyti, navigiert durch ein 15x15-Spielfeld und loest Level mit Waenden und Beepern.

## Funktionen

- Interaktives 15x15-Spielfeld
- 50 vorgefertigte Level mit Missionen
- Ansteigender Schwierigkeitsgrad von Einzelwänden bis zum Labyrinth
- Automatische Prüfung, ob der Ziel-Beeper aufgenommen wurde
- Editor mit Zeilennummern, Python-Syntax-Highlighting und Tab-Unterstuetzung
- Optionales Beispiele-Fenster mit Inhalten aus `EXAMPLES.md`
- Roboterbewegung mit sichtbarer Richtungsanzeige
- Waende, Randkollisionen und Beeper
- Beeper aufnehmen und ablegen
- Sensorfunktionen fuer Bedingungen und Schleifen
- Beeper koennen per Mausklick auf dem Spielfeld platziert oder entfernt werden
- Responsive Oberflaeche mit grossem Editorbereich

## Voraussetzungen

- Python 3.10 oder neuer
- PySide6
- Ein Desktop-System mit Qt-Unterstuetzung

## Installation

```bash
git clone <REPOSITORY-URL>
cd pyti_lernprogramm
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Abhaengigkeiten installieren:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Start

```bash
python main.py
```

Das Programm laedt die UI-Datei relativ zu `main.py`. Es kann daher auch aus einem anderen Arbeitsverzeichnis gestartet werden.

## Erste Schritte

1. Waehle rechts ein Level aus.
2. Schreibe ein Python-Skript in den Editor.
3. Klicke auf `Start`.
4. Beobachte Pyti auf dem Spielfeld.
5. Platziere zusaetzliche Beeper bei Bedarf mit einem Mausklick auf ein Feld.

Beispiel:

```python
while frontClear():
    moveForward()

if onBeeper():
    pickBeeper()
```

## Verfuegbare Befehle

### Aktionen

| Befehl | Beschreibung |
| --- | --- |
| `moveForward()` | Einen Schritt in Blickrichtung gehen |
| `turnLeft()` | 90 Grad nach links drehen |
| `turnRight()` | 90 Grad nach rechts drehen |
| `turnAround()` | 180 Grad drehen |
| `pickBeeper()` | Beeper vom aktuellen Feld aufnehmen |
| `dropBeeper()` | Einen Beeper aus dem Inventar ablegen |

### Sensoren

| Sensor | Rueckgabe |
| --- | --- |
| `onBeeper()` | `True`, wenn auf dem aktuellen Feld ein Beeper liegt |
| `beeperAhead()` | `True`, wenn direkt vor Pyti ein Beeper liegt |
| `frontClear()` | `True`, wenn das Feld vor Pyti frei ist |
| `leftClear()` | `True`, wenn das Feld links frei ist |
| `rightClear()` | `True`, wenn das Feld rechts frei ist |
| `anyBeeperInBag()` | `True`, wenn Pyti mindestens einen Beeper traegt |

Da der Editor Python-Code ausfuehrt, koennen auch `if`, `while`, Variablen und Funktionen verwendet werden.

## Projektstruktur

```text
.
├── main.py              # Anwendungseinstieg und UI-Aufbau
├── game_window.ui       # Qt-Grundfenster
├── commands.py          # Pyti-Befehle und Skriptausfuehrung
├── pyti.py              # Roboter, Bewegung und Beeper-Inventar
├── playing_field.py     # Raster, Rendering, Level- und Sensorlogik
├── editor.py            # Code-Editor mit Zeilennummern
├── highlighter.py       # Python-Syntax-Highlighting
├── EXAMPLES.md          # Beispielprogramme und Programmiermuster
├── level.py             # Leveldefinitionen
├── requirements.txt     # Python-Abhaengigkeiten
├── VERSION              # Aktuelle Version
└── docs/
    └── ARCHITECTURE.md  # Technische Architektur
```

## Tests und lokale Pruefung

Automatisierte Verhaltenstests sind derzeit noch nicht enthalten. Die folgenden
Befehle pruefen die Python-Syntax und den Start der Anwendung.

Syntaxpruefung:

```bash
python -m py_compile main.py commands.py playing_field.py pyti.py editor.py highlighter.py level.py
```

Headless-Start unter Linux:

```bash
QT_QPA_PLATFORM=offscreen python main.py
```

Fuer einen kurzen Smoke-Test kann der Prozess mit `timeout` beendet werden:

```bash
timeout 2s env QT_QPA_PLATFORM=offscreen python main.py
```

## Sicherheitswarnung

Die Anwendung verwendet in `commands.py` `exec()`, damit Lernende normalen Python-Code mit den bereitgestellten Pyti-Befehlen schreiben koennen. Die Ausfuehrung erfolgt im Prozess der Anwendung und hat Zugriff auf die verfuegbaren Python-Builtins. Dadurch kann ein Skript grundsaetzlich auch Dateien lesen oder veraendern und Prozesse starten. Fuehre deshalb nur vollstaendig vertrauenswuerdige Skripte aus. Die Anwendung ist keine Sandbox fuer fremden oder nicht vertrauenswuerdigen Code.

## Versionierung

Die aktuelle Version steht in [VERSION](VERSION). Aenderungen werden in [CHANGELOG.md](CHANGELOG.md) dokumentiert. Das Projekt verwendet Semantic Versioning:

- `MAJOR`: inkompatible Aenderungen
- `MINOR`: neue abwaertskompatible Funktionen
- `PATCH`: Fehlerkorrekturen

## Lizenz

Vor einer Veroeffentlichung auf GitHub muss eine passende Lizenzdatei ergaenzt werden. Ohne Lizenz gelten standardmaessig die gesetzlichen Urheberrechte; andere duerfen den Code dann nicht automatisch veraendern oder weiterveroeffentlichen.

## GitHub-Check

Vor dem ersten Push sollten diese lokalen Pruefungen erfolgreich sein:

```bash
python -m py_compile main.py commands.py playing_field.py pyti.py editor.py highlighter.py level.py
QT_QPA_PLATFORM=offscreen timeout 2s python main.py
```

Das Projekt benoetigt keine Datenbank und keinen Build-Schritt. Fuer einen
oeffentlichen Upload sollte ausserdem eine Lizenz ausgewaehlt und als `LICENSE`
Datei abgelegt werden.
