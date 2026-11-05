import json
import sys
from pathlib import Path

from PySide6.QtCore import QProcess, QProcessEnvironment, Qt
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .admin_test_inventory import load_test_cases


class AdminTestsTab(QWidget):
    def __init__(self, project_root=None):
        super().__init__()
        self.project_root = Path(project_root or Path(__file__).resolve().parents[1])
        self.test_root = self.project_root / "tests"
        self.test_rows = {}
        self.class_rows = {}
        self._pending_output = ""
        layout = QVBoxLayout(self)
        self.summary = QLabel(self)
        layout.addWidget(self.summary)
        self.run_button = QPushButton("Alle Tests ausführen", self)
        self.run_button.clicked.connect(self.run_tests)
        layout.addWidget(self.run_button)
        self.table = QTableWidget(0, 4, self)
        self.table.setHorizontalHeaderLabels(
            ["Status", "Modul", "Testfall", "Ergebnis"]
        )
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table, 1)
        self.output = QPlainTextEdit(self)
        self.output.setReadOnly(True)
        self.output.document().setMaximumBlockCount(500)
        layout.addWidget(self.output)
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self._read_output)
        self.process.finished.connect(self._finished)
        self.process.errorOccurred.connect(self._process_error)
        self._load_tests()

    def _load_tests(self):
        if not self.test_root.is_dir():
            self.summary.setText(
                "Entwicklertests sind in dieser Installation nicht enthalten."
            )
            self.run_button.setEnabled(False)
            return
        for test_id, class_id, module, name in load_test_cases(self.test_root):
            row = self.table.rowCount()
            self.test_rows[test_id] = row
            self.class_rows.setdefault(class_id, []).append(row)
            self.table.insertRow(row)
            for column, value in enumerate(
                ("Noch nicht ausgeführt", module, name, "")
            ):
                self.table.setItem(row, column, self._item(value))
        count = len(self.test_rows)
        self.summary.setText(f"{count} Testfälle in {len(self.class_rows)} Klassen geladen.")
        if not count:
            self.run_button.setEnabled(False)

    @staticmethod
    def _item(value):
        item = QTableWidgetItem(value)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    def run_tests(self):
        if self.process.state() != QProcess.NotRunning:
            return
        for row in self.test_rows.values():
            self.table.item(row, 0).setText("Läuft …")
            self.table.item(row, 3).setText("")
        self.output.clear()
        self.summary.setText("Testsuite läuft im Hintergrund …")
        self.run_button.setEnabled(False)
        environment = QProcessEnvironment.systemEnvironment()
        environment.insert("QT_QPA_PLATFORM", "offscreen")
        self.process.setProcessEnvironment(environment)
        self.process.setWorkingDirectory(str(self.project_root))
        self.process.start(
            sys.executable, ["-m", "pyti_app.admin_test_runner", str(self.project_root)]
        )

    def _read_output(self):
        text = bytes(self.process.readAllStandardOutput()).decode(
            "utf-8", errors="replace"
        )
        self._pending_output += text
        self.output.moveCursor(QTextCursor.MoveOperation.End)
        self.output.insertPlainText(text)
        lines = self._pending_output.splitlines(keepends=True)
        self._pending_output = ""
        if lines and not lines[-1].endswith(("\n", "\r")):
            self._pending_output = lines.pop()
        for line in lines:
            self._apply_result(line.strip())

    def _apply_result(self, line):
        marker = "PYTI_TEST_RESULT:"
        position = line.find(marker)
        if position < 0:
            return
        result = json.loads(line[position + len(marker):])
        row = self.test_rows.get(result["id"])
        if row is not None:
            self._set_result(row, result["status"])
            return
        for row in self.class_rows.get(result["class"], []):
            self._set_result(row, result["status"])

    def _set_result(self, row, result):
        if result in ("OK", "ok"):
            status = "OK"
        elif result.startswith(("skipped", "ÜBERSPRUNGEN")):
            status = "ÜBERSPRUNGEN"
        elif result in ("FAIL", "ERROR"):
            status = result
        elif result.startswith("Nicht ausgeführt"):
            status = "NICHT AUSGEFÜHRT"
        else:
            status = "UNBEKANNT"
        self.table.item(row, 0).setText(status)
        self.table.item(row, 3).setText(result)

    def _finished(self, exit_code, _exit_status):
        self._read_output()
        for row in self.test_rows.values():
            if self.table.item(row, 0).text() == "Läuft …":
                self._set_result(row, "Nicht ausgeführt; Details siehe Ausgabe")
        result = "erfolgreich" if exit_code == 0 else "mit Fehlern beendet"
        self.summary.setText(f"Testsuite {result} (Exit-Code {exit_code}).")
        self.run_button.setEnabled(bool(self.test_rows))

    def _process_error(self, error):
        if error == QProcess.FailedToStart:
            self.summary.setText(
                f"Testsuite konnte nicht gestartet werden: {self.process.errorString()}"
            )
            self.run_button.setEnabled(bool(self.test_rows))
