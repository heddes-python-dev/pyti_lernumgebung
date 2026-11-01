"""Visual level editor used by the local admin dialog."""

from copy import deepcopy

from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGridLayout,
    QLabel,
    QListWidget,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from .admin_coordinates import CoordinateEditor
from .admin_store import AdminStore
from .custom_levels import EigeneLevelSpeicher


class LevelEditorTab(QWidget):
    def __init__(self, levels, parent=None, allow_custom_deletion=False):
        super().__init__(parent)
        self.levels = deepcopy(levels)
        self.active_name = ""
        self.allow_custom_deletion = allow_custom_deletion
        layout = QGridLayout(self)
        self.level_list = QListWidget(self)
        self.level_list.setMinimumWidth(230)
        layout.addWidget(self.level_list, 0, 0, 1, 1)
        self.delete_button = QPushButton("Eigenes Level löschen", self)
        self.delete_button.setEnabled(allow_custom_deletion)
        layout.addWidget(self.delete_button, 1, 0)
        self.details = QWidget(self)
        form = QFormLayout(self.details)
        self.description = QPlainTextEdit(self.details)
        self.description.setMaximumHeight(90)
        form.addRow("Missionsbeschreibung:", self.description)
        self.start_x, self.start_y = self._coordinate(), self._coordinate()
        self.direction = QComboBox(self.details)
        self.direction.addItems(["Norden", "Osten", "Süden", "Westen"])
        form.addRow("Start X / Y:", self._pair(self.start_x, self.start_y))
        form.addRow("Startblickrichtung:", self.direction)
        self.goal_x, self.goal_y = self._coordinate(), self._coordinate()
        form.addRow("Ziel X / Y:", self._pair(self.goal_x, self.goal_y))
        self.walls = CoordinateEditor("Wände", self.details)
        self.beepers = CoordinateEditor("Beeper", self.details)
        objects = QGridLayout()
        objects.addWidget(self.walls, 0, 0)
        objects.addWidget(self.beepers, 0, 1)
        form.addRow("Spielfeldobjekte:", objects)
        layout.addWidget(self.details, 0, 1)
        layout.addWidget(QLabel(
            "Koordinaten beginnen links oben bei (0, 0).", self
        ), 1, 1)
        self.level_list.addItems(self.levels)
        self.level_list.currentTextChanged.connect(self._change_level)
        self.level_list.currentTextChanged.connect(self._update_delete_button)
        self.level_list.setCurrentRow(0)

    @staticmethod
    def _coordinate():
        field = QSpinBox()
        field.setRange(0, 14)
        return field

    @staticmethod
    def _pair(first, second):
        row = QWidget()
        layout = QGridLayout(row)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(first, 0, 0)
        layout.addWidget(second, 0, 1)
        return row

    def _change_level(self, name):
        if self.active_name:
            self._capture()
        self.active_name = name
        if not name:
            return
        level = self.levels[name]
        self.description.setPlainText(level["description"])
        self.start_x.setValue(level["start_x"])
        self.start_y.setValue(level["start_y"])
        self.direction.setCurrentIndex(level["start_richtung"])
        goal_x, goal_y = level["goal"]["position"]
        self.goal_x.setValue(goal_x)
        self.goal_y.setValue(goal_y)
        self.walls.set_coordinates(level["waende"])
        self.beepers.set_coordinates(level["beeper"])

    def _capture(self):
        level = self.levels[self.active_name]
        level.update({
            "description": self.description.toPlainText(),
            "start_x": self.start_x.value(),
            "start_y": self.start_y.value(),
            "start_richtung": self.direction.currentIndex(),
            "waende": self.walls.coordinates(),
            "beeper": self.beepers.coordinates(),
        })
        level["goal"]["position"] = [self.goal_x.value(), self.goal_y.value()]

    def _update_delete_button(self, name):
        self.delete_button.setEnabled(
            self.allow_custom_deletion
            and name.startswith(EigeneLevelSpeicher.PREFIX)
        )

    def remove_level(self, name):
        if not name.startswith(EigeneLevelSpeicher.PREFIX) or name not in self.levels:
            raise ValueError("Es können nur vorhandene eigene Level gelöscht werden.")
        if self.active_name:
            self._capture()
        row = next(
            index for index in range(self.level_list.count())
            if self.level_list.item(index).text() == name
        )
        self.levels.pop(name)
        self.active_name = ""
        self.level_list.takeItem(row)
        if self.level_list.count():
            self.level_list.setCurrentRow(min(row, self.level_list.count() - 1))
        else:
            self.details.setEnabled(False)
            self.delete_button.setEnabled(False)

    def values(self):
        if self.active_name:
            self._capture()
        for name, level in self.levels.items():
            AdminStore.validate_level(level)
        return deepcopy(self.levels)
