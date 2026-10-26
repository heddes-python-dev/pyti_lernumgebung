"""Standalone visual level creator with local draft persistence."""

from PySide6.QtWidgets import QDialog

from .level_creator_actions import LevelCreatorActions
from .field_manager import SpielfeldManager
from .level_creator_data import LevelEntwurfSpeicher, neuer_entwurf
from .level_generator import GRID_SIZE
from .robot import Pyti
from .level_creator_ui import build_creator_ui


class LevelCreatorDialog(LevelCreatorActions, QDialog):
    def __init__(
        self, draft_path, register_level, existing_level_keys, parent=None
    ):
        super().__init__(parent)
        self.register_level = register_level
        self.existing_level_keys = existing_level_keys
        self.store = LevelEntwurfSpeicher(draft_path)
        self.persist_enabled = True
        self.loading = False
        try:
            self.drafts = self.store.laden()
        except (OSError, ValueError, TypeError, KeyError) as error:
            self.drafts = [neuer_entwurf()]
            self.persist_enabled = False
            self.load_error = f"Entwürfe nicht geladen; Datei bleibt erhalten: {error}"
        else:
            self.load_error = ""
        self.active_index = 0
        self.robot = Pyti(grid_size=GRID_SIZE)
        self.field = SpielfeldManager(grid_size=GRID_SIZE)
        self.setWindowTitle("Pyti – Level-Creator")
        self.resize(1080, 790)
        self._build_ui()
        self._load_draft(0)

    def _build_ui(self):
        build_creator_ui(self)
        self.draft_list.addItems(self._draft_labels())
        self.draft_list.currentIndexChanged.connect(self._select_draft)
        self.new_button.clicked.connect(self._new_draft)
        self.delete_button.clicked.connect(self._delete_draft)
        self.name.textChanged.connect(self._edited)
        self.mission.textChanged.connect(self._edited)
        self.direction.currentIndexChanged.connect(self._direction_changed)
        self.register_button.clicked.connect(self._register)
        self.export_button.clicked.connect(self._export)

    def _draft_labels(self):
        return [draft["name"].strip() or "Unbenanntes Level" for draft in self.drafts]

    def _select_draft(self, index):
        if self.loading or index < 0:
            return
        self._save_active()
        self._load_draft(index)

    def _load_draft(self, index):
        self.active_index = index
        draft = self.drafts[index]
        self.loading = True
        self.name.setText(draft["name"])
        self.mission.setText(draft["mission"])
        self.direction.setCurrentIndex(draft["level"]["start_richtung"])
        self.loading = False
        level = self._level_data(draft)
        self.field.lade_level(level, self.robot)
        if not self.load_error:
            self.status.setText("Entwurf wird lokal gespeichert.")

    def _level_data(self, draft):
        level = dict(draft["level"])
        goal = tuple(level["goal"]["position"])
        level["description"] = (
            f"Mission: {draft['mission']} Ziel: Erreiche den Beeper bei {goal} "
            "und hebe ihn auf."
        )
        return level

    def _snapshot(self):
        level = {
            "start_x": self.robot.x,
            "start_y": self.robot.y,
            "start_richtung": self.direction.currentIndex(),
            "waende": sorted(self.field.wand_koordinaten),
            "beeper": sorted(self.field.beeper_koordinaten),
            "goal": {
                "type": "collect_beeper",
                "position": self.field.ziel_position,
            },
        }
        return {
            "name": self.name.text(),
            "mission": self.mission.text(),
            "level": level,
        }

    def _save_active(self):
        if not hasattr(self, "name"):
            return
        self.drafts[self.active_index] = self._snapshot()
        self.loading = True
        self.draft_list.setItemText(
            self.active_index,
            self.drafts[self.active_index]["name"].strip() or "Unbenanntes Level",
        )
        self.loading = False
        if self.persist_enabled:
            self._persist()

    def _persist(self):
        try:
            self.store.speichern(self.drafts)
        except (OSError, ValueError, TypeError, KeyError) as error:
            self.status.setText(f"Entwurf konnte nicht gespeichert werden: {error}")
        else:
            self.status.setText("Entwurf lokal gespeichert.")

    def _edited(self, *_args):
        if not self.loading:
            self._save_active()

    def _direction_changed(self, *_args):
        if not self.loading:
            self.robot.richtung = self.direction.currentIndex()
            self.field.pyti_zeichnen(self.robot)
            self._save_active()
