# Logik- und Plausibilitätsprüfung

**Prüfdatum:** 26. Oktober 2026<br>
**Prüfumfang:** Spiellogik, Leveldaten, Skriptausführung, Admin-Konfiguration,
GUI-Interaktionen, vorhandene Verhaltenstests und zugehörige Dokumentation.

## Ergebnis in Kürze

Die zentralen Lernabläufe sind im geprüften Stand funktional: Alle 50
Standardlevel sind erreichbar. Für jedes Level wurde außerdem eine kürzeste
Route abgeleitet und mit den tatsächlichen Pyti-Befehlen ausgeführt; alle 50
Durchläufe erreichten das Ziel korrekt. Die 22 automatisierten Tests bestanden.

Es gibt dennoch konkrete Verbesserungsmöglichkeiten: Zwei Missionsformulierungen
versprechen eine Einmaligkeit, die die kürzesten Bewegungswege nicht bestätigen;
ein wiederholter Ladevorgang kann eine alte Konfigurationswarnung stehen lassen;
und Skriptfehler sind in der Oberfläche noch nicht ausreichend erklärt. Die
Levelstatistik misst Bewegungsrouten, nicht die Anzahl aller Python-Programme,
mit denen ein Level gelöst werden kann.

## Geprüfte Fakten

- `python -m unittest discover -s tests -v`: **22 Tests bestanden**.
- `python -m compileall -q pyti_app tests` und `git diff --check`: erfolgreich.
- Die vorhandenen Leveltests bestätigen Rastergrenzen, freie Start- und
  Zielzellen, Ziel-Beeper und Erreichbarkeit für alle **50 Level**.
- Ein zusätzlicher Prüflauf hat für jedes Level eine kürzeste Route berechnet
  und diese mit dem realen Interpreter (Dreh-, Bewegungs- und Aufhebe-Befehle)
  ausgeführt: **50 von 50 erfolgreich**. Dieser Lauf ist derzeit noch kein
  dauerhafter Regressionstest.
- Es gibt **50 unterschiedliche Wandlayouts**. Die Wandanzahl reicht von
  0 bis 66; die kürzesten Wege haben 4 bis 28 Rasterbewegungen.
- Die Anzahl gleich langer, kürzester Bewegungsrouten reicht von 1 bis
  1.324.718; nur 13 von 50 Leveln haben genau eine kürzeste Bewegungsroute.
  Diese Zahlen sagen nichts darüber aus, wie viele unterschiedliche Skripte
  oder längere Lösungswege existieren.
- Die Python-Dateien bleiben innerhalb der projektweiten Grenze von 150 Zeilen.

## Befunde

### 1. Missionsversprechen und Levelgeometrie stimmen nicht immer überein

Die Levelbeschreibung „Das Tor“ spricht von der „einzigen günstigen Durchfahrt“;
für das Level gibt es 350 gleich lange, kürzeste Bewegungsrouten. Diese
Routenstatistik beweist nicht, dass es mehrere Durchgänge durch das Tor gibt:
Sie zählt die gesamte Route und nicht einzelne Öffnungen. „Labyrinth Bronze“
verspricht „den einzigen langen Weg“, hat aber 21.904 kürzeste
Bewegungsrouten. Die Formulierungen sind daher nicht durch die aktuelle
Eindeutigkeitsprüfung abgesichert und sollten an ein klares Kriterium gebunden
werden.

**Empfehlung:** Entweder die Missionstexte präzisieren, damit sie keine
Einmaligkeit behaupten, oder die Hindernisgeometrie gezielt auf einen
nachweislich eindeutigen Lösungsweg ausrichten. Die Prüfung sollte ausdrücklich
definieren, ob „eindeutig“ eine kürzeste Route, einen Korridordurchgang oder
einen gesamten Lösungsweg meint.

Fundstellen: [`level_specs.py`](../pyti_app/level_specs.py#L21) und
[`level_specs.py`](../pyti_app/level_specs.py#L36).

### 2. Eine wiederholte Konfigurationsprüfung kann eine alte Warnung behalten

[`AdminStore.load`](../pyti_app/admin_store.py#L19) setzt `load_error`, wenn
eine Konfiguration fehlerhaft ist. Ein nachfolgender erfolgreicher Ladevorgang
oder das Fehlen der Datei setzt den alten Wert nicht zurück. Das wurde mit
einer fehlerhaften JSON-Datei und anschließend entferntem Konfigurationsfile
reproduziert: `load_error` blieb unverändert. Im üblichen Startablauf wird der
Store neu erstellt; nach dem Speichern setzt das Admin-Panel die Warnung zurück.
Betroffen sind daher vor allem wiederholte Ladevorgänge derselben Store-Instanz
und die Zuverlässigkeit der Statusanzeige.

**Empfehlung:** Den Fehlerstatus zu Beginn eines Ladevorgangs zurücksetzen und
einen Test für „Fehler, danach Erfolg“ ergänzen.

### 3. Fehlerdetails sind für Lernende nicht direkt sichtbar

Der Interpreter erfasst den letzten Fehler und gibt Details in der Konsole aus.
Die Statuszeile im Fenster verweist bei einem Fehlschlag nur auf die Konsole;
Fehlertyp, verständlicher Kontext und Skriptzeile werden dort nicht angezeigt.
Das ist bereits als offener Punkt in der Roadmap aufgeführt.

Fundstellen: [`script_runtime.py`](../pyti_app/script_runtime.py#L96) und
[`app_controller.py`](../pyti_app/app_controller.py#L118).

### 4. Python-Skripte sind nicht isoliert

Die Lernskripte laufen mit regulären Python-Built-ins per `exec()` im Prozess
der Anwendung. Das Projekt dokumentiert diese Grenze und warnt vor
nicht vertrauenswürdigen Skripten; Zeitlimit und Stopp-Funktion sind keine
Sandbox. Für selbst geschriebene lokale Lernskripte ist das eine bekannte
Betriebsgrenze. Falls künftig fremde oder automatisch bezogene Skripte
ausgeführt werden sollen, muss Isolation vor dieser Erweiterung geplant werden.

Fundstelle: [`script_runtime.py`](../pyti_app/script_runtime.py#L96).

## Priorisierte nächste Schritte

1. **P1 – Fehler verständlich im Fenster anzeigen:** Fehlertyp, Meldung und
   Zeilennummer des Lernskripts in der Status-/Ergebnisansicht zeigen; gezielte
   Tests für Syntaxfehler, Laufzeitfehler, Kollision, Zeitlimit und Abbruch.
2. **P1 – Missionsaussagen plausibilisieren:** Für Level mit
   Einmaligkeitsversprechen das gemeinte Eindeutigkeitskriterium festlegen.
   Danach Missionsbeschreibung oder Layout ändern und die Zusage automatisiert
   prüfen.
3. **P2 – Konfigurationsstatus zuverlässig erneuern:** Veraltete Ladefehler
   bei erneutem Einlesen löschen und Erfolg nach vorherigem Fehler testen.
4. **P2 – Leveltests dauerhaft stärken:** Den erfolgreichen 50-Level-
   Interpreter-Prüflauf als Regressionstest aufnehmen; zusätzlich
   Levelwechsel, Zurücksetzen, manuelle Wand-/Beeperänderungen und
   Zielprüfung in Kombination testen.
5. **P2 – Lernfortschritt und Editorzustand:** Abgeschlossene Level sowie
   Skripttexte kontrolliert lokal speichern und Wiederherstellung mit Tests
   absichern.
6. **P3 – Bedienbarkeit und Auslieferung:** Animationsgeschwindigkeit
   einstellbar machen und einen reproduzierbaren Start-/Installations-
   Smoke-Test für unterstützte Desktop-Umgebungen definieren.
7. **Bedingt – Isolation:** Nur wenn Skripte aus nicht vertrauenswürdigen
   Quellen zugelassen werden, vorab einen isolierten Ausführungsansatz
   entwerfen und dessen Grenzen dokumentieren.

## Grenzen dieser Prüfung

Die automatisierten Tests und Prüfläufe belegen die getesteten Logikpfade,
nicht jede denkbare Eingabe oder jede Desktop-Umgebung. Es wurde kein
plattformübergreifender Installationslauf, keine physische Druckausgabe und
keine unabhängige Usability-Prüfung mit Lernenden durchgeführt. Die
Routenstatistik betrachtet ausschließlich kürzeste Bewegungsfolgen auf dem
Raster; sie zählt weder Python-Skriptvarianten noch unterschiedliche
Programmierstrategien.
