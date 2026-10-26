import os
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QPushButton, QTextBrowser

from pyti_app.project_info import erstelle_projektinfo_dialog
from pyti_app.ui_builder import baue_ui


class ProjektinfoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_dialog_enthaelt_projektinfos_links_und_sicherheitshinweis(self):
        dialog = erstelle_projektinfo_dialog(None, "1.4.0")
        browser = dialog.findChild(QTextBrowser)
        self.assertIsNotNone(browser)
        content = browser.toHtml()
        for expected in (
            "1.4.0",
            "Thomas Heddes",
            "19. September 2026",
            "MIT",
            "iLollek",
            "keine Sandbox",
            "keine zertifizierte Schulsoftware",
            "CONTRIBUTING.md",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, content)
        self.assertTrue(browser.openExternalLinks())
        dialog.close()

    def test_hauptfenster_bietet_ueber_pyti_knopf(self):
        root = Path(__file__).resolve().parents[1]
        widgets = baue_ui(root, [])
        try:
            self.assertIsInstance(widgets.about_button, QPushButton)
            self.assertEqual(widgets.about_button.text(), "Über Pyti")
            self.assertTrue(widgets.about_button.isVisibleTo(widgets.window))
        finally:
            widgets.window.close()


if __name__ == "__main__":
    unittest.main()
