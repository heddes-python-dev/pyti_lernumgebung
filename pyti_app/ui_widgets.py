"""Typed container for widgets constructed by the main window builder."""

from dataclasses import dataclass

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QMenu,
    QMenuBar,
    QPushButton,
    QSlider,
    QWidget,
)

from .editor import CodeEditor
from .field_view import SpielfeldView


@dataclass
class PytiWidgets:
    window: QWidget
    level_liste: QListWidget
    editor: CodeEditor
    start_button: QPushButton | None
    reset_button: QPushButton
    stop_button: QPushButton
    next_level_button: QPushButton
    hint_button: QPushButton
    speed_slider: QSlider
    speed_label: QLabel
    status: QLabel
    mission: QLabel
    spielfeld_view: SpielfeldView
    menu_bar: QMenuBar
    menus: tuple[QMenu, QMenu]
    examples_action: QAction
    admin_action: QAction
    creator_action: QAction
    first_mission_action: QAction
    about_action: QAction
