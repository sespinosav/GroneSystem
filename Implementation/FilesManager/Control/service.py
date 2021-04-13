# importing the requests library
import requests
import os

class FilesManagerService():

    def __init__(self):
        self.kernelUrl = "http://127.0.0.1:8001/api/kernel/"

    def sendOkInit(self):      
        # sending get request and saving the response as response object
        requests.get(url = self.kernelUrl, data = {"codterm":0, "msg": "FilesManager TurnOn OK"})
    
    def turnOff(self):
        os.system("cmd /c start /min ..\Kernel\killFilesManager.bat")