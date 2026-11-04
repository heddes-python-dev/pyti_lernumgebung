# Pyti-Lernweg: pädagogische Roadmap

Diese Roadmap beschreibt, wie Pyti vom ersten Ausprobieren zu zunehmend
selbstständigem Programmieren führen kann. Sie ergänzt die technische
[Projekt-Roadmap](../ROADMAP.md), ersetzt sie aber nicht. Die Phasen sind
inhaltliche Schritte und keine verbindlichen Veröffentlichungstermine.

**Status, 3. November 2026:** Phase 1 ist als Entwurfs- und Klärungsphase
abgeschlossen. Die Einstiegsmission aus Phase 2 und die ersten Vorlagen und
Hilfen aus Phase 3 sind implementiert und automatisiert geprüft. Eine
Erprobung mit Lernenden fand noch nicht statt. Daraus folgt weder eine
pädagogische Wirksamkeits- noch eine allgemeine Eignungsaussage. Wegen der
Ausführung regulärer Python-Skripte ohne Sandbox ist ein Kindertest auf einem
normalen Rechner derzeit nicht freigegeben; siehe
[technische Roadmap](../ROADMAP.md).

## Rolle der drei Programme

- **Pyti Lernumgebung** ermöglicht den ersten Kontakt mit Programmierung:
  Lernende geben Befehle, beobachten die Wirkung am Roboter und entwickeln
  schrittweise eigene Lösungen.
- **Pyti Inspector** ist ein optionaler, eigenständiger Begleiter. Er kann
  sichtbar machen, welche Befehle, Sensorwerte und Zustände während eines
  Pyti-Skripts auftreten. Er ist weder Voraussetzung für Pyti noch ein eigener
  Python-Kurs.
- **LearnPython IDE** ist ein eigenständiges Angebot für späteres,
  systematisches Pythonlernen. Es setzt einen anderen Lernrahmen und muss
  nicht in Pyti integriert werden.

Die Programme bleiben eigenständig. Ein sinnvoller Lernweg entsteht durch
verständliche Inhalte und freiwillige Übergänge, nicht durch eine gemeinsame
Oberfläche, ein gemeinsames Konto oder synchronisierte Daten.

## Leitlinien

- Mit konkreten Aktionen und sichtbarer Rückmeldung beginnen; Syntax nur
  einführen, wenn sie für die nächste Aufgabe gebraucht wird.
- Erst verstehen lassen, was ein Programm tut, dann schrittweise erklären,
  wie Python das ausdrückt.
- Vorhersagen, Ausführen und Erklären miteinander verbinden.
- Spielfeldschwierigkeit und Programmierkompetenz getrennt planen.
- Hilfen anbieten, ohne eine einzige korrekte Lösungsstrategie vorzuschreiben.
- Annahmen über Alter, Lesefähigkeit und Selbstständigkeit als Hypothesen
  behandeln und mit Lernenden überprüfen.
- Erprobungsdaten zur Verbesserung des Lernangebots von persönlichen
  Fortschrittsdaten einzelner Lernender trennen.

Der gewünschte erste Erfolg ist: **Ein Lernender verändert eine kleine Stelle
im bereitgestellten Code, startet Pyti und erklärt die sichtbare Wirkung.**
Das setzt keinen vorherigen Python-Kurs voraus, aber eine passende Einführung
und ein funktionierendes Beispiel.

## Phase 1 – Lernende, Lernziele und Reihenfolge verstehen

**Ziel:** Klären, für wen der Einstieg gedacht ist, welche Kompetenzen Pyti
vermitteln soll und woran Lernen erkennbar wird.

- Die Zielgruppe zunächst als überprüfbare Annahme beschreiben. „Grundschulkinder
  etwa 8–10 Jahre“ ist eine mögliche Ausgangshypothese, keine bestätigte
  Eignungsaussage.
- Nutzungssituation, Vorkenntnisse, Geräte- und Lesesituation sowie mögliche
  Unterstützungsbedarfe untersuchen.
- Eine Kompetenzfolge vom konkreten Befehl über Reihenfolge und Wiederholung
  bis zu Sensoren, Bedingungen und selbstständigem Kombinieren entwickeln.
- Die Folge Karel-inspiriert gestalten: kleine Anweisungen, unmittelbare
  sichtbare Wirkung und schrittweise eingeführte Kontrollstrukturen. Keine
  konkrete Karel-Kursreihenfolge als übernommen oder belegt darstellen.
- Für jedes Lernziel beobachtbare Nachweise festlegen, etwa Vorhersagen,
  Codeänderung, Erklärung oder Transfer auf eine ähnliche Aufgabe.
- Den vorhandenen Levelbestand nach Spielfeldmerkmalen erfassen und
  Spielfeldkomplexität ausdrücklich von Python-Kompetenz unterscheiden.
- Prüfen, was die bestehende Zielkontrolle tatsächlich nachweist und was sie
  nicht über Strategie oder Verständnis aussagen kann.
- Den fachlichen Lernzielentwurf und eine strukturierte, zunächst manuelle
  Erprobung dokumentieren. Eine spätere Admin-Eingabe darf erst auf
  tatsächlichen Pilot-Daten und geklärten Anforderungen aufbauen.

**Ergebnis:** Ein überprüfbares Lernzielmodell mit Voraussetzungen und
Beobachtungskriterien und eine Bestandsaufnahme der Aufgaben. Der
Lernzielentwurf steht in [LERNZIELE.md](LERNZIELE.md); Ablauf,
Erfassungsbogen und anonymisierbares Datenschema stehen in
[PHASE1_ERPROBUNG.md](PHASE1_ERPROBUNG.md). Die Zielgruppenannahme bleibt eine
Hypothese, bis die Erprobungen ausgewertet wurden.

**Arbeitsstand:** Lernzielentwurf, Bestandsaufnahme und Erprobungsunterlagen
sind vorbereitet. Die Zielgruppe ist als Arbeitshypothese festgehalten. Es
wurden noch keine Erprobungsdaten mit Kindern oder Lehrkräften erhoben; die
Eignung ist daher nicht bestätigt.

**Abschlusskriterium / Freigabe für Phase 2:** Lernzielentwurf,
Beobachtungskriterien, Einordnung der bestehenden Level und ein konkreter
Plan zur späteren Überprüfung liegen dokumentiert vor. Die Zielgruppe wird
ausdrücklich nur als Arbeitshypothese übernommen. Unter dieser Einschränkung
kann Phase 1 als **Entwurfs- und Klärungsphase** abgeschlossen und Phase 2
begonnen werden. Die empirische Validierung bleibt offen und muss vor
allgemeinen Eignungsaussagen nachgeholt werden. Die Erprobungsunterlagen
ersetzen keine tatsächlich durchgeführte Erprobung.

## Phase 2 – Einen zugänglichen Erstkontakt gestalten

**Ziel:** Den ersten Erfolg ohne unerklärte Python-Vorkenntnisse ermöglichen.

- Einen konkreten Erstmissionsentwurf für einzelne Bewegungsbefehle erstellen
  und prüfen, bevor Schleifen oder Sensoren vorausgesetzt werden.
- Eine kurze, geführte Einstiegsaufgabe erstellen: kleines Beispiel ändern,
  Wirkung vorhersagen, ausführen und in eigenen Worten beschreiben.
- Start, Editor, Spielfeld und Neustart so erklären, wie sie in der Aufgabe
  gebraucht werden.
- Befehle und ihre Argumente zunächst an konkreten Aktionen vermitteln.
- Anweisungen knapp, eindeutig und in einer für die Zielgruppe passenden
  Sprache formulieren; neue Fachbegriffe erklären.
- Den ersten Einstieg ohne vorausgesetzte Schleifen- oder Sensorsyntax
  gestalten; die geführte Mission arbeitet zunächst mit einzelnen Befehlen.
- Erste Aufgaben so wählen, dass sie nicht zugleich neue Python-Syntax und
  deutlich höhere Labyrinthkomplexität verlangen.

Die geführte Mission ist in der App umgesetzt und durch automatisierte Tests
für die Level 0.0.1 bis 0.1.0 geprüft. Der Ablauf und die noch offenen
pädagogischen Fragen stehen in [PHASE2_ERSTE_MISSION.md](PHASE2_ERSTE_MISSION.md).
Mit Lernenden ist die Mission noch nicht erprobt.

**Ergebnis:** Ein automatisiert geprüfter und anschließend pädagogisch
erprobter Einstieg, mit dem neue Lernende das erste Code-Wirkungs-Erlebnis
nachvollziehen können, ohne vorher einen Python-Kurs absolviert zu haben.

## Phase 3 – Hilfen und Code-Skelette schrittweise zurücknehmen

**Ziel:** Vom Verändern eines Beispiels zum selbstständigen Lösen führen.

- Für ausgewählte Einstiegsaufgaben vollständige, kommentierte Beispiele zum
  Verändern anbieten.
- Danach Vorlagen mit einzelnen Lücken nutzen, die jeweils zu einem klaren
  Lernziel passen.
- Wiederkehrende Abläufe zuerst sichtbar machen und zählen lassen, bevor
  eine `for`-Schleife eingeführt wird.
- Sensoren und Bedingungen an konkreten Situationen erklären; erst danach
  zustandsabhängige Wiederholung mit `while` behandeln.
- Freiwillige, gestufte Tipps anbieten: Denkanstoß, konkreter Hinweis,
  Beispiel.
- Vorlagen und Hilfen dürfen vorhandenen Editorinhalt nicht ungefragt
  ersetzen; freie Lösungen bleiben möglich.
- Hilfen nach Erprobung schrittweise reduzieren und Lernenden nicht dauerhaft
  die Lösungsentscheidung abnehmen.

Für die erste Mission sind ein vollständiges ausführbares Beispiel, eine
gültige Lückenvorlage mit genau einer markierten Aktion und drei
nacheinander angezeigte Tipps implementiert. Die Lösung wird nach Anzeige
aller Tipps freigeschaltet. Die technische Funktion ist automatisiert
geprüft; ob die Abstufung verständlich und hilfreich ist, bleibt offen. Details
und Prüffragen stehen in [PHASE3_HILFEN.md](PHASE3_HILFEN.md).

**Ergebnis:** Eine erprobte Aufgabenfolge, in der die Unterstützung
nachvollziehbar abnimmt und Lernende vergleichbare Aufgaben zunehmend
selbstständig bearbeiten.

## Phase 4 – Fehler verständlich machen und Lösungen lernfördernd begleiten

**Ziel:** Rückmeldungen so gestalten, dass sie beim Verstehen und beim nächsten
Versuch helfen.

- Häufige Anfängerfehler wie Einrückungs-, Syntax- und Namensfehler mit
  verständlichen Erklärungen versehen.
- Originalmeldung, Fehlertyp und Zeilennummer erhalten; Erklärung und einen
  sinnvollen nächsten Prüfschritt ergänzen.
- Korrekturvorschläge nur dann geben, wenn sie hinreichend sicher sind.
  Unbekannte Fälle müssen weiterhin als Originalmeldung sichtbar bleiben.
- Nach erfolgreicher Ausführung optionale, zum Lernziel passende Hinweise
  geben, zum Beispiel auf wiederholte Befehle, die sich mit einer Schleife
  ausdrücken ließen.
- Funktionierende Lösungen nicht abwerten, nur weil sie anders als die
  erwartete Musterlösung formuliert sind.
- Fehlermeldungen nicht mit einer Sicherheitsgrenze verwechseln:
  verständliche Rückmeldung isoliert die Ausführung nicht.

**Ergebnis:** Erprobte Erklärungen und optionale Lerntipps, die keine falschen
Fehler- oder Erfolgsaussagen erzeugen und bei unbekannten Fällen transparent
bleiben.

## Phase 5 – Lernfortschritt und Kompetenzen sichtbar machen

**Ziel:** Lernenden zeigen, was sie ausprobiert haben und welche nächsten
Schritte möglich sind, ohne sie zu bewerten oder zu bestrafen.

- Zunächst festlegen, welche Lernereignisse sinnvoll sind: ein Level
  abgeschlossen, eine Strategie ausprobiert oder ein Konzept geübt.
- Spielfelder und Aufgaben mit Lernzielen verknüpfen, bevor aus absolvierten
  Leveln Kompetenzbeherrschung abgeleitet wird.
- Eine einfache, verständliche Übersicht zu geübten Kompetenzen und möglichen
  nächsten Aufgaben entwerfen.
- Speicherort, Zweck, Export, Zurücksetzen und Verhalten bei Neuinstallation
  vor einer Implementierung festlegen.
- So wenig Daten wie möglich lokal speichern. Erprobungsnotizen zu
  Unterrichtsversuchen nicht in persönliche Schülerprofile oder automatische
  Bewertung überführen.
- Keine Pflichtfreischaltung und keinen Verlust bereits erreichter Erfolge
  einführen.

**Ergebnis:** Ein verständlicher und überprüfbarer Entwurf für lokale
Fortschrittsanzeige und Datenspeicherung; erst danach wird die technische
Umsetzung geplant.

## Phase 6 – Mit Lernenden erproben, verbessern und Übergänge prüfen

**Ziel:** Didaktische Annahmen über mehrere Iterationen mit tatsächlicher
Nutzung überprüfen.

- Aufgaben früh und wiederholt mit einer kleinen Gruppe Lernender sowie
  begleitenden Lehrkräften erproben.
- Vor jeder Runde Prüffrage, Aufgabe und Beobachtungskriterien festlegen.
- Dokumentieren, an welchen Stellen Lernende stocken, welche Hilfen sie
  nutzen und ob sie das Konzept erklären oder auf eine neue Aufgabe
  übertragen können.
- Rückmeldungen zu Verständlichkeit, Schwierigkeit, Bedienbarkeit, Dauer und
  Barrierefreiheit erfassen und in konkrete Änderungen überführen.
- Geänderte Aufgaben erneut prüfen; Beobachtungen mehrerer Personen
  zusammenfassen, ohne Einzelfälle zu verallgemeinern.
- Freiwillige Übergänge erläutern: Inspector kann beim Beobachten eines
  Ablaufs helfen; LearnPython IDE kann systematisches Pythonlernen anbieten.
  Keines der Programme muss installiert oder abgeschlossen werden, um ein
  anderes zu nutzen.
- Pädagogische Erprobung nicht mit einer Freigabe für unbeaufsichtigten
  Schuleinsatz gleichsetzen. Sicherheit, Datenschutz, Installation und
  Barrierefreiheit sind eigenständige Freigabekriterien der technischen
  Roadmap.

**Ergebnis:** Dokumentierte Beobachtungen, daraus abgeleitete Änderungen
und eine erneute Prüfung der geänderten Aufgaben. Aussagen zur Eignung gelten
nur für die tatsächlich erprobten Aufgaben und Bedingungen.

## Reihenfolge und Status

Die Phasen sind aufeinanderfolgende Arbeitsschritte. Phase 2 kann auf dem
abgeschlossenen Lernzielentwurf aus Phase 1 aufbauen, auch wenn die
Zielgruppenannahme noch nicht empirisch validiert ist. Bis zur Erprobung
werden Entscheidungen als vorläufig behandelt. Erkenntnisse aus späteren
Erprobungen können dazu führen, dass Phase 1 erneut geöffnet und der Entwurf
angepasst wird. Phase 6 beschreibt die systematische Erprobung und
Verbesserung der entwickelten Lernangebote.

| Phase | Ergebnis | Status |
|---|---|---|
| 1. Lernende, Lernziele und Reihenfolge verstehen | Lernzielentwurf, Aufgabenbestandaufnahme und Prüfplan | Abgeschlossen als Entwurf; Erprobung offen |
| 2. Zugänglichen Erstkontakt gestalten | Erprobter Einstieg ohne vorausgesetzte Python-Kenntnisse | Prototyp implementiert und automatisiert geprüft; Erprobung und Überarbeitung offen |
| 3. Hilfen schrittweise zurücknehmen | Aufgabenfolge mit abgestuften Vorlagen und Tipps | Erste Stufe implementiert und automatisiert geprüft; pädagogische Erprobung offen |
| 4. Lernförderndes Feedback gestalten | Erprobte Erklärungen und optionale Lösungshinweise | Offen |
| 5. Fortschritt sichtbar machen | Datenschutzbewusster Entwurf für Kompetenzübersicht und Speicherung | Offen |
| 6. Erproben und verbessern | Dokumentierte Iterationen und begrenzte, belegte Aussagen | Offen |

Die Roadmap beschreibt pädagogische Entwicklungsziele. Sie behauptet nicht,
dass diese Funktionen bereits umgesetzt oder mit der Zielgruppe validiert
sind. Ein Statuswechsel auf „Abgeschlossen“ sollte erst erfolgen, wenn das
jeweilige Abschlusskriterium erfüllt und die dafür nötige Evidenz dokumentiert
ist.
