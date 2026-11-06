"""Small per-level prompts for planning, trying, and reflecting."""


def _level_number(name):
    prefix = name.partition(" ")[0]
    try:
        major, minor, patch = (int(part) for part in prefix.split("."))
    except ValueError:
        return 0
    if (major, minor, patch) == (1, 0, 0):
        return 100
    if major == 0 and minor == 0:
        return patch
    if major == 0:
        return 10 + (minor - 1) * 10 + patch
    return 0


def prompts_for_level(name, level):
    number = _level_number(name)
    if number <= 10:
        objective = "Befehle in der passenden Reihenfolge ausführen."
        reflection = "Welche Anweisung hat Pyti zuletzt bewegt oder gedreht?"
    elif number <= 30:
        objective = "Einen Weg in Bewegungen und Richtungswechsel zerlegen."
        reflection = "Wie hast du entschieden, wann Pyti abbiegen muss?"
    elif number <= 50:
        objective = "Hindernisse beobachten und eine sichere Route planen."
        reflection = "Welche Stelle deiner Route war am schwierigsten?"
    elif number <= 60:
        objective = "Einen Sprung gezielt mit Bewegung und Drehung verbinden."
        reflection = "Woran erkennst du, ob ein Sprung hier sinnvoll ist?"
    elif number <= 80:
        objective = "Mehrere Wegabschnitte und Sprünge vorausplanen."
        reflection = "Wie hast du deine Sprünge mit den Drehungen abgestimmt?"
    elif number:
        objective = "Sensoren, Wiederholungen und Sprünge passend kombinieren."
        reflection = "Was würdest du an deiner Lösung beim nächsten Mal ändern?"
    else:
        objective = "Eine Route planen und Pyti Schritt für Schritt steuern."
        reflection = "Welche Entscheidung hat dir beim Finden des Wegs geholfen?"

    goal = tuple(level.get("goal", {}).get("position", ()))
    if number > 50:
        hint = (
            f"Prüfe vor jedem Sprung die Blickrichtung. Das Ziel liegt bei {goal}; "
            "ein Sprung bewegt Pyti zwei Felder weit."
        )
    elif level.get("waende"):
        hint = (
            f"Vergleiche Start, Blickrichtung und Ziel {goal}. "
            "Prüfe an einer Wand, ob ein anderer Weg oder ein Sensor hilft."
        )
    else:
        hint = (
            f"Vergleiche Pytis Start und Blickrichtung mit dem Ziel {goal}. "
            "Plane zuerst die Richtung, dann die Anzahl der Schritte."
        )
    return objective, hint, reflection
