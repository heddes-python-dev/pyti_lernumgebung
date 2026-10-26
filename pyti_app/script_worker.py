"""Hintergrundthread und Qt-Signalbrücke für Lernskripte."""

import threading
from dataclasses import dataclass, field

from PySide6.QtCore import QObject, Qt, QThread, Signal, Slot

from .script_runtime import BefehlsInterpreter


@dataclass
class _AktionsAnfrage:
    abbruch_event: threading.Event
    erledigt: threading.Event = field(default_factory=threading.Event)
    ergebnis: object = None
    fehler: Exception | None = None


class SkriptBruecke(QObject):
    _aktion_angefordert = Signal(str, object)

    def __init__(self, interpreter):
        super().__init__()
        self.interpreter = interpreter
        self._aktion_angefordert.connect(
            self._aktion_ausfuehren, Qt.QueuedConnection
        )

    def aufrufen(self, befehl, abbruch_event):
        if abbruch_event.is_set():
            return self._abbrechen()
        request = _AktionsAnfrage(abbruch_event)
        self._aktion_angefordert.emit(befehl, request)
        while not request.erledigt.wait(0.05):
            if abbruch_event.is_set():
                return self._abbrechen()
        if abbruch_event.is_set():
            return self._abbrechen()
        if request.fehler:
            raise request.fehler
        return request.ergebnis

    @staticmethod
    def _abbrechen():
        from .script_runtime import SkriptAbbruchError

        raise SkriptAbbruchError("Skriptausführung wurde abgebrochen.")

    @Slot(str, object)
    def _aktion_ausfuehren(self, befehl, request):
        if request.abbruch_event.is_set():
            request.erledigt.set()
            return
        try:
            request.ergebnis = self.interpreter.aktion_ausfuehren(befehl)
        except Exception as error:
            request.fehler = error
        finally:
            request.erledigt.set()


class SkriptAusfuehrer(QThread):
    beendet = Signal(bool, bool)

    def __init__(self, skript_text, interpreter, bruecke, parent=None):
        super().__init__(parent)
        self.skript_text = skript_text
        self.interpreter = interpreter
        self.bruecke = bruecke
        self.abbruch_event = threading.Event()

    def abbrechen(self):
        self.abbruch_event.set()

    def run(self):
        try:
            success = self.interpreter.interpretiere_und_fuehre_aus(
                self.skript_text,
                ausfuehren=lambda name: self.bruecke.aufrufen(
                    name, self.abbruch_event
                ),
                abbruch_event=self.abbruch_event,
            )
        except Exception as error:
            print(f"\n[FEHLER BEI DER SKRIPTAUSFÜHRUNG]: {error}")
            success = False
        self.beendet.emit(success, self.abbruch_event.is_set())
