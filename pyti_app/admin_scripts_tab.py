"""Manage reusable Python examples from the admin panel."""

from copy import deepcopy

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ScriptsTab(QWidget):
    load_requested = Signal(str)

    def __init__(self, scripts, parent=None):
        super().__init__(parent)
        self.scripts = deepcopy(scripts)
        self.active_row = -1
        layout = QHBoxLayout(self)
        self.script_list = QListWidget(self)
        self.script_list.setMinimumWidth(180)
        layout.addWidget(self.script_list)
        editor = QWidget(self)
        editor_layout = QVBoxLayout(editor)
        editor_layout.addWidget(QLabel("Name der Vorlage:", editor))
        self.name = QLineEdit(editor)
        editor_layout.addWidget(self.name)
        editor_layout.addWidget(QLabel("Python-Beispiel:", editor))
        self.code = QPlainTextEdit(editor)
        editor_layout.addWidget(self.code, 1)
        buttons = QHBoxLayout()
        self.add_button = QPushButton("Neu", editor)
        self.save_button = QPushButton("Vorlage übernehmen", editor)
        self.delete_button = QPushButton("Löschen", editor)
        self.load_button = QPushButton("In Editor laden", editor)
        for button in (
            self.add_button, self.save_button, self.delete_button,
            self.load_button,
        ):
            buttons.addWidget(button)
        editor_layout.addLayout(buttons)
        layout.addWidget(editor, 1)
        self.script_list.addItems(item["name"] for item in self.scripts)
        self.script_list.currentRowChanged.connect(self._selection_changed)
        self.add_button.clicked.connect(self.add_script)
        self.save_button.clicked.connect(self.save_current)
        self.delete_button.clicked.connect(self.delete_current)
        self.load_button.clicked.connect(self.load_selected)
        if self.scripts:
            self.script_list.setCurrentRow(0)

    def _selection_changed(self, current):
        if 0 <= self.active_row < len(self.scripts):
            self._capture(self.active_row)
        self.active_row = current
        if 0 <= current < len(self.scripts):
            item = self.scripts[current]
            self.name.setText(item["name"])
            self.code.setPlainText(item["code"])

    def _capture(self, row):
        self.scripts[row] = {
            "name": self.name.text().strip(),
            "code": self.code.toPlainText(),
        }
        self.script_list.item(row).setText(self.scripts[row]["name"])

    def add_script(self):
        self.scripts.append({"name": "Neue Vorlage", "code": ""})
        self.script_list.addItem("Neue Vorlage")
        self.script_list.setCurrentRow(len(self.scripts) - 1)

    def save_current(self):
        row = self.script_list.currentRow()
        if row >= 0:
            self._capture(row)

    def delete_current(self):
        row = self.script_list.currentRow()
        if row < 0:
            return
        self.save_current()
        self.script_list.blockSignals(True)
        self.scripts.pop(row)
        self.script_list.takeItem(row)
        if self.scripts:
            self.script_list.setCurrentRow(0)
        self.script_list.blockSignals(False)
        self.active_row = -1
        if self.scripts:
            self._selection_changed(self.script_list.currentRow())
        else:
            self.name.clear()
            self.code.clear()

    def load_selected(self):
        row = self.script_list.currentRow()
        if row >= 0:
            self.save_current()
            self.load_requested.emit(self.scripts[row]["code"])

    def values(self):
        self.save_current()
        return deepcopy(self.scripts)
