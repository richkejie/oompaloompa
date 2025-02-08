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

        self.led_on_button.clicked.connect(lambda: self.set_led_state(True))
        self.led_off_button.clicked.connect(lambda: self.set_led_state(False))

    def set_led_state(self, on: bool):
        if on:
            print("LED turned on")
        else:
            print("LED turned off")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

