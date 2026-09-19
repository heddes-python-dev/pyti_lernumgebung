
```markdown
# Pyti-Skript-Beispiele (Cookbook)

Diese Sammlung zeigt verschiedene Ansätze und Programmiermuster, um Pyti zu steuern – vom einfachen Skript bis hin zur objektorientierten Programmierung.

## 1. Grundlagen: Suchen und Sammeln

Laufe so lange nach vorne, wie der Weg frei ist, und sammle jeden Beeper auf dem Weg ein:

```python
while frontClear():
    moveForward()
    if onBeeper():
        pickBeeper()

```

## 2. Bedingungen: Hindernisse umgehen

Prüfe vor jedem Schritt, ob der Weg frei ist. Wenn nicht, weiche aus (z. B. nach links):

```python
if frontClear():
    moveForward()
else:
    turnLeft()
    moveForward()
    turnRight()

```

## 3. Eigene Funktionen schreiben

Du kannst den Code in eigene Funktionen auslagern, um wiederkehrende Aufgaben zu strukturieren:

```python
def gehe_bis_wand():
    while frontClear():
        moveForward()

def sammle_falls_vorhanden():
    if onBeeper():
        pickBeeper()

# Ausführung
gehe_bis_wand()
sammle_falls_vorhanden()

```

## 4. Objektorientierte Programmierung (OOP) für Fortgeschrittene

Da der Editor normalen Python-Code ausführt, kannst du Pyti auch innerhalb von Klassen steuern:

```python
class PytiController:
    def __init__(self):
        self.beeper_zaehler = 0

    def durchsuche_feld(self):
        while frontClear():
            moveForward()
            if onBeeper():
                pickBeeper()
                self.beeper_zaehler += 1
        
        print(f"Mission beendet! Eingesammelte Beeper: {self.beeper_zaehler}")

# Bot initialisieren und starten
bot = PytiController()
bot.durchsuche_feld()

```

---

*Tipp: Du kannst diese Skripte direkt in den Editor kopieren und in späteren Leveln ausprobieren, um zu sehen, wie sich verschiedene Programmierstile auf Pytis Verhalten auswirken.*

```
