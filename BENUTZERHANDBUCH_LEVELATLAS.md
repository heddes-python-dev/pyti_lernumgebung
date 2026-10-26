# Anhang A – Levelkarten und Arbeitsheft

Diese 100 Arbeitsblätter beziehen sich auf die Standardlevel.
Koordinaten und Wandzahlen stammen aus den Leveldaten; Mindestwege sind
per Breitensuche auf dem Raster berechnet. Ein Schritt ist entweder
Gehen oder ein Sprung über genau ein Feld; Drehungen zählen nicht.
Ein Sprung ist nur über eine Wand möglich und landet auf einem freien Feld.
Die Zahl kürzester Wege zählt alternative Aktionsrouten, nicht Skripte.
Sie zählt keine Anzahl aller möglichen Programme. Jede Karte ist
eine eigene Druckseite.


\newpage

## Level 01 – 0.0.1 Der erste Beeper

**Mission: Gehe geradeaus und lerne moveForward(). Ziel: Erreiche den Beeper bei (4, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(4, 0)` |
| Wände | 0 |
| Kürzester Weg (Gehen/Springen) | 4 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Anweisungsfolge und erste Drehungen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 02 – 0.0.2 Der erste Dreh

**Mission: Verbinde Geradeauslaufen mit einer ersten Drehung. Ziel: Erreiche den Beeper bei (4, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 4)` |
| Startblickrichtung | Osten |
| Ziel | `(4, 1)` |
| Wände | 1 |
| Kürzester Weg (Gehen/Springen) | 7 Aktionen |
| Kürzeste Aktionsrouten | 34 |

**Lernfokus:** Anweisungsfolge und erste Drehungen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 03 – 0.0.3 Eine Wand

**Mission: Umgehe die einzelne Blockade. Ziel: Erreiche den Beeper bei (5, 2) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 2)` |
| Startblickrichtung | Osten |
| Ziel | `(5, 2)` |
| Wände | 2 |
| Kürzester Weg (Gehen/Springen) | 5 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Anweisungsfolge und erste Drehungen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 04 – 0.0.4 Zwei Richtungen

**Mission: Wechsle zwischen horizontalem und vertikalem Weg. Ziel: Erreiche den Beeper bei (6, 4) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(6, 4)` |
| Wände | 3 |
| Kürzester Weg (Gehen/Springen) | 7 Aktionen |
| Kürzeste Aktionsrouten | 4 |

**Lernfokus:** Anweisungsfolge und erste Drehungen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 05 – 0.0.5 Die Ecke

**Mission: Finde den Weg um die Eckbarriere. Ziel: Erreiche den Beeper bei (5, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 5)` |
| Startblickrichtung | Osten |
| Ziel | `(5, 0)` |
| Wände | 4 |
| Kürzester Weg (Gehen/Springen) | 9 Aktionen |
| Kürzeste Aktionsrouten | 6 |

**Lernfokus:** Anweisungsfolge und erste Drehungen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 06 – 0.0.6 Kleine Treppe

**Mission: Folge dem Verlauf der Treppenwände. Ziel: Erreiche den Beeper bei (6, 3) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 8)` |
| Startblickrichtung | Osten |
| Ziel | `(6, 3)` |
| Wände | 5 |
| Kürzester Weg (Gehen/Springen) | 9 Aktionen |
| Kürzeste Aktionsrouten | 6 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 07 – 0.0.7 Zickzack

**Mission: Schlängle dich durch die versetzten Wände. Ziel: Erreiche den Beeper bei (7, 4) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(7, 4)` |
| Wände | 6 |
| Kürzester Weg (Gehen/Springen) | 9 Aktionen |
| Kürzeste Aktionsrouten | 5 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 08 – 0.0.8 Die Gasse

**Mission: Suche den Eingang zur freien Gasse. Ziel: Erreiche den Beeper bei (8, 6) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 6)` |
| Startblickrichtung | Osten |
| Ziel | `(8, 6)` |
| Wände | 7 |
| Kürzester Weg (Gehen/Springen) | 8 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 09 – 0.0.9 Sackgasse

**Mission: Erkenne die Sackgasse und nimm den Umweg. Ziel: Erreiche den Beeper bei (8, 7) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(8, 7)` |
| Wände | 8 |
| Kürzester Weg (Gehen/Springen) | 11 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 10 – 0.1.0 Der Tunnel

**Mission: Bleibe im schmalen Korridor auf Kurs. Ziel: Erreiche den Beeper bei (9, 5) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 5)` |
| Startblickrichtung | Osten |
| Ziel | `(9, 5)` |
| Wände | 9 |
| Kürzester Weg (Gehen/Springen) | 9 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 11 – 0.1.1 Kreuzung

**Mission: Wähle an mehreren Kreuzungen den richtigen Weg. Ziel: Erreiche den Beeper bei (9, 8) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(2, 2)` |
| Startblickrichtung | Osten |
| Ziel | `(9, 8)` |
| Wände | 10 |
| Kürzester Weg (Gehen/Springen) | 11 Aktionen |
| Kürzeste Aktionsrouten | 38 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 12 – 0.1.2 Umweg nach Norden

**Mission: Umgehe die Barrieren und arbeite nach Norden. Ziel: Erreiche den Beeper bei (8, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 9)` |
| Startblickrichtung | Osten |
| Ziel | `(8, 1)` |
| Wände | 11 |
| Kürzester Weg (Gehen/Springen) | 13 Aktionen |
| Kürzeste Aktionsrouten | 217 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 13 – 0.1.3 Umweg nach Süden

**Mission: Plane einen sicheren Weg nach Süden. Ziel: Erreiche den Beeper bei (2, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(8, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(2, 10)` |
| Wände | 12 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 95 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 14 – 0.1.4 Das Karree

**Mission: Umkreise den blockierten Innenbereich. Ziel: Erreiche den Beeper bei (10, 2) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(2, 2)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 2)` |
| Wände | 13 |
| Kürzester Weg (Gehen/Springen) | 8 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 15 – 0.1.5 Das Kreuz

**Mission: Entkomme aus dem Kreuzungsbereich und erreiche den Beeper. Ziel: Erreiche den Beeper bei (0, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(4, 4)` |
| Startblickrichtung | Osten |
| Ziel | `(0, 0)` |
| Wände | 14 |
| Kürzester Weg (Gehen/Springen) | 4 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Bedingungen, Sensoren und einfache Umwege.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 16 – 0.1.6 Doppelter Korridor

**Mission: Navigiere durch zwei hintereinanderliegende Korridore. Ziel: Erreiche den Beeper bei (11, 8) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 2)` |
| Startblickrichtung | Osten |
| Ziel | `(11, 8)` |
| Wände | 15 |
| Kürzester Weg (Gehen/Springen) | 15 Aktionen |
| Kürzeste Aktionsrouten | 11 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 17 – 0.1.7 Die Spirale

**Mission: Folge dem spiralförmigen Wandmuster nach innen. Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 16 |
| Kürzester Weg (Gehen/Springen) | 13 Aktionen |
| Kürzeste Aktionsrouten | 7 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 18 – 0.1.8 Das Tor

**Mission: Finde eine günstige Durchfahrt durch die Barriere. Ziel: Erreiche den Beeper bei (5, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(5, 12)` |
| Startblickrichtung | Osten |
| Ziel | `(5, 1)` |
| Wände | 17 |
| Kürzester Weg (Gehen/Springen) | 6 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 19 – 0.1.9 Wand-Slalom

**Mission: Weiche den versetzten Wänden im Slalom aus. Ziel: Erreiche den Beeper bei (12, 4) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 10)` |
| Startblickrichtung | Osten |
| Ziel | `(12, 4)` |
| Wände | 18 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 792 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 20 – 0.2.0 Das L-Labyrinth

**Mission: Umgehe zwei lange L-förmige Hindernisse. Ziel: Erreiche den Beeper bei (12, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 10)` |
| Startblickrichtung | Osten |
| Ziel | `(12, 1)` |
| Wände | 19 |
| Kürzester Weg (Gehen/Springen) | 15 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 21 – 0.2.1 Drei Kammern

**Mission: Durchquere drei getrennte Wandbereiche. Ziel: Erreiche den Beeper bei (12, 8) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(12, 8)` |
| Wände | 20 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 6 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 22 – 0.2.2 Der Haken

**Mission: Finde den Ausgang aus dem hakenförmigen Aufbau. Ziel: Erreiche den Beeper bei (1, 12) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(2, 2)` |
| Startblickrichtung | Osten |
| Ziel | `(1, 12)` |
| Wände | 21 |
| Kürzester Weg (Gehen/Springen) | 6 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 23 – 0.2.3 Diagonale

**Mission: Arbeite dich an der diagonalen Wandstruktur vorbei. Ziel: Erreiche den Beeper bei (12, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 12)` |
| Startblickrichtung | Osten |
| Ziel | `(12, 0)` |
| Wände | 22 |
| Kürzester Weg (Gehen/Springen) | 18 Aktionen |
| Kürzeste Aktionsrouten | 4 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 24 – 0.2.4 Die Schleife

**Mission: Verlasse die Schleife und halte auf das Ziel zu. Ziel: Erreiche den Beeper bei (13, 11) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 11)` |
| Wände | 23 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 25 – 0.2.5 Korridor-Netz

**Mission: Wähle im Korridornetz die passende Abzweigung. Ziel: Erreiche den Beeper bei (13, 7) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 7)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 7)` |
| Wände | 24 |
| Kürzester Weg (Gehen/Springen) | 13 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Planen, Schleifen und systematisches Prüfen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 26 – 0.2.6 Der Innenhof

**Mission: Durchquere den Innenhof ohne an einer Wand zu enden. Ziel: Erreiche den Beeper bei (7, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(7, 13)` |
| Startblickrichtung | Osten |
| Ziel | `(7, 1)` |
| Wände | 25 |
| Kürzester Weg (Gehen/Springen) | 13 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 27 – 0.2.7 Vier Abzweigungen

**Mission: Prüfe an jeder Abzweigung die freie Richtung. Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 26 |
| Kürzester Weg (Gehen/Springen) | 18 Aktionen |
| Kürzeste Aktionsrouten | 9 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 28 – 0.2.8 Das Fenster

**Mission: Nutze die Öffnungen im Fenster-Muster. Ziel: Erreiche den Beeper bei (12, 2) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(2, 12)` |
| Startblickrichtung | Osten |
| Ziel | `(12, 2)` |
| Wände | 27 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 29 – 0.2.9 Schlangengänge

**Mission: Folge den geschwungenen Gängen bis zum Ausgang. Ziel: Erreiche den Beeper bei (13, 12) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 12)` |
| Wände | 28 |
| Kürzester Weg (Gehen/Springen) | 19 Aktionen |
| Kürzeste Aktionsrouten | 11 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 30 – 0.3.0 Die Ringmauer

**Mission: Finde die Lücke in der Ringmauer. Ziel: Erreiche den Beeper bei (13, 7) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 7)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 7)` |
| Wände | 29 |
| Kürzester Weg (Gehen/Springen) | 12 Aktionen |
| Kürzeste Aktionsrouten | 22 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 31 – 0.3.1 Doppelschleuse

**Mission: Passiere zwei Schleusen mit jeweils einer Öffnung. Ziel: Erreiche den Beeper bei (13, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 13)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 0)` |
| Wände | 30 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 585 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 32 – 0.3.2 Das Raster

**Mission: Überquere das dichte Raster Schritt für Schritt. Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 31 |
| Kürzester Weg (Gehen/Springen) | 18 Aktionen |
| Kürzeste Aktionsrouten | 46 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 33 – 0.3.3 Labyrinth Bronze

**Mission: Finde einen möglichst kurzen Weg durch das Labyrinth. Ziel: Erreiche den Beeper bei (13, 9) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 9)` |
| Wände | 32 |
| Kürzester Weg (Gehen/Springen) | 21 Aktionen |
| Kürzeste Aktionsrouten | 36680 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 34 – 0.3.4 Labyrinth Silber

**Mission: Nutze Sensoren, um Sackgassen zu erkennen. Ziel: Erreiche den Beeper bei (12, 2) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(2, 12)` |
| Startblickrichtung | Osten |
| Ziel | `(12, 2)` |
| Wände | 34 |
| Kürzester Weg (Gehen/Springen) | 18 Aktionen |
| Kürzeste Aktionsrouten | 340 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 35 – 0.3.5 Labyrinth Nord

**Mission: Steige durch mehrere verschachtelte Korridore nach Norden. Ziel: Erreiche den Beeper bei (7, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(7, 13)` |
| Startblickrichtung | Osten |
| Ziel | `(7, 0)` |
| Wände | 36 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 6 |

**Lernfokus:** Korridore, Kreuzungen und Fehlerbehandlung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 36 – 0.3.6 Labyrinth Süd

**Mission: Finde den Ausgang am anderen Ende des Labyrinths. Ziel: Erreiche den Beeper bei (7, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(7, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(7, 13)` |
| Wände | 38 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 3 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 37 – 0.3.7 Das Irrgarten-Herz

**Mission: Erreiche das Zentrum des großen Irrgartens. Ziel: Erreiche den Beeper bei (7, 7) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 7)` |
| Startblickrichtung | Osten |
| Ziel | `(7, 7)` |
| Wände | 40 |
| Kürzester Weg (Gehen/Springen) | 7 Aktionen |
| Kürzeste Aktionsrouten | 7 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 38 – 0.3.8 Verlorene Kreuzung

**Mission: Orientiere dich in einem dichten Kreuzungsnetz. Ziel: Erreiche den Beeper bei (1, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(14, 14)` |
| Startblickrichtung | Osten |
| Ziel | `(1, 1)` |
| Wände | 42 |
| Kürzester Weg (Gehen/Springen) | 24 Aktionen |
| Kürzeste Aktionsrouten | 381646 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 39 – 0.3.9 Die lange Schleife

**Mission: Durchlaufe die lange Schleife ohne Abkürzung. Ziel: Erreiche den Beeper bei (14, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 14)` |
| Startblickrichtung | Osten |
| Ziel | `(14, 0)` |
| Wände | 44 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 6 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 40 – 0.4.0 Labyrinth Gold

**Mission: Finde im komplexen Muster den sicheren Zielkorridor. Ziel: Erreiche den Beeper bei (13, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 13)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 1)` |
| Wände | 46 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 150 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 41 – 0.4.1 Das große Labyrinth

**Mission: Löse das vollständige Labyrinth mit Sensoren und Schleifen. Ziel: Erreiche den Beeper bei (14, 14) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(14, 14)` |
| Wände | 48 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 42 – 0.4.2 Meisterprüfung

**Mission: Bewältige alle zuvor geübten Navigationsmuster. Ziel: Erreiche den Beeper bei (0, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(14, 14)` |
| Startblickrichtung | Osten |
| Ziel | `(0, 0)` |
| Wände | 50 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 6 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 43 – 0.4.3 Der letzte Korridor

**Mission: Finde den versteckten Durchgang durch das Endspiel. Ziel: Erreiche den Beeper bei (14, 7) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 7)` |
| Startblickrichtung | Osten |
| Ziel | `(14, 7)` |
| Wände | 52 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 17 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 44 – 0.4.4 Vier Tore

**Mission: Öffne gedanklich die vier Tore des Labyrinths. Ziel: Erreiche den Beeper bei (7, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(7, 14)` |
| Startblickrichtung | Osten |
| Ziel | `(7, 0)` |
| Wände | 54 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 2 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 45 – 0.4.5 Das Wendewerk

**Mission: Plane viele Drehungen, ohne eine Sackgasse zu übersehen. Ziel: Erreiche den Beeper bei (14, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(14, 10)` |
| Wände | 56 |
| Kürzester Weg (Gehen/Springen) | 18 Aktionen |
| Kürzeste Aktionsrouten | 37 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 46 – 0.4.6 Die Tiefen

**Mission: Dringe bis in die tiefste Kammer vor. Ziel: Erreiche den Beeper bei (0, 14) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(14, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(0, 14)` |
| Wände | 58 |
| Kürzester Weg (Gehen/Springen) | 21 Aktionen |
| Kürzeste Aktionsrouten | 151 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 47 – 0.4.7 Labyrinth Diamant

**Mission: Finde den Zielweg durch das nahezu vollständige Raster. Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 60 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 390 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 48 – 0.4.8 Der Endspurt

**Mission: Halte trotz dichter Wände die Orientierung. Ziel: Erreiche den Beeper bei (14, 1) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 13)` |
| Startblickrichtung | Osten |
| Ziel | `(14, 1)` |
| Wände | 62 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 22 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 49 – 0.4.9 Meisterlabyrinth

**Mission: Löse das anspruchsvollste bisherige Labyrinth. Ziel: Erreiche den Beeper bei (0, 0) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(14, 14)` |
| Startblickrichtung | Osten |
| Ziel | `(0, 0)` |
| Wände | 64 |
| Kürzester Weg (Gehen/Springen) | 18 Aktionen |
| Kürzeste Aktionsrouten | 5 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 50 – 0.5.0 Das große Finale

**Mission: Finde den Weg zum letzten Beeper und beende die Lernstrecke. Ziel: Erreiche den Beeper bei (14, 14) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(0, 0)` |
| Startblickrichtung | Osten |
| Ziel | `(14, 14)` |
| Wände | 66 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 2 |

**Lernfokus:** Komplexe Wege, robuste Schleifen und eigener Lösungsplan.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 51 – 0.5.1 Der erste Sprung

**Mission: Springe über die blockierte Verbindung im Labyrinth. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 52 – 0.5.2 Sprung im Tunnel

**Mission: Nutze die Sprungstelle im schmalen Tunnel. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 23 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 53 – 0.5.3 Die versperrte Ecke

**Mission: Finde den Umweg durch das Ecklabyrinth. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 54 – 0.5.4 Kammerwechsel

**Mission: Verbinde die Kammern trotz blockierter Durchgänge. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 41 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 55 – 0.5.5 Sprungkreuzung

**Mission: Wähle an der Kreuzung den passenden Sprung. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 29 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 56 – 0.5.6 Der geheime Korridor

**Mission: Suche den versteckten Weg zwischen den Wänden. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 23 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 57 – 0.5.7 Doppelte Abzweigung

**Mission: Prüfe jeden Abzweig, bevor du springst. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 58 – 0.5.8 Der kurze Durchbruch

**Mission: Nutze den Sprung, ohne den Zielkorridor zu verfehlen. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 29 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 59 – 0.5.9 Wand im Weg

**Mission: Überwinde die Wand im begehbaren Abschnitt. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 60 – 0.6.0 Sprungprüfung Bronze

**Mission: Kombiniere Orientierung und Sprung im Labyrinth. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 41 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Erste Sprünge und kleine Labyrinthe.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 61 – 0.6.1 Das verschachtelte Tor

**Mission: Finde den Weg durch die ineinanderliegenden Gänge. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 35 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 62 – 0.6.2 Das blockierte Tor

**Mission: Finde den Weg durch den blockierten Durchgang. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 63 – 0.6.3 Korridorwechsel

**Mission: Wechsle sicher zwischen den schmalen Korridoren. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 23 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 64 – 0.6.4 Die stille Kammer

**Mission: Finde die Verbindung aus der abgeschlossenen Kammer. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 41 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 65 – 0.6.5 Sprungfolge

**Mission: Plane den Sprung, ohne die Orientierung zu verlieren. Überwinde 1 Sprungbarriere mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 180 |
| Kürzester Weg (Gehen/Springen) | 35 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 66 – 0.6.6 Drei Wege

**Mission: Prüfe Sackgassen und wähle den passenden Durchgang. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 40 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 67 – 0.6.7 Das versetzte Tor

**Mission: Nutze versetzte Sprungstellen im Labyrinth. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 28 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 68 – 0.6.8 Die inneren Gänge

**Mission: Finde den Zugang zu den inneren Gängen. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 28 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 69 – 0.6.9 Kreuz und Quer

**Mission: Verbinde die getrennten Bereiche mit gezielten Sprüngen. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 70 – 0.7.0 Sprungprüfung Silber

**Mission: Löse das größere Labyrinth mit Sensoren und Sprüngen. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 22 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Mehrere Sprungstellen und verschachtelte Korridore.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 71 – 0.7.1 Die Kammerreihe

**Mission: Durchquere mehrere hintereinanderliegende Kammern. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 72 – 0.7.2 Der lange Umweg

**Mission: Vergleiche Abzweigungen und halte den Zielkurs. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 73 – 0.7.3 Das doppelte Raster

**Mission: Orientiere dich im dicht verzweigten Raster. Überwinde 2 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 181 |
| Kürzester Weg (Gehen/Springen) | 28 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 74 – 0.7.4 Verlorener Durchgang

**Mission: Finde den Durchgang zwischen den verschlossenen Gängen. Überwinde 3 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 182 |
| Kürzester Weg (Gehen/Springen) | 15 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 75 – 0.7.5 Der versiegelte Durchgang

**Mission: Finde den richtigen Sprung aus dem verschlungenen Gang. Überwinde 3 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 182 |
| Kürzester Weg (Gehen/Springen) | 33 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 76 – 0.7.6 Sprungnetz

**Mission: Nutze Sensoren, um Sprung und Richtungswechsel zu planen. Überwinde 3 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 182 |
| Kürzester Weg (Gehen/Springen) | 21 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 77 – 0.7.7 Der verschachtelte Irrgarten

**Mission: Finde aus den eng verzweigten Gängen zurück zum Ziel. Überwinde 4 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 183 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 78 – 0.7.8 Kammerlabyrinth

**Mission: Durchquere die verzweigten Bereiche trotz blockierter Türen. Überwinde 4 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 183 |
| Kürzester Weg (Gehen/Springen) | 14 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 79 – 0.7.9 Die falsche Fährte

**Mission: Lass dich von Sackgassen nicht vom Ziel abbringen. Überwinde 4 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 183 |
| Kürzester Weg (Gehen/Springen) | 32 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 80 – 0.8.0 Sprungprüfung Gold

**Mission: Kombiniere längere Planung mit mehreren Sprüngen. Überwinde 5 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (10, 10) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(10, 10)` |
| Wände | 184 |
| Kürzester Weg (Gehen/Springen) | 31 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Komplexe Kammerlabyrinthe und Sensorplanung.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 81 – 0.8.1 Die verschlungenen Gänge

**Mission: Folge den verwinkelten Korridoren bis zum Ziel. Überwinde 4 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 156 |
| Kürzester Weg (Gehen/Springen) | 38 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 82 – 0.8.2 Der verzweigte Pfad

**Mission: Finde das Ziel in den verzweigten Gängen. Überwinde 4 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 156 |
| Kürzester Weg (Gehen/Springen) | 56 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 83 – 0.8.3 Sprünge im Raster

**Mission: Unterscheide offene Korridore von blockierten Übergängen. Überwinde 5 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 157 |
| Kürzester Weg (Gehen/Springen) | 19 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 84 – 0.8.4 Die äußeren Gänge

**Mission: Durchlaufe die äußeren Korridore und finde den Zielweg. Überwinde 5 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 157 |
| Kürzester Weg (Gehen/Springen) | 31 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 85 – 0.8.5 Kreuzung der Kammern

**Mission: Wähle an jeder Kammerkreuzung einen sicheren Weg. Überwinde 6 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 158 |
| Kürzester Weg (Gehen/Springen) | 48 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 86 – 0.8.6 Das lange Tor

**Mission: Überwinde die Sprungstellen entlang des langen Korridors. Überwinde 6 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 158 |
| Kürzester Weg (Gehen/Springen) | 48 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 87 – 0.8.7 Der Irrgartenkern

**Mission: Finde den Weg durch die dicht verschachtelten Bereiche. Überwinde 7 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 159 |
| Kürzester Weg (Gehen/Springen) | 23 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 88 – 0.8.8 Verschachtelte Zonen

**Mission: Plane eine Route durch die ineinanderliegenden Labyrinthzonen. Überwinde 7 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 159 |
| Kürzester Weg (Gehen/Springen) | 35 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 89 – 0.8.9 Die letzte Abzweigung

**Mission: Prüfe die letzten Alternativen vor dem Ziel. Überwinde 8 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 160 |
| Kürzester Weg (Gehen/Springen) | 22 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 90 – 0.9.0 Sprungprüfung Diamant

**Mission: Löse das komplexe Raster mit einer durchdachten Sprungfolge. Überwinde 8 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 160 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Dichte Labyrinthe und lange Sprungfolgen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 91 – 0.9.1 Das große Sprunglabyrinth

**Mission: Nutze alle erlernten Strategien im großen Labyrinth. Überwinde 6 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 158 |
| Kürzester Weg (Gehen/Springen) | 42 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 92 – 0.9.2 Kammern ohne Karte

**Mission: Orientiere dich Schritt für Schritt durch unbekannte Kammern. Überwinde 6 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 158 |
| Kürzester Weg (Gehen/Springen) | 48 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 93 – 0.9.3 Der versperrte Zielweg

**Mission: Finde den Zielweg über mehrere Sprungübergänge. Überwinde 7 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 159 |
| Kürzester Weg (Gehen/Springen) | 17 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 94 – 0.9.4 Der lange Irrgarten

**Mission: Vermeide Sackgassen und plane die gesamte Route. Überwinde 7 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 159 |
| Kürzester Weg (Gehen/Springen) | 47 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 95 – 0.9.5 Sprungfolge Meister

**Mission: Kombiniere Sensoren, Schleifen und präzise Sprünge. Überwinde 8 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 160 |
| Kürzester Weg (Gehen/Springen) | 40 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 96 – 0.9.6 Das letzte Netz

**Mission: Finde im verzweigten Netz die Verbindung zum Ziel. Überwinde 8 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 160 |
| Kürzester Weg (Gehen/Springen) | 16 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 97 – 0.9.7 Meisterlabyrinth Nord

**Mission: Löse das große Nordlabyrinth mit mehreren Sprungbarrieren. Überwinde 9 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 161 |
| Kürzester Weg (Gehen/Springen) | 39 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 98 – 0.9.8 Meisterlabyrinth Süd

**Mission: Durchquere die verschachtelten Südkorridore. Überwinde 9 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 161 |
| Kürzester Weg (Gehen/Springen) | 27 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 99 – 0.9.9 Die finale Prüfung

**Mission: Setze Sensoren, Schleifen und Sprünge gezielt zusammen. Überwinde 10 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 162 |
| Kürzester Weg (Gehen/Springen) | 26 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Level 100 – 1.0.0 Das große Finale

**Mission: Bewältige das größte Labyrinth und erreiche den Ziel-Beeper. Überwinde 10 Sprungbarrieren mit jump(). Ziel: Erreiche den Beeper bei (13, 13) und hebe ihn auf.**

| Merkmal | Leveldaten |
|---|---|
| Start | `(1, 1)` |
| Startblickrichtung | Osten |
| Ziel | `(13, 13)` |
| Wände | 162 |
| Kürzester Weg (Gehen/Springen) | 20 Aktionen |
| Kürzeste Aktionsrouten | 1 |

**Lernfokus:** Meisterlabyrinthe mit Schleifen, Sensoren und Sprüngen.

### Vor dem Programmieren

1. Zeichne oder markiere Start und Ziel auf einem 15×15-Raster.
2. Markiere die Wände und nenne eine mögliche erste Entscheidung.
3. Überlege, welche Prüfung vor einer riskanten Bewegung hilft.

### Mein Lösungsplan

Welche Teilstrecken oder Entscheidungen wiederholen sich?

________________________________________________________________________

Welche Sensoren oder Python-Konstrukte willst du verwenden?

________________________________________________________________________

### Test und Rückblick

Was soll Pyti nach den ersten drei Aktionen tun?

________________________________________________________________________

Wo ist dein Programm zuerst anders gelaufen als erwartet?

________________________________________________________________________

Hat Pyti den Ziel-Beeper aufgenommen und trägt ihn noch?

☐ Ja  ☐ Nein    Was würdest du beim nächsten Versuch ändern?

________________________________________________________________________

\newpage

## Lehrkraft- und Adminnotizen

Vor der Ausgabe kann im Admin-Panel die lokale Levelkonfiguration
angepasst werden. Die hier gedruckten Koordinaten beschreiben die
mitgelieferten Standardlevel; nach Änderungen können sie abweichen.
Eine Anpassung der Schwierigkeit kann über die Anzahl und Lage der
Wände erfolgen. Vor dem Speichern muss der Ziel-Beper erreichbar bleiben.

### Beobachtungsbogen

| Lernende Person | Level | Beobachtung | Nächster Schritt |
|---|---:|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Freie Notizen

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________
