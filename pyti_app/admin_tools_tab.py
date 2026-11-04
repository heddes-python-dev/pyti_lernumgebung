"""Central entry point for admin utilities and data protection."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class AdminToolsTab(QWidget):
    open_creator = Signal()
    export_backup = Signal()
    restore_backup = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(
            "Verwalte Level, erstelle eigene Aufgaben und sichere die lokalen "
            "Einstellungen, Skriptvorlagen und Levelentwürfe.",
            self,
        ))
        self.creator_button = QPushButton("Level-Creator öffnen", self)
        self.export_button = QPushButton("Sicherung exportieren …", self)
        self.restore_button = QPushButton("Sicherung wiederherstellen …", self)
        self.creator_button.clicked.connect(self.open_creator)
        self.export_button.clicked.connect(self.export_backup)
        self.restore_button.clicked.connect(self.restore_backup)
        layout.addWidget(self.creator_button)
        layout.addWidget(self.export_button)
        layout.addWidget(self.restore_button)
        layout.addStretch()
