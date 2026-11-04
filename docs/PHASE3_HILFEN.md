# Phase 3: Vorlagen und gestufte Hilfen

**Status, 3. November 2026:** Erste Vorlagen und Hilfen für die erste Mission
sind in der App umgesetzt und automatisiert geprüft. Die didaktische
Abstufung ist noch nicht mit Lernenden erprobt.

## Aktuelle Abstufung

Wähle zuerst ein Level von **0.0.1 bis 0.1.0**, dann öffne **Hilfe → Erste
Mission**. Die Vorlagen beziehen sich auf das ausgewählte Level. Lernende
können frei zwischen den Optionen wählen:

1. **Vollständiges Beispiel:** Die vollständige, an den aktiven Level
   angepasste Route einschließlich `pickBeeper()` wird geladen und ihre
   sichtbare Wirkung beobachtet.
2. **Lückenvorlage:** Ein gültiges Python-Programm mit genau einer markierten
   Lücke wird geladen. Wenn die Route eine Drehung enthält, fehlt ein
   Richtungswechsel; sonst fehlt der letzte Bewegungsbefehl. Bei einem direkt
   benachbarten Beeper fehlt nur `pickBeeper()`.
3. **Gestufte Tipps:** Nacheinander einen Denkanstoß zur Startausrichtung,
   zur Zahl der Bewegungen und Drehungen und zum letzten fehlenden Befehl
   anzeigen.
4. **Lösung:** Der Dialog zeigt den Tippfortschritt sichtbar an. Erst nach
   Anzeige aller drei Tipps wird das Laden der vollständigen Lösung angeboten;
   anschließend bestätigt der Dialog, dass die Schaltfläche freigeschaltet ist.
5. **Freie Lösung:** Der Editor bleibt unabhängig von Vorlage und Tipps
   bearbeitbar. Es gibt keine Pflicht, die Musterlösung zu übernehmen.

Das vollständige Beispiel, die Lückenvorlage und die Lösung verwenden die
Aufgabe des ausgewählten Levels. Die Vorlagen werden aus dem effektiv
geladenen Start, der Blickrichtung, dem Ziel und den Wänden erzeugt. Eine
kürzeste sichere Route mit Vorwärtsbewegungen und Drehungen wird gesucht.
Wenn das Ziel ohne Sprung nicht erreichbar ist, werden keine automatischen
Codevorlagen angeboten. So bleiben Spielfeld und Lernziel konsistent mit
lokalen Admin-Änderungen. Schleifen und Sensoren werden in diesen Vorlagen
noch nicht verlangt.

## Verhalten beim Laden

- Jede Vorlage setzt das ausgewählte Level zurück, damit Startposition und
  Spielfeldzustand reproduzierbar sind.
- Nicht leerer Editorinhalt wird niemals ungefragt ersetzt. Pyti fragt vor
  dem Einfügen nach und bricht das Laden bei Ablehnung ab.
- Die Lückenvorlage bleibt gültiger Python-Code, weil die Lücke ein Kommentar
  ist. Die vollständige Beispielvorlage ist dagegen bereits ausführbar und
  sammelt den Beeper auf.
- Nach einem Lauf bleibt der Code erhalten. **Level neu starten** setzt den
  Roboter zurück, nicht den Editor.

## Noch offene pädagogische Prüfung

Mit Lernenden ist noch zu prüfen:

- ob die Reihenfolge vom vollständigen Beispiel zur Lückenvorlage verständlich
  ist oder eine empfohlene Reihenfolge deutlicher sein sollte;
- ob die an den Level angepassten Kommentare und Tipps ohne zusätzliche
  Erklärung verständlich sind;
- ob drei Tipps eine hilfreiche Abstufung darstellen;
- ob die verzögerte Anzeige der Lösung motiviert oder unnötig erschwert;
- ob Lernende erkennen, dass sie auch eine andere funktionierende Lösung
  verwenden dürfen;
- ob die zweite Vorlagenstufe tatsächlich mehr Selbstständigkeit verlangt,
  ohne dass die Aufgabe dadurch frustrierend wird.

Die aktuelle Umsetzung ist deshalb ein erprobbarer Prototyp, nicht der
Nachweis einer wirksamen pädagogischen Progression. Ergebnisse und Änderungen
gehören in die dokumentierte Pilotauswertung.
