# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint

import sys

import os

import requests

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.kernelUrl = "http://127.0.0.1:8001/api/kernel/"

        self.setGeometry(100, 700, 300, 15)

        self.setWindowIcon(QIcon('register.jpg'))

        self.layout = QVBoxLayout()

        data = requests.post(self.kernelUrl, {"cmd":"load", "src":"GUI", "dst":"FILESMANAGER", "msg":"logs"}).json()

        body = [i['body'] for i in data]

        logs = []

        for i in body:
            if "2021" in i:
                logs.append(i)
        
        print(logs)

        
        for i in logs:
            self.label = QLabel(i)
            self.label.setStyleSheet("QLabel"
                             "{"
                             "color : #FA5339;"
                             "}"
                             "QLabel"
                             "{"
                             "font-size: 30px;"
                             "}")
            self.layout.addWidget(self.label)
        self.setWindowTitle(f"LOGS {sys.argv[1]}")
        # showing all the widgets
        self.setLayout(self.layout)
        self.show()


if __name__ == "__main__":
	# create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())
