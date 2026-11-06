"""Displays actionable functional checks in the admin dialog."""

from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .admin_checks import pruefe_system


def _wall_layout_count(levels):
    layouts = set()
    for data in levels.values():
        if not isinstance(data, dict):
            continue
        walls = data.get("waende", [])
        if not isinstance(walls, (list, tuple)):
            continue
        normalized = []
        for wall in walls:
            if isinstance(wall, (list, tuple)) and len(wall) == 2:
                x, y = wall
                if isinstance(x, int) and isinstance(y, int):
                    normalized.append((x, y))
        if normalized:
            layouts.add(tuple(sorted(normalized)))
    return len(layouts)


class HealthTab(QWidget):
    def __init__(self, levels, widgets, interpreter, version, startup_error=""):
        super().__init__()
        self.levels = levels
        self.widgets = widgets
        self.interpreter = interpreter
        self.startup_error = startup_error
        self.run_count = 0
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Pyti-Version: {version}", self))
        layout.addWidget(QLabel(
            f"{len(levels)} Level · {_wall_layout_count(levels)} unterschiedliche Wandlayouts",
            self,
        ))
        self.result_summary = QLabel(self)
        layout.addWidget(self.result_summary)
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
        self.run_count += 1
        problems = sum(status in ("FEHLER", "WARNUNG") for status, *_ in results)
        notices = sum(status == "HINWEIS" for status, *_ in results)
        self.result_summary.setText(
            f"Prüfung {self.run_count} abgeschlossen: {len(results)} Bereiche · "
            f"{problems} Warnungen/Fehler · {notices} Hinweise · "
            f"{datetime.now().strftime('%H:%M:%S')}"
        )
        self.table.setRowCount(len(results))
        for row, (status, name, detail) in enumerate(results):
            for column, value in enumerate((status, name, detail)):
                item = QTableWidgetItem(value)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.table.setItem(row, column, item)
        self.table.resizeColumnsToContents()
