"""Editing and export actions for level creator drafts."""

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox

from .level_creator_data import export_code, neuer_entwurf


class LevelCreatorActions:
    def _register(self):
        self._save_active()
        draft = self._snapshot()
        key = f"Eigenes Level: {draft['name'].strip()}"
        if key in self.existing_level_keys():
            answer = QMessageBox.question(
                self,
                "Eigenes Level ersetzen?",
                f"„{key}“ ist bereits gespeichert. Soll es ersetzt werden?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if answer != QMessageBox.Yes:
                return
        try:
            key = self.register_level(draft["name"], self._level_data(draft))
        except (OSError, ValueError, TypeError, KeyError) as error:
            self.status.setText(f"Level nicht übernommen: {error}")
            QMessageBox.warning(self, "Level nicht gespeichert", str(error))
            return
        self.status.setText(
            f"„{key}“ gespeichert. Es erscheint jetzt in der Levelauswahl."
        )

    def _cell_clicked(self, button, x, y):
        action = self.mode.currentData()
        position = (x, y)
        if action == "wall":
            if button != Qt.RightButton:
                return
            changed = self.field.toggle_wand(x, y)
        elif button != Qt.LeftButton:
            return
        elif action == "beeper":
            if position == self.field.ziel_position:
                self.status.setText("Der Ziel-Beeper muss auf dem Zielfeld bleiben.")
                return
            changed = self.field.toggle_beeper(x, y)
        elif action == "start":
            changed = position not in self.field.wand_koordinaten
            if changed:
                self.robot.x, self.robot.y = position
                self.field.pyti_zeichnen(self.robot)
        else:
            changed = position not in self.field.wand_koordinaten
            if changed:
                self.field.ziel_position = position
                self.field.beeper_koordinaten.add(position)
                self.field.darstellung.zeichne_raster(position)
                self.field.darstellung.zeichne_waende(self.field.wand_koordinaten)
                self.field.pyti_zeichnen(self.robot)
        if not changed:
            self.status.setText("Diese Zelle ist für die gewählte Aktion gesperrt.")
        else:
            self._save_active()

    def _new_draft(self):
        self._save_active()
        base = "Eigenes Level"
        names = {draft["name"] for draft in self.drafts}
        suffix = 2
        while base in names:
            base = f"Eigenes Level {suffix}"
            suffix += 1
        self.drafts.append(neuer_entwurf(base))
        self.loading = True
        self.draft_list.addItem(base)
        self.draft_list.setCurrentIndex(len(self.drafts) - 1)
        self.loading = False
        self._load_draft(len(self.drafts) - 1)
        if self.persist_enabled:
            self._persist()

    def _delete_draft(self):
        if len(self.drafts) == 1:
            self.drafts[0] = neuer_entwurf()
            self._load_draft(0)
        else:
            self.drafts.pop(self.active_index)
            self.loading = True
            self.draft_list.removeItem(self.active_index)
            self.active_index = min(self.active_index, len(self.drafts) - 1)
            self.draft_list.setCurrentIndex(self.active_index)
            self.loading = False
            self._load_draft(self.active_index)
        if self.persist_enabled:
            self._persist()

    def _export(self):
        self._save_active()
        draft = self._snapshot()
        try:
            code = export_code(draft["name"], draft)
        except (ValueError, TypeError, KeyError) as error:
            self.status.setText(str(error))
            QMessageBox.warning(self, "Level nicht exportiert", str(error))
            return
        filename = self.name.text().strip().replace(" ", "_") or "eigenes_level"
        path, _ = QFileDialog.getSaveFileName(
            self, "Leveldefinition speichern",
            str(Path.home() / f"{filename}.py"), "Python-Dateien (*.py)",
        )
        if not path:
            return
        try:
            Path(path).write_text(code, encoding="utf-8")
        except OSError as error:
            self.status.setText(f"Export fehlgeschlagen: {error}")
            QMessageBox.critical(self, "Export fehlgeschlagen", str(error))
            return
        self.status.setText(f"Leveldefinition exportiert: {path}")
