# Himmelsrichtungen
NORD, OST, SÜD, WEST = 0, 1, 2, 3

class PytiWandKollisionError(Exception):
    """Wird ausgelöst, wenn Pyti versucht, gegen eine Wand zu laufen."""
    pass

class Pyti:
    def __init__(self, x=0, y=0, richtung=OST, grid_size=15):
        self.x = x
        self.y = y
        self.richtung = richtung
        self.grid_size = grid_size
        self.beeper_im_inventar = 0  # <--- NEU: Zählt aufgesammelte Beeper

    def vor(self):
        naechstes_x = self.x
        naechstes_y = self.y

        if self.richtung == NORD:
            naechstes_y -= 1
        elif self.richtung == OST:
            naechstes_x += 1
        elif self.richtung == SÜD:
            naechstes_y += 1
        elif self.richtung == WEST:
            naechstes_x -= 1

        if 0 <= naechstes_x < self.grid_size and 0 <= naechstes_y < self.grid_size:
            self.x = naechstes_x
            self.y = naechstes_y
        else:
            richtungen_namen = ["NORD", "OST", "SÜD", "WEST"]
            raise PytiWandKollisionError(
                f"AUTSCH! Pyti steht auf (X={self.x}, Y={self.y}), schaut nach "
                f"{richtungen_namen[self.richtung]} und läuft gegen die Wand!"
            )

    def links_drehen(self):
        self.richtung = (self.richtung - 1) % 4

    def rechts_drehen(self):
        self.richtung = (self.richtung + 1) % 4

    def pick_beeper(self, spielfeld):
        """Hebt einen Beeper auf."""
        if spielfeld.hat_beeper(self.x, self.y):
            spielfeld.entferne_beeper(self.x, self.y)
            self.beeper_im_inventar += 1
        else:
            raise Exception("Kein Beeper auf diesem Feld zum Aufheben!")

    def drop_beeper(self, spielfeld):
        """Legt einen Beeper ab."""
        if getattr(self, 'beeper_im_inventar', 0) > 0:
            spielfeld.lege_beeper(self.x, self.y)
            self.beeper_im_inventar -= 1
        else:
            raise Exception("Keine Beeper im Inventar zum Ablegen!")