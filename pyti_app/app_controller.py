"""Verbindet Levelauswahl, Benutzeroberfläche und Skriptausführung."""

from PySide6.QtCore import Qt
from .learning_path_actions import LearningPathActions
from .script_ui_handler import SkriptUIHandler
from .script_worker import SkriptAusfuehrer


class PytiController(LearningPathActions):
    def __init__(
        self, widgets, levels, robot, field, interpreter, bridge,
        progress_store=None, completed_levels=(), active_level="",
    ):
        self.ui = widgets
        self.levels = levels
        self.robot = robot
        self.field = field
        self.interpreter = interpreter
        self.bridge = bridge
        self.progress_store = progress_store
        self.completed_levels = set(completed_levels)
        self.hint_text = ""
        self.next_level_name = ""
        self.active = False
        self.worker = None
        self.ui_handler = None
        self.controls = [
            widgets.level_liste, widgets.reset_button, widgets.editor,
            widgets.spielfeld_view, widgets.examples_action,
            widgets.admin_action, widgets.creator_action,
            widgets.first_mission_action, widgets.about_action,
            widgets.speed_slider, widgets.hint_button,
            widgets.next_level_button,
        ]
        if widgets.start_button is not None:
            self.controls.append(widgets.start_button)
        widgets.level_liste.currentItemChanged.connect(self.level_wechsel)
        if widgets.start_button is not None:
            widgets.start_button.clicked.connect(self.start)
        widgets.reset_button.clicked.connect(self.reset_level)
        widgets.stop_button.clicked.connect(self.stop)
        widgets.speed_slider.setValue(interpreter.action_delay_ms)
        widgets.speed_slider.valueChanged.connect(self._set_speed)
        widgets.hint_button.clicked.connect(self.show_hint)
        widgets.next_level_button.clicked.connect(self.next_level)
        self._set_speed(widgets.speed_slider.value())
        widgets.level_liste.setCurrentRow(0)
        if active_level in levels:
            item = widgets.level_liste.findItems(active_level, Qt.MatchExactly)
            if item:
                widgets.level_liste.setCurrentItem(item[0])

    def reset_level(self):
        if self.active:
            return
        self.level_wechsel(self.ui.level_liste.currentItem())
        self.ui.status.setText("Level neu gestartet.")

    def level_wechsel(self, item, _previous=None):
        if item is None:
            return
        name = item.text()
        self.field.lade_level(self.levels[name], self.robot)
        self._show_level(name)
        self._update_next_level()
        self._save_progress(name)
        print(f"Level geladen: {name}")

    def start(self):
        if self.active:
            return
        self.active = True
        self.previous_enabled = [(w, w.isEnabled()) for w in self.controls]
        for widget, _enabled in self.previous_enabled:
            widget.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.ui.status.setText("Skript läuft …")
        self.ui.status.setToolTip("")
        self.worker = SkriptAusfuehrer(
            self.ui.editor.toPlainText(), self.interpreter, self.bridge
        )
        self.ui_handler = SkriptUIHandler(
            self.ui.window,
            self._on_script_finished,
            self._on_thread_finished,
            self.stop,
            lambda: self.worker is not None and self.worker.isRunning(),
        )
        self.worker.beendet.connect(
            self.ui_handler.skript_beendet, Qt.QueuedConnection
        )
        self.worker.finished.connect(
            self.ui_handler.thread_beendet, Qt.QueuedConnection
        )
        self.worker.start()

    def stop(self):
        if self.worker is not None and self.active:
            self.ui.stop_button.setEnabled(False)
            self.ui.status.setText("Abbruch wird ausgeführt …")
            self.worker.abbrechen()

    def _on_script_finished(self, success, cancelled):
        if success:
            current = self.ui.level_liste.currentItem()
            data = self.levels[current.text()] if current else None
            if data and self.field.ziel_erreicht(self.robot, data.get("goal")):
                level_name = current.text() if current else ""
                self.completed_levels.add(level_name)
                self._show_level(level_name)
                self.ui.mission.setText(
                    self.ui.mission.text() + "<br><b>Geschafft! Ziel erreicht.</b>"
                )
                self._update_next_level()
                self.ui.status.setText(
                    "Skript erfolgreich beendet. Ziel erreicht!"
                )
                self._save_progress(level_name)
            else:
                self.ui.status.setText(
                    "Skript ausgeführt. Ziel noch nicht erreicht. "
                    "Code bleibt im Editor."
                )
        elif cancelled:
            self.ui.status.setText("Skriptausführung abgebrochen.")
            self.ui.status.setToolTip("")
        else:
            error = self.interpreter.last_execution_error
            self.ui.status.setText(error or "Skript wurde mit einem Fehler beendet.")
            self.ui.status.setToolTip(error)
        self.active = False
        self.ui.stop_button.setEnabled(False)
        for widget, enabled in self.previous_enabled:
            widget.setEnabled(enabled)
        self._update_next_level()

    def _on_thread_finished(self):
        self.worker = None
        self.ui_handler = None
