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


if __name__ == "__main__":
    unittest.main()
