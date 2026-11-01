import os
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QMenuBar, QPushButton, QTextBrowser

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
            "SansikaDev",
            "Regressionstest für Menüaktionen",
            "keine Sandbox",
            "keine zertifizierte Schulsoftware",
            "CONTRIBUTING.md",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, content)
        self.assertTrue(browser.openExternalLinks())
        dialog.close()

    def test_hauptfenster_bietet_allgemeine_aktionen_in_menues(self):
        root = Path(__file__).resolve().parents[1]
        widgets = baue_ui(root, [])
        try:
            menu_bar = widgets.window.findChild(QMenuBar)
            self.assertIsNotNone(menu_bar)
            self.assertEqual(
                [action.text() for action in menu_bar.actions()],
                ["Werkzeuge", "Hilfe"],
            )
            self.assertEqual(
                [action.text() for action in widgets.menus[0].actions()],
                ["Beispiele", "Administration", "Eigenes Level erstellen"],
            )
            self.assertEqual(
                [action.text() for action in widgets.menus[1].actions()],
                ["Über Pyti"],
            )
            self.assertIs(widgets.about_action, widgets.menus[1].actions()[0])
            self.assertFalse(
                any(
                    button.text() in {
                        "Beispiele", "Administration",
                        "Eigenes Level erstellen", "Über Pyti",
                    }
                    for button in widgets.window.findChildren(QPushButton)
                )
            )
        finally:
            widgets.window.close()


if __name__ == "__main__":
    unittest.main()
