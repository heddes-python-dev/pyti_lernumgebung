"""Initialisiert Qt und startet die Pyti-Lernumgebung."""

import sys
from pathlib import Path

from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QApplication

from .admin_panel import AdminPanel
from .admin_store import AdminStore
from .app_controller import PytiController
from .field_manager import SpielfeldManager
from .level_generator import GRID_SIZE
from .level_creator_dialog import LevelCreatorDialog
from .custom_levels import EigeneLevelSpeicher
from .level_catalog import register_custom_level
from .levels import LEVELS
from .robot import Pyti
from .script_runtime import BefehlsInterpreter
from .script_worker import SkriptBruecke
from .ui_builder import baue_ui


def hauptprogramm():
    app = QApplication(sys.argv)
    app.setOrganizationName("Pyti")
    app.setApplicationName("Lernumgebung")
    basis_pfad = Path(__file__).resolve().parent.parent
    config_pfad = Path(
        QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)
    ) / "admin.json"
    store = AdminStore(config_pfad)
    custom_store = EigeneLevelSpeicher(config_pfad.parent / "custom_levels.json")
    custom_error = ""
    try:
        custom_levels = custom_store.laden()
    except (OSError, ValueError, TypeError, KeyError) as error:
        custom_levels = {}
        custom_error = f"Eigene Level konnten nicht geladen werden: {error}"
    defaults = {**LEVELS, **custom_levels}
    settings, levels, scripts = store.load(defaults)
    if custom_error:
        store.load_error = "; ".join(filter(None, (store.load_error, custom_error)))
    widgets = baue_ui(basis_pfad, levels.keys())
    robot = Pyti(grid_size=GRID_SIZE)
    field = SpielfeldManager(grid_size=GRID_SIZE)
    interpreter = BefehlsInterpreter(
        robot, field, settings["max_execution_time"], settings["action_delay_ms"]
    )
    bridge = SkriptBruecke(interpreter)
    controller = PytiController(widgets, levels, robot, field, interpreter, bridge)
    controller.admin_settings = settings
    controller.admin_scripts = scripts
    version = (basis_pfad / "VERSION").read_text(encoding="utf-8").strip()
    widgets.admin_button.clicked.connect(
        lambda: AdminPanel(
            store, controller, controller.admin_settings,
            controller.admin_scripts, version, store.load_error
        ).exec()
    )
    draft_path = config_pfad.parent / "level_creator_drafts.json"
    widgets.creator_button.clicked.connect(
        lambda: LevelCreatorDialog(
            draft_path,
            lambda name, level: register_custom_level(
                controller.levels, widgets.level_liste, name, level, custom_store
            ),
            lambda: controller.levels.keys(),
            widgets.window,
        ).exec()
    )
    widgets.spielfeld_view.setScene(field.scene)
    widgets.spielfeld_view.spielfeld_manager = field
    widgets.window.grid_spielfeld = widgets.spielfeld_view
    widgets.window.show()
    sys.exit(app.exec())
