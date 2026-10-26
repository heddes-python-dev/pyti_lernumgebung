import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtGui import QColor, QImage
from PySide6.QtWidgets import QApplication

from pyti_app.editor import CodeEditor


class CodeEditorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_zeilennummern_werden_pro_editorzeile_aktualisiert(self):
        editor = CodeEditor()
        editor.setPlainText("erste\nzweite\ndritte")
        editor.resize(600, 300)
        editor.show()
        self.app.processEvents()

        area = editor.line_number_area
        image = QImage(area.size(), QImage.Format_ARGB32)
        image.fill(QColor("transparent"))
        area.render(image)
        line_height = editor.fontMetrics().height()
        masks = []
        for line in range(3):
            masks.append(tuple(
                image.pixel(x, y) != QColor("#f0f0f0").rgba()
                for y in range(line * line_height, (line + 1) * line_height)
                for x in range(image.width())
            ))

        self.assertNotEqual(masks[0], masks[1])
        self.assertNotEqual(masks[1], masks[2])
        editor.close()


if __name__ == "__main__":
    unittest.main()
