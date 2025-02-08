from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PyQt5 import uic

import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_window.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

