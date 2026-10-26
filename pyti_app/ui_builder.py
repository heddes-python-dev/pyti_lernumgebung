"""Lädt das Qt-Fenster und baut die Widgetbereiche zusammen."""

from dataclasses import dataclass

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from .editor import CodeEditor
from .example_dialog import zeige_beispiele
from .field_view import SpielfeldView


@dataclass
class PytiWidgets:
    window: QWidget
    level_liste: QListWidget
    editor: CodeEditor
    start_button: QPushButton | None
    reset_button: QPushButton
    stop_button: QPushButton
    status: QLabel
    mission: QLabel
    spielfeld_view: SpielfeldView
    beispiele_button: QPushButton
    admin_button: QPushButton
    creator_button: QPushButton
    about_button: QPushButton


def lade_fenster(ui_pfad):
    ui_file = QFile(str(ui_pfad))
    if not ui_file.open(QFile.ReadOnly):
        raise FileNotFoundError(f"UI-Datei nicht gefunden: {ui_pfad}")
    try:
        window = QUiLoader().load(ui_file)
    finally:
        ui_file.close()
    if window is None:
        raise RuntimeError(f"Qt konnte das Fenster nicht laden: {ui_pfad}")
    return window


def baue_ui(basis_pfad, level_namen):
    window = lade_fenster(basis_pfad / "game_window.ui")
    window.setMinimumSize(1100, 760)
    window.resize(1400, 900)
    alter_view = window.grid_spielfeld
    start_button = getattr(window, "btn_ausfuehren", None)
    alter_view.hide()
    alter_view.deleteLater()

    haupt_layout = QHBoxLayout(window)
    haupt_layout.setContentsMargins(20, 20, 20, 20)
    haupt_layout.setSpacing(16)
    feld_spalte = QWidget(window)
    feld_layout = QVBoxLayout(feld_spalte)
    feld_layout.setContentsMargins(0, 0, 0, 0)
    feld_layout.setSpacing(10)
    seitenleiste = QWidget(window)
    sidebar = QVBoxLayout(seitenleiste)
    sidebar.setContentsMargins(0, 0, 0, 0)
    sidebar.setSpacing(8)
    seitenleiste.setMinimumWidth(320)
    seitenleiste.setMaximumWidth(420)
    seitenleiste.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    level_liste = QListWidget(seitenleiste)
    level_liste.setFixedHeight(86)
    level_liste.addItems(level_namen)
    sidebar.addWidget(level_liste)
    reset = QPushButton("Level neu starten", seitenleiste)
    reset.setToolTip("Setzt Pyti, Wände, Beeper und Inventar im aktuellen Level zurück")
    sidebar.addWidget(reset)
    editor = CodeEditor(seitenleiste)
    editor.setObjectName("input_befehl")
    editor.setMinimumHeight(365)
    editor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    window.input_befehl = editor
    sidebar.addWidget(editor, 1)
    sidebar.addWidget(_baue_hilfe(seitenleiste))

    beispiele = QPushButton("Beispiele", seitenleiste)
    beispiele.setToolTip("Öffnet das Pyti-Cookbook mit Beispielprogrammen")
    sidebar.addWidget(beispiele)
    beispiele.clicked.connect(lambda: zeige_beispiele(window, basis_pfad))
    admin = QPushButton("Administration", seitenleiste)
    admin.setToolTip("Systemstatus, Einstellungen und Level verwalten")
    sidebar.addWidget(admin)
    creator = QPushButton("Eigenes Level erstellen", seitenleiste)
    creator.setToolTip("Level grafisch entwerfen und als Python-Datei exportieren")
    sidebar.addWidget(creator)
    about = QPushButton("Über Pyti", seitenleiste)
    about.setToolTip("Projektinformationen, Mitwirkende und Sicherheitshinweise")
    sidebar.addWidget(about)
    start_layout = QHBoxLayout()
    if start_button is not None:
        start_layout.addWidget(start_button)
    stop = QPushButton("Stopp", seitenleiste)
    stop.setEnabled(False)
    start_layout.addWidget(stop)
    sidebar.addLayout(start_layout)
    status = QLabel("Bereit", seitenleiste)
    status.setWordWrap(True)
    status.setMinimumHeight(40)
    sidebar.addWidget(status)

    view = SpielfeldView(None, None, window)
    feld_layout.addWidget(view, 1)
    mission = QLabel(feld_spalte)
    mission.setMinimumHeight(80)
    mission.setMaximumHeight(130)
    mission.setWordWrap(True)
    mission.setStyleSheet(
        "background:#f0f4f8;border:1px solid #cbd5e1;border-radius:6px;"
        "padding:8px;font-size:13px;color:#1e293b;"
    )
    feld_layout.addWidget(mission)
    haupt_layout.addWidget(feld_spalte, 1)
    haupt_layout.addWidget(seitenleiste)
    return PytiWidgets(
        window, level_liste, editor, start_button, reset, stop, status,
        mission, view, beispiele, admin, creator, about,
    )


def _baue_hilfe(parent):
    help_box = QTextBrowser(parent)
    help_box.setFixedHeight(120)
    help_box.setHtml(
        "<b>Aktionen:</b><br>"
        "<code>moveForward()</code>, <code>turnLeft()</code><br>"
        "<code>turnRight()</code>, <code>turnAround()</code><br>"
        "<code>pickBeeper()</code>, <code>dropBeeper()</code>, "
        "<code>jump()</code> (nur über eine Wand)<br>"
        "<b>Sensoren (True/False):</b><br>"
        "<code>frontClear()</code>, <code>leftClear()</code>, "
        "<code>rightClear()</code><br><code>onBeeper()</code>, "
        "<code>beeperAhead()</code><br><code>anyBeeperInBag()</code>"
    )
    return help_box
