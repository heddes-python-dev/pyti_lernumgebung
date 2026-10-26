"""Displays actionable functional checks in the admin dialog."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .admin_checks import pruefe_system


class HealthTab(QWidget):
    def __init__(self, levels, widgets, interpreter, version, startup_error=""):
        super().__init__()
        self.levels = levels
        self.widgets = widgets
        self.interpreter = interpreter
        self.startup_error = startup_error
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Pyti-Version: {version}", self))
        unique = {
            tuple(sorted(tuple(wall) for wall in data["waende"]))
            for data in levels.values()
        }
        layout.addWidget(QLabel(
            f"{len(levels)} Level · {len(unique)} unterschiedliche Wandlayouts",
            self,
        ))
        self.run_button = QPushButton("Prüfungen erneut ausführen", self)
        self.run_button.clicked.connect(self.refresh)
        layout.addWidget(self.run_button)
        self.table = QTableWidget(0, 3, self)
        self.table.setHorizontalHeaderLabels(["Status", "Bereich", "Ergebnis"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.table, 1)
        self.refresh()

    def refresh(self):
        results = pruefe_system(
            self.levels, self.widgets, self.interpreter, self.startup_error
        )
        self.table.setRowCount(len(results))
        for row, (status, name, detail) in enumerate(results):
            for column, value in enumerate((status, name, detail)):
                item = QTableWidgetItem(value)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.table.setItem(row, column, item)
        self.table.resizeColumnsToContents()
