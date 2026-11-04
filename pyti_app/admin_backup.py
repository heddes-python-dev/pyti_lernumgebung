"""Validated export and restore of local Pyti administration data."""

import json
from copy import deepcopy
from pathlib import Path

from .admin_script_data import validate_scripts
from .admin_store import AdminStore
from .custom_levels import EigeneLevelSpeicher
from .level_creator_data import LevelEntwurfSpeicher

FORMAT = "pyti-admin-backup"
VERSION = 1


def create_backup(settings, levels, scripts, custom_levels, drafts):
    data = {
        "format": FORMAT,
        "version": VERSION,
        "settings": AdminStore._settings(settings),
        "levels": deepcopy(levels),
        "scripts": validate_scripts(scripts),
        "custom_levels": deepcopy(custom_levels),
        "drafts": deepcopy(drafts),
    }
    return validate_backup(data)


def validate_backup(data):
    if not isinstance(data, dict) or data.get("format") != FORMAT:
        raise ValueError("Die Datei ist keine Pyti-Administrationssicherung.")
    if data.get("version") != VERSION:
        raise ValueError("Die Sicherungsversion wird nicht unterstützt.")
    settings = AdminStore._settings(data.get("settings"))
    levels = data.get("levels")
    if not isinstance(levels, dict) or not levels:
        raise ValueError("Die Sicherung enthält keine gültigen Level.")
    for name, level in levels.items():
        if not isinstance(name, str) or not isinstance(level, dict):
            raise ValueError("Die Sicherung enthält einen ungültigen Level-Eintrag.")
        AdminStore.validate_level(level)
    custom_levels = data.get("custom_levels")
    if not isinstance(custom_levels, dict):
        raise ValueError("Eigene Level in der Sicherung sind ungültig.")
    for name, level in custom_levels.items():
        if not isinstance(name, str) or not name.startswith(
            EigeneLevelSpeicher.PREFIX
        ) or not isinstance(level, dict):
            raise ValueError("Die Sicherung enthält einen ungültigen eigenen Level.")
        AdminStore.validate_level(level)
    registered_custom = {
        name: level for name, level in levels.items()
        if name.startswith(EigeneLevelSpeicher.PREFIX)
    }
    if registered_custom.keys() != custom_levels.keys():
        raise ValueError("Eigene Level und Levelkatalog der Sicherung stimmen nicht überein.")
    for name, level in custom_levels.items():
        if json.dumps(level, sort_keys=True) != json.dumps(
            registered_custom[name], sort_keys=True
        ):
            raise ValueError(f"Eigener Level stimmt nicht überein: {name}")
    drafts = data.get("drafts")
    if not isinstance(drafts, list):
        raise ValueError("Levelentwürfe in der Sicherung sind ungültig.")
    for draft in drafts:
        if (
            not isinstance(draft, dict)
            or not isinstance(draft.get("name"), str)
            or not isinstance(draft.get("mission"), str)
            or not isinstance(draft.get("level"), dict)
        ):
            raise ValueError("Die Sicherung enthält einen ungültigen Levelentwurf.")
        AdminStore.validate_level(LevelEntwurfSpeicher._level_data(draft))
    return {
        "format": FORMAT,
        "version": VERSION,
        "settings": settings,
        "levels": deepcopy(levels),
        "scripts": validate_scripts(data.get("scripts")),
        "custom_levels": deepcopy(custom_levels),
        "drafts": deepcopy(drafts),
    }


def export_backup(path, data):
    validated = validate_backup(data)
    _atomic_write(Path(path), json.dumps(
        validated, ensure_ascii=False, indent=2
    ).encode("utf-8"))


def import_backup(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"Sicherung konnte nicht gelesen werden: {error}") from error
    return validate_backup(data)


def restore_backup(data, admin_store, custom_store, draft_store):
    validated = validate_backup(data)
    paths = (admin_store.path, custom_store.path, draft_store.path)
    previous = {
        path: path.read_bytes() if path.exists() else None for path in paths
    }
    try:
        admin_store.save(
            validated["settings"], validated["levels"], validated["scripts"]
        )
        custom_store.ersetzen(validated["custom_levels"])
        draft_store.speichern(validated["drafts"])
    except Exception as error:
        failures = []
        for path, content in previous.items():
            try:
                if content is None:
                    path.unlink(missing_ok=True)
                else:
                    _atomic_write(path, content)
            except OSError as rollback_error:
                failures.append(f"{path}: {rollback_error}")
        if failures:
            raise RuntimeError(
                "Wiederherstellung fehlgeschlagen; Rollback unvollständig: "
                + "; ".join(failures)
            ) from error
        raise


def _atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".restore-tmp")
    temporary.write_bytes(content)
    temporary.replace(path)
