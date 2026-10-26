import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEventLoop, QThread, QTimer
from PySide6.QtTest import QSignalSpy
from PySide6.QtWidgets import QApplication

from pyti_app.field_manager import SpielfeldManager
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptAusfuehrer, SkriptBruecke


class SkriptWorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.field = SpielfeldManager()
        self.robot = Pyti()
        self.field.lade_level(LEVELS["0.0.1 Der erste Beeper"], self.robot)
        self.interpreter = BefehlsInterpreter(self.robot, self.field)
        self.bridge = SkriptBruecke(self.interpreter)

    def wait_for_worker(self, worker, spy):
        loop = QEventLoop()
        timeout = QTimer()
        timeout.setSingleShot(True)
        timeout.timeout.connect(loop.quit)
        worker.beendet.connect(loop.quit)
        timeout.start(2000)
        worker.start()
        if not spy.count():
            loop.exec()
        timeout.stop()
        self.assertTrue(spy.count(), "Worker lief in ein Timeout.")
        self.assertTrue(worker.wait(2000))

    def test_aktionen_laufen_im_gui_thread(self):
        gui_thread = QThread.currentThread()
        action_threads = []
        original = self.interpreter.aktion_ausfuehren

        def inspect_thread(command):
            action_threads.append(QThread.currentThread())
            return original(command)

        self.interpreter.aktion_ausfuehren = inspect_thread
        worker = SkriptAusfuehrer("turnRight()", self.interpreter, self.bridge)
        spy = QSignalSpy(worker.beendet)
        self.wait_for_worker(worker, spy)
        self.assertTrue(spy.at(0)[0])
        self.assertTrue(action_threads)
        self.assertTrue(all(thread == gui_thread for thread in action_threads))

    def test_gui_timer_kann_endlosschleife_stoppen(self):
        worker = SkriptAusfuehrer(
            "while True:\n    pass", self.interpreter, self.bridge
        )
        spy = QSignalSpy(worker.beendet)
        timer_ran = []
        QTimer.singleShot(50, lambda: (timer_ran.append(True), worker.abbrechen()))
        self.wait_for_worker(worker, spy)
        self.assertTrue(timer_ran)
        self.assertFalse(spy.at(0)[0])
        self.assertTrue(spy.at(0)[1])


if __name__ == "__main__":
    unittest.main()
