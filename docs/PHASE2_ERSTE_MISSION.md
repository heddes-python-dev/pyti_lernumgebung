# Phase 2: Entwurf der ersten Pyti-Mission

**Status, 3. November 2026:** In der App umgesetzt und automatisiert geprüft;
Erprobung mit Lernenden und Überarbeitung anhand von Beobachtungen stehen
aus. Interne Funktionstests dürfen nur mit eigenem, vertrauenswürdigem Code
auf einem Linux-Entwicklungsgerät mit bubblewrap erfolgen. Die Linux-
Isolation wurde noch nicht unabhängig sicherheitsgeprüft; ein Test mit
Kindern auf einem normalen persönlichen oder Schulrechner ist nicht
freigegeben. Auf macOS und Windows wird die Skriptausführung verweigert.

Diese Mission ist der erste konkrete Entwurf für einen zugänglichen Pyti-
Einstieg. Sie soll mit möglichst wenig Python-Syntax zeigen, dass eine
zusätzliche Anweisung den sichtbaren Ablauf verändert. Sie ist kein
Kompetenztest und beweist keine Eignung für eine Altersgruppe.

## Lernziel

Der Lernende kann:

- eine vorhandene Folge einzelner Befehle beobachten;
- vorhersagen, was der nächste passende Befehl bewirkt;
- den Befehl in den Editor einfügen und Pyti erneut starten;
- beschreiben, wie die zusätzliche Anweisung Pyti dem Ziel näher bringt oder
  das Levelziel erfüllt.

Schleifen, Bedingungen und Sensoren werden in dieser ersten Mission nicht
vorausgesetzt oder eingeführt.

## Vorbereitung

- Wähle ein Level von **„0.0.1 Der erste Beeper“** bis
  **„0.1.0 Der Tunnel“** und öffne danach **Hilfe → Erste Mission**.
- Die Mission liest Start, Blickrichtung, Beeper und Wände aus dem
  ausgewählten, tatsächlich geladenen Level. Sie berechnet einen sicheren
  Weg mit Vorwärtsbewegungen und Drehungen; lokale Admin-Änderungen werden
  berücksichtigt.
- Eine Vorlage wird nur erzeugt, wenn der Beeper ohne Sprünge erreichbar ist.
  Bei einem anderen Aufbau erklärt die App, warum sie keine automatische
  Vorlage anbietet.
- Die Aufgabe wird begleitet. Anleitung kann vorgelesen oder gemeinsam
  betrachtet werden.
- Der Lernende soll keinen Namen, kein Konto und keine persönlichen Daten
  eingeben.

## Ablauf für Lernende

Wähle zuerst das Level, das du üben möchtest, und öffne **Hilfe → Erste
Mission**. Die Anleitung nennt das ausgewählte Level und beschreibt eine
sichere Route zum Beeper. Klicke auf **Vollständiges Beispiel laden**. Das
Beispiel enthält die vollständige Route und `pickBeeper()`; bestehender Code
wird nur nach ausdrücklicher Bestätigung ersetzt. Für eine eigene Ergänzung
kann stattdessen die Lückenvorlage geladen werden.

### 1. Erste Beobachtung

Das vollständige Beispiel führt Pyti bis zum Beeper und sammelt ihn auf.
Frage vor dem Start:

> „Was glaubst du, wo Pyti nach diesen Befehlen steht?“

Starte Pyti und vergleicht die Vorhersage mit dem Spielfeld.

### 2. Kleine Änderung

Bitte den Lernenden, die Lückenvorlage zu laden und den markierten Befehl
einzufügen. Wenn die Route eine Drehung enthält, fehlt ein Richtungswechsel;
sonst fehlt der letzte Bewegungsbefehl. Bei einem direkt benachbarten Beeper
fehlt `pickBeeper()`. Frage vor dem Start:

> „Was wird sich jetzt verändern?“

Klicke auf **Level neu starten** und starte Pyti erneut. Die begleitende
Person fragt:

> „Was hat sich durch die zusätzliche Zeile verändert?“

Erwartete Erklärung in eigenen Worten oder durch Zeigen: Der ergänzte Befehl
hat Pyti bewegt oder den Beeper aufnehmen lassen. Fachbegriffe wie
„Anweisung“ oder „Sequenz“ sind nicht erforderlich. Vor jedem erneuten Lauf
**Level neu starten**; der Editorinhalt bleibt erhalten.

Für dieselbe Mission kann als nächster Unterstützungsgrad die
[Lückenvorlage mit gestuften Tipps](PHASE3_HILFEN.md) gewählt werden.

## Hinweise für die Begleitung

- Erst fragen lassen, was das Kind erwartet; nicht sofort die richtige
  Antwort vorsagen.
- Wenn das Kind stockt, abgestufte Hilfen anbieten: auf die Befehle zeigen,
  gemeinsam die Schritte bis zum Beeper zählen, dann bei Bedarf den nächsten
  passenden Befehl vormachen.
- Eine andere Formulierung oder Zeigegeste als Erklärung akzeptieren.
- Wenn die erste Vorhersage nicht eintritt, das als Anlass zum gemeinsamen
  Vergleichen behandeln, nicht als Fehler des Kindes.
- Die Lückenvorlage lässt genau einen Befehl offen. Das vollständige Beispiel
  bleibt verfügbar, falls der Lernende die Lösung vergleichen möchte.
- Die Anwendung unterscheidet jetzt zwischen erfolgreicher Skriptausführung
  und erreichtem Levelziel. Auch nach erfolgreichem Abschluss bleibt der Code
  im Editor. Dieser Ablauf muss noch mit Lernenden erprobt werden.

## Beobachtung für die spätere Erprobung

Bei einer Pilotierung kann der vorhandene
[Phase-1-Erprobungsbogen](PHASE1_ERPROBUNG.md) verwendet werden. Ergänzend
beobachten:

- Versteht das Kind, dass jede Codezeile eine Bewegung auslöst?
- Kann es die Befehle zählen oder deren Wirkung vorhersagen?
- Findet es, wo der nächste Befehl eingefügt werden muss?
- Kann es die Veränderung nach dem zweiten Lauf erklären?
- Ist der Lauf ohne erreichten Ziel-Beeper für das Kind verständlich oder
  wirkt es wie ein Fehlschlag?
- Ist `pickBeeper()` als optionaler nächster Schritt nachvollziehbar?
- Entsteht durch die englischen Befehlsnamen, das Tippen oder die Bedienung
  eine Hürde?

Diese Beobachtungen dienen dazu, die Mission zu überarbeiten. Es gibt keinen
automatischen Punktwert und keine Eignungsentscheidung über das Kind.
Eine Erprobung mit Kindern beginnt erst nach Klärung der technischen
Sicherheitsfreigabe, der Gerätesituation, der erforderlichen Zustimmungen
und der pädagogischen Begleitung. Die Freigabestufen sind in der
[technischen Roadmap](../ROADMAP.md) beschrieben.

## Offene Designfragen

- Soll eine Einführung die Zeilen eintippen lassen oder eine vorbereitete
  Vorlage zum Ergänzen anbieten?
- Braucht es vor der ersten Mission eine kurze Erklärung, wie der Editor und
  der Startknopf bedient werden?
- Ist die unvollständige erste Fahrt motivierend, wenn sie als Vorhersage-
  Experiment angekündigt wird?
- Ist eine deutsche, kindgerechte Bezeichnung zusätzlich zu den echten
  Python-Befehlen hilfreich?
- Ist der automatisch angepasste Ablauf auch bei unterschiedlichen freien
  Geraden für Lernende verständlich?
