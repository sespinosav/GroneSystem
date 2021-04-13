import sys
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDesktopWidget
)

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import requests

from random import randint

import os

class Log(QWidget):
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
        self.setWindowTitle("LOGS")
        self.setLayout(self.layout)

class FileExplorer(QWidget):
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


        a =["melo","caramelo","nice","yes"]
        for i in a:
            self.label = QLabel(i)
            self.label.setStyleSheet(
                                "QLabel"
                                "{"
                                "font-size: 20px;"
                                "}")

            self.layout.addWidget(self.label)
        self.setWindowTitle("FILES")
        self.setLayout(self.layout)

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kernelUrl = "http://127.0.0.1:8001/api/kernel/"

        #Set geometries and titles
        self.setGeometry(0, 0, 900, 900)
        self.setWindowTitle("GRONESYSTEM")

        self.windows = []
        self.count = 0
        self.countLog = 0
        self.countFiles = 0
        
        #set icon
        self.setWindowIcon(QIcon('groneSystem.png'))
        
        #Center APP
        self.center()

        self.setButtons()
    
    def setButtons(self):
        logs = QPushButton("SHOW LOGS", self)
        logs.setGeometry(0, 0, 900, 300)
        logs.clicked.connect(
            self.logsWindow
        )
        logs.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #FA5339;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             "QPushButton"
                             "{"
                             "font-size: 80px;"
                             "}"
                             )

        apps = QPushButton("LAUNCH CALCULATOR", self)
        apps.setGeometry(0, 300, 900, 300)
        apps.clicked.connect(
            self.appsWindow
        )
        apps.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #F294FF;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #39FAE4;"
                             "}"
                             "QPushButton"
                             "{"
                             "font-size: 80px;"
                             "}"
                             )

        folders = QPushButton("FILES EXPLORER", self)
        folders.setGeometry(0, 600, 900, 300)
        folders.clicked.connect(
           self.filesWindow
        )
        folders.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #F1F593;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #FF565D;"
                             "}"
                             "QPushButton"
                             "{"
                             "font-size: 80px;"
                             "}"
                             )

    def filesWindow(self):
        self.countFiles += 1
        requests.post(self.kernelUrl, {"cmd":"init", "src":"GUI", "dst":"APP", "msg":f"GroneFile{self.countFiles}"})
        os.system(f"cmd /c start /min initFiles.bat {self.countFiles}")

    def logsWindow(self):
        self.countLog += 1
        requests.post(self.kernelUrl, {"cmd":"init", "src":"GUI", "dst":"APP", "msg":f"GroneLog{self.countLog}"})
        os.system(f"cmd /c start /min initLog.bat {self.countLog}")

    def appsWindow(self):
        self.count += 1
        requests.post(self.kernelUrl, {"cmd":"init", "src":"GUI", "dst":"APP", "msg":f"GroneApp{self.count}"})
        os.system(f"cmd /c start /min initApp.bat {self.count}")


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()