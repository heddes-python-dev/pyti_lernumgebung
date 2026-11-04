# Roadmap & TODO

Geplante Features, Ideen und Erweiterungen für Pyti. Die Punkte sind nach
Themen geordnet; die Reihenfolge innerhalb eines Abschnitts ist eine sinnvolle
Umsetzungsreihenfolge, keine verbindliche Terminplanung.

Die [pädagogische Lernweg-Roadmap](docs/LERNWEG_ROADMAP.md) beschreibt die
Lernprogression und Erprobung. Diese Datei fokussiert auf technische
Entwicklung und Projektbereitschaft.

## Open Source und Einsatz in Schulen

Ziel ist, Pyti als offenes, gemeinschaftlich weiterentwickeltes Lernwerkzeug
bekannt zu machen und es schrittweise für begleitete Schuleinsätze
vorzubereiten. Der öffentliche Quellcode und ein GitHub-Release sind wichtige
Anfangsschritte, aber noch keine Freigabe für unbeaufsichtigten Schuleinsatz.

### 1. Projekt auffindbar und verständlich machen

- [ ] GitHub-Projektbeschreibung, Themen und README-Einstieg auf Zielgruppe,
  Lernziele, unterstützte Systeme und aktuellen Projektstatus abstimmen.
- [ ] Einen kurzen Screenshot oder eine Demo sowie einen schnellen
  Installations- und Startweg prominent anbieten.
- [x] Eine klare Anlaufstelle für Fehlerberichte, Ideen und Fragen benennen;
  auf Beiträge und Rückmeldungen zeitnah reagieren.
- [x] Eine README-Sektion mit offenen `good first issue`-Aufgaben als Einstieg
  für neue Mitwirkende pflegen.
- [ ] Releases mit nachvollziehbaren Änderungen, getesteten Downloads und
  bekannten Einschränkungen pflegen.

### 2. Beiträge einfach und sicher ermöglichen

- [x] `CONTRIBUTING.md` mit Entwicklungsinstallation, Tests, Stilregeln,
  Branch-/Pull-Request-Ablauf und Hinweisen für neue Mitwirkende ergänzen.
- [x] GitHub-Vorlagen für Fehlerberichte und Funktionsideen einrichten; bei
  Fehlerberichten Betriebssystem, Python-Version und reproduzierbare Schritte
  abfragen, aber keine persönlichen oder sensiblen Daten erbitten.
- [x] CI für unterstützte Python-Versionen und Desktop-Betriebssysteme
  einrichten: Tests, Syntax- und Größenprüfungen sowie Paket-/Start-Smoke-Test.
- [x] Review-, Release- und Sicherheitsverantwortung in
  `GOVERNANCE.md`/`SECURITY.md` festlegen. Aktuell ist
  `@heddes-python-dev` verantwortlich; vertrauliche Sicherheitsmeldungen und
  Dependabot-Sicherheitsupdates sind aktiviert. GitHub-Branch-Protection ist
  noch nicht aktiv und wird erst mit einer zweiten unabhängigen
  Maintainer-Person verpflichtend eingerichtet. Pull Requests und Releases
  müssen die CI bestehen; reale externe Beiträge werden nach Eingang reviewed.

### 3. Pädagogische Qualität mit Schulen erproben

- [ ] Für Lernpfade Zielgruppe, benötigte Vorkenntnisse, Lernziele,
  Aufgabenschritte, Hinweise und Erfolgskriterien je Einheit definieren.
- [ ] Aufgaben und Handbuch mit Lehrkräften und Lernenden erproben; Feedback
  zu Verständlichkeit, Schwierigkeit, Unterrichtsdauer und Barrierefreiheit
  dokumentieren und in konkrete Verbesserungen überführen.
- [ ] Altersgerechte Sprache, Tastaturbedienung, Kontraste, Skalierung und
  Screenreader-Nutzbarkeit prüfen; Einschränkungen offen dokumentieren.
- [ ] Installations-, Update- und Wiederherstellungsabläufe auf den tatsächlich
  in Schulen verwendeten Geräten und Betriebssystemen testen.
- [ ] Verantwortlichkeiten, Supportgrenzen und einen Prozess zum Melden und
  Bearbeiten von Sicherheitsproblemen veröffentlichen.

### 4. Sicherheitsfreigabe vor breitem Schuleinsatz

- [x] Skriptausführung und Bedrohungsgrenze neu bewerten: uneingeschränktes
  `exec()` im App-Prozess, Zeitlimit und Stoppknopf bieten keine Isolation.
  Das derzeitige Ziel ist deshalb auf Linux mit bubblewrap beschränkt.
- [x] Linux-Isolation implementieren: Kindprozess in User-, PID-, Netzwerk-
  und weiteren Namespaces, temporäres Root-Dateisystem mit Positivliste der
  benötigten Python-Laufzeit und Systembibliotheken, begrenzte temporäre
  Dateisysteme, Prozess-/CPU-/Speicherlimits, begrenztes Aktionsprotokoll und
  fail-closed Verhalten. Automatisierte Tests prüfen unter anderem, dass
  Hostdateien nicht sichtbar oder veränderbar sind, dass Netzwerkzugriff
  blockiert ist sowie Fehlerweitergabe und Timeout.
- [ ] Die Isolation unabhängig prüfen und mit adversarialen Tests auf den
  tatsächlich verwendeten Schul-Linux-Systemen absichern. Bis zur Prüfung
  keine Nutzung mit nicht vertrauenswürdigen Skripten und keine Kindertests
  auf normalen Rechnern freigeben. Auf macOS und Windows bleibt die
  Skriptausführung deaktiviert.
- [x] Aktuellen Datenschutz- und Speicherumfang prüfen: kein Konto, keine
  Datenbank und keine App-Telemetrie; Admin- und eigene Leveldaten liegen
  lokal. Künftige Telemetrie oder Online-Funktionen erfordern eine gesonderte
  Prüfung und transparente Zustimmung.

Ein breiter Schuleinsatz gilt erst dann als vorbereitet, wenn die offenen
Sicherheits-, Installations-, Bedienbarkeits- und Pilotkriterien überprüft
und mit Belegen dokumentiert sind. MIT-Lizenz und öffentlicher Quellcode
allein bedeuten keine Sicherheits- oder Qualitätszertifizierung.

### Stufenweise Erprobungsfreigabe

„Intern testen“ und „Kindern zur Erprobung geben“ sind unterschiedliche
Freigabestufen:

- **Interner Funktionstest durch Projektverantwortliche:** Kann mit eigenen,
  vertrauenswürdigen Skripten auf Linux mit funktionierender bubblewrap-
  Isolation stattfinden. Dabei App-Ablauf, Levelneustart, Editorzustand,
  Hilfetexte und Fehleranzeigen prüfen. Keine fremden oder unbekannten
  Skripte ausführen.
- **Begleiteter Test mit Kindern, die Code verändern und starten:** Noch
  nicht freigegeben. Die Isolation ist implementiert, aber nicht unabhängig
  geprüft; Erwachsenenaufsicht allein ersetzt diese Prüfung und die
  Freigabevoraussetzungen für den konkreten Pilot nicht.
- **Freigabe für einen begleiteten Kindertest:** Erst nach dokumentierter
  unabhängiger Sicherheitsbewertung und einer zur Bedrohung passenden,
  überprüften Ausführungsbegrenzung; zusätzlich müssen Installationsweg,
  Wiederherstellung, Datenschutz, Einwilligungen und Zuständigkeiten für den
  konkreten Pilot geklärt sein. Falls diese Bedingungen nicht erfüllt sind,
  nur mit einer kontrollierten Umgebung testen, in der keine persönlichen
  oder wichtigen Daten und keine vertraulichen Zugänge erreichbar sind; diese
  Maßnahme ist keine Sandbox und keine allgemeine Freigabe.
- **Breiter Schuleinsatz:** Bleibt gesperrt, bis auch die übrigen
  Sicherheits-, Plattform-, Barrierefreiheits- und Supportkriterien erfüllt
  und dokumentiert sind. Die derzeitige bubblewrap-Implementierung allein
  stellt keine Sicherheitsfreigabe dar.

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
- [x] **Level-Missionen plausibilisieren:** Eindeutigkeitsversprechen werden
  nur bei genau einer kürzesten Bewegungsroute verwendet; beschriebene
  Hindernisse müssen den Weg tatsächlich beeinflussen. Regressionstests
  prüfen entsprechende Missionstexte, die frühe Geometrie und alle 100
  Standardlevel.
- [x] **Level im Interpreter regressionsprüfen:** Für jedes der 100
  Standardlevel eine kürzeste Route ermitteln, daraus ein Python-Skript mit
  echten Pyti-Befehlen erzeugen, es durch den Interpreter ausführen und das
  Erreichen des Ziel-Beepers prüfen.

## Gameplay & Motivation

- [x] **Automatisierte Zielprüfung:** Automatische Erkennung, wenn der
  Ziel-Beeper eingesammelt wurde, inklusive Erfolgsmeldung.
- [x] **Geführte erste Mission:** Levelabhängiges vollständiges Beispiel,
  eine einzelne sinnvolle Lücke, drei gestufte Tipps und nach den Tipps
  freischaltbare Lösung für die ausgewählten frühen Level. Technisch
  automatisiert geprüft; pädagogische Erprobung bleibt in der
  [Lernweg-Roadmap](docs/LERNWEG_ROADMAP.md) offen.
- [ ] **Fortschrittsspeicherung:** Abgeschlossene Level lokal (z. B. in einer
  JSON-Datei) speichern und beim nächsten Start wiederherstellen.
- [ ] **Lernpfad für Level:** Pro Level Lernziel, optionalen Tipp und eine
  kurze Reflexionsfrage anzeigen. Nach erfolgreichem Abschluss einen
  „Nächstes Level“-Weg anbieten.
- [ ] **Geschwindigkeitsregler:** Die Animationsgeschwindigkeit von
  beobachtend langsam bis schnell einstellbar machen.

## Editor & Usability

- [x] **Lokales Admin-Panel:** Funktionsprüfungen anzeigen, Einstellungen und
  Level grafisch bearbeiten, eigene Level nach Bestätigung löschen sowie
  Beispielskripte ohne Quellcodeänderungen verwalten. Änderungen werden lokal
  gespeichert; Standardlevel sind vor dem Löschen geschützt.
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
  erstellen, Entwürfe lokal speichern, geprüfte Level automatisch in die
  Levelauswahl übernehmen und gespeicherte eigene Level wieder löschen;
  Standardlevel bleiben geschützt, optional bleibt der Python-Quelltextexport.

## Auslieferung

- [ ] **Installations-Smoke-Test:** Start, Laden der UI-Datei, Levelauswahl
  und ein minimales Lernskript auf den unterstützten Desktop-Umgebungen
  reproduzierbar prüfen.
- [ ] **Skripte aus fremden Quellen isolieren:** Nur erforderlich, falls
  nicht vertrauenswürdiger Code künftig ausgeführt werden soll. Die aktuelle
  `exec()`-Ausführung ist ausdrücklich keine Sandbox.
