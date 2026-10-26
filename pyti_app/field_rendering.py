"""Grafische Darstellung der Spielfeldzellen und -objekte."""

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QPainter,
    QPainterPath,
    QPen,
    QPolygonF,
)
from PySide6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsLineItem,
    QGraphicsPathItem,
    QGraphicsPolygonItem,
    QGraphicsRectItem,
    QGraphicsScene,
)

CELL_SIZE = 40


class SpielfeldDarstellung:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.scene = QGraphicsScene()
        self.raster_items = []
        self.wand_items = []
        self.avatar_items = []
        self.beeper_items = []
        self.zeichne_raster(None)

    def zeichne_raster(self, ziel_position):
        self._entferne_items(self.raster_items)
        ziel_stift = QPen(QColor("#72b7a0"), 2, Qt.DashLine)
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                zelle = QGraphicsRectItem(
                    x * CELL_SIZE + 1,
                    y * CELL_SIZE + 1,
                    CELL_SIZE - 2,
                    CELL_SIZE - 2,
                )
                ist_ziel = (x, y) == ziel_position
                farbe = "#e4f4ec" if ist_ziel else (
                    "#fbfdff" if (x + y) % 2 == 0 else "#f1f6f9"
                )
                zelle.setBrush(QBrush(QColor(farbe)))
                zelle.setPen(ziel_stift if ist_ziel else QPen(Qt.NoPen))
                zelle.setZValue(-2)
                self.scene.addItem(zelle)
                self.raster_items.append(zelle)
        self._zeichne_gitterlinien()
        self.scene.setSceneRect(
            0, 0, self.grid_size * CELL_SIZE, self.grid_size * CELL_SIZE
        )

    def _zeichne_gitterlinien(self):
        stift = QPen(QColor("#cbd8e0"), 1)
        for index in range(self.grid_size + 1):
            self.raster_items.append(self.scene.addLine(
                index * CELL_SIZE, 0, index * CELL_SIZE,
                self.grid_size * CELL_SIZE, stift,
            ))
            self.raster_items.append(self.scene.addLine(
                0, index * CELL_SIZE, self.grid_size * CELL_SIZE,
                index * CELL_SIZE, stift,
            ))
        for item in self.raster_items[-2 * (self.grid_size + 1):]:
            item.setZValue(-1)

    def zeichne_waende(self, koordinaten):
        self._entferne_items(self.wand_items)
        for x, y in koordinaten:
            left, top = x * CELL_SIZE + 2, y * CELL_SIZE + 2
            path = QPainterPath()
            path.addRoundedRect(left, top, CELL_SIZE - 4, CELL_SIZE - 4, 6, 6)
            wall = QGraphicsPathItem(path)
            wall.setBrush(QBrush(QColor("#526574")))
            wall.setPen(QPen(QColor("#354653"), 1.5))
            wall.setZValue(1)
            self.scene.addItem(wall)
            self.wand_items.append(wall)
            edge = self.scene.addLine(
                left + 6, top + 5, left + CELL_SIZE - 10, top + 5,
                QPen(QColor("#8294a0"), 1.5),
            )
            edge.setZValue(2)
            self.wand_items.append(edge)

    def zeichne_pyti(self, pyti):
        self._entferne_items(self.avatar_items)
        x, y = pyti.x * CELL_SIZE, pyti.y * CELL_SIZE
        cx, cy = x + CELL_SIZE / 2, y + CELL_SIZE / 2
        body = QGraphicsEllipseItem(x + 6, y + 6, 28, 28)
        body.setBrush(QBrush(QColor("#3186d5")))
        body.setPen(QPen(QColor("#164a83"), 2))
        body.setZValue(4)
        self.scene.addItem(body)
        self.avatar_items.append(body)
        points = {
            0: (QPointF(cx, y + 5), QPointF(cx - 5, y + 15), QPointF(cx + 5, y + 15)),
            1: (QPointF(x + 35, cy), QPointF(x + 25, cy - 5), QPointF(x + 25, cy + 5)),
            2: (QPointF(cx, y + 35), QPointF(cx - 5, y + 25), QPointF(cx + 5, y + 25)),
            3: (QPointF(x + 5, cy), QPointF(x + 15, cy - 5), QPointF(x + 15, cy + 5)),
        }[pyti.richtung]
        arrow = QGraphicsPolygonItem(QPolygonF(points))
        arrow.setBrush(QBrush(QColor("#fffdf4")))
        arrow.setPen(QPen(QColor("#164a83"), 1))
        arrow.setZValue(5)
        self.scene.addItem(arrow)
        self.avatar_items.append(arrow)

    def zeichne_beeper(self, koordinaten):
        self._entferne_items(self.beeper_items)
        for x, y in koordinaten:
            left, top = x * CELL_SIZE + 10, y * CELL_SIZE + 10
            item = QGraphicsEllipseItem(left, top, 20, 20)
            item.setBrush(QBrush(QColor("#ffc943")))
            item.setPen(QPen(QColor("#b66a12"), 1.5))
            item.setZValue(3)
            self.scene.addItem(item)
            self.beeper_items.append(item)
            shine = QGraphicsEllipseItem(left + 4, top + 3, 6, 5)
            shine.setBrush(QBrush(QColor("#fff4c2")))
            shine.setPen(QPen(Qt.NoPen))
            shine.setZValue(3)
            self.scene.addItem(shine)
            self.beeper_items.append(shine)

    def _entferne_items(self, items):
        for item in items:
            self.scene.removeItem(item)
        items.clear()
