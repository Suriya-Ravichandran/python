import sys
from PyQt5.QtWidgets import QApplication, Qwidgets, QPushButton, QMessageBox

class MyApp(Qwidgets):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setW