"""Verbindet Levelauswahl, Benutzeroberfläche und Skriptausführung."""

from PySide6.QtCore import QEvent, QObject, Qt, Slot

from .script_worker import SkriptAusfuehrer


class SkriptUIHandler(QObject):
    def __init__(self, window, beenden, thread_beendet, abbrechen, laeuft):
        super().__init__(window)
        self._beenden = beenden
        self._thread_beendet = thread_beendet
        self._abbrechen = abbrechen
        self._laeuft = laeuft
        self._schluss_ausstehend = False
        window.installEventFilter(self)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Close and self._laeuft():
            self._schluss_ausstehend = True
            self._abbrechen()
            event.ignore()
            return True
        return super().eventFilter(watched, event)

    @Slot(bool, bool)
    def skript_beendet(self, erfolgreich, abgebrochen):
        self._beenden(erfolgreich, abgebrochen)

    @Slot()
    def thread_beendet(self):
        parent = self.parent()
        if parent is not None:
            parent.removeEventFilter(self)
        self._thread_beendet()
        if self._schluss_ausstehend and parent is not None:
            parent.close()


class PytiController:
    def __init__(self, widgets, levels, robot, field, interpreter, bridge):
        self.ui = widgets
        self.levels = levels
        self.robot = robot
        self.field = field
        self.interpreter = interpreter
        self.bridge = bridge
        self.active = False
        self.worker = None
        self.ui_handler = None
        self.controls = [
            widgets.level_liste,
            widgets.reset_button,
            widgets.editor,
            widgets.spielfeld_view,
            widgets.beispiele_button,
            widgets.admin_button,
        ]
        if widgets.start_button is not None:
            self.controls.append(widgets.start_button)
        widgets.level_liste.currentItemChanged.connect(self.level_wechsel)
        if widgets.start_button is not None:
            widgets.start_button.clicked.connect(self.start)
        widgets.reset_button.clicked.connect(self.reset_level)
        widgets.stop_button.clicked.connect(self.stop)
        widgets.level_liste.setCurrentRow(0)

    def reset_level(self):
        if self.active:
            return
        self.level_wechsel(self.ui.level_liste.currentItem())
        self.ui.status.setText("Level neu gestartet.")

    def level_wechsel(self, item, _previous=None):
        if item is None:
            return
        name = item.text()
        data = self.levels[name]
        self.field.lade_level(data, self.robot)
        self.ui.mission.setText(
            f"<b>Mission ({name}):</b><br>{data.get('description', '')}"
        )
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
            self.ui.editor.clear()
            current = self.ui.level_liste.currentItem()
            data = self.levels[current.text()] if current else None
            if data and self.field.ziel_erreicht(self.robot, data.get("goal")):
                self.ui.mission.setText(
                    self.ui.mission.text() + "<br><b>Geschafft! Ziel erreicht.</b>"
                )
            self.ui.status.setText("Skript erfolgreich beendet.")
        elif cancelled:
            self.ui.status.setText("Skriptausführung abgebrochen.")
        else:
            self.ui.status.setText("Skript beendet. Details stehen in der Konsole.")
        self.active = False
        self.ui.stop_button.setEnabled(False)
        for widget, enabled in self.previous_enabled:
            widget.setEnabled(enabled)

    def _on_thread_finished(self):
        self.worker = None
        self.ui_handler = None
