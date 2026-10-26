"""Top-level admin dialog connecting editors, checks, and persistent storage."""

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMessageBox,
    QTabWidget,
    QVBoxLayout,
)

from .admin_store import AdminStore
from .admin_health_tab import HealthTab
from .admin_level_tab import LevelEditorTab
from .admin_scripts_tab import ScriptsTab
from .admin_settings_tab import SettingsTab


class AdminPanel(QDialog):
    def __init__(
        self, store, controller, settings, scripts, version, startup_error=""
    ):
        super().__init__(controller.ui.window)
        self.store = store
        self.controller = controller
        self.startup_error = startup_error
        self.setWindowTitle("Pyti – Administration")
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
        self.settings = SettingsTab(settings, self)
        self.levels = LevelEditorTab(controller.levels, self)
        self.scripts = ScriptsTab(scripts, self)
        self.scripts.load_requested.connect(self._load_script)
        self.tabs.addTab(self.health, "Systemstatus")
        self.tabs.addTab(self.settings, "Einstellungen")
        self.tabs.addTab(self.levels, "Level bearbeiten")
        self.tabs.addTab(self.scripts, "Beispielskripte")
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
        except (OSError, ValueError, TypeError, KeyError) as error:
            QMessageBox.critical(self, "Änderungen nicht gespeichert", str(error))
            return
        self.controller.levels.clear()
        self.controller.levels.update(levels)
        self.controller.interpreter.max_execution_time = (
            settings["max_execution_time"]
        )
        self.controller.interpreter.action_delay_ms = settings["action_delay_ms"]
        self.controller.admin_settings = settings
        self.controller.admin_scripts = scripts
        self.store.load_error = ""
        current = self.controller.ui.level_liste.currentItem()
        if current is not None:
            self.controller.level_wechsel(current)
        self.startup_error = ""
        self.health.levels = self.controller.levels
        self.health.startup_error = ""
        self.health.refresh()
        self.save_status.setText("Änderungen gespeichert.")
