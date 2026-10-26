# Changelog

Alle bemerkenswerten Aenderungen dieses Projekts werden hier dokumentiert.

## [1.4.0] - 2026-10-26

### Hinzugefuegt

- Standardlevel von 50 auf 100 erweitert; die Levelnummerierung reicht
  gestuft von `0.0.1` bis `1.0.0`.
- Neue Sprungaktion `jump()`, die genau eine Wand überwindet, und zunehmend
  komplexe, reproduzierbar erzeugte Labyrinthe mit Sprungbarrieren.
- Druckbares A4-Handbuch mit 100 Level-Arbeitsblättern.

### Verbessert

- Sprünge sind nur über eine Wand auf ein freies Landefeld möglich; die
  Erreichbarkeitsprüfung, Admin-Prüfungen und Labyrinthgenerierung verwenden
  dieselbe Regel.
- Alle Standardlevel werden automatisiert mit echten Pyti-Befehlen über den
  Interpreter gelöst und auf das Erreichen des Ziels geprüft.
- Dokumentation und Logikprüfung an den Umfang von 100 Leveln angepasst.

## [1.3.0] - 2026-10-26

### Hinzugefuegt

- Grafischer Level-Creator mit mehreren lokal gespeicherten Entwürfen,
  geprüfter Spielfeldbearbeitung, automatischer Levelregistrierung und
  optionalem Python-Quelltextexport. Eigene Level werden ohne manuelle
  Änderung an Python-Dateien sofort und dauerhaft in Pyti übernommen.
- Skriptfehler mit Zeilennummer direkt in der Oberfläche anzeigen.

### Verbessert

- Admin-Systemcheck akzeptiert eigene Level zusätzlich zu den Standardleveln.
- Benutzerhandbuch um Creator-Ablauf und automatische Levelregistrierung
  ergänzt.

## [1.2.0] - 2026-10-26

### Hinzugefuegt

- Admin-Panel mit Systemstatus, lokalen Einstellungen, Levelbearbeitung und
  Verwaltung von Beispielskripten
- Spielfeldbearbeitung mit Beeper per Linksklick und Waenden per Rechtsklick
- Knopf zum Zuruecksetzen des ausgewaehlten Levels auf den Startzustand
- Abbrechbare Skriptausfuehrung im Hintergrund mit Qt-Signalbruecke
- Verhaltenstests fuer Spiellogik, Level, Editor, Mausbedienung, Admin-Panel
  und Skriptworker
- Ausfuehrliches druckbares Handbuch mit 50 Level-Arbeitsblaettern
- Dokumentierte Logik- und Plausibilitaetspruefung mit priorisierten
  naechsten Schritten

### Verbessert

- Anwendung in Module unter `pyti_app/` gegliedert; Root-Module bleiben als
  Kompatibilitaetsimporte erhalten
- Zeilennummern im Editor werden fuer alle sichtbaren Zeilen korrekt gezeichnet
- Level-, Wand-, Beeper- und Inventarlogik durch Tests abgesichert
- README, Architektur, Roadmap und Benutzerhandbuch an den Funktionsumfang
  angepasst

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
