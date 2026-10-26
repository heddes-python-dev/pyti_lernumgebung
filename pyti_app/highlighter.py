"""Python-Syntax-Highlighting für den Code-Editor."""

import keyword
import re

from PySide6.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat


class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.regeln = []
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#0000ff"))
        keyword_format.setFontWeight(QFont.Bold)
        self.regeln.extend(
            (rf"\b{wort}\b", keyword_format) for wort in keyword.kwlist
        )
        command_format = QTextCharFormat()
        command_format.setForeground(QColor("#800080"))
        command_format.setFontWeight(QFont.Bold)
        commands = (
            "moveForward", "turnLeft", "turnRight", "turnAround", "jump",
            "pickBeeper", "dropBeeper", "onBeeper", "beeperAhead",
            "frontClear", "leftClear", "rightClear", "anyBeeperInBag",
        )
        self.regeln.extend(
            (rf"\b{command}\b", command_format) for command in commands
        )
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#008000"))
        self.regeln.extend([
            (r'".*?"', string_format),
            (r"'.*?'", string_format),
        ])
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#808080"))
        comment_format.setFontItalic(True)
        self.regeln.append((r"#.*$", comment_format))

    def highlightBlock(self, text):
        for pattern, text_format in self.regeln:
            for match in re.finditer(pattern, text):
                self.setFormat(match.start(), match.end() - match.start(), text_format)
