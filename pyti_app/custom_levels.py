"""Store and validate user-created levels independently from Python source."""

import json
from copy import deepcopy
from pathlib import Path

from .admin_store import AdminStore


class EigeneLevelSpeicher:
    PREFIX = "Eigenes Level: "

    def __init__(self, path):
        self.path = Path(path)

    def laden(self):
        if not self.path.exists():
            return {}
        data = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("levels"), dict):
            raise ValueError("Die Datei eigener Level hat ein ungültiges Format.")
        levels = deepcopy(data["levels"])
        for name, level in levels.items():
            if not name.startswith(self.PREFIX) or not isinstance(level, dict):
                raise ValueError(f"Ungültiger eigener Level-Eintrag: {name}")
            AdminStore.validate_level(level)
        return levels

    def speichern(self, name, level):
        key = self.schluessel(name)
        AdminStore.validate_level(level)
        levels = self.laden()
        levels[key] = deepcopy(level)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(
            json.dumps({"levels": levels}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary.replace(self.path)
        return key

    @classmethod
    def schluessel(cls, name):
        normalized = name.strip()
        if not normalized:
            raise ValueError("Bitte gib dem Level einen Namen.")
        return f"{cls.PREFIX}{normalized}"
