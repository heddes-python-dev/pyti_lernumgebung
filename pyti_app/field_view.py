"""Interaktive Qt-Ansicht des Spielfelds."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QGraphicsView

from .field_rendering import CELL_SIZE


class SpielfeldView(QGraphicsView):
    def __init__(self, scene, spielfeld_manager, parent=None):
        super().__init__(scene, parent)
        self.spielfeld_manager = spielfeld_manager
        self.setRenderHint(QPainter.Antialiasing)
        self.setFrameShape(QGraphicsView.NoFrame)
        self.setAlignment(Qt.AlignCenter)
        self.setBackgroundBrush(QColor("#e7eff4"))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setToolTip(
            "Linksklick: Beeper setzen/entfernen · Rechtsklick: Wand setzen/entfernen"
        )

    def mousePressEvent(self, event):
        if event.button() in (Qt.LeftButton, Qt.RightButton):
            pos = self.mapToScene(event.position().toPoint())
            x, y = int(pos.x() // CELL_SIZE), int(pos.y() // CELL_SIZE)
            if 0 <= x < self.spielfeld_manager.grid_size and 0 <= y < self.spielfeld_manager.grid_size:
                if event.button() == Qt.RightButton:
                    self.spielfeld_manager.toggle_wand(x, y)
                else:
                    self.spielfeld_manager.toggle_beeper(x, y)
            event.accept()
            return
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() in (Qt.LeftButton, Qt.RightButton):
            event.accept()
            return
        super().mouseReleaseEvent(event)
