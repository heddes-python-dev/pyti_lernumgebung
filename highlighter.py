from PySide6.QtCore import Qt
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
import keyword

class PythonHighlighter(QSyntaxHighlighter):
    """Färbt Python-Code ein: Keywords in Blau, Pyti-Befehle in Lila."""
    
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # 1. Format für echte Python-Keywords (for, while, def, etc.) - BLAU
        python_keyword_format = QTextCharFormat()
        python_keyword_format.setForeground(QColor("#0000FF"))
        python_keyword_format.setFontWeight(QFont.Bold)
        
        for word in keyword.kwlist:
            pattern = f"\\b{word}\\b"
            self.highlighting_rules.append((pattern, python_keyword_format))

        # 2. Format für Pyti-Roboterbefehle - LILA / MAGENTA
        robot_command_format = QTextCharFormat()
        robot_command_format.setForeground(QColor("#800080"))  # Kräftiges Lila
        robot_command_format.setFontWeight(QFont.Bold)
        
        robot_commands = [
            'moveForward', 
            'turnLeft', 
            'turnRight', 
            'turnAround',
            'pickBeeper',
            'dropBeeper',
            'onBeeper',
            'beeperAhead',
            'frontClear',
            'leftClear',
            'rightClear',
            'anyBeeperInBag'
        ]
        
        for word in robot_commands:
            pattern = f"\\b{word}\\b"
            self.highlighting_rules.append((pattern, robot_command_format))

        # 3. Format für Strings / Zeichenketten - GRÜN
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#008000"))
        self.highlighting_rules.append(("\".*?\"", string_format))
        self.highlighting_rules.append(("'.*?'", string_format))

        # 4. Format für Kommentare - GRAU
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#808080"))
        comment_format.setFontItalic(True)
        self.highlighting_rules.append(("#.*$", comment_format))

    def highlightBlock(self, text):
        import re
        for pattern, fmt in self.highlighting_rules:
            for match in re.finditer(pattern, text):
                start = match.start()
                length = match.end() - start
                self.setFormat(start, length, fmt)