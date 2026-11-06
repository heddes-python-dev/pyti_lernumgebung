"""Lädt das Qt-Fenster und baut die Widgetbereiche zusammen."""

from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMenuBar,
    QPushButton,
    QSlider,
    QSizePolicy,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from .editor import CodeEditor
from .field_view import SpielfeldView
from .ui_menus import baue_menues
from .ui_widgets import PytiWidgets


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

    window_layout = QVBoxLayout(window)
    window_layout.setContentsMargins(0, 0, 0, 0)
    menu_bar, menus, actions = baue_menues(window, basis_pfad)
    window_layout.setMenuBar(menu_bar)
    content = QWidget(window)
    window_layout.addWidget(content)

    haupt_layout = QHBoxLayout(content)
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
    speed_row = QHBoxLayout()
    speed_label = QLabel(seitenleiste)
    speed_row.addWidget(speed_label)
    speed_slider = QSlider(Qt.Horizontal, seitenleiste)
    speed_slider.setRange(0, 2000)
    speed_slider.setSingleStep(50)
    speed_slider.setPageStep(200)
    speed_slider.setToolTip("Animationspause zwischen Pyti-Aktionen")
    speed_row.addWidget(speed_slider, 1)
    sidebar.addLayout(speed_row)
    editor = CodeEditor(seitenleiste)
    editor.setObjectName("input_befehl")
    editor.setMinimumHeight(365)
    editor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    window.input_befehl = editor
    sidebar.addWidget(editor, 1)
    sidebar.addWidget(_baue_hilfe(seitenleiste))

    start_layout = QHBoxLayout()
    if start_button is not None:
        start_layout.addWidget(start_button)
    stop = QPushButton("Stopp", seitenleiste)
    stop.setEnabled(False)
    start_layout.addWidget(stop)
    sidebar.addLayout(start_layout)
    path_controls = QHBoxLayout()
    hint_button = QPushButton("Tipp anzeigen", seitenleiste)
    path_controls.addWidget(hint_button)
    next_level_button = QPushButton("Nächstes Level", seitenleiste)
    next_level_button.setEnabled(False)
    path_controls.addWidget(next_level_button)
    sidebar.addLayout(path_controls)
    status = QLabel("Bereit", seitenleiste)
    status.setWordWrap(True)
    status.setMinimumHeight(40)
    sidebar.addWidget(status)

    view = SpielfeldView(None, None, window)
    feld_layout.addWidget(view, 1)
    mission = QLabel(feld_spalte)
    mission.setMinimumHeight(80)
    mission.setMaximumHeight(180)
    mission.setWordWrap(True)
    mission.setStyleSheet(
        "background:#f0f4f8;border:1px solid #cbd5e1;border-radius:6px;"
        "padding:8px;font-size:13px;color:#1e293b;"
    )
    feld_layout.addWidget(mission)
    haupt_layout.addWidget(feld_spalte, 1)
    haupt_layout.addWidget(seitenleiste)
    return PytiWidgets(
        window, level_liste, editor, start_button, reset, stop, next_level_button,
        hint_button, speed_slider, speed_label, status, mission, view, menu_bar,
        menus, *actions,
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
