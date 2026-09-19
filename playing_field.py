from PySide6.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsView, QGraphicsRectItem
from PySide6.QtGui import QColor, QPen, QBrush
from PySide6.QtCore import Qt

CELL_SIZE = 40

class SpielfeldView(QGraphicsView):
    """Eine interaktive Grafikansicht, die Mausklicks in Beeper-Aktionen umwandelt."""
    def __init__(self, scene, spielfeld_manager, parent=None):
        super().__init__(scene, parent)
        self.spielfeld_manager = spielfeld_manager

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Klick-Position in Szenen-Koordinaten umrechnen
            pos = self.mapToScene(event.pos())
            x = int(pos.x() // CELL_SIZE)
            y = int(pos.y() // CELL_SIZE)

            # Prüfen, ob der Klick innerhalb des Spielfelds liegt
            if 0 <= x < self.spielfeld_manager.grid_size and 0 <= y < self.spielfeld_manager.grid_size:
                self.spielfeld_manager.toggle_beeper(x, y)
        
        # Standard-Verhalten beibehalten
        super().mousePressEvent(event)

class SpielfeldManager:
    def __init__(self, grid_size=15):
        self.grid_size = grid_size
        self.scene = QGraphicsScene()
        self.avatar_items = []
        self.beeper_items = []
        self.wand_items = []            # <--- NEU: Liste für Wand-Grafiken
        self.beeper_koordinaten = set() # Speichert (x, y) von Beepern
        self.wand_koordinaten = set()   # <--- NEU: Speichert (x, y) von Wänden
        self._raster_zeichnen()

    def _raster_zeichnen(self):
        pen = QPen(QColor("lightgray"))
        for i in range(self.grid_size + 1):
            self.scene.addLine(i * CELL_SIZE, 0, i * CELL_SIZE, self.grid_size * CELL_SIZE, pen)
            self.scene.addLine(0, i * CELL_SIZE, self.grid_size * CELL_SIZE, i * CELL_SIZE, pen)

    def lade_level(self, level_daten, pyti):
        """Lädt ein komplettes Level (Startposition, Wände, Beeper)."""
        self.beeper_koordinaten.clear()
        self.wand_koordinaten.clear()

        # Pyti-Startwerte setzen
        pyti.x = level_daten.get("start_x", 0)
        pyti.y = level_daten.get("start_y", 0)
        pyti.richtung = level_daten.get("start_richtung", 1)
        pyti.beeper_im_inventar = 0

        # Wände & Beeper übernehmen
        for wx, wy in level_daten.get("waende", []):
            self.wand_koordinaten.add((wx, wy))
        for bx, by in level_daten.get("beeper", []):
            self.beeper_koordinaten.add((bx, by))

        # Alles neu zeichnen
        self._waende_zeichnen()
        self._beeper_zeichnen()
        self.pyti_zeichnen(pyti)

    def _waende_zeichnen(self):
        """Zeichnet Wände als graue Blöcke auf das Spielfeld."""
        for item in self.wand_items:
            self.scene.removeItem(item)
        self.wand_items.clear()

        for wx, wy in self.wand_koordinaten:
            wx_pos = wx * CELL_SIZE + 2
            wy_pos = wy * CELL_SIZE + 2
            wand_item = QGraphicsRectItem(wx_pos, wy_pos, CELL_SIZE - 4, CELL_SIZE - 4)
            wand_item.setBrush(QBrush(QColor("dimgray")))
            wand_item.setPen(QPen(QColor("black"), 1))
            self.scene.addItem(wand_item)
            self.wand_items.append(wand_item)

    def pyti_zeichnen(self, pyti):
        # 1. Alten Avatar löschen
        for item in self.avatar_items:
            self.scene.removeItem(item)
        self.avatar_items.clear()

        px = pyti.x * CELL_SIZE + 5
        py = pyti.y * CELL_SIZE + 5
        cx = px + 15
        cy = py + 15

        body = QGraphicsEllipseItem(px, py, 30, 30)
        body.setBrush(QBrush(QColor("dodgerblue")))
        body.setPen(QPen(QColor("darkblue"), 2))
        self.scene.addItem(body)
        self.avatar_items.append(body)

        pen_dir = QPen(QColor("navy"), 4)
        if pyti.richtung == 0:  # NORD
            dir_item = QGraphicsLineItem(cx, cy, cx, py)
        elif pyti.richtung == 1:  # OST
            dir_item = QGraphicsLineItem(cx, cy, px + 30, cy)
        elif pyti.richtung == 2:  # SÜD
            dir_item = QGraphicsLineItem(cx, cy, cx, py + 30)
        elif pyti.richtung == 3:  # WEST
            dir_item = QGraphicsLineItem(cx, cy, px, cy)
        
        dir_item.setPen(pen_dir)
        self.scene.addItem(dir_item)
        self.avatar_items.append(dir_item)

        # 2. Beeper auf dem Spielfeld aktualisieren/zeichnen
        self._beeper_zeichnen()

    def _beeper_zeichnen(self):
        for item in self.beeper_items:
            self.scene.removeItem(item)
        self.beeper_items.clear()

        for bx, by in self.beeper_koordinaten:
            bx_pos = bx * CELL_SIZE + 12
            by_pos = by * CELL_SIZE + 12
            beeper_item = QGraphicsEllipseItem(bx_pos, by_pos, 16, 16)
            beeper_item.setBrush(QBrush(QColor("gold")))
            beeper_item.setPen(QPen(QColor("darkorange"), 1))
            self.scene.addItem(beeper_item)
            self.beeper_items.append(beeper_item)

    def toggle_beeper(self, x, y):
        """Platziert einen Beeper, falls keiner da ist, oder entfernt ihn."""
        if (x, y) in self.beeper_koordinaten:
            self.beeper_koordinaten.remove((x, y))
            print(f"Beeper entfernt bei X={x}, Y={y}")
        else:
            self.beeper_koordinaten.add((x, y))
            print(f"Beeper platziert bei X={x}, Y={y}")
        
        self._beeper_zeichnen()    

    # --- Sensor- und Welt-Methoden für den Interpreter ---

    def hat_beeper(self, x, y):
        """Prüft, ob auf dem Feld (x, y) ein Beeper liegt."""
        return (x, y) in self.beeper_koordinaten

    def lege_beeper(self, x, y):
        """Platziert einen Beeper auf dem Feld."""
        self.beeper_koordinaten.add((x, y))
        self._beeper_zeichnen()

    def entferne_beeper(self, x, y):
        """Entfernt einen Beeper vom Feld."""
        if (x, y) in self.beeper_koordinaten:
            self.beeper_koordinaten.remove((x, y))
            self._beeper_zeichnen()

    def ziel_erreicht(self, roboter, ziel):
        """Prüft, ob der Roboter das definierte Levelziel erfüllt hat."""
        if not ziel or ziel.get("type") != "collect_beeper":
            return False

        ziel_position = tuple(ziel.get("position", ()))
        return (
            (roboter.x, roboter.y) == ziel_position
            and roboter.beeper_im_inventar > 0
            and not self.hat_beeper(*ziel_position)
        )

    def ist_weg_frei(self, roboter, richtung="vorne"):
        """Prüft, ob in die gewünschte Richtung der Weg frei ist (Rand + Wände)."""
        aktuelle_richtung = roboter.richtung
        ziel_richtung = aktuelle_richtung

        if richtung == "links":
            ziel_richtung = (aktuelle_richtung - 1) % 4
        elif richtung == "rechts":
            ziel_richtung = (aktuelle_richtung + 1) % 4
        elif richtung == "hinten":
            ziel_richtung = (aktuelle_richtung + 2) % 4

        test_x, test_y = roboter.x, roboter.y
        if ziel_richtung == 0:  # NORD
            test_y -= 1
        elif ziel_richtung == 1:  # OST
            test_x += 1
        elif ziel_richtung == 2:  # SÜD
            test_y += 1
        elif ziel_richtung == 3:  # WEST
            test_x -= 1

        # 1. Prüfen, ob innerhalb des Grids
        im_grid = 0 <= test_x < self.grid_size and 0 <= test_y < self.grid_size
        if not im_grid:
            return False

        # 2. Prüfen, ob keine Wand im Weg ist <--- NEU
        keine_wand = (test_x, test_y) not in self.wand_koordinaten
        
        return keine_wand

    def beeper_voraus_pruefen(self, roboter):
        """Prüft, ob direkt vor Pyti ein Beeper liegt."""
        test_x, test_y = roboter.x, roboter.y
        if roboter.richtung == 0:
            test_y -= 1
        elif roboter.richtung == 1:
            test_x += 1
        elif roboter.richtung == 2:
            test_y += 1
        elif roboter.richtung == 3:
            test_x -= 1
        return self.hat_beeper(test_x, test_y)