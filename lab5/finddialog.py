from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class FindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.editor = None
        self.text_to_find = None
        self.find_button = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Find")
        self.text_to_find = QLineEdit(self)
        self.find_button = QPushButton("Find", self)
        self.find_button.clicked.connect(self.on_find_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.text_to_find)
        layout.addWidget(self.find_button)
        self.setLayout(layout)

    def on_find_clicked(self):
        self.accept()

    def get_find_text(self):
        return self.text_to_find.text()