"""Persistent local drafts and Python export for the level creator."""

import json
from copy import deepcopy
from pathlib import Path
from pprint import pformat

from .admin_store import AdminStore


def neuer_entwurf(name="Eigenes Level"):
    ziel = (1, 0)
    return {
        "name": name,
        "mission": "Plane einen Weg zum Ziel.",
        "level": {
            "start_x": 0,
            "start_y": 0,
            "start_richtung": 1,
            "waende": [],
            "beeper": [ziel],
            "goal": {"type": "collect_beeper", "position": ziel},
        },
    }


class LevelEntwurfSpeicher:
    def __init__(self, path):
        self.path = Path(path)

    def laden(self):
        if not self.path.exists():
            return [neuer_entwurf()]
        data = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("drafts"), list):
            raise ValueError("Die Entwurfsdatei muss eine Entwurfsliste enthalten.")
        if not data["drafts"]:
            return [neuer_entwurf()]
        drafts = deepcopy(data["drafts"])
        for draft in drafts:
            if not isinstance(draft, dict) or not isinstance(draft.get("level"), dict):
                raise ValueError("Ein gespeicherter Levelentwurf ist ungültig.")
            if not isinstance(draft.get("name"), str) or not isinstance(
                draft.get("mission"), str
            ):
                raise ValueError("Name und Mission eines Entwurfs müssen Text sein.")
            AdminStore.validate_level(self._level_data(draft))
        return drafts

    def speichern(self, drafts):
        for draft in drafts:
            AdminStore.validate_level(self._level_data(draft))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(
            json.dumps({"drafts": drafts}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary.replace(self.path)

    @staticmethod
    def _level_data(draft):
        level = deepcopy(draft["level"])
        goal = tuple(level["goal"]["position"])
        level["description"] = (
            f"Mission: {draft['mission']} Ziel: Erreiche den Beeper bei {goal} "
            "und hebe ihn auf."
        )
        return level


def export_code(name, draft):
    if not name.strip():
        raise ValueError("Bitte gib dem Level vor dem Export einen Namen.")
    data = LevelEntwurfSpeicher._level_data(draft)
    AdminStore.validate_level(data)
    snippet = {name.strip(): data}
    return (
        "# Optionaler Python-Quelltextexport; zum Aktivieren in Pyti "
        "'Speichern & in Pyti uebernehmen' verwenden.\n"
        f"LEVELS.update({pformat(snippet, sort_dicts=False, width=88)})\n"
    )
