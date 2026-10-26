"""Erzeugt die öffentliche Levelsammlung."""

from .level_generator import baue_level
from .maze_generator import baue_labyrinth
from .level_specs import LEVEL_SPECS, level_nummer, maze_level_specs

LEVELS = {}
for nummer, (name, start, ziel, waende, mission) in enumerate(LEVEL_SPECS, 1):
    LEVELS[f"{level_nummer(nummer)} {name}"] = baue_level(
        start, ziel, waende, nummer // 5, mission
    )

for nummer, (name, groesse, spruenge, mission) in enumerate(
    maze_level_specs(), len(LEVEL_SPECS) + 1
):
    level = baue_labyrinth((0, 0), (groesse - 1, groesse - 1), groesse,
                           nummer, spruenge)
    level["description"] = (
        f"Mission: {mission} Ziel: Erreiche den Beeper bei "
        f"{tuple(level['goal']['position'])} und hebe ihn auf."
    )
    LEVELS[f"{level_nummer(nummer)} {name}"] = level
