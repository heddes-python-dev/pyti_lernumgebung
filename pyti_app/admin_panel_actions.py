"""Shared navigation and custom-level actions for the admin panel."""

from .admin_level_tab import LevelEditorTab
from PySide6.QtWidgets import QMessageBox


class AdminPanelActions:
    def _open_creator(self):
        if self.open_creator is None:
            return
        answer = QMessageBox.question(
            self,
            "Änderungen speichern?",
            "Änderungen im Admin-Bereich werden vor dem Öffnen des "
            "Level-Creators dauerhaft gespeichert.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes or not self.save():
            return
        self.open_creator()
        self.levels = self._replace_tab(
            self.levels,
            LevelEditorTab(
                self.controller.levels, self,
                allow_custom_deletion=self.custom_level_store is not None,
            ),
            "Level bearbeiten",
        )
        self.levels.delete_button.clicked.connect(self._confirm_delete_level)

    def _confirm_delete_level(self):
        name = self.levels.active_name
        if self.custom_level_store is None or not name.startswith(
            self.custom_level_store.PREFIX
        ):
            return
        answer = QMessageBox.question(
            self,
            "Eigenes Level löschen?",
            f"„{name}“ wird dauerhaft aus Pyti entfernt. Fortfahren?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
        self.levels.remove_level(name)
        self.deleted_custom_levels.add(name)
        self.save_status.setText(
            "Löschen vorgemerkt. Klicke auf Speichern, um es dauerhaft zu übernehmen."
        )
