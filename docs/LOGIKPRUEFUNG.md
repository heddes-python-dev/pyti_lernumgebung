# Logik- und Plausibilitätsprüfung

**Prüfdatum:** 26. Oktober 2026<br>
**Prüfumfang:** Spiellogik, 100 Standardlevel, Sprungregeln,
Skriptausführung, Admin-Konfiguration, GUI-Interaktionen und Dokumentation.

## Ergebnis in Kürze

Alle 100 Standardlevel von `0.0.1` bis `1.0.0` sind erreichbar. Für jedes
Level berechnet ein Regressionstest eine kürzeste Route, erzeugt daraus echte
Pyti-Befehle, führt das Skript im Interpreter aus und prüft das Ziel. Die
späteren 50 Level sind reproduzierbare Labyrinthe mit Wand-Sprungbarrieren;
die Testlösungen verwenden jeweils genau die in der Mission genannte Anzahl
an Sprüngen. Die vollständige Testsuite bestand mit **36 Tests**.

`jump()` überspringt genau eine Wand und landet zwei Rasterfelder weiter.
Das Landefeld muss frei und innerhalb des Spielfelds liegen. Ohne eine Wand
im Zwischenfeld ist der Sprung nicht erlaubt. Dieselbe Regel gilt auch für
die Level-Erreichbarkeits- und Admin-Prüfungen.

## Geprüfte Fakten

- `QT_QPA_PLATFORM=offscreen python -m unittest discover -s tests -v`:
  **36 Tests bestanden**.
- `python -m compileall -q pyti_app tests docs *.py`,
  `git diff --check` und die Prüfung der 150-Zeilen-Grenze: erfolgreich.
- **100 von 100** Leveln haben gültige, erreichbare Ziele und werden über den
  tatsächlichen Interpreter erfolgreich abgeschlossen.
- Alle **100 Wandlayouts sind unterschiedlich**. Die Anzahl der Wände reicht
  von 0 bis 184.
- Mit Gehen und legalen Wand-Sprüngen reichen kürzeste Lösungen von 4 bis
  56 Aktionen. Die Zahl gleich langer kürzester Aktionsrouten reicht von 1
  bis 381.646; 65 Level haben genau eine kürzeste Aktionsroute. Drehungen,
  längere Programme und unterschiedliche Skriptvarianten werden dabei nicht
  als eigene Routen gezählt.
- Die 50 Labyrinthmissionen werden zunehmend größer und erfordern laut
  Mission zwischen 1 und 10 Sprungbarrieren. Die Interpreter-Regression
  prüft die jeweilige Sprunganzahl anhand einer kürzesten Route.

## Befunde

### 1. Missionsversprechen und Levelgeometrie (behoben)

Die frühere Mission „Das Tor“ versprach eine „einzige günstige Durchfahrt“;
„Labyrinth Bronze“ sprach vom „einzigen langen Weg“. Die damalige Zählung
ergab mehrere gleich kurze Wege. Das Kriterium ist nun ausdrücklich:
Eine Mission darf eine eindeutige kürzeste Route nur versprechen, wenn genau
eine kürzeste Aktionsroute existiert. Gehen und regelgerechte Sprünge zählen
als Aktionen, Drehungen und Skriptvarianten nicht als eigene Routen.
Eindeutigkeitsbegriffe werden für alle 100 Standardlevel geprüft.

Fundstellen: [`level_specs.py`](../pyti_app/level_specs.py) und
Regressionstest [`test_level_routes.py`](../tests/test_level_routes.py).

### 2. Sprungregel und Labyrinthgeometrie (behoben)

Eine freie Sprungregel hätte Sprünge auch über offene Korridore erlaubt und
damit viele Labyrinthbarrieren zu Abkürzungen gemacht. Die Regel wurde auf
„nur über eine Wand, auf ein freies Landefeld“ präzisiert. Zusätzlich füllte
der Generator anfangs nur den Labyrinthbereich mit Wänden; außerhalb des
Bereichs waren dadurch offene Abkürzungen vorhanden. Der Generator blockiert
nun den gesamten übrigen Rasterbereich und verteilt Sprungbarrieren
eindeutig. Tests prüfen die Sprungbedingungen, alle erreichbaren Ziele und
die tatsächlich ausgeführten Sprünge in sämtlichen 100 Leveln.

Fundstellen: [`field_manager.py`](../pyti_app/field_manager.py),
[`level_paths.py`](../pyti_app/level_paths.py),
[`maze_generator.py`](../pyti_app/maze_generator.py) und
[`test_jump.py`](../tests/test_jump.py).

### 3. Eine wiederholte Konfigurationsprüfung kann eine alte Warnung behalten (behoben)

Ursprünglich setzte [`AdminStore.load`](../pyti_app/admin_store.py) den
Ladefehler bei erfolgreichem erneutem Laden oder fehlender Konfigurationsdatei
nicht zurück. Die Implementierung löscht den alten Fehlerstatus bei jedem
Ladevorgang; Regressionstests prüfen fehlerhafte und anschließende gültige
oder fehlende Konfigurationen.

### 4. Fehlerdetails sind für Lernende nicht direkt sichtbar (behoben)

Syntax- und Laufzeitfehler werden in der Anwendung mit Fehlertyp, Meldung und
Zeilennummer angezeigt. Die Statusanzeige und der Tooltip verweisen nicht
mehr nur auf die Konsole.

Fundstellen: [`script_runtime.py`](../pyti_app/script_runtime.py) und
[`app_controller.py`](../pyti_app/app_controller.py).

### 5. Python-Skripte sind nicht isoliert

Lernskripte laufen mit regulären Python-Built-ins per `exec()` im Prozess der
Anwendung. Das Zeitlimit und die Stopp-Funktion bilden keine Sandbox.
Nicht vertrauenswürdige Skripte dürfen daher nicht als sicher behandelt
werden. Isolation ist vor einer möglichen Ausführung fremder oder automatisch
bezogener Programme gesondert zu planen.

Fundstelle: [`script_runtime.py`](../pyti_app/script_runtime.py).

## Priorisierte nächste Schritte

1. **P2 – Levelzustände:** Levelwechsel, Zurücksetzen und manuelle
   Wand-/Beeperänderungen in Kombination weiter absichern.
2. **P2 – Lernfortschritt und Editorzustand:** Abgeschlossene Level und
   Skripttexte kontrolliert lokal speichern und Wiederherstellung testen.
3. **P3 – Bedienbarkeit und Auslieferung:** Animationsgeschwindigkeit
   einstellbar machen und einen reproduzierbaren Start-/Installations-
   Smoke-Test für unterstützte Desktop-Umgebungen definieren.
4. **Bedingt – Isolation:** Nur wenn Skripte aus nicht vertrauenswürdigen
   Quellen zugelassen werden, vorab einen isolierten Ausführungsansatz
   entwerfen und dessen Grenzen dokumentieren.

## Grenzen dieser Prüfung

Automatisierte Tests belegen die geprüften Logikpfade, nicht jede Eingabe
oder Desktop-Umgebung. Es wurde kein plattformübergreifender
Installationslauf, keine physische Druckausgabe und keine unabhängige
Usability-Prüfung mit Lernenden durchgeführt. Die Routenstatistik betrachtet
kürzeste Bewegungsfolgen einschließlich erlaubter Sprünge; sie zählt weder
Python-Skriptvarianten noch längere Lösungswege.
