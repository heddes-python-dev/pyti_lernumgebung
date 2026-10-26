"""Erzeugt die öffentliche Levelsammlung."""

from .level_generator import baue_level
from .level_specs import LEVEL_SPECS

LEVELS = {
    f"0.0.{nummer} {name}": baue_level(
        start, ziel, waende, nummer // 5, mission
    )
    for nummer, (name, start, ziel, waende, mission) in enumerate(LEVEL_SPECS, 1)
}
