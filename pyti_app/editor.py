"""Code-Editor mit Zeilennummern und Syntax-Highlighting."""

from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QColor, QPainter, QTextFormat
from PySide6.QtWidgets import QPlainTextEdit, QTextEdit, QWidget

from .highlighter import PythonHighlighter


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        return QSize(self.code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.code_editor.line_number_area_paint_event(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.line_number_area = LineNumberArea(self)
        self.highlighter = PythonHighlighter(self.document())
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)
        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def line_number_area_width(self):
        digits, count = 1, max(1, self.blockCount())
        while count >= 10:
            count //= 10
            digits += 1
        return 10 + self.fontMetrics().horizontalAdvance("9") * digits

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(
                0, rect.y(), self.line_number_area.width(), rect.height()
            )
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        rect = self.contentsRect()
        self.line_number_area.setGeometry(
            QRect(rect.left(), rect.top(), self.line_number_area_width(), rect.height())
        )

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor("#f0f0f0"))
        block = self.firstVisibleBlock()
        number = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingGeometry(block).height())
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                painter.setPen(QColor("#707070"))
                painter.drawText(
                    0, top, self.line_number_area.width() - 6,
                    self.fontMetrics().height(), Qt.AlignRight, str(number + 1),
                )
            block = block.next()
            number = block.blockNumber()
            top = bottom
            bottom = top + int(self.blockBoundingGeometry(block).height())

    def highlight_current_line(self):
        selections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            selection.format.setBackground(QColor("#e8f2fc"))
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.selection = self.textCursor()
            selection.selection.clearSelection()
            selections.append(selection)
        self.setExtraSelections(selections)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Tab:
            self.insertPlainText("    ")
            event.accept()
            return
        super().keyPressEvent(event)
