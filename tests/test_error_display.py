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


class FehleranzeigeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_syntax_und_laufzeitfehler_enthalten_skriptzeile(self):
        interpreter = BefehlsInterpreter(Pyti(), SpielfeldManager())
        self.assertFalse(interpreter.interpretiere_und_fuehre_aus(
            "wert = 1\nif True print(wert)"
        ))
        self.assertIn("SyntaxError (Zeile 2):", interpreter.last_execution_error)

        self.assertFalse(interpreter.interpretiere_und_fuehre_aus(
            "wert = 1\nraise ValueError('kaputt')"
        ))
        self.assertEqual(
            interpreter.last_execution_error,
            "ValueError (Zeile 2): kaputt",
        )

    def test_worker_fehler_erscheint_im_hauptfenster(self):
        root = Path(__file__).resolve().parents[1]
        widgets = baue_ui(root, LEVELS.keys())
        robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(robot, field)
        controller = PytiController(
            widgets, dict(LEVELS), robot, field, interpreter,
            SkriptBruecke(interpreter),
        )
        widgets.editor.setPlainText("wert = 1\nif True print(wert)")

        controller.start()
        loop = QEventLoop()
        poll = QTimer()
        poll.timeout.connect(
            lambda: loop.quit()
            if not controller.active and controller.worker is None
            else None
        )
        poll.start(10)
        QTimer.singleShot(3000, loop.quit)
        loop.exec()
        poll.stop()
        try:
            self.assertIsNone(controller.worker)
            self.assertIn("SyntaxError (Zeile 2):", widgets.status.text())
            self.assertEqual(widgets.status.toolTip(), widgets.status.text())
            self.assertTrue(widgets.status.wordWrap())
        finally:
            widgets.window.close()


if __name__ == "__main__":
    unittest.main()
