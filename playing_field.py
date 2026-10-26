"""Compatibility-Importe für die Spielfeldansicht und -logik."""

from pyti_app.field_manager import SpielfeldManager
from pyti_app.field_rendering import CELL_SIZE
from pyti_app.field_view import SpielfeldView

__all__ = ["CELL_SIZE", "SpielfeldManager", "SpielfeldView"]
