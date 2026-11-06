"""Persist completed levels and the last selected level locally."""

import json
from pathlib import Path


class ProgressStore:
    def __init__(self, path):
        self.path = Path(path)
        self.load_error = ""
        self._load_failed = False

    def load(self):
        self.load_error = ""
        self._load_failed = False
        if not self.path.exists():
            return set(), ""
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("version") != 1:
                raise ValueError("Ungültiges Fortschrittsformat.")
            completed = data.get("completed_levels")
            active = data.get("active_level", "")
            if (
                not isinstance(completed, list)
                or any(not isinstance(name, str) for name in completed)
                or not isinstance(active, str)
            ):
                raise ValueError("Ungültige Levelangaben im Lernfortschritt.")
        except (OSError, ValueError, TypeError) as error:
            self.load_error = f"Lernfortschritt konnte nicht geladen werden: {error}"
            self._load_failed = True
            raise
        return set(completed), active

    def save(self, completed_levels, active_level):
        if self._load_failed:
            raise ValueError(
                "Die fehlerhafte Fortschrittsdatei wird nicht überschrieben."
            )
        completed = list(completed_levels)
        if any(not isinstance(name, str) for name in completed):
            raise ValueError("Levelnamen im Lernfortschritt müssen Text sein.")
        if not isinstance(active_level, str):
            raise ValueError("Der aktive Levelname muss Text sein.")
        data = {
            "version": 1,
            "completed_levels": sorted(set(completed)),
            "active_level": active_level,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        temporary.replace(self.path)
