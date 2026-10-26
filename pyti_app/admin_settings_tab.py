"""Editable execution settings for the admin dialog."""

from PySide6.QtWidgets import (
    QFormLayout,
    QLabel,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class SettingsTab(QWidget):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        form = QFormLayout()
        self.timeout = QSpinBox(self)
        self.timeout.setRange(1, 300)
        self.timeout.setSuffix(" Sekunden")
        self.timeout.setValue(settings["max_execution_time"])
        self.delay = QSpinBox(self)
        self.delay.setRange(0, 2000)
        self.delay.setSingleStep(50)
        self.delay.setSuffix(" ms")
        self.delay.setValue(settings["action_delay_ms"])
        form.addRow("Maximale Skriptlaufzeit:", self.timeout)
        form.addRow("Pause zwischen Aktionen:", self.delay)
        layout.addLayout(form)
        warning = QLabel(
            "Das Zeitlimit ersetzt keine sichere Sandbox. "
            "Nur vertrauenswürdige Skripte ausführen.",
            self,
        )
        warning.setWordWrap(True)
        layout.addWidget(warning)
        layout.addStretch()

    def values(self):
        return {
            "max_execution_time": self.timeout.value(),
            "action_delay_ms": self.delay.value(),
        }
