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

        self.setGeometry(1500, 100, 300, 15)

        #set icon
        self.setWindowIcon(QIcon('files.png'))

        # creating a label
        self.file = QLabel(self)

        # setting alignment to the label
        self.file.setAlignment(Qt.AlignRight)

        # creating label multi line
        self.file.setWordWrap(True)

        # adding number button to the screen
        push1 = QPushButton("1", self)
        push1.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #F1F593;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #FF565D;"
                                "}"
                                "QPushButton"
                                "{"
                                "font-size: 20px;"
                                "}"
                            )

        # creating a push button
        push2 = QPushButton("2", self)
        push2.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #F1F593;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #FF565D;"
                                "}"
                                "QPushButton"
                                "{"
                                "font-size: 20px;"
                                "}"
                                )

        # creating a push button
        push3 = QPushButton("3", self)
        push3.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #F1F593;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #FF565D;"
                                "}"
                                "QPushButton"
                                "{"
                                "font-size: 20px;"
                                "}"
                                )

        push4 = QPushButton("-", self)
        push4.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #F1F593;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #FF565D;"
                                "}"
                                "QPushButton"
                                "{"
                                "font-size: 20px;"
                                "}"
                                )

        # setting style sheet to the label
        self.file.setStyleSheet("QLabel"
                                "{"
                                "border : 4px solid black;"
                                "background : #FF565D;"
                                "}"
                                )

        create = QPushButton("CREATE FOLDER", self)
        create.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #F1F593;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #FF565D;"
                                "}"
                                "QPushButton"
                                "{"
                                "font-size: 30px;"
                                "}"
                                )

        delete = QPushButton("DELETE FOLDER", self)
        delete.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #F1F593;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #FF565D;"
                                "}"
                                "QPushButton"
                                "{"
                                "font-size: 30px;"
                                "}"
                                )

        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        create.clicked.connect(self.create)
        delete.clicked.connect(self.delete)
        
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.file)
        self.layout.addWidget(push1)
        self.layout.addWidget(push2)
        self.layout.addWidget(push3)
        self.layout.addWidget(push4)
        self.layout.addWidget(QLabel(""))
        self.layout.addWidget(create)
        self.layout.addWidget(delete)
        self.layout.addWidget(QLabel(""))

        self.kernelUrl = "http://127.0.0.1:8001/api/kernel/"

        data = requests.post(self.kernelUrl, {"cmd":"load", "src":"GUI", "dst":"FILESMANAGER", "msg":"files"}).json()

        print(data)

        description = [i['description'] for i in data]

        folders = []

        for i in description:
            if "create" in i:
                folders.append(i.split(" ")[1])

        for i in folders:
            self.label = QLabel(i)
            self.label.setStyleSheet(
                                "QLabel"
                                "{"
                                "font-size: 20px;"
                                "}")

            self.layout.addWidget(self.label)
        self.setWindowTitle(f"FILES {sys.argv[1]}")
        self.setLayout(self.layout)
        self.show()

    def action1(self):
        text = self.file.text()
        self.file.setText(text + "1")

    def action2(self):
        text = self.file.text()
        self.file.setText(text + "2")

    def action3(self):
        text = self.file.text()
        self.file.setText(text + "3")

    def action4(self):
        text = self.file.text()
        self.file.setText(text + "-")

    def create(self):
        requests.post(self.kernelUrl, {"cmd":"create", "src":"GUI", "dst":"FILESMANAGER", "msg":f"{self.file.text()}"})
        text = self.file.text()
    
    def delete(self):
        text = self.file.text()
        self.file.setText(text + "delete")


if __name__ == "__main__":
	# create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())
