"""UI actions for learning prompts, speed, and level progression."""

from .learning_path import prompts_for_level


class LearningPathActions:
    def _show_level(self, name):
        data = self.levels[name]
        objective, self.hint_text, reflection = prompts_for_level(name, data)
        completed = name in self.completed_levels
        self.ui.mission.setText(
            f"<b>Mission ({name}):</b><br>{data.get('description', '')}<br>"
            f"<b>Lernziel:</b> {objective}<br>"
            f"<b>Reflexionsfrage:</b> {reflection}"
            f"<br><b>Fortschritt:</b> {self._completed_count()}/{len(self.levels)} Level"
            f"{'<br><b>Bereits abgeschlossen.</b>' if completed else ''}"
        )

    def _set_speed(self, delay_ms):
        self.interpreter.action_delay_ms = delay_ms
        self.ui.speed_label.setText(
            f"Geschwindigkeit: {delay_ms} ms Pause (0 = schnell)"
        )

    def show_hint(self):
        self.ui.status.setText(f"Tipp: {self.hint_text}")

    def _update_next_level(self):
        current = self.ui.level_liste.currentRow()
        self.next_level_name = ""
        if current >= 0 and current + 1 < self.ui.level_liste.count():
            self.next_level_name = self.ui.level_liste.item(current + 1).text()
        item = self.ui.level_liste.currentItem()
        self.ui.next_level_button.setEnabled(
            bool(self.next_level_name)
            and item is not None
            and item.text() in self.completed_levels
        )
        self.ui.next_level_button.setToolTip(
            f"Weiter zu {self.next_level_name}" if self.next_level_name
            else "Der Lernpfad ist abgeschlossen."
        )

    def _completed_count(self):
        return sum(name in self.completed_levels for name in self.levels)

    def next_level(self):
        if self.next_level_name:
            self.ui.level_liste.setCurrentRow(
                self.ui.level_liste.currentRow() + 1
            )

    def _save_progress(self, active_level):
        if self.progress_store is None:
            return
        try:
            self.progress_store.save(self.completed_levels, active_level)
        except (OSError, ValueError, TypeError) as error:
            self.ui.status.setText(f"Lernfortschritt nicht gespeichert: {error}")
