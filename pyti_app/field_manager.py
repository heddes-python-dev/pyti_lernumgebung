"""Weltzustand, Sensoren und Levelziele."""

from .field_rendering import SpielfeldDarstellung


class SpielfeldManager:
    def __init__(self, grid_size=15):
        self.grid_size = grid_size
        self.darstellung = SpielfeldDarstellung(grid_size)
        self.scene = self.darstellung.scene
        self.beeper_koordinaten = set()
        self.wand_koordinaten = set()
        self.ziel_position = None
        self.pyti_position = None

    def lade_level(self, level_daten, pyti):
        self.beeper_koordinaten.clear()
        self.wand_koordinaten.clear()
        ziel = level_daten.get("goal", {})
        self.ziel_position = tuple(ziel.get("position", ())) if ziel else None
        self.darstellung.zeichne_raster(self.ziel_position)
        pyti.x = level_daten.get("start_x", 0)
        pyti.y = level_daten.get("start_y", 0)
        pyti.richtung = level_daten.get("start_richtung", 1)
        pyti.beeper_im_inventar = 0
        pyti.ziel_beeper_im_inventar = 0
        pyti.normale_beeper_im_inventar = 0
        self.wand_koordinaten.update(map(tuple, level_daten.get("waende", [])))
        self.beeper_koordinaten.update(map(tuple, level_daten.get("beeper", [])))
        self.darstellung.zeichne_waende(self.wand_koordinaten)
        self.darstellung.zeichne_beeper(self.beeper_koordinaten)
        self.pyti_zeichnen(pyti)

    def pyti_zeichnen(self, pyti):
        self.pyti_position = (pyti.x, pyti.y)
        self.darstellung.zeichne_pyti(pyti)
        self.darstellung.zeichne_beeper(self.beeper_koordinaten)

    def toggle_wand(self, x, y):
        position = (x, y)
        if position in self.wand_koordinaten:
            self.wand_koordinaten.remove(position)
        elif (
            0 <= x < self.grid_size
            and 0 <= y < self.grid_size
            and position != self.pyti_position
            and position != self.ziel_position
            and position not in self.beeper_koordinaten
        ):
            self.wand_koordinaten.add(position)
        else:
            return False
        self.darstellung.zeichne_waende(self.wand_koordinaten)
        return True

    def toggle_beeper(self, x, y):
        if (
            (x, y) in self.wand_koordinaten
            and (x, y) not in self.beeper_koordinaten
        ):
            return False
        if (x, y) in self.beeper_koordinaten:
            self.beeper_koordinaten.remove((x, y))
            print(f"Beeper entfernt bei X={x}, Y={y}")
        else:
            self.beeper_koordinaten.add((x, y))
            print(f"Beeper platziert bei X={x}, Y={y}")
        self.darstellung.zeichne_beeper(self.beeper_koordinaten)
        return True

    def hat_beeper(self, x, y):
        return (x, y) in self.beeper_koordinaten

    def lege_beeper(self, x, y):
        self.beeper_koordinaten.add((x, y))
        self.darstellung.zeichne_beeper(self.beeper_koordinaten)

    def entferne_beeper(self, x, y):
        if (x, y) in self.beeper_koordinaten:
            self.beeper_koordinaten.remove((x, y))
            self.darstellung.zeichne_beeper(self.beeper_koordinaten)

    def sammle_beeper(self, x, y):
        if (x, y) not in self.beeper_koordinaten:
            return False
        self.beeper_koordinaten.remove((x, y))
        self.darstellung.zeichne_beeper(self.beeper_koordinaten)
        return True

    def ziel_erreicht(self, roboter, ziel):
        if not ziel or ziel.get("type") != "collect_beeper":
            return False
        position = tuple(ziel.get("position", ()))
        return (
            (roboter.x, roboter.y) == position
            and roboter.ziel_beeper_im_inventar > 0
            and not self.hat_beeper(*position)
        )

    def ist_weg_frei(self, roboter, richtung="vorne"):
        index = roboter.richtung + {
            "vorne": 0, "rechts": 1, "hinten": 2, "links": -1
        }.get(richtung, 0)
        dx, dy = ((0, -1), (1, 0), (0, 1), (-1, 0))[index % 4]
        ziel = roboter.x + dx, roboter.y + dy
        return (
            0 <= ziel[0] < self.grid_size
            and 0 <= ziel[1] < self.grid_size
            and ziel not in self.wand_koordinaten
        )

    def beeper_voraus_pruefen(self, roboter):
        if not self.ist_weg_frei(roboter):
            return False
        dx, dy = ((0, -1), (1, 0), (0, 1), (-1, 0))[roboter.richtung]
        return self.hat_beeper(roboter.x + dx, roboter.y + dy)
