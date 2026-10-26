"""Loads and saves local admin settings, level overrides, and script templates."""

import json
from collections import deque
from copy import deepcopy
from pathlib import Path

from .admin_script_data import DEFAULT_SCRIPTS, validate_scripts
from .level_generator import GRID_SIZE

DEFAULT_SETTINGS = {"max_execution_time": 30, "action_delay_ms": 200}


class AdminStore:
    def __init__(self, path):
        self.path = Path(path)
        self.load_error = ""

    def load(self, default_levels):
        levels = deepcopy(default_levels)
        scripts = deepcopy(DEFAULT_SCRIPTS)
        settings = dict(DEFAULT_SETTINGS)
        if not self.path.exists():
            return settings, levels, scripts
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("Die Admin-Datei muss ein JSON-Objekt enthalten.")
            settings = self._settings(data.get("settings", settings))
            levels = self._levels(default_levels, data.get("levels", {}))
            scripts = validate_scripts(data.get("scripts", scripts))
        except (OSError, ValueError, TypeError, KeyError) as error:
            self.load_error = f"Admin-Datei konnte nicht geladen werden: {error}"
            return dict(DEFAULT_SETTINGS), deepcopy(default_levels), scripts
        return settings, levels, scripts

    def save(self, settings, levels, scripts):
        settings = self._settings(settings)
        scripts = validate_scripts(scripts)
        for level in levels.values():
            self.validate_level(level)
        data = {"settings": settings, "levels": levels, "scripts": scripts}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        temporary.replace(self.path)

    @staticmethod
    def _settings(data):
        if not isinstance(data, dict):
            raise ValueError("Einstellungen müssen ein Objekt sein.")
        runtime = data.get("max_execution_time", 30)
        delay = data.get("action_delay_ms", 200)
        if type(runtime) is not int or not 1 <= runtime <= 300:
            raise ValueError("Zeitlimit muss zwischen 1 und 300 Sekunden liegen.")
        if type(delay) is not int or not 0 <= delay <= 2000:
            raise ValueError("Aktionsverzögerung muss zwischen 0 und 2000 ms liegen.")
        return {"max_execution_time": runtime, "action_delay_ms": delay}

    @staticmethod
    def _levels(defaults, overrides):
        if not isinstance(overrides, dict):
            raise ValueError("Leveldaten müssen als Objekt gespeichert sein.")
        levels = deepcopy(defaults)
        for name, values in overrides.items():
            if name not in levels or not isinstance(values, dict):
                raise ValueError(f"Unbekannter oder ungültiger Level: {name}")
            levels[name].update(values)
            AdminStore.validate_level(levels[name])
        return levels

    @staticmethod
    def validate_level(level):
        if not isinstance(level.get("description"), str):
            raise ValueError("Der Missionstext muss Text sein.")
        for key in ("start_x", "start_y", "start_richtung"):
            value = level.get(key)
            maximum = 3 if key == "start_richtung" else GRID_SIZE - 1
            if type(value) is not int or not 0 <= value <= maximum:
                raise ValueError(f"Ungültiger Wert für {key}.")
        goal = level.get("goal", {})
        if not isinstance(goal, dict) or goal.get("type") != "collect_beeper":
            raise ValueError("Das Ziel muss ein Sammel-Beeper-Ziel sein.")
        position = goal["position"] if "position" in goal else None
        if not isinstance(position, (list, tuple)) or len(position) != 2:
            raise ValueError("Das Ziel benötigt zwei Koordinaten.")
        goal = AdminStore._coordinates(position, "Ziel")
        walls = {AdminStore._coordinates(item, "Wand") for item in level["waende"]}
        beepers = {AdminStore._coordinates(item, "Beeper") for item in level["beeper"]}
        if walls & beepers:
            raise ValueError("Beeper dürfen nicht in Wänden liegen.")
        start = (level["start_x"], level["start_y"])
        if start in walls or goal in walls:
            raise ValueError("Start und Ziel dürfen nicht in einer Wand liegen.")
        if goal not in beepers:
            raise ValueError("Auf dem Ziel muss ein Beeper liegen.")
        if not AdminStore._reachable(start, goal, walls):
            raise ValueError("Das Ziel ist durch Wände nicht erreichbar.")

    @staticmethod
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

    @staticmethod
    def _coordinates(value, label):
        if not isinstance(value, (list, tuple)) or len(value) != 2:
            raise ValueError(f"{label} benötigt X- und Y-Koordinaten.")
        x, y = value
        if any(
            type(item) is not int or not 0 <= item < GRID_SIZE for item in (x, y)
        ):
            raise ValueError(
                f"{label}-Koordinaten müssen zwischen 0 und {GRID_SIZE - 1} liegen."
            )
        return x, y
