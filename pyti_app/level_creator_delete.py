"""Delete registered custom levels from the level creator."""

from collections.abc import Collection
from typing import TYPE_CHECKING, Callable

from PySide6.QtWidgets import QMessageBox

from .custom_levels import EigeneLevelSpeicher

if TYPE_CHECKING:
    from PySide6.QtWidgets import QComboBox, QLabel, QPushButton


class LevelCreatorDeleteActions:
    if TYPE_CHECKING:
        status: QLabel
        saved_level_list: QComboBox
        delete_saved_button: QPushButton
        existing_level_keys: Callable[[], Collection[str]]
        delete_level: Callable[[str], None] | None

    def _refresh_registered_levels(self, selected_key=None):
        keys = sorted(
            key for key in self.existing_level_keys()
            if key.startswith(EigeneLevelSpeicher.PREFIX)
        )
        self.saved_level_list.clear()
        for key in keys:
            label = key[len(EigeneLevelSpeicher.PREFIX):]
            self.saved_level_list.addItem(label, key)
        if selected_key in keys:
            self.saved_level_list.setCurrentIndex(keys.index(selected_key))
        self.delete_saved_button.setEnabled(
            self.delete_level is not None and bool(keys)
        )

    def _delete_registered_level(self):
        key = self.saved_level_list.currentData()
        if not key or self.delete_level is None:
            return
        answer = QMessageBox.question(
            self,
            "Eigenes Level löschen?",
            f"„{key}“ wird dauerhaft aus Pyti entfernt. Fortfahren?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
        try:
            self.delete_level(key)
        except (OSError, ValueError, TypeError, KeyError) as error:
            self.status.setText(f"Level nicht gelöscht: {error}")
            QMessageBox.warning(self, "Level nicht gelöscht", str(error))
            return
        self._refresh_registered_levels()
        self.status.setText(f"„{key}“ wurde aus Pyti entfernt.")
