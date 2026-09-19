import time
from PySide6.QtCore import QEventLoop, QTimer
from pyti import PytiWandKollisionError

class BefehlsInterpreter:
    """Führt den Code aus dem CodeEditor als echtes Python-Skript aus."""
    
    def __init__(self, roboter, spielfeld_manager):
        self.roboter = roboter
        self.spielfeld_manager = spielfeld_manager

    def _warte_flüssig(self, sekunden=0.2):
        """Wartet kurz, hält aber den Qt-Eventloop am Laufen."""
        loop = QEventLoop()
        QTimer.singleShot(int(sekunden * 1000), loop.quit)
        loop.exec()

    def interpretiere_und_fuehre_aus(self, skript_text):
        
        # --- Roboter-Aktionen ---
        def moveForward():
            # Zuerst prüfen, ob der Weg nach vorne frei ist (Rand & Wände)
            if self.spielfeld_manager.ist_weg_frei(self.roboter, richtung="vorne"):
                self.roboter.vor()
                self.spielfeld_manager.pyti_zeichnen(self.roboter)
                self._warte_flüssig(0.2)
            else:
                # Kollision! Wir werfen den Fehler, der unten abgefangen wird
                raise PytiWandKollisionError("Autsch! Pyti ist gegen eine Wand oder den Rand gelaufen.")
            
        def turnLeft():
            self.roboter.links_drehen()
            self.spielfeld_manager.pyti_zeichnen(self.roboter)
            self._warte_flüssig(0.2)

        def turnRight():
            self.roboter.rechts_drehen()
            self.spielfeld_manager.pyti_zeichnen(self.roboter)
            self._warte_flüssig(0.2)

        def turnAround():
            self.roboter.rechts_drehen()
            self.roboter.rechts_drehen()
            self.spielfeld_manager.pyti_zeichnen(self.roboter)
            self._warte_flüssig(0.2)

        def pickBeeper():
            self.roboter.pick_beeper(self.spielfeld_manager)
            self.spielfeld_manager.pyti_zeichnen(self.roboter)
            self._warte_flüssig(0.2)

        def dropBeeper():
            self.roboter.drop_beeper(self.spielfeld_manager)
            self.spielfeld_manager.pyti_zeichnen(self.roboter)
            self._warte_flüssig(0.2)

        # --- Sensor-Abfragen (Geben True/False zurück) ---
        def onBeeper():
            return self.spielfeld_manager.hat_beeper(self.roboter.x, self.roboter.y)

        def beeperAhead():
            # Prüft, ob auf dem Feld vor Pyti ein Beeper liegt
            return self.spielfeld_manager.beeper_voraus_pruefen(self.roboter)

        def frontClear():
            # Prüft, ob der Weg nach vorne frei ist (keine Wand/kein Rand)
            return self.spielfeld_manager.ist_weg_frei(self.roboter, richtung="vorne")

        def leftClear():
            return self.spielfeld_manager.ist_weg_frei(self.roboter, richtung="links")

        def rightClear():
            return self.spielfeld_manager.ist_weg_frei(self.roboter, richtung="rechts")

        # Bonus-Befehl: Prüft, ob Pyti Beeper im Gepäck hat
        def anyBeeperInBag():
            return self.roboter.beeper_im_inventar > 0

        # Die Skript-Umgebung mit allen Befehlen
        skript_umgebung = {
            'moveForward': moveForward,
            'turnLeft': turnLeft,
            'turnRight': turnRight,
            'turnAround': turnAround,
            'pickBeeper': pickBeeper,
            'dropBeeper': dropBeeper,
            'onBeeper': onBeeper,
            'beeperAhead': beeperAhead,
            'frontClear': frontClear,
            'leftClear': leftClear,
            'rightClear': rightClear,
            'anyBeeperInBag': anyBeeperInBag
        }

        print("--- Starte Skript-Ausführung ---")
        try:
            skript_umgebung["__builtins__"] = __builtins__
            exec(skript_text, skript_umgebung, skript_umgebung)
            print("--- Skript erfolgreich beendet ---")
            return True
            
        except PytiWandKollisionError as e:
            print(f"\n[FEHLER-STOPP]: {e}")
        except Exception as e:
            print(f"\n[SYNTAX- ODER LAUFZEIT-FEHLER im Skript]: {e}")

        return False