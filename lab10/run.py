import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QRegExp
import re


class AuthApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.numbers_label = QLabel("Введите цифры:")
        self.numbers_input = QLineEdit()
        layout.addWidget(self.numbers_label)
        layout.addWidget(self.numbers_input)

        self.convert_button = QPushButton("Преобразовать")
        self.convert_button.clicked.connect(self.convert_numbers)
        layout.addWidget(self.convert_button)

        self.text_label = QLabel("")
        layout.addWidget(self.text_label)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()

        # Проверка введенного email с помощью регулярного выражения
        email_validator = QRegExp(r'^[a-zA-Z0-9._%+-]+@working\.ru$')
        if email_validator.exactMatch(email):
            self.result_label.setText("Успешная авторизация")
        else:
            self.result_label.setText("Неверный email")

    def convert_numbers(self):
        input_text = self.numbers_input.text()
        converted_text = ""

        # Преобразование введенных цифр в текстовое представление
        digits_to_text = {
            '1': 'один',
            '2': 'два',
            '3': 'три',
            '4': 'четыре',
            '5': 'пять',
            '6': 'шесть',
            '7': 'семь',
            '8': 'восемь',
            '9': 'девять',
            '0': 'ноль'
        }

        # Преобразуем каждую цифру
        for digit in input_text:
            if digit.isdigit():
                converted_text += digits_to_text[digit] + ' '

        self.text_label.setText(converted_text.strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthApp()
    window.show()
    sys.exit(app.exec())