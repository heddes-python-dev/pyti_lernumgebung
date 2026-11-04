"""Geführter Einstieg mit vollständigem Beispiel und Lückenvorlage."""

from html import escape

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
)

from .beginner_mission_data import erstelle_erste_mission


def zeige_erste_mission(parent, widgets, levels):
    dialog = QDialog(parent)
    selected = widgets.level_liste.currentItem()
    level_name = selected.text() if selected else next(iter(levels), "")
    dialog.setWindowTitle(f"Erste Mission: {level_name}")
    dialog.setMinimumWidth(520)
    layout = QVBoxLayout(dialog)
    anleitung = QTextBrowser(dialog)
    level = levels.get(level_name)
    mission = erstelle_erste_mission(level) if level else None
    anleitung.setHtml(_anleitung_html(mission, level_name))
    layout.addWidget(anleitung)
    template_row = QHBoxLayout()
    starter_button = QPushButton("Vollständiges Beispiel laden", dialog)
    gap_button = QPushButton("Lückenvorlage laden", dialog)
    if mission is None:
        starter_button.setEnabled(False)
        gap_button.setEnabled(False)
    template_row.addWidget(starter_button)
    template_row.addWidget(gap_button)
    layout.addLayout(template_row)

    hint_button = QPushButton("Tipp anzeigen", dialog)
    solution_button = QPushButton("Lösung laden", dialog)
    solution_button.setEnabled(False)
    hint_row = QHBoxLayout()
    hint_row.addWidget(hint_button)
    hint_row.addWidget(solution_button)
    layout.addLayout(hint_row)
    hint_label = QLabel(dialog)
    hint_label.setWordWrap(True)
    hint_label.setText(
        "Die Lösung wird nach allen drei angezeigten Tipps freigeschaltet."
        if mission is not None
        else "Für dieses Level sind keine Tipps oder Lösungsvorlage verfügbar."
    )
    layout.addWidget(hint_label)
    if mission is None:
        hint_button.setEnabled(False)

    buttons = QDialogButtonBox(QDialogButtonBox.Close, parent=dialog)
    buttons.rejected.connect(dialog.reject)
    if mission is not None:
        starter_button.clicked.connect(
            lambda: _lade_code(
                dialog,
                widgets,
                mission.starter_code,
                "Vollständiges Beispiel geladen.",
            )
        )
        gap_button.clicked.connect(
            lambda: _lade_code(
                dialog,
                widgets,
                mission.luecken_code,
                "Lückenvorlage geladen. Ergänze den nächsten Befehl.",
            )
        )
    hint_index = 0

    def zeige_tipp():
        nonlocal hint_index
        hint_nummer = hint_index + 1
        hint_label.setText(
            f"Tipp {hint_nummer} von {len(mission.hinweise)}:\n"
            f"{mission.hinweise[hint_index]}"
        )
        hint_index += 1
        if hint_index == len(mission.hinweise):
            hint_button.setEnabled(False)
            solution_button.setEnabled(True)
            hint_label.setText(
                f"{hint_label.text()}\n\nAlle Tipps angezeigt. "
                "„Lösung laden“ ist jetzt freigeschaltet."
            )

    hint_button.clicked.connect(zeige_tipp)
    if mission is not None:
        solution_button.clicked.connect(
            lambda: _lade_code(
                dialog,
                widgets,
                mission.loesung_code,
                "Lösung geladen. Vergleiche sie mit deiner Vorlage.",
            )
        )
    layout.addWidget(buttons)
    dialog.exec()


def _anleitung_html(mission, level_name):
    erklaerung = (
        mission.beschreibung
        if mission is not None
        else (
            "Für dieses Level kann keine sichere Vorlage erstellt werden. "
            "Nutze den Editor frei oder wähle ein anderes Level."
        )
    )
    return (
        f"<h2>{escape(level_name)}</h2>"
        "<p>Pyti Schritt für Schritt bewegen</p>"
        f"<p>{erklaerung}</p>"
        "<p>Jeder <code>moveForward()</code>-Befehl bewegt Pyti ein Feld "
        "nach vorn. Ergänze die Vorlage passend zu diesem Level. "
        "Jede Vorlage kann den aktuellen Editorinhalt nur nach deiner "
        "Bestätigung ersetzen.</p>"
        "<p>Nach jedem Lauf bleibt dein Code erhalten. Klicke auf "
        "<b>Level neu starten</b>, bevor du denselben Ablauf erneut "
        "ausführst. Pyti hat das Levelziel erst erreicht, wenn der Beeper "
        "auch aufgenommen wurde.</p>"
    )


def _lade_code(dialog, widgets, code, status):
    if widgets.editor.toPlainText().strip():
        answer = QMessageBox.question(
            dialog,
            "Editorinhalt ersetzen?",
            "Der vorhandene Code wird durch das Einstiegsbeispiel ersetzt.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
    widgets.reset_button.click()
    widgets.editor.setPlainText(code)
    widgets.status.setText(status)
    dialog.accept()
