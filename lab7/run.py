import sys

from PyQt6.QtCore import QDataStream, QIODevice, QByteArray, Qt
from PyQt6.QtGui import QAction, QStandardItem, QStandardItemModel, QDrag
from PyQt6.QtWidgets import *

class TreeWidget(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

    def mimeData(self, indexes):
        mime_data = super().mimeData(indexes)
        encoded_data = QByteArray()
        stream = QDataStream(encoded_data, QIODevice.WriteOnly)

        for index in indexes:
            self.write_item_to_stream(self.model.itemFromIndex(index), stream)

        mime_data.setData('application/x-qabstractitemmodeldatalist', encoded_data)
        return mime_data

    def dropMimeData(self, data, action, row, column, parent):
        if not data.hasFormat('application/x-qabstractitemmodeldatalist'):
            return False

        encoded_data = data.data('application/x-qabstractitemmodeldatalist')
        stream = QDataStream(encoded_data, QIODevice.ReadOnly)

        while not stream.atEnd():
            row = stream.readInt32()
            column = stream.readInt32()
            map_items = stream.readInt32()

            parent_item = self.model.itemFromIndex(parent)
            for _ in range(map_items):
                key = stream.readInt32()
                value = stream.readQVariant()

                if row == 0 and column == 0:
                    item = self.read_item_from_stream(stream)
                    parent_item.insertRow(row, item)

        return True

    def write_item_to_stream(self, item, stream):
        stream.writeInt32(0)
        stream.writeInt32(0)
        stream.writeInt32(1)
        stream.writeInt32(0)
        stream.writeQVariant(item.text())

        child_count = item.rowCount()
        stream.writeInt32(child_count)

        for i in range(child_count):
            self.write_item_to_stream(item.child(i), stream)

    def read_item_from_stream(self, stream):
        text = stream.readQVariant()
        item = QStandardItem(text)

        child_count = stream.readInt32()

        for _ in range(child_count):
            child_item = self.read_item_from_stream(stream)
            item.appendRow(child_item)

        return item


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree Widget App")
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        self.create_actions()
        self.create_menus()
        self.status_label = QLabel()
        self.statusBar().addWidget(self.status_label)

    def create_actions(self):
        self.load_action = QAction("Load File", self)
        self.load_action.triggered.connect(self.load_file)

        self.new_window_action = QAction("New Window", self)
        self.new_window_action.triggered.connect(self.new_window)

        self.add_item_action = QAction("Add Item", self)
        self.add_item_action.triggered.connect(self.add_item)

    def create_menus(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(self.load_action)
        file_menu.addAction(self.new_window_action)
        file_menu.addAction(self.add_item_action)

    def new_window(self):
        mdi_child = QMdiSubWindow()
        tree_widget = TreeWidget()
        mdi_child.setWidget(tree_widget)
        self.mdi_area.addSubWindow(mdi_child)
        mdi_child.show()

    def add_item(self):
        active_sub_window = self.mdi_area.activeSubWindow()
        if active_sub_window:
            tree_widget = active_sub_window.widget()
            item, ok = QInputDialog.getText(self, "Add Item", "Enter item text:")
            if ok and item:
                root_item = tree_widget.model.invisibleRootItem()
                root_item.appendRow(QStandardItem(item))

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                mdi_child = QMdiSubWindow()
                tree_widget = TreeWidget()
                for line in lines:
                    items = line.strip().split()
                    parent = tree_widget.model.invisibleRootItem()
                    for item in items:
                        parent.appendRow(QStandardItem(item))
                        parent = parent.child(parent.rowCount() - 1)

                mdi_child.setWidget(tree_widget)
                self.mdi_area.addSubWindow(mdi_child)
                mdi_child.show()

    def update_status_bar(self, tree_widget):
        leaf_count = 0
        current_item = tree_widget.currentIndex()
        full_path = []
        while current_item.isValid():
            full_path.insert(0, current_item.data())
            if not current_item.child(0).isValid():
                leaf_count += 1
            current_item = current_item.parent()

        self.status_label.setText(f"Leaf Count: {leaf_count} | Path: {' > '.join(full_path)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())