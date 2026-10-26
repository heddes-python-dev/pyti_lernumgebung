"""Click-to-edit grid used by the level creator."""

from PySide6.QtCore import Qt

from .field_rendering import CELL_SIZE
from .field_view import SpielfeldView


class LevelCreatorView(SpielfeldView):
    def __init__(self, scene, field, clicked, parent=None):
        super().__init__(scene, field, parent)
        self.cell_clicked = clicked
        self.setToolTip("Zelle mit dem gewählten Werkzeug bearbeiten")

    def mousePressEvent(self, event):
        if event.button() in (Qt.LeftButton, Qt.RightButton):
            point = self.mapToScene(event.position().toPoint())
            x, y = int(point.x() // CELL_SIZE), int(point.y() // CELL_SIZE)
            if 0 <= x < self.spielfeld_manager.grid_size and 0 <= y < self.spielfeld_manager.grid_size:
                self.cell_clicked(event.button(), x, y)
            event.accept()
            return
        super().mousePressEvent(event)
