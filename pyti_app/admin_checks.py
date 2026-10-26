"""Non-destructive health checks for the local admin panel."""

import importlib
from collections import deque

from .field_manager import SpielfeldManager
from .admin_store import AdminStore
from .level_generator import GRID_SIZE
from .robot import Pyti
from .script_runtime import BefehlsInterpreter
from .levels import LEVELS


def pruefe_system(levels, widgets, interpreter, startup_error=""):
    results = [
        _check("Module", _check_imports),
        _check("Spiellogik", _check_gameplay),
        _check("Level", lambda: _check_levels(levels)),
        _check("Oberfläche", lambda: _check_ui(widgets)),
    ]
    if startup_error:
        results.append(("WARNUNG", "Konfiguration", startup_error))
    else:
        results.append(("OK", "Konfiguration", "Admin-Daten geladen."))
    error = interpreter.last_execution_error
    results.append((
        "FEHLER" if error else "OK",
        "Letzter Skriptfehler",
        error or "Seit Programmstart kein Skriptfehler.",
    ))
    return results


def _check(name, callback):
    try:
        detail = callback()
        return "OK", name, detail or "Prüfung erfolgreich."
    except Exception as error:
        return "FEHLER", name, f"{type(error).__name__}: {error}"


def _check_imports():
    modules = (
        "pyti_app.application", "pyti_app.app_controller",
        "pyti_app.field_manager", "pyti_app.level_generator",
        "pyti_app.script_runtime", "pyti_app.script_worker",
        "pyti_app.admin_panel", "pyti_app.admin_store",
    )
    for module in modules:
        importlib.import_module(module)
    return f"{len(modules)} Anwendungsmodule importierbar."


def _check_gameplay():
    field = SpielfeldManager(grid_size=3)
    robot = Pyti(grid_size=3)
    level = {
        "start_x": 0, "start_y": 0, "start_richtung": 1,
        "waende": [], "beeper": [(1, 0), (2, 0)],
        "goal": {"type": "collect_beeper", "position": (1, 0)},
        "description": "Admin-Selbsttest",
    }
    field.lade_level(level, robot)
    interpreter = BefehlsInterpreter(robot, field)
    if interpreter.aktion_ausfuehren("frontClear") is not True:
        raise RuntimeError("Der Wegsensor meldet fälschlich eine Blockade.")
    if interpreter.aktion_ausfuehren("beeperAhead") is not True:
        raise RuntimeError("Der Beeper-Sensor erkennt den Beeper nicht.")
    interpreter.aktion_ausfuehren("moveForward")
    interpreter.aktion_ausfuehren("pickBeeper")
    interpreter.aktion_ausfuehren("moveForward")
    interpreter.aktion_ausfuehren("pickBeeper")
    interpreter.aktion_ausfuehren("dropBeeper")
    interpreter.aktion_ausfuehren("turnAround")
    interpreter.aktion_ausfuehren("moveForward")
    if not field.ziel_erreicht(robot, level["goal"]):
        raise RuntimeError("Ziel-Beeper ging beim Ablegen eines anderen verloren.")
    interpreter.aktion_ausfuehren("dropBeeper")
    if field.ziel_erreicht(robot, level["goal"]):
        raise RuntimeError("Abgelegter Ziel-Beeper wird weiter als gesammelt gezählt.")
    return "Sensoren, Bewegung, Beeper und Zielprüfung funktionieren."


def _check_levels(levels):
    missing = set(LEVELS) - set(levels)
    if missing:
        raise ValueError(f"Standardlevel fehlen: {', '.join(sorted(missing))}.")
    for name, level in levels.items():
        AdminStore.validate_level(level)
        start = (level["start_x"], level["start_y"])
        goal = tuple(level["goal"]["position"])
        walls = set(map(tuple, level["waende"]))
        if start in walls or goal in walls:
            raise ValueError(f"{name}: Start oder Ziel liegt in einer Wand.")
        if not _reachable(start, goal, walls):
            raise ValueError(f"{name}: Ziel ist nicht erreichbar.")
    return f"{len(levels)} Level geprüft; alle Ziele sind erreichbar."


def _reachable(start, goal, walls):
    visited = {start}
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            point = x + dx, y + dy
            if (
                0 <= point[0] < GRID_SIZE and 0 <= point[1] < GRID_SIZE
                and point not in walls and point not in visited
            ):
                if point == goal:
                    return True
                visited.add(point)
                queue.append(point)
    return start == goal


def _check_ui(widgets):
    required = (
        widgets.window, widgets.level_liste, widgets.editor,
        widgets.reset_button, widgets.stop_button, widgets.status,
        widgets.spielfeld_view, widgets.creator_button,
        widgets.admin_button,
    )
    if any(widget is None for widget in required):
        raise ValueError("Mindestens ein benötigtes UI-Element fehlt.")
    return "Fenster, Levelauswahl, Editor und Spielfeld vorhanden."
