import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')
        self.pen_width = 4  # Default pen width

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def set_pen_width(self, width):
        self.pen_width = width

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = int(e.position().x())
            self.last_y = int(e.position().y())
            return  # Ignore the first time.

        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(self.pen_width)  # Set pen width
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, int(e.position().x()), int(e.position().y()))
        painter.end()
        self.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = int(e.position().x())
        self.last_y = int(e.position().y())

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


class QPaletteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class MainWindow(QtWidgets.QMainWindow):
    l = QtWidgets.QVBoxLayout()

    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        w.setLayout(self.l)
        self.l.addWidget(self.canvas)

        self.setCentralWidget(w)

        self.init_menu()

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')

        save_action = QtGui.QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_image)
        file_menu.addAction(save_action)

        tools_menu = menubar.addMenu('&Tools')

        increase_pen_width_action = QtGui.QAction('&Increase Pen Width', self)
        increase_pen_width_action.setShortcut('Ctrl+I')
        increase_pen_width_action.triggered.connect(self.increase_pen_width)
        tools_menu.addAction(increase_pen_width_action)

        decrease_pen_width_action = QtGui.QAction('&Decrease Pen Width', self)
        decrease_pen_width_action.setShortcut('Ctrl+D')
        decrease_pen_width_action.triggered.connect(self.decrease_pen_width)
        tools_menu.addAction(decrease_pen_width_action)

        change_color_action = QtGui.QAction('&Change Pen Color', self)
        change_color_action.setShortcut('Ctrl+C')
        change_color_action.triggered.connect(self.change_pen_color)
        tools_menu.addAction(change_color_action)

    def save_image(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                                                             "PNG Files (*.png);;JPEG Files (*.jpeg *.jpg);;All Files (*)")
        if file_path:
            self.canvas.pixmap().save(file_path)

    def increase_pen_width(self):
        self.canvas.set_pen_width(self.canvas.pen_width + 5)

    def decrease_pen_width(self):
        self.canvas.set_pen_width(self.canvas.pen_width - 5)

    def change_pen_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_pen_color(color.name())


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
