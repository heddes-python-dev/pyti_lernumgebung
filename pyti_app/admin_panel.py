"""Top-level admin dialog connecting editors, checks, and persistent storage."""

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMessageBox,
    QTabWidget,
    QVBoxLayout,
)

from .admin_backup_actions import AdminBackupActions
from .admin_panel_actions import AdminPanelActions
from .admin_store import AdminStore
from .admin_health_tab import HealthTab
from .admin_level_tab import LevelEditorTab
from .admin_tests_tab import AdminTestsTab
from .admin_scripts_tab import ScriptsTab
from .admin_settings_tab import SettingsTab
from .admin_tools_tab import AdminToolsTab


class AdminPanel(AdminBackupActions, AdminPanelActions, QDialog):
    def __init__(
        self,
        store,
        controller,
        settings,
        scripts,
        version,
        startup_error="",
        custom_level_store=None,
        draft_store=None,
        open_creator=None,
    ):
        super().__init__(controller.ui.window)
        self.store = store
        self.custom_level_store = custom_level_store
        self.draft_store = draft_store
        self.open_creator = open_creator
        self.deleted_custom_levels = set()
        self.controller = controller
        self.startup_error = startup_error
        self.setWindowTitle("Pyti – Admin-Bereich")
        self.resize(980, 720)
        layout = QVBoxLayout(self)
        self.save_status = QLabel(
            "Änderungen werden dauerhaft gespeichert, wenn du auf Speichern klickst.",
            self,
        )
        layout.addWidget(self.save_status)
        self.tabs = QTabWidget(self)
        self.health = HealthTab(
            controller.levels, controller.ui, controller.interpreter,
            version, startup_error,
        )
        self.tests = AdminTestsTab()
        self.settings = SettingsTab(settings, self)
        self.levels = LevelEditorTab(
            controller.levels,
            self,
            allow_custom_deletion=custom_level_store is not None,
        )
        self.levels.delete_button.clicked.connect(self._confirm_delete_level)
        self.scripts = ScriptsTab(scripts, self)
        self.scripts.load_requested.connect(self._load_script)
        self.tools = AdminToolsTab(self)
        self.tools.open_creator.connect(self._open_creator)
        self.tools.export_backup.connect(self._export_backup)
        self.tools.restore_backup.connect(self._restore_backup)
        self.tools.creator_button.setEnabled(open_creator is not None)
        self.tools.export_button.setEnabled(
            custom_level_store is not None and draft_store is not None
        )
        self.tools.restore_button.setEnabled(
            custom_level_store is not None and draft_store is not None
        )
        self.tabs.addTab(self.health, "Systemstatus")
        self.tabs.addTab(self.tests, "Entwicklertests")
        self.tabs.addTab(self.settings, "Einstellungen")
        self.tabs.addTab(self.levels, "Level bearbeiten")
        self.tabs.addTab(self.scripts, "Beispielskripte")
        self.tabs.addTab(self.tools, "Verwaltung")
        layout.addWidget(self.tabs)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel, self
        )
        self.buttons.accepted.connect(self.save)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

    def _load_script(self, code):
        self.controller.ui.editor.setPlainText(code)

    def save(self):
        try:
            levels = self.levels.values()
            settings = self.settings.values()
            scripts = self.scripts.values()
            for level in levels.values():
                AdminStore.validate_level(level)
            self.store.save(settings, levels, scripts)
            if self.deleted_custom_levels:
                custom_level_store = self.custom_level_store
                if custom_level_store is None:
                    raise ValueError("Der Speicher eigener Level ist nicht verfügbar.")
                custom_level_store.loeschen_mehrere(self.deleted_custom_levels)
        except (OSError, ValueError, TypeError, KeyError) as error:
            QMessageBox.critical(self, "Änderungen nicht gespeichert", str(error))
            return False
        self.controller.levels.clear()
        self.controller.levels.update(levels)
        self.controller.interpreter.max_execution_time = (
            settings["max_execution_time"]
        )
        self.controller.interpreter.action_delay_ms = settings["action_delay_ms"]
        self.controller.admin_settings = settings
        self.controller.admin_scripts = scripts
        self.deleted_custom_levels.clear()
        self.store.load_error = ""
        self._refresh_level_list(levels)
        self.startup_error = ""
        self.health.levels = self.controller.levels
        self.health.startup_error = ""
        self.health.refresh()
        self.save_status.setText("Änderungen gespeichert.")
        return True

    def _refresh_level_list(self, levels):
        current = self.controller.ui.level_liste.currentItem()
        current_name = current.text() if current is not None else ""
        for row in range(self.controller.ui.level_liste.count() - 1, -1, -1):
            if self.controller.ui.level_liste.item(row).text() not in levels:
                self.controller.ui.level_liste.takeItem(row)
        if current_name in levels:
            for row in range(self.controller.ui.level_liste.count()):
                if self.controller.ui.level_liste.item(row).text() == current_name:
                    self.controller.ui.level_liste.setCurrentRow(row)
                    break
        elif self.controller.ui.level_liste.count():
            self.controller.ui.level_liste.setCurrentRow(0)
        self.controller.level_wechsel(
            self.controller.ui.level_liste.currentItem()
        )
