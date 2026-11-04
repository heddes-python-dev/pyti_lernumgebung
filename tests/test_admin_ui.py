import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.admin_checks import _check_sandbox, pruefe_system
from pyti_app.admin_panel import AdminPanel
from pyti_app.admin_store import AdminStore
from pyti_app.app_controller import PytiController
from pyti_app.custom_levels import EigeneLevelSpeicher
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_creator_data import LevelEntwurfSpeicher
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui
from sandbox_test_support import sandbox_unavailable_reason


class AdminUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_sandbox_check_reports_unsupported_os_as_information(self):
        with patch("pyti_app.admin_checks.sys.platform", "win32"):
            self.assertEqual(
                _check_sandbox(),
                (
                    "HINWEIS",
                    "Skriptsandbox",
                    "Skriptausführung wird auf diesem Betriebssystem "
                    "nicht unterstützt.",
                ),
            )

    def test_central_admin_tabs_save_and_restore_settings(self):
        widgets = baue_ui(Path.cwd(), LEVELS.keys())
        robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(robot, field)
        controller = PytiController(
            widgets, dict(LEVELS), robot, field, interpreter,
            SkriptBruecke(interpreter),
        )
        try:
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                store = AdminStore(root / "admin.json")
                custom_store = EigeneLevelSpeicher(root / "custom.json")
                draft_store = LevelEntwurfSpeicher(root / "drafts.json")
                settings, levels, scripts = store.load(controller.levels)
                controller.levels.update(levels)
                panel = AdminPanel(
                    store, controller, settings, scripts, "1.2.0",
                    custom_level_store=custom_store,
                    draft_store=draft_store,
                    open_creator=lambda: None,
                )
                self.assertEqual(
                    [panel.tabs.tabText(i) for i in range(panel.tabs.count())],
                    [
                        "Systemstatus", "Einstellungen", "Level bearbeiten",
                        "Beispielskripte", "Verwaltung",
                    ],
                )
                self.assertEqual(panel.windowTitle(), "Pyti – Admin-Bereich")
                self.assertTrue(panel.tools.creator_button.isEnabled())
                self.assertTrue(panel.tools.export_button.isEnabled())
                self.assertTrue(panel.tools.restore_button.isEnabled())
                panel.settings.timeout.setValue(12)
                panel.settings.delay.setValue(50)
                self.assertTrue(panel.save())
                self.assertEqual(interpreter.max_execution_time, 12)
                self.assertEqual(interpreter.action_delay_ms, 50)
                reopened = AdminPanel(
                    store, controller, controller.admin_settings,
                    controller.admin_scripts, "1.2.0",
                    custom_level_store=custom_store, draft_store=draft_store,
                )
                self.assertEqual(reopened.settings.timeout.value(), 12)
                statuses = pruefe_system(
                    controller.levels, widgets, interpreter
                )
                status_by_name = {
                    name: status for status, name, _ in statuses
                }
                if sys.platform.startswith("linux"):
                    expected_sandbox_status = (
                        "FEHLER" if sandbox_unavailable_reason() else "OK"
                    )
                else:
                    expected_sandbox_status = "HINWEIS"
                self.assertEqual(
                    status_by_name["Skriptsandbox"], expected_sandbox_status
                )
                self.assertTrue(
                    all(
                        status in ("OK", "HINWEIS")
                        for status, name, _ in statuses
                        if name != "Skriptsandbox"
                    ),
                    repr(statuses),
                )
                reopened.close()
                panel.close()
        finally:
            widgets.window.close()


if __name__ == "__main__":
    unittest.main()
