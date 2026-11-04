import os
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import (
    QApplication, QDialog, QLabel, QMessageBox, QPushButton, QTextBrowser,
)

from pyti_app.app_controller import PytiController
from pyti_app.beginner_mission import _lade_code, zeige_erste_mission
from pyti_app.beginner_mission_data import erstelle_erste_mission
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class ErsteMissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.widgets = baue_ui(
            Path(__file__).resolve().parents[1], LEVELS.keys()
        )
        self.robot = Pyti(grid_size=GRID_SIZE)
        self.field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(self.robot, self.field)
        self.controller = PytiController(
            self.widgets, dict(LEVELS), self.robot, self.field, interpreter,
            SkriptBruecke(interpreter),
        )

    def tearDown(self):
        self.widgets.window.close()

    def test_laden_waehlt_erstes_level_und_fuegt_startercode_ein(self):
        dialog = QDialog(self.widgets.window)
        self.widgets.editor.setPlainText("")
        self.robot.x, self.robot.y = 3, 0
        mission = erstelle_erste_mission(LEVELS["0.0.1 Der erste Beeper"])

        _lade_code(dialog, self.widgets, mission.starter_code, "Beispiel geladen.")

        self.assertEqual(self.widgets.level_liste.currentRow(), 0)
        self.assertEqual((self.robot.x, self.robot.y), (0, 0))
        self.assertEqual(self.widgets.editor.toPlainText(), mission.starter_code)
        self.assertIn("Beispiel geladen", self.widgets.status.text())
        self.assertEqual(dialog.result(), QDialog.Accepted)

    def test_vorhandener_code_bleibt_bei_abgelehnter_ersetzung_erhalten(self):
        dialog = QDialog(self.widgets.window)
        self.widgets.editor.setPlainText("turnLeft()")

        with patch(
            "pyti_app.beginner_mission.QMessageBox.question",
            return_value=QMessageBox.No,
        ):
            _lade_code(
                dialog,
                self.widgets,
                erstelle_erste_mission(
                    LEVELS["0.0.1 Der erste Beeper"]
                ).starter_code,
                "Beispiel geladen.",
            )

        self.assertEqual(self.widgets.editor.toPlainText(), "turnLeft()")
        self.assertEqual(dialog.result(), 0)

    def test_loesung_wird_erst_nach_drei_freiwilligen_tipps_angeboten(self):
        self.widgets.editor.setPlainText("")
        mission = erstelle_erste_mission(LEVELS["0.0.1 Der erste Beeper"])
        loesung = mission.loesung_code

        def simuliere_dialog(dialog):
            buttons = {
                button.text(): button
                for button in dialog.findChildren(QPushButton)
            }
            solution = buttons["Lösung laden"]
            hints = buttons["Tipp anzeigen"]
            self.assertFalse(solution.isEnabled())
            hints.click()
            tipps = [label.text() for label in dialog.findChildren(QLabel)]
            self.assertTrue(any("Tipp 1 von 3" in text for text in tipps))
            self.assertTrue(any(
                mission.hinweise[0] in text for text in tipps
            ))
            self.assertFalse(solution.isEnabled())
            hints.click()
            self.assertFalse(solution.isEnabled())
            hints.click()
            self.assertTrue(solution.isEnabled())
            self.assertTrue(any("Lösung laden“ ist jetzt freigeschaltet" in
                                label.text() for label in dialog.findChildren(QLabel)))
            solution.click()

        with patch(
            "pyti_app.beginner_mission.QDialog.exec",
            new=simuliere_dialog,
        ):
            zeige_erste_mission(self.widgets.window, self.widgets, LEVELS)

        self.assertEqual(self.widgets.editor.toPlainText(), loesung)

    def test_mission_nutzt_den_aktiven_nachbar_beeper_override(self):
        levels = dict(LEVELS)
        level = dict(LEVELS["0.0.1 Der erste Beeper"])
        level.update(
            start_x=0,
            start_y=14,
            start_richtung=1,
            beeper=[(1, 14)],
            waende=[],
            goal={"type": "collect_beeper", "position": (1, 14)},
        )
        levels["0.0.1 Der erste Beeper"] = level
        self.widgets.editor.setPlainText("")

        def simuliere_dialog(dialog):
            browser = dialog.findChild(QTextBrowser)
            self.assertIn("1 Bewegungsschritt und 0 Drehungen", browser.toPlainText())
            buttons = {
                button.text(): button
                for button in dialog.findChildren(QPushButton)
            }
            buttons["Vollständiges Beispiel laden"].click()

        with patch(
            "pyti_app.beginner_mission.QDialog.exec",
            new=simuliere_dialog,
        ):
            zeige_erste_mission(self.widgets.window, self.widgets, levels)

        self.assertEqual(
            self.widgets.editor.toPlainText(),
            "moveForward()\npickBeeper()\n",
        )


if __name__ == "__main__":
    unittest.main()
