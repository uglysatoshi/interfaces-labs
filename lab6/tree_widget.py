from PyQt6.QtWidgets import *


class TreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabel('Пути')
        self.itemClicked.connect(self.update_status_bar_on_click)

    def update_status_bar_on_click(self, item):
        full_path = []
        while item:
            full_path.append(item.text(0))
            item = item.parent()
        self.window().statusBar().showMessage(" -> ".join(reversed(full_path)))
