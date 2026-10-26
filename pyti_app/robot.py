"""Roboterzustand, Bewegung und Beeper-Inventar."""

NORD, OST, SÜD, WEST = 0, 1, 2, 3


class PytiWandKollisionError(Exception):
    """Wird ausgelöst, wenn Pyti gegen eine Wand oder den Rand läuft."""


class Pyti:
    def __init__(self, x=0, y=0, richtung=OST, grid_size=15):
        self.x = x
        self.y = y
        self.richtung = richtung
        self.grid_size = grid_size
        self.beeper_im_inventar = 0
        self.ziel_beeper_im_inventar = 0
        self.normale_beeper_im_inventar = 0

    def vor(self):
        delta = {
            NORD: (0, -1),
            OST: (1, 0),
            SÜD: (0, 1),
            WEST: (-1, 0),
        }[self.richtung]
        naechstes_x = self.x + delta[0]
        naechstes_y = self.y + delta[1]
        if 0 <= naechstes_x < self.grid_size and 0 <= naechstes_y < self.grid_size:
            self.x, self.y = naechstes_x, naechstes_y
            return
        namen = ("NORD", "OST", "SÜD", "WEST")
        raise PytiWandKollisionError(
            f"AUTSCH! Pyti steht auf (X={self.x}, Y={self.y}), schaut nach "
            f"{namen[self.richtung]} und läuft gegen die Wand!"
        )

    def springen(self):
        delta = {
            NORD: (0, -2),
            OST: (2, 0),
            SÜD: (0, 2),
            WEST: (-2, 0),
        }[self.richtung]
        naechstes_x = self.x + delta[0]
        naechstes_y = self.y + delta[1]
        if 0 <= naechstes_x < self.grid_size and 0 <= naechstes_y < self.grid_size:
            self.x, self.y = naechstes_x, naechstes_y
            return
        raise PytiWandKollisionError("Pyti kann nicht über den Spielfeldrand springen.")

    def links_drehen(self):
        self.richtung = (self.richtung - 1) % 4

    def rechts_drehen(self):
        self.richtung = (self.richtung + 1) % 4

    def pick_beeper(self, spielfeld):
        if not spielfeld.sammle_beeper(self.x, self.y):
            raise Exception("Kein Beeper auf diesem Feld zum Aufheben!")
        self.beeper_im_inventar += 1
        if (self.x, self.y) == spielfeld.ziel_position:
            self.ziel_beeper_im_inventar += 1
        else:
            self.normale_beeper_im_inventar += 1

    def drop_beeper(self, spielfeld):
        if self.beeper_im_inventar <= 0:
            raise Exception("Keine Beeper im Inventar zum Ablegen!")
        spielfeld.lege_beeper(self.x, self.y)
        self.beeper_im_inventar -= 1
        if self.normale_beeper_im_inventar > 0:
            self.normale_beeper_im_inventar -= 1
        elif self.ziel_beeper_im_inventar > 0:
            self.ziel_beeper_im_inventar -= 1
