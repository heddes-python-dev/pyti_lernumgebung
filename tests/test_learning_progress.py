import os
import tempfile
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from pyti_app.app_controller import PytiController
from pyti_app.field_manager import SpielfeldManager
from pyti_app.level_generator import GRID_SIZE
from pyti_app.levels import LEVELS
from pyti_app.progress_store import ProgressStore
from pyti_app.robot import Pyti
from pyti_app.script_runtime import BefehlsInterpreter
from pyti_app.script_worker import SkriptBruecke
from pyti_app.ui_builder import baue_ui


class LearningProgressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_completion_next_level_speed_and_restore(self):
        with tempfile.TemporaryDirectory() as directory:
            store = ProgressStore(Path(directory) / "progress.json")
            completed, active = store.load()
            widgets, controller, robot, field, interpreter = self._controller(
                store, completed, active
            )
            try:
                widgets.level_liste.setCurrentRow(1)
                self.assertIn("Lernziel:", widgets.mission.text())
                self.assertIn("Reflexionsfrage:", widgets.mission.text())
                widgets.hint_button.click()
                self.assertTrue(widgets.status.text().startswith("Tipp:"))
                widgets.speed_slider.setValue(1250)
                self.assertEqual(interpreter.action_delay_ms, 1250)
                self.assertIn("1250 ms", widgets.speed_label.text())
                self.assertFalse(widgets.next_level_button.isEnabled())

                level_name = widgets.level_liste.currentItem().text()
                goal = tuple(controller.levels[level_name]["goal"]["position"])
                robot.x, robot.y = goal
                robot.ziel_beeper_im_inventar = 1
                field.beeper_koordinaten.discard(goal)
                controller.active = True
                controller.previous_enabled = [
                    (widget, widget.isEnabled()) for widget in controller.controls
                ]
                controller._on_script_finished(True, False)

                self.assertIn(level_name, controller.completed_levels)
                self.assertTrue(widgets.next_level_button.isEnabled())
                self.assertEqual(store.load()[0], {level_name})
                widgets.next_level_button.click()
                self.assertEqual(widgets.level_liste.currentRow(), 2)
                self.assertEqual(store.load()[1], widgets.level_liste.currentItem().text())

                saved, last_level = store.load()
                widgets.window.close()
                restored = self._controller(store, saved, last_level)
                try:
                    self.assertEqual(restored[0].level_liste.currentRow(), 2)
                    self.assertIn(level_name, restored[1].completed_levels)
                finally:
                    restored[0].window.close()
            finally:
                widgets.window.close()

    def _controller(self, store, completed, active):
        widgets = baue_ui(Path(__file__).resolve().parents[1], LEVELS.keys())
        robot = Pyti(grid_size=GRID_SIZE)
        field = SpielfeldManager(grid_size=GRID_SIZE)
        interpreter = BefehlsInterpreter(robot, field, action_delay_ms=200)
        controller = PytiController(
            widgets, dict(LEVELS), robot, field, interpreter,
            SkriptBruecke(interpreter), store, completed, active,
        )
        return widgets, controller, robot, field, interpreter


if __name__ == "__main__":
    unittest.main()
