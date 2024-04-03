from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from mdi import MdiChild


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MDI Приложение QTreeWidget")
        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)

        self.setup_menu()

    def setup_menu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Файл')

        newAction = QAction('&Новое окно', self)
        newAction.triggered.connect(self.new_mdi_child)
        fileMenu.addAction(newAction)

    def new_mdi_child(self):
        mdiChild = MdiChild()
        subWindow = QMdiSubWindow()
        subWindow.setWidget(mdiChild)
        subWindow.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(subWindow)
        mdiChild.show()
