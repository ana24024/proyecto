import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def _init_(self):
        super()._init_()
        uic.loadUi("proyecto.ui", self)

if _name_ == '_main_':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI
    GUI.show()
    sys.exit(app.exec_())
