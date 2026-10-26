"""Small visual editor for wall and beeper coordinates."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class CoordinateEditor(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel(title, self))
        self.items = QListWidget(self)
        self.items.setMaximumHeight(130)
        layout.addWidget(self.items)

        form = QFormLayout()
        self.x = self._coordinate()
        self.y = self._coordinate()
        form.addRow("X:", self.x)
        form.addRow("Y:", self.y)
        layout.addLayout(form)
        buttons = QHBoxLayout()
        add = QPushButton("Hinzufügen", self)
        remove = QPushButton("Ausgewählten entfernen", self)
        buttons.addWidget(add)
        buttons.addWidget(remove)
        layout.addLayout(buttons)
        add.clicked.connect(self.add_coordinate)
        remove.clicked.connect(self.remove_coordinate)
        self.items.currentItemChanged.connect(self._select_coordinate)

    @staticmethod
    def _coordinate():
        field = QSpinBox()
        field.setRange(0, 14)
        return field

    def coordinates(self):
        return [
            list(self.items.item(index).data(Qt.UserRole))
            for index in range(self.items.count())
        ]

    def set_coordinates(self, coordinates):
        self.items.clear()
        for point in sorted({tuple(point) for point in coordinates}):
            self._append(point)

    def add_coordinate(self):
        point = self.x.value(), self.y.value()
        for index in range(self.items.count()):
            item = self.items.item(index)
            if tuple(item.data(Qt.UserRole)) == point:
                self.items.setCurrentItem(item)
                return
        self._append(point)

    def _append(self, point):
        item = QListWidgetItem(f"X={point[0]}, Y={point[1]}")
        item.setData(Qt.UserRole, point)
        self.items.addItem(item)
        self.items.setCurrentItem(item)

    def remove_coordinate(self):
        row = self.items.currentRow()
        if row >= 0:
            self.items.takeItem(row)

    def _select_coordinate(self, item, _previous):
        if item is not None:
            x, y = item.data(Qt.UserRole)
            self.x.setValue(x)
            self.y.setValue(y)
