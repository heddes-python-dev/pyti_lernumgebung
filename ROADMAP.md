# Roadmap & TODO

Geplante Features, Ideen und Erweiterungen für Pyti. Die Punkte sind nach
Themen geordnet; die Reihenfolge innerhalb eines Abschnitts ist eine sinnvolle
Umsetzungsreihenfolge, keine verbindliche Terminplanung.

## Prioritäten aus der Logikprüfung

Der geprüfte Stand und die Belege sind in
[docs/LOGIKPRUEFUNG.md](docs/LOGIKPRUEFUNG.md) dokumentiert. Daraus ergeben
sich diese nächsten Schritte:

1. **P1:** Skriptfehler mit Typ, Meldung und Zeilennummer direkt in der
   Anwendung anzeigen.
2. **P1:** Eindeutigkeitsversprechen der Level-Missionen mit den tatsächlichen
   Levelwegen abgleichen.
3. **P2:** Veraltete Admin-Konfigurationswarnungen bei erneutem Einlesen
   zurücksetzen und regressionsprüfen.
4. **P2:** Den Interpreter-Lösungsdurchlauf für alle Level als dauerhaften
   Test ergänzen.
5. **P2/P3:** Fortschritt, Editorzustand, Geschwindigkeit und
   Installations-Smoke-Tests in der nachfolgenden Reihenfolge umsetzen.
6. **Bedingt:** Skriptisolation nur vorsehen, wenn nicht vertrauenswürdiger
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
- [ ] **Verständliche Fehlerausgabe:** Syntax- und Laufzeitfehler mit
  Fehlertyp, Meldung und Zeilennummer in der Anwendung anzeigen,
  statt sie nur in der Konsole auszugeben. Zeitlimit und Stopp-Funktion sind
  bereits umgesetzt; offen ist die verständliche Anzeige im Anwendungsfenster.
- [ ] **Admin-Warnungen erneuern:** Ladefehler beim erneuten Einlesen einer
  gültigen oder nicht vorhandenen Konfiguration löschen und den Ablauf
  „fehlerhafte Datei, danach erfolgreicher Ladevorgang“ testen.
- [ ] **Level-Missionen plausibilisieren:** Eindeutigkeitsversprechen in
  Missionstexten anhand eines ausdrücklich definierten Kriteriums prüfen und
  entweder Formulierungen oder Levelgeometrie anpassen.
- [ ] **Level im Interpreter regressionsprüfen:** Für jedes Standardlevel eine
  gültige Lösung mit tatsächlichen Pyti-Befehlen ausführen und das Erreichen
  des Ziels prüfen; der aktuelle Audit-Lauf ist noch kein dauerhafter Test.

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

- [ ] **Level-Creator-Modus:** Eigene Level grafisch auf dem Spielfeld
  erstellen und die passende Definition für `level.py` exportieren.

## Auslieferung

- [ ] **Installations-Smoke-Test:** Start, Laden der UI-Datei, Levelauswahl
  und ein minimales Lernskript auf den unterstützten Desktop-Umgebungen
  reproduzierbar prüfen.
- [ ] **Skripte aus fremden Quellen isolieren:** Nur erforderlich, falls
  nicht vertrauenswürdiger Code künftig ausgeführt werden soll. Die aktuelle
  `exec()`-Ausführung ist ausdrücklich keine Sandbox.
