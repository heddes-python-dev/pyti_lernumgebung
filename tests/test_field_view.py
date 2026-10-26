import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QPointF, Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication

from pyti_app.field_manager import SpielfeldManager
from pyti_app.field_rendering import CELL_SIZE
from pyti_app.field_view import SpielfeldView
from pyti_app.robot import Pyti


class SpielfeldMausTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_rechtsklick_setzt_und_entfernt_wand(self):
        field = SpielfeldManager()
        field.lade_level({"start_x": 5, "start_y": 5}, Pyti())
        view = SpielfeldView(field.scene, field)
        view.resize(600, 600)
        view.show()
        self.app.processEvents()
        point = view.mapFromScene(QPointF(6.5 * CELL_SIZE, 5.5 * CELL_SIZE))

        QTest.mouseClick(view.viewport(), Qt.RightButton, pos=point)
        self.assertIn((6, 5), field.wand_koordinaten)
        QTest.mouseClick(view.viewport(), Qt.RightButton, pos=point)
        self.assertNotIn((6, 5), field.wand_koordinaten)
        view.close()


if __name__ == "__main__":
    unittest.main()
