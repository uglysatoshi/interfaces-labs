import sys
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QPainter, QPen


class ClockWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Clock Widget")
        self.resize(200, 200)
        self.setFixedSize(200, 200)
        self.angle = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def update_clock(self):
        self.angle += 6
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(Qt.PenStyle.SolidLine)
        painter.drawEllipse(10, 10, 180, 180)

        painter.setPen(QPen(Qt.GlobalColor.red, 2))
        painter.translate(100, 100)
        painter.rotate(self.angle)
        painter.drawLine(0, 0, 0, -80)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Array Processing and Clock Simulation')
        self.layout = QVBoxLayout()

        self.process_button = QPushButton("Process Array")
        self.process_button.clicked.connect(self.start_array)
        self.layout.addWidget(self.process_button)

        self.clock_button = QPushButton("Start Clock Simulation")
        self.clock_button.clicked.connect(self.start_clock_simulation)
        self.layout.addWidget(self.clock_button)

        self.setLayout(self.layout)

    def start_clock_simulation(self):
        self.clock_widget = ClockWidget()
        self.clock_widget.show()

    def start_array(self):
        array = []
        for i in range(20):
            array.append(i)
        random.shuffle(array)
        QMessageBox.information(self, "Processed Array", f"The processed array is:\n{array}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())