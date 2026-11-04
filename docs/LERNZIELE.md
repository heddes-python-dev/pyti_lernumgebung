# Phase 1: Lernende und Lernziele

Dieses Dokument ist der fachliche Entwurf für Phase 1 der
[Lernweg-Roadmap](LERNWEG_ROADMAP.md). Es trennt überprüfte Eigenschaften der
aktuellen Anwendung von pädagogischen Annahmen, die noch mit Lernenden und
Lehrkräften erprobt werden müssen.

## 1. Zielgruppe: Arbeitshypothese, keine bestätigte Eignung

**Ausgangshypothese:** Pyti soll Kindern im Grundschulalter, zunächst etwa
8–10 Jahren, einen ersten Kontakt mit Programmierung ermöglichen. Python-
Vorkenntnisse sollen nicht vorausgesetzt werden.

Vor der Erprobung ist noch offen:

- ob Kinder dieser Altersgruppe die aktuelle Oberfläche und die Anleitungen
  ohne zusätzliche Erklärung bedienen können;
- ob sie die englischen Bezeichner der Pyti-Befehle lesen und voneinander
  unterscheiden können;
- welche Lesefähigkeit, Konzentrationsdauer und Unterstützung die Aufgaben
  voraussetzen dürfen;
- ob die Installation und der Start im vorgesehenen Einsatzort von den
  Kindern selbst oder von Erwachsenen übernommen werden;
- welche Vorkenntnisse und Geräte in der tatsächlichen Nutzungssituation
  vorhanden sind.

Die Altersangabe ist deshalb eine zu prüfende Planungsannahme. Beobachtungen
aus einer kleinen Pilotierung können konkrete Hürden und Verbesserungen
aufzeigen, aber keine pauschale Eignung für alle Kinder dieses Alters
beweisen.

## 2. Gewünschter erster Lernerfolg

Ein Lernender kann mit der vorgesehenen Einführung:

1. eine kleine, klar markierte Stelle in einem Programm verändern;
2. vor dem Start vermuten, was Pyti dadurch tun wird;
3. das Programm starten und die sichtbare Wirkung beobachten;
4. die Wirkung mit eigenen Worten beschreiben oder zeigen.

Dieser Nachweis geht über „Pyti hat das Level geschafft“ hinaus: Er verbindet
eine eigene Änderung mit einer Vorhersage und einer Erklärung.

## 3. Kompetenzfolge als zu prüfender Entwurf

Die Stufen beschreiben angestrebte Lernschritte, nicht bestehende
Freischaltungen. Die Erprobung soll prüfen, ob Voraussetzungen, Reihenfolge
und Wortwahl tragfähig sind.

| Stufe | Lernziel | Voraussetzung | Beobachtbarer Hinweis |
|---|---|---|---|
| 1. Aktion und Wirkung | Einen einzelnen bereitgestellten Befehl verändern oder ergänzen und die Wirkung vorhersagen. | Pyti ist gestartet; ein funktionierendes Beispiel und die Bedienung sind erklärt. | Der Lernende ändert eine Stelle, startet das Programm und zeigt oder beschreibt die Wirkung. |
| 2. Reihenfolge | Verstehen, dass Anweisungen nacheinander ausgeführt werden und eine andere Reihenfolge einen anderen Ablauf bewirken kann. | Einzelne Pyti-Aktionen und sichtbare Zustandsänderungen. | Der Lernende sagt den Ablauf einer kurzen Befehlsfolge voraus und vergleicht ihn mit der Ausführung. |
| 3. Weg planen und zerlegen | Eine räumliche Aufgabe in überschaubare Bewegungen und Richtungswechsel aufteilen. | Startposition, Blickrichtung, Ziel und Hindernisse erkennen. | Der Lernende kann eine einfache Route planen und einen unerwarteten Verlauf an einer Stelle erklären. |
| 4. Wiederholung entdecken | Gleiche oder ähnliche Aktionen als Muster erkennen, bevor Schleifensyntax verlangt wird. | Kurze, sichtbare Befehlsfolgen. | Der Lernende zeigt wiederholte Schritte und erklärt, welche Aktion mehrfach vorkommt. |
| 5. Feste Wiederholung ausdrücken | Eine bekannte Wiederholung mit einem geführten `for`-Beispiel ausdrücken und einen einfachen Parameter ändern. | Wiederholungsmuster; Syntax, Doppelpunkt, Einrückung und `range()` werden eingeführt. | Der Lernende sagt voraus, wie viele Aktionen ausgeführt werden, verändert die Anzahl und überprüft das Ergebnis. |
| 6. Zustand und Entscheidung | Einen Sensor als Frage über die Spielwelt verwenden und mit `if` zwischen Aktionen unterscheiden. | Einfache Sensorwerte sowie beide möglichen Fälle sind erklärt. | Der Lernende sagt für mindestens zwei unterschiedliche Spielfeldzustände voraus, welcher Zweig ausgeführt wird. |
| 7. Zustandsabhängige Wiederholung | Verstehen, wann eine `while`-Schleife fortgesetzt wird und wodurch sie endet. | Bedingungen, Sensorwerte, Einrückung und Abbruchmöglichkeit. | Der Lernende erklärt Fortsetzung und Ende der Schleife und erkennt, wenn die Bedingung nicht wie erwartet wechselt. |
| 8. Selbstständig kombinieren | Sequenz, Wiederholung und Entscheidung auf eine neue, ähnliche Aufgabe übertragen. | Vorherige Konzepte; Hilfen sind bei Bedarf verfügbar. | Der Lernende plant, testet, korrigiert und erklärt eine eigene Lösung. |

Eigene Funktionen, Variablen und Objektorientierung sind mögliche spätere
Vertiefungen, aber keine Voraussetzung für den ersten Pyti-Erfolg.

## 4. Befund zur aktuellen Pyti-Umgebung

### Was das Programm bereitstellt

- Die Anwendung enthält 100 Standardlevel.
- Die ersten 50 Level werden aus beschreibenden Aufgaben und
  Hindernismustern auf einem 15×15-Spielfeld erstellt. Ihre Missionsnamen
  beschreiben vor allem Weg-, Abzweigungs- und Labyrinthaufgaben.
- Die Level 51–100 werden als Labyrinthe mit der zusätzlichen Aktion
  `jump()` erzeugt. Größe und Sprungzahl verändern sich in Gruppen; die
  Levelnummer ist daher keine verlässliche Skala für Python-Kompetenz.
- Das Laufzeitsystem bietet Bewegungs- und Drehbefehle, Beeper-Aktionen,
  `jump()` sowie Sensoren wie `frontClear()`, `onBeeper()` und
  `beeperAhead()`.
- Die Levelprüfung prüft, ob Pyti auf der Zielposition steht und den Ziel-
  Beeper aufgenommen hat. Sie prüft nicht, ob eine bestimmte Syntax,
  Strategie oder Erklärung verwendet wurde.

### Stand des ersten Einstiegs

Das Benutzerhandbuch verweist inzwischen auf **Hilfe → Erste Mission**. Die
geführte Mission erzeugt für das ausgewählte Level ein vollständiges
Beispiel, eine Vorlage mit einer einzelnen markierten Lücke und gestufte
Tipps. Die erste Stufe verwendet Bewegungs- und Drehbefehle; Schleifen und
Sensoren werden nicht vorausgesetzt. Code, Vorlagen und Missionstexte sind
automatisiert geprüft. Das belegt technische Funktion, aber weder
Verständlichkeit für Kinder noch einen Lernerfolg.

Der Schnellstart in [EXAMPLES.md](../EXAMPLES.md) enthält weiterhin Beispiele
mit Schleifen und Sensoren. Diese sind optionale Programmierbeispiele und
nicht die Voraussetzung für den geführten Ersteinstieg. Ob Anleitung,
Aufgabenlänge und Vorlagen ohne zusätzliche Erklärung zugänglich sind, bleibt
eine Frage für die spätere Erprobung.

## 5. Zwei getrennte Aufgabenanforderungen

Bei jeder Aufgabe sind mindestens zwei Aspekte getrennt zu beschreiben:

- **Programmieranforderung:** neue Befehle oder Syntax, Reihenfolge,
  Wiederholung, Bedingungen und benötigte Selbstständigkeit.
- **Spielfeldanforderung:** Weglänge, Richtungswechsel, Hindernisse,
  Sackgassen, Korridore und Sprungmechanik.

Ein dichteres Labyrinth belegt keine höhere Python-Kompetenz. Umgekehrt kann
ein einfaches Spielfeld geeignet sein, um eine neue Programmieridee
einzuführen. Levelnummern und Levelabschluss dürfen daher nicht ohne weitere
Beobachtung als Kompetenzstufen ausgelegt werden.

## 6. Noch offene Evidenz

Die folgenden Fragen brauchen Rückmeldungen aus einer Erprobung:

- Können Lernende der angenommenen Altersgruppe die geführte erste Mission
  verstehen und anwenden?
- Können sie Levelauswahl, Codeeditor, Start und Neustart finden?
- Welche Hilfe ist nötig, um den ersten Code zu verändern?
- Verstehen sie, warum Pyti sich sichtbar bewegt und wann das Ziel erreicht
  wurde?
- Welche Form der Erklärung ist hilfreich: selbst lesen, vorlesen, zeigen
  oder gemeinsam durchführen?
- Welche Bedingungen, etwa Gerät, Lesesituation und erwachsene Begleitung,
  beeinflussen den Einstieg?

Das Vorgehen und ein anonymisierter Erfassungsbogen stehen in
[PHASE1_ERPROBUNG.md](PHASE1_ERPROBUNG.md). Der Lernzielentwurf und die
Erprobungsunterlagen schließen Phase 1 als Entwurfs- und Klärungsphase ab.
Die praktische Erprobung bleibt offen; sie ist Voraussetzung für bestätigte
Eignungsaussagen, aber kein Hindernis für die laufende Arbeit an Phase 2.
