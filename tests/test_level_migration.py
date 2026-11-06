import unittest

from pyti_app.admin_store import AdminStore
from pyti_app.levels import LEVELS


class LevelMigrationTests(unittest.TestCase):
    def test_alte_levelnamen_werden_ueber_den_titel_weitergefuehrt(self):
        overrides = {
            "0.0.50 Das große Finale": {
                "description": "Alte gespeicherte Admin-Mission"
            }
        }
        migrated = AdminStore._levels(LEVELS, overrides)
        self.assertEqual(
            migrated["0.5.0 Das große Finale"]["description"],
            "Alte gespeicherte Admin-Mission",
        )

    def test_umbenannte_levelnamen_werden_ueber_die_stabile_nummer_migriert(self):
        overrides = {
            "0.0.5 Die Ecke": {
                "description": "Gespeicherte Levelbeschreibung"
            }
        }
        migrated = AdminStore._levels(LEVELS, overrides)
        self.assertEqual(
            migrated["0.0.5 Die lange Kurve"]["description"],
            "Gespeicherte Levelbeschreibung",
        )

    def test_umbenanntes_level_mit_kanonischer_nummer_wird_migriert(self):
        overrides = {
            "0.1.0 Der Tunnel": {
                "description": "Gespeicherte Tunnelmission"
            }
        }
        migrated = AdminStore._levels(LEVELS, overrides)
        target = next(name for name in LEVELS if name.startswith("0.1.0 "))
        self.assertEqual(
            migrated[target]["description"], "Gespeicherte Tunnelmission"
        )


if __name__ == "__main__":
    unittest.main()
