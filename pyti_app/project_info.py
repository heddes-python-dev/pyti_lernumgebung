"""Projektinformationen in einem Dialog der Desktop-Anwendung anzeigen."""

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QTextBrowser,
    QVBoxLayout,
)


PROJECT_URL = "https://github.com/heddes-python-dev/pyti_lernumgebung"
RELEASE_URL = f"{PROJECT_URL}/releases/latest"


def erstelle_projektinfo_dialog(parent, version):
    dialog = QDialog(parent)
    dialog.setWindowTitle("Über Pyti")
    dialog.setMinimumSize(520, 480)
    layout = QVBoxLayout(dialog)
    text = QTextBrowser(dialog)
    text.setOpenExternalLinks(True)
    text.setHtml(_projektinfo_html(version))
    layout.addWidget(text)
    buttons = QDialogButtonBox(QDialogButtonBox.Close, parent=dialog)
    buttons.rejected.connect(dialog.reject)
    buttons.accepted.connect(dialog.accept)
    layout.addWidget(buttons)
    return dialog


def _projektinfo_html(version):
    return f"""
        <h2>Pyti Lernumgebung</h2>
        <p><b>Version:</b> {version}</p>
        <p>Pyti vermittelt Python und algorithmisches Denken mit sichtbaren
        Aufgaben: Lernende programmieren den Roboter und beobachten direkt,
        wie ihr Code das Spielfeld verändert.</p>
        <p><b>Initiator und Hauptentwickler:</b>
        <a href="https://github.com/heddes-python-dev">Thomas Heddes
        (@heddes-python-dev)</a><br>
        <b>Öffentlicher Projektstart:</b> 19. September 2026<br>
        <b>Bisherige Mitwirkende:</b>
        <a href="https://github.com/iLollek">@iLollek</a> (Korrektur von
        Rechtschreibung und Grammatik)<br>
        <b>Lizenz:</b> MIT</p>
        <h3>Open Source und Mitmachen</h3>
        <p>Pyti ist ein offenes Projekt. Fehlerberichte, Ideen, Dokumentation,
        Unterrichtserfahrungen und Codebeiträge sind willkommen.</p>
        <ul>
        <li><a href="{PROJECT_URL}">Projekt und Quellcode auf GitHub</a></li>
        <li><a href="{RELEASE_URL}">Neueste Version und Downloads</a></li>
        </ul>
        <h3>Hinweis zu Sicherheit und Schuleinsatz</h3>
        <p>Pyti führt normalen Python-Code im Anwendungsprozess aus und ist
        <b>keine Sandbox</b>. Führe nur Skripte aus, denen du vertraust.
        Die Anwendung ist keine zertifizierte Schulsoftware und nicht für
        unbeaufsichtigte Ausführung nicht vertrauenswürdiger Skripte
        freigegeben. Isolation, Barrierefreiheit und Schulpilotierungen sind
        offene Entwicklungsziele.</p>
        <p><a href="{PROJECT_URL}/blob/master/ROADMAP.md">
        Roadmap und Schulziele</a> ·
        <a href="{PROJECT_URL}/blob/master/CONTRIBUTING.md">
        Mitwirkungsleitfaden</a></p>
    """
