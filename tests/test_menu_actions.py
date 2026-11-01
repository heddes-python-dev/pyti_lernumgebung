import os
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication

from pyti_app.app_controller import PytiController
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class MenueAktionenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_allgemeine_menueaktionen_bleiben_gesperrt_und_kehren_zurueck(self):
        widgets = baue_ui(Path(__file__).resolve().parents[1], LEVELS.keys())
        robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(robot, field)
        controller = PytiController(
            widgets, dict(LEVELS), robot, field, interpreter,
            SkriptBruecke(interpreter),
        )
        actions = [
            action
            for menu in widgets.menus
            for action in menu.actions()
            if not action.isSeparator()
        ]
        self.assertEqual(
            [action.text() for action in actions],
            [
                "Beispiele",
                "Administration",
                "Eigenes Level erstellen",
                "Über Pyti",
            ],
        )
        widgets.admin_action.setEnabled(False)
        widgets.about_action.setEnabled(True)
        previous = [action.isEnabled() for action in actions]
        self.assertEqual(previous, [True, False, True, True])
        widgets.editor.setPlainText("while True:\n    pass\n")
        controller.start()
        try:
            self._warte(lambda: controller.worker is not None and controller.worker.isRunning())
            self.assertTrue(controller.active)
            self.assertTrue(all(not action.isEnabled() for action in actions))

            controller.stop()
            self._warte(lambda: not controller.active and controller.worker is None)

            self.assertEqual(
                [action.isEnabled() for action in actions],
                previous,
            )
        finally:
            worker = controller.worker
            if worker is not None and worker.isRunning():
                controller.stop()
                self._warte(lambda: controller.worker is None)
            widgets.window.close()

    def _warte(self, fertig, timeout_ms=2000):
        if fertig():
            return
        loop = QEventLoop()
        timer = QTimer()
        timer.timeout.connect(lambda: loop.quit() if fertig() else None)
        timer.start(10)
        QTimer.singleShot(timeout_ms, loop.quit)
        loop.exec()
        timer.stop()
        self.assertTrue(fertig(), "Warten auf den Skript-Worker lief in ein Timeout.")


if __name__ == "__main__":
    unittest.main()
