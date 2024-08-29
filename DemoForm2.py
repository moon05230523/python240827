# DemoForm2.py
# DeomoForm2.ui + DemoForm2.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from_class = uic.loadUiType("DemoForm2.ui")[0]

class DemoForm(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def firstClick(self):
        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()