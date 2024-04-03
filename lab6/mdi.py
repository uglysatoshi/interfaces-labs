from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from tree_widget import TreeWidget


class MdiChild(QMainWindow):
    def __init__(self):
        super().__init__()

        self.addNodeLineEdit = None
        self.toolbar = None
        self.treeWidget = TreeWidget()
        self.setCentralWidget(self.treeWidget)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.setup_toolbar()

    def setup_toolbar(self):
        self.toolbar = QToolBar("Инструменты")
        self.addToolBar(self.toolbar)

        open_action = QAction('Открыть', self)
        open_action.triggered.connect(self.open_file)
        self.toolbar.addAction(open_action)

        add_node_action = QAction('Добавить узел', self)
        add_node_action.triggered.connect(self.show_add_node_dialog)
        self.toolbar.addAction(add_node_action)

        delete_node_action = QAction('Удалить узел', self)
        delete_node_action.triggered.connect(self.delete_node)
        self.toolbar.addAction(delete_node_action)

        self.addNodeLineEdit = QLineEdit()
        self.toolbar.addWidget(self.addNodeLineEdit)

    def open_file(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Выберите файл с путями")
        if filePath:
            self.treeWidget.clear()
            with open(filePath, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.add_path(line)

    def add_path(self, path):
        parts = path.split()
        currentNode = self.treeWidget.invisibleRootItem()
        for part in parts:
            found = False
            for i in range(currentNode.childCount()):
                child = currentNode.child(i)
                if child.text(0) == part:
                    currentNode = child
                    found = True
                    break
            if not found:
                newNode = QTreeWidgetItem(currentNode)
                newNode.setText(0, part)
                currentNode = newNode

    def show_add_node_dialog(self):
        path = self.addNodeLineEdit.text().strip()
        if path:
            self.add_path(path)
            self.addNodeLineEdit.clear()

    def delete_node(self):
        selectedItems = self.treeWidget.selectedItems()
        if selectedItems:
            for item in selectedItems:
                (item.parent() or self.treeWidget.invisibleRootItem()).removeChild(item)
        else:
            QMessageBox.warning(self, "Удаление узла", "Пожалуйста, выберите узел для удаления.")

