from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from finddialog import FindDialog


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.find_action = None
        self.select_all_action = None
        self.paste_action = None
        self.delete_action = None
        self.copy_action = None
        self.cut_action = None
        self.exit_action = None
        self.font_action = None
        self.left_align_action = None
        self.center_align_action = None
        self.right_align_action = None
        self.open_action = None
        self.save_action = None
        self.editor = None
        self.init_ui()

    def init_ui(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        self.create_actions()
        self.create_menus()

        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 800, 600)

    def create_actions(self):
        self.left_align_action = QAction("Left Align", self)
        self.left_align_action.setStatusTip("Align text to the left")
        self.left_align_action.triggered.connect(self.set_alignment_left)

        self.center_align_action = QAction("Center", self)
        self.center_align_action.setStatusTip("Center text")
        self.center_align_action.triggered.connect(self.set_alignment_center)

        self.right_align_action = QAction("Right Align", self)
        self.right_align_action.setStatusTip("Align text to the right")
        self.right_align_action.triggered.connect(self.set_alignment_right)

        self.font_action = QAction("Change Font", self)
        self.font_action.setStatusTip("Change the font")
        self.font_action.triggered.connect(self.change_font)

        self.cut_action = QAction("Cut", self)
        self.cut_action.setStatusTip("Cut selected text")
        self.cut_action.triggered.connect(self.editor.cut)
        self.cut_action.setShortcut("Ctrl+X")

        self.copy_action = QAction("Copy", self)
        self.copy_action.setStatusTip("Copy selected text")
        self.copy_action.triggered.connect(self.editor.copy)
        self.copy_action.setShortcut("Ctrl+C")

        self.paste_action = QAction("Paste", self)
        self.paste_action.setStatusTip("Paste text from clipboard")
        self.paste_action.triggered.connect(self.editor.paste)
        self.paste_action.setShortcut("Ctrl+V")

        self.delete_action = QAction("Delete", self)
        self.delete_action.setStatusTip("Delete selected text")
        self.delete_action.triggered.connect(self.editor.clear)
        self.delete_action.setShortcut("Delete")

        self.select_all_action = QAction("Select All", self)
        self.select_all_action.setStatusTip("Select all text")
        self.select_all_action.triggered.connect(self.editor.selectAll)
        self.select_all_action.setShortcut("Ctrl+A")

        self.find_action = QAction("Find", self)
        self.find_action.setStatusTip("Find text")
        self.find_action.triggered.connect(self.find_text)
        self.find_action.setShortcut("Ctrl+F")

        self.open_action = QAction("Open", self)
        self.open_action.setStatusTip("Open file")
        self.open_action.triggered.connect(self.open_file)
        self.open_action.setShortcut("Ctrl+O")

        self.save_action = QAction("Save", self)
        self.save_action.setStatusTip("Save file")
        self.save_action.triggered.connect(self.save_file)
        self.save_action.setShortcut("Ctrl+S")

        self.exit_action = QAction("Exit", self)
        self.exit_action.setStatusTip("Exit application")
        self.exit_action.triggered.connect(self.close)
        self.exit_action.setShortcut("Ctrl+Q")

    def create_menus(self):
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.exit_action)

        edit_menu = self.menuBar().addMenu("Edit")

        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)
        edit_menu.addAction(self.delete_action)
        edit_menu.addAction(self.select_all_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.left_align_action)
        edit_menu.addAction(self.center_align_action)
        edit_menu.addAction(self.right_align_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.find_action)

        view_menu = self.menuBar().addMenu("View")
        view_menu.addAction(self.font_action)

    def set_alignment_left(self):
        self.editor.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def set_alignment_center(self):
        self.editor.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_alignment_right(self):
        self.editor.setAlignment(Qt.AlignmentFlag.AlignRight)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name:
            with open(file_name, "r") as file:
                self.editor.setText(file.read())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File")
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.editor.toPlainText())

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setFont(font)

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_Plus or event.key() == Qt.Key.Key_Equal:
                self.increase_font_size()
            elif event.key() == Qt.Key.Key_Minus:
                self.decrease_font_size()
        super().keyPressEvent(event)

    def increase_font_size(self):
        font = self.editor.font()
        font.setPointSize(font.pointSize() + 4)
        self.editor.setFont(font)

    def decrease_font_size(self):
        font = self.editor.font()
        font.setPointSize(max(1, font.pointSize() - 4))
        self.editor.setFont(font)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def find_text(self):
        dialog = FindDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            text_to_find = dialog.get_find_text().strip()
            if text_to_find:
                self.highlight_text(text_to_find)
            else:
                QMessageBox.information(self, "Notepad", "The search query cannot be empty.")

    def highlight_text(self, text):
        plain_format = QTextCharFormat()
        cursor = self.editor.textCursor()
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.setCharFormat(plain_format)
        cursor.clearSelection()
        self.editor.setTextCursor(cursor)

        formatter = QTextCharFormat()
        formatter.setBackground(QColor("yellow"))

        cursor.beginEditBlock()
        document = self.editor.document()
        search_cursor = QTextCursor(document)
        while True:
            search_cursor = document.find(text, search_cursor)
            if search_cursor.isNull():
                break
            search_cursor.mergeCharFormat(formatter)
        cursor.endEditBlock()
