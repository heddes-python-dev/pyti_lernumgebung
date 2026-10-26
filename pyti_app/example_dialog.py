"""Shows the bundled Markdown cookbook in a separate dialog."""

from pathlib import Path

from PySide6.QtWidgets import QDialog, QTextBrowser, QVBoxLayout


def zeige_beispiele(parent, basis_pfad: Path):
    dialog = QDialog(parent)
    dialog.setWindowTitle("Pyti-Beispiele")
    dialog.resize(760, 620)
    layout = QVBoxLayout(dialog)
    browser = QTextBrowser(dialog)
    beispiele = basis_pfad / "EXAMPLES.md"
    if beispiele.is_file():
        browser.setMarkdown(beispiele.read_text(encoding="utf-8"))
    else:
        browser.setPlainText("Die Datei EXAMPLES.md wurde nicht gefunden.")
    layout.addWidget(browser)
    dialog.exec()
