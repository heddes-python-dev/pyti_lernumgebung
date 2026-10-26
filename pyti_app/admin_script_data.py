"""Default and validation helpers for reusable script templates."""

DEFAULT_SCRIPTS = [
    {
        "name": "Zum Beeper",
        "code": "while not onBeeper():\n    moveForward()\npickBeeper()",
    }
]


def validate_scripts(data):
    if not isinstance(data, list):
        raise ValueError("Skriptvorlagen müssen eine Liste sein.")
    result = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Jede Vorlage braucht einen Namen und Skripttext.")
        name, code = item.get("name"), item.get("code")
        if not isinstance(name, str) or not name.strip() or not isinstance(
            code, str
        ):
            raise ValueError("Jede Vorlage braucht einen Namen und Skripttext.")
        result.append({"name": name.strip(), "code": code})
    return result
