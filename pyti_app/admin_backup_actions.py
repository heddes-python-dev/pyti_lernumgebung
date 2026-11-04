"""Qt actions for exporting, restoring, and applying admin backups."""

from PySide6.QtWidgets import QFileDialog, QMessageBox

from .admin_backup import create_backup, export_backup, import_backup, restore_backup
from .admin_level_tab import LevelEditorTab
from .admin_scripts_tab import ScriptsTab


class AdminBackupActions:
    def _export_backup(self):
        try:
            data = create_backup(
                self.settings.values(), self.levels.values(),
                self.scripts.values(), self.custom_level_store.laden(),
                self.draft_store.laden(),
            )
        except (OSError, ValueError, TypeError, KeyError) as error:
            QMessageBox.warning(self, "Sicherung nicht erstellt", str(error))
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Pyti-Sicherung exportieren", "pyti-sicherung.json",
            "Pyti-Sicherung (*.json)",
        )
        if not path:
            return
        try:
            export_backup(path, data)
        except (OSError, ValueError, TypeError) as error:
            QMessageBox.critical(self, "Export fehlgeschlagen", str(error))
            return
        self.save_status.setText(f"Sicherung exportiert: {path}")

    def _restore_backup(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Pyti-Sicherung auswählen", "", "Pyti-Sicherung (*.json)"
        )
        if not path:
            return
        try:
            data = import_backup(path)
        except (OSError, ValueError, TypeError, KeyError) as error:
            QMessageBox.warning(self, "Sicherung ungültig", str(error))
            return
        answer = QMessageBox.question(
            self,
            "Sicherung wiederherstellen?",
            "Einstellungen, Level, Skriptvorlagen und Entwürfe werden durch "
            "die ausgewählte Sicherung ersetzt.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
        try:
            restore_backup(
                data, self.store, self.custom_level_store, self.draft_store
            )
        except (OSError, ValueError, TypeError, KeyError, RuntimeError) as error:
            QMessageBox.critical(self, "Wiederherstellung fehlgeschlagen", str(error))
            return
        self._apply_backup(data)
        self.save_status.setText("Sicherung wiederhergestellt.")

    def _apply_backup(self, data):
        self.controller.levels.clear()
        self.controller.levels.update(data["levels"])
        self.controller.interpreter.max_execution_time = (
            data["settings"]["max_execution_time"]
        )
        self.controller.interpreter.action_delay_ms = (
            data["settings"]["action_delay_ms"]
        )
        self.controller.admin_settings = data["settings"]
        self.controller.admin_scripts = data["scripts"]
        self.settings.timeout.setValue(data["settings"]["max_execution_time"])
        self.settings.delay.setValue(data["settings"]["action_delay_ms"])
        self.levels = self._replace_tab(
            self.levels, LevelEditorTab(
                data["levels"], self,
                allow_custom_deletion=self.custom_level_store is not None,
            ), "Level bearbeiten",
        )
        self.levels.delete_button.clicked.connect(self._confirm_delete_level)
        self.scripts = self._replace_tab(
            self.scripts, ScriptsTab(data["scripts"], self), "Beispielskripte"
        )
        self.scripts.load_requested.connect(self._load_script)
        self.deleted_custom_levels.clear()
        self.store.load_error = ""
        self._refresh_level_list(data["levels"])
        self.health.levels = self.controller.levels
        self.health.startup_error = ""
        self.health.refresh()

    def _replace_tab(self, old, new, title):
        index = self.tabs.indexOf(old)
        self.tabs.removeTab(index)
        old.deleteLater()
        self.tabs.insertTab(index, new, title)
        return new
