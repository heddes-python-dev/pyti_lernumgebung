"""Hintergrundthread und Qt-Signalbrücke für Lernskripte."""

import threading
from dataclasses import dataclass, field

from PySide6.QtCore import QObject, Qt, QThread, Signal, Slot

from .script_sandbox import LinuxScriptSandbox, SandboxError
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
        self.sandbox = LinuxScriptSandbox()
        self.abbruch_event = threading.Event()

    def abbrechen(self):
        self.abbruch_event.set()

    def run(self):
        success = False
        telemetry_active = self._emit_telemetry(
            "session_start", message="Pyti-Skript gestartet"
        )

        def telemetry_event(event_type, **payload):
            nonlocal telemetry_active
            if telemetry_active:
                telemetry_active = self._emit_telemetry(event_type, **payload)

        try:
            self.interpreter.last_execution_error = ""
            success, error = self.sandbox.execute(
                self.skript_text,
                self._aktion_ausfuehren,
                self.interpreter.max_execution_time,
                self.abbruch_event,
                telemetry_event if telemetry_active else None,
            )
            self.interpreter.last_execution_error = error
        except InterruptedError:
            success = False
        except (SandboxError, TimeoutError) as error:
            self.interpreter.last_execution_error = str(error)
            self._emit_telemetry(
                "error", message=str(error), traceback=str(error)
            )
            success = False
        except Exception as error:
            print(f"\n[FEHLER BEI DER SKRIPTAUSFÜHRUNG]: {error}")
            self.interpreter.last_execution_error = str(error)
            self._emit_telemetry(
                "error", message=str(error), traceback=str(error)
            )
            success = False
        if success:
            message = "Skript erfolgreich beendet"
        elif self.abbruch_event.is_set():
            message = "Skript abgebrochen"
        else:
            message = "Skript beendet"
        self._emit_telemetry("session_end", message=message)
        self.beendet.emit(success, self.abbruch_event.is_set())

    def _emit_telemetry(self, event_type, **payload):
        handler = getattr(self.interpreter, "telemetry_handler", None)
        if handler is None:
            return False
        try:
            return handler(event_type, **payload) is not False
        except Exception as error:
            print(f"\n[INSPECTOR-TELEMETRIE DEAKTIVIERT]: {error}")
            self.interpreter.telemetry_handler = None
            return False

    def _aktion_ausfuehren(self, name):
        result = self.bruecke.aufrufen(name, self.abbruch_event)
        if name in (
            "moveForward", "turnLeft", "turnRight", "turnAround",
            "pickBeeper", "dropBeeper", "jump",
        ) and self.abbruch_event.wait(self.interpreter.action_delay_ms / 1000):
            raise InterruptedError("Skriptausfuehrung abgebrochen.")
        return result
