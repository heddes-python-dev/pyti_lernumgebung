"""Build the visual editor controls for the level creator dialog."""

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
)

from .level_creator_view import LevelCreatorView


def build_creator_ui(dialog):
    layout = QVBoxLayout(dialog)
    draft_row = QHBoxLayout()
    dialog.draft_list = QComboBox(dialog)
    dialog.new_button = QPushButton("Neuer Entwurf", dialog)
    dialog.delete_button = QPushButton("Entwurf löschen", dialog)
    draft_row.addWidget(dialog.draft_list, 1)
    draft_row.addWidget(dialog.new_button)
    draft_row.addWidget(dialog.delete_button)
    layout.addLayout(draft_row)

    form = QFormLayout()
    dialog.name = QLineEdit(dialog)
    dialog.mission = QLineEdit(dialog)
    dialog.mode = QComboBox(dialog)
    for title, value in (
        ("Wand setzen/entfernen (Rechtsklick)", "wall"),
        ("Beeper setzen/entfernen (Linksklick)", "beeper"),
        ("Startpunkt setzen (Linksklick)", "start"),
        ("Ziel setzen (Linksklick)", "goal"),
    ):
        dialog.mode.addItem(title, value)
    dialog.direction = QComboBox(dialog)
    dialog.direction.addItems(["Norden", "Osten", "Süden", "Westen"])
    form.addRow("Levelname:", dialog.name)
    form.addRow("Mission:", dialog.mission)
    form.addRow("Spielfeld-Werkzeug:", dialog.mode)
    form.addRow("Startblickrichtung:", dialog.direction)
    layout.addLayout(form)

    dialog.view = LevelCreatorView(
        dialog.field.scene, dialog.field, dialog._cell_clicked, dialog
    )
    dialog.view.setMinimumSize(620, 620)
    layout.addWidget(dialog.view, 1)
    footer = QHBoxLayout()
    dialog.status = QLabel(
        dialog.load_error or "Entwurf wird lokal gespeichert.", dialog
    )
    dialog.status.setWordWrap(True)
    dialog.register_button = QPushButton("Speichern & in Pyti übernehmen", dialog)
    dialog.export_button = QPushButton("Python-Datei exportieren", dialog)
    footer.addWidget(dialog.status, 1)
    footer.addWidget(dialog.register_button)
    footer.addWidget(dialog.export_button)
    layout.addLayout(footer)
