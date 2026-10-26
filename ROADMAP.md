# Roadmap & TODO

Geplante Features, Ideen und Erweiterungen für Pyti. Die Punkte sind nach
Themen geordnet; die Reihenfolge innerhalb eines Abschnitts ist eine sinnvolle
Umsetzungsreihenfolge, keine verbindliche Terminplanung.

## Prioritäten aus der Logikprüfung

Der geprüfte Stand und die Belege sind in
[docs/LOGIKPRUEFUNG.md](docs/LOGIKPRUEFUNG.md) dokumentiert. Daraus ergeben
sich diese nächsten Schritte:

1. **P2/P3:** Fortschritt, Editorzustand, Geschwindigkeit und
   Installations-Smoke-Tests in der nachfolgenden Reihenfolge umsetzen.
2. **Bedingt:** Skriptisolation nur vorsehen, wenn nicht vertrauenswürdiger
   Code ausgeführt werden soll.

## Zuverlässigkeit & Ausführung

- [x] **Automatisierte Verhaltenstests:** Tests für Bewegung, Drehungen,
  Kollisionen, Sensoren, Beeper-Inventar, Zielprüfung und die Erreichbarkeit
  aller Level ergänzen. Damit wird die Spiellogik bei späteren Änderungen
  überprüfbar.
- [x] **Responsive, abbrechbare Skriptausführung:** Skripte außerhalb des
  GUI-Threads ausführen und eine Stopp-Funktion anbieten. Änderungen an der
  Oberfläche müssen sicher über Qt-Signale an den GUI-Thread übergeben werden.
  Das bereits vorhandene 30-Sekunden-Zeitlimit bleibt eine zusätzliche
  Absicherung, ersetzt aber weder responsive Bedienung noch einen Abbruchknopf.
- [x] **Verständliche Fehlerausgabe:** Syntax- und Laufzeitfehler mit
  Fehlertyp, Meldung und Zeilennummer in der Anwendung anzeigen,
  statt sie nur in der Konsole auszugeben. Zeitlimit und Stopp-Funktion sind
  bereits umgesetzt; Fehlerdetails erscheinen in der Statusanzeige und im
  Tooltip des Hauptfensters.
- [x] **Admin-Warnungen erneuern:** Ladefehler beim erneuten Einlesen einer
  gültigen oder nicht vorhandenen Konfiguration löschen und den Ablauf
  „fehlerhafte Datei, danach erfolgreicher Ladevorgang“ testen.
- [x] **Level-Missionen plausibilisieren:** Einzigartigkeitsversprechen gelten
  nur bei genau einer kürzesten Bewegungsroute auf dem Raster. Der Regressionstest
  prüft alle 100 Standardlevel und sichert entsprechende Missionstexte ab.
- [x] **Level im Interpreter regressionsprüfen:** Für jedes der 100
  Standardlevel eine kürzeste Route ermitteln, daraus ein Python-Skript mit
  echten Pyti-Befehlen erzeugen, es durch den Interpreter ausführen und das
  Erreichen des Ziel-Beepers prüfen.

## Gameplay & Motivation

- [x] **Automatisierte Zielprüfung:** Automatische Erkennung, wenn der
  Ziel-Beeper eingesammelt wurde, inklusive Erfolgsmeldung.
- [ ] **Fortschrittsspeicherung:** Abgeschlossene Level lokal (z. B. in einer
  JSON-Datei) speichern und beim nächsten Start wiederherstellen.
- [ ] **Lernpfad für Level:** Pro Level Lernziel, optionalen Tipp und eine
  kurze Reflexionsfrage anzeigen. Nach erfolgreichem Abschluss einen
  „Nächstes Level“-Weg anbieten.
- [ ] **Geschwindigkeitsregler:** Die Animationsgeschwindigkeit von
  beobachtend langsam bis schnell einstellbar machen.

## Editor & Usability

- [x] **Lokales Admin-Panel:** Funktionsprüfungen anzeigen, Einstellungen und
  Level grafisch bearbeiten sowie Beispielskripte ohne Quellcodeänderungen
  verwalten. Änderungen werden lokal gespeichert.
- [ ] **Code-Persistence:** Den eingegebenen Skripttext beim Levelwechsel
  zwischenspeichern und bei Bedarf wiederherstellen.
- [x] **Level-Neustart per Knopfdruck:** Den ausgewählten Level mit Startpunkt,
  Richtung, Beepern, Wänden und Inventar zurücksetzen; der Skripttext bleibt
  im Editor erhalten.
- [x] **Spielfeldbearbeitung per Maus:** Beeper per Linksklick und Wände per
  Rechtsklick setzen oder entfernen; ungültige Wandpositionen bleiben
  geschützt.

## Kreativ-Werkzeuge & Extras

- [x] **Level-Creator-Modus:** Eigene Level in einem separaten Dialog grafisch
  erstellen, Entwürfe lokal speichern und geprüfte Level automatisch in die
  Levelauswahl übernehmen; optional bleibt der Python-Quelltextexport.

## Auslieferung

- [ ] **Installations-Smoke-Test:** Start, Laden der UI-Datei, Levelauswahl
  und ein minimales Lernskript auf den unterstützten Desktop-Umgebungen
  reproduzierbar prüfen.
- [ ] **Skripte aus fremden Quellen isolieren:** Nur erforderlich, falls
  nicht vertrauenswürdiger Code künftig ausgeführt werden soll. Die aktuelle
  `exec()`-Ausführung ist ausdrücklich keine Sandbox.
