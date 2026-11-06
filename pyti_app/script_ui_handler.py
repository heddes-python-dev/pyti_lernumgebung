"""Marshal script worker completion safely to the Qt UI thread."""

from PySide6.QtCore import QEvent, QObject, Qt, Slot


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
