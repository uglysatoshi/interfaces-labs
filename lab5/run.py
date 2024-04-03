from mainwindow import Notepad
import sys
from PyQt6.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec())
