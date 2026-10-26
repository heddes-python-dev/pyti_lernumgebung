"""Ausführung der Python-Lernskripte und Bereitstellung der Pyti-Befehle."""

import sys
import threading
import time

from .robot import PytiWandKollisionError
from .script_errors import format_script_error

MAX_AUSFUEHRUNGSZEIT = 30
AKTIONS_VERZOEGERUNG = 0.2


class SkriptZeitlimitError(TimeoutError):
    """Das Skript hat das erlaubte Zeitlimit überschritten."""


class SkriptAbbruchError(Exception):
    """Das Skript wurde durch die Stopp-Funktion abgebrochen."""


class BefehlsInterpreter:
    def __init__(
        self, roboter, spielfeld_manager,
        max_execution_time=MAX_AUSFUEHRUNGSZEIT,
        action_delay_ms=AKTIONS_VERZOEGERUNG * 1000,
    ):
        self.roboter = roboter
        self.spielfeld_manager = spielfeld_manager
        self.max_execution_time = max_execution_time
        self.action_delay_ms = action_delay_ms
        self.last_execution_error = ""

    def aktion_ausfuehren(self, befehl):
        welt = self.spielfeld_manager
        robot = self.roboter
        if befehl == "moveForward":
            if not welt.ist_weg_frei(robot):
                raise PytiWandKollisionError(
                    "Autsch! Pyti ist gegen eine Wand oder den Rand gelaufen."
                )
            robot.vor()
        elif befehl == "jump":
            if not welt.ist_sprung_frei(robot):
                raise PytiWandKollisionError(
                    "Pyti kann nur über eine Wand auf ein freies Landefeld springen."
                )
            robot.springen()
        elif befehl == "turnLeft":
            robot.links_drehen()
        elif befehl == "turnRight":
            robot.rechts_drehen()
        elif befehl == "turnAround":
            robot.rechts_drehen()
            robot.rechts_drehen()
        elif befehl == "pickBeeper":
            robot.pick_beeper(welt)
        elif befehl == "dropBeeper":
            robot.drop_beeper(welt)
        elif befehl == "onBeeper":
            return welt.hat_beeper(robot.x, robot.y)
        elif befehl == "beeperAhead":
            return welt.beeper_voraus_pruefen(robot)
        elif befehl in ("frontClear", "leftClear", "rightClear"):
            richtung = {
                "frontClear": "vorne",
                "leftClear": "links",
                "rightClear": "rechts",
            }[befehl]
            return welt.ist_weg_frei(robot, richtung)
        elif befehl == "anyBeeperInBag":
            return robot.beeper_im_inventar > 0
        else:
            raise ValueError(f"Unbekannter Pyti-Befehl: {befehl}")
        welt.pyti_zeichnen(robot)

    def interpretiere_und_fuehre_aus(
        self, skript_text, *, ausfuehren=None, abbruch_event=None
    ):
        abbruch_event = abbruch_event or threading.Event()
        names = (
            "moveForward", "turnLeft", "turnRight", "turnAround",
            "pickBeeper", "dropBeeper", "jump", "onBeeper", "beeperAhead",
            "frontClear", "leftClear", "rightClear", "anyBeeperInBag",
        )
        actions = set(names[:7])

        def aufrufen(name):
            if abbruch_event.is_set():
                raise SkriptAbbruchError("Skriptausführung wurde abgebrochen.")
            result = ausfuehren(name) if ausfuehren else self.aktion_ausfuehren(name)
            delay = self.action_delay_ms / 1000
            if ausfuehren and name in actions and abbruch_event.wait(delay):
                raise SkriptAbbruchError("Skriptausführung wurde abgebrochen.")
            return result

        namespace = {
            name: (lambda name=name: aufrufen(name))
            for name in names
        }
        return self._skript_ausfuehren(skript_text, namespace, abbruch_event)

    def _skript_ausfuehren(self, text, namespace, abbruch_event):
        print("--- Starte Skript-Ausführung ---")
        deadline = time.monotonic() + self.max_execution_time
        try:
            namespace["__builtins__"] = __builtins__
            code = compile(text, "<pyti-script>", "exec")

            def pruefe(frame, event, _arg):
                if frame.f_code.co_filename != "<pyti-script>":
                    return None
                if abbruch_event.is_set():
                    raise SkriptAbbruchError("Skriptausführung wurde abgebrochen.")
                if event == "line" and time.monotonic() >= deadline:
                    raise SkriptZeitlimitError(
                        f"Das Skript wurde nach "
                        f"{self.max_execution_time} Sekunden abgebrochen."
                    )
                return pruefe

            vorheriger_trace = sys.gettrace()
            try:
                sys.settrace(pruefe)
                exec(code, namespace, namespace)
            finally:
                sys.settrace(vorheriger_trace)
            print("--- Skript erfolgreich beendet ---")
            return True
        except SkriptAbbruchError as error:
            print(f"\n[ABGEBROCHEN]: {error}")
        except PytiWandKollisionError as error:
            self.last_execution_error = format_script_error(error)
            print(f"\n[FEHLER-STOPP]: {error}")
        except SkriptZeitlimitError as error:
            self.last_execution_error = format_script_error(error)
            print(f"\n[ZEITLIMIT-STOPP]: {error}")
        except (Exception, KeyboardInterrupt, SystemExit) as error:
            self.last_execution_error = format_script_error(error)
            print(f"\n[SYNTAX- ODER LAUFZEIT-FEHLER im Skript]: {error}")
        return False
