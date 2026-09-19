# Changelog

Alle bemerkenswerten Aenderungen dieses Projekts werden hier dokumentiert.

## [1.1.0] - 2026-09-19

### Hinzugefuegt

- 50 Level mit ansteigendem Schwierigkeitsgrad von Einzelbarrieren bis zum Labyrinth
- Maschinenlesbare Levelziele und Erfolgsmeldung nach dem Aufnehmen des Ziel-Beepers
- Optionales Beispiele-Fenster fuer `EXAMPLES.md`
- Missionstexte fuer alle Level mit erreichbaren Zielpositionen

### Verbessert

- Klassen und eigene Funktionen koennen Pyti-Befehle im Skript verwenden
- Level werden beim Programmstart schnell und deterministisch erzeugt
- Dokumentation zu Installation, Architektur, Sicherheit und lokaler Pruefung erweitert

## [1.0.0] - 2026-09-19

### Hinzugefuegt

- PySide6-Desktopanwendung fuer die Roboterlernwelt Pyti
- 15x15-Spielfeld mit Raster, Waenden und Beepern
- 50 spielbare Level mit Missionsbeschreibungen
- Python-Code-Editor mit Zeilennummern und Syntax-Highlighting
- Bewegungs-, Dreh-, Beeper- und Sensorbefehle
- Interaktive Beeper-Platzierung per Mausklick
- Responsive Fensteraufteilung mit grossem Editorbereich
- Dokumentation und festgelegte PySide6-Abhaengigkeit ueber `requirements.txt`

### Technische Hinweise

- Skripte werden mit `exec()` im Prozess der Anwendung ausgefuehrt.
- Nur vertrauenswuerdige Skripte ausfuehren.
