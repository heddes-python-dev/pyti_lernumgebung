import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from pyti import Pyti
from playing_field import SpielfeldManager, SpielfeldView
from commands import BefehlsInterpreter
from editor import CodeEditor
from level import LEVELS

def hauptprogramm():
    app = QApplication(sys.argv)

    # --- PFAD RELATIV ZU MAIN.PY AUFLÖSEN ---
    basis_pfad = Path(__file__).resolve().parent
    ui_pfad = basis_pfad / "game_window.ui"

    ui_file = QFile(str(ui_pfad))
    if not ui_file.open(QFile.ReadOnly):
        print(f"Fehler: UI-Datei unter '{ui_pfad}' nicht gefunden.")
        return
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    if not window:
        print("Fehler beim Laden des Fensters.")
        return

    window.setMinimumSize(1100, 760)
    window.resize(1400, 900)

    altes_view = window.grid_spielfeld
    btn_ausfuehren = getattr(window, "btn_ausfuehren", None)

    haupt_layout = QHBoxLayout(window)
    haupt_layout.setContentsMargins(20, 20, 20, 20)
    haupt_layout.setSpacing(16)

    spielfeld_container = QWidget(window)
    spielfeld_layout = QVBoxLayout(spielfeld_container)
    spielfeld_layout.setContentsMargins(0, 0, 0, 0)
    spielfeld_layout.setSpacing(10)

    altes_view.hide()
    altes_view.deleteLater()

    # --- RECHTE SEITENLEISTE MIT LAYOUT ---
    sidebar_container = QWidget(window)
    sidebar_layout = QVBoxLayout(sidebar_container)
    sidebar_layout.setContentsMargins(0, 0, 0, 0)
    sidebar_layout.setSpacing(10)
    sidebar_container.setMinimumWidth(320)
    sidebar_container.setMaximumWidth(420)
    sidebar_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    # 1. Level-Liste
    level_liste = QListWidget(sidebar_container)
    level_liste.setFixedHeight(86)
    level_liste.addItems(LEVELS.keys())
    sidebar_layout.addWidget(level_liste, 0)

    # 2. Code-Editor
    code_editor = CodeEditor(sidebar_container)
    code_editor.setObjectName("input_befehl")
    code_editor.setMinimumHeight(400)
    code_editor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    window.input_befehl = code_editor
    sidebar_layout.addWidget(code_editor, 1)

    # 3. Befehls-Referenz (Hilfe-Box)
    help_box = QTextBrowser(sidebar_container)
    help_box.setFixedHeight(145)
    help_box.setHtml("""
    <b style='color: #333;'>Aktionen:</b><br>
    <code style='color: #0066cc;'>moveForward()</code>, <code style='color: #0066cc;'>turnLeft()</code><br>
    <code style='color: #0066cc;'>turnRight()</code>, <code style='color: #0066cc;'>turnAround()</code><br>
    <code style='color: #0066cc;'>pickBeeper()</code>, <code style='color: #0066cc;'>dropBeeper()</code><br>
    <b style='color: #333;'>Sensoren (True/False):</b><br>
    <code style='color: #2e8b57;'>frontClear()</code>, <code style='color: #2e8b57;'>leftClear()</code>, <code style='color: #2e8b57;'>rightClear()</code><br>
    <code style='color: #2e8b57;'>onBeeper()</code>, <code style='color: #2e8b57;'>beeperAhead()</code><br>
    <code style='color: #2e8b57;'>anyBeeperInBag()</code>
    """)
    sidebar_layout.addWidget(help_box, 0)

    beispiele_button = QPushButton("Beispiele", sidebar_container)
    beispiele_button.setToolTip("Öffnet das Pyti-Cookbook mit Beispielprogrammen")
    beispiele_button.setMinimumHeight(32)
    sidebar_layout.addWidget(beispiele_button, 0)

    def beispiele_anzeigen():
        beispiele_pfad = basis_pfad / "EXAMPLES.md"
        dialog = QDialog(window)
        dialog.setWindowTitle("Pyti-Beispiele")
        dialog.resize(760, 620)
        dialog_layout = QVBoxLayout(dialog)
        beispiele_browser = QTextBrowser(dialog)
        if beispiele_pfad.is_file():
            beispiele_browser.setMarkdown(
                beispiele_pfad.read_text(encoding="utf-8")
            )
        else:
            beispiele_browser.setPlainText(
                "Die Datei EXAMPLES.md wurde nicht gefunden."
            )
        dialog_layout.addWidget(beispiele_browser)
        dialog.exec()

    beispiele_button.clicked.connect(beispiele_anzeigen)

    # 4. Den Original-Button aus der .ui-Datei ins Layout holen
    if btn_ausfuehren is not None:
        btn_ausfuehren.setMinimumHeight(36)
        btn_ausfuehren.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sidebar_layout.addWidget(btn_ausfuehren)
    else:
        print("Button 'btn_ausfuehren' nicht in UI gefunden.")

    # --- SPIELFELD UND MISSIONSBESCHREIBUNG ---
    interaktive_view = SpielfeldView(None, None, window)
    interaktive_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    spielfeld_layout.addWidget(interaktive_view, 1)

    missions_label = QLabel(spielfeld_container)
    missions_label.setMinimumHeight(80)
    missions_label.setMaximumHeight(130)
    missions_label.setWordWrap(True)
    missions_label.setStyleSheet("""
        background-color: #f0f4f8;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 8px;
        font-size: 13px;
        color: #1e293b;
    """)
    spielfeld_layout.addWidget(missions_label)

    haupt_layout.addWidget(spielfeld_container, 1)
    haupt_layout.addWidget(sidebar_container, 0)
    # --------------------------------------------

    # 1. SCHICHTEN INITIALISIEREN
    pyti = Pyti(x=0, y=0, richtung=1, grid_size=15)
    spielfeld = SpielfeldManager(grid_size=15)
    interpreter = BefehlsInterpreter(pyti, spielfeld)

    interaktive_view.setScene(spielfeld.scene)
    interaktive_view.spielfeld_manager = spielfeld
    window.grid_spielfeld = interaktive_view

    # --- LEVEL-AUSWAHL LOGIK ---
    aktuelles_level = {"daten": None}

    def level_ausgewaehlt(item):
        level_name = item.text()
        level_daten = LEVELS[level_name]
        aktuelles_level["daten"] = level_daten
        spielfeld.lade_level(level_daten, pyti)

        beschreibung = level_daten.get("description", "Keine Beschreibung verfügbar.")
        missions_label.setText(f"<b>Mission ({level_name}):</b><br>{beschreibung}")
        print(f"Level geladen: {level_name}")

    level_liste.currentItemChanged.connect(
        lambda current, _previous: level_ausgewaehlt(current) if current else None
    )

    erster_name = list(LEVELS.keys())[0]
    spielfeld.lade_level(LEVELS[erster_name], pyti)
    level_liste.setCurrentRow(0)
    # ----------------------------

    # 2. BEFEHLS-AUSFÜHRUNG VERKNÜPFEN
    def befehl_starten():
        skript_text = window.input_befehl.toPlainText()
        if interpreter.interpretiere_und_fuehre_aus(skript_text):
            window.input_befehl.clear()
            level_daten = aktuelles_level["daten"]
            if level_daten and spielfeld.ziel_erreicht(pyti, level_daten.get("goal")):
                missions_label.setText(
                    missions_label.text() + "<br><b>Geschafft! Ziel erreicht.</b>"
                )

    if btn_ausfuehren is not None:
        btn_ausfuehren.clicked.connect(befehl_starten)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    hauptprogramm()