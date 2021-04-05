from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Control.service import KernelService

import os
import requests

class KernelView(APIView):
    def __init__(self):
        self.service = KernelService()
        self.appilcationsUrl = "http://127.0.0.1:8002/api/applications/"
        self.filesManagerUrl = "http://127.0.0.1:8003/api/filesManager/"

    def get(self, request):
        if "cmd" in request.data:
            if request.data["cmd"] == "stop":
                requests.get(url = self.filesManagerUrl, data = request.data)
                requests.get(url = self.appilcationsUrl, data = request.data)

                os.system("cmd /c start /min killGui.bat")
                os.system("cmd /c start /min killKernel.bat")

        elif request.data["msg"] == "Applications TurOn OK":
            requests.post(url = self.filesManagerUrl, data = request.data)
        elif request.data["msg"] == "FilesManager TurnOn OK":
            requests.post(url = self.filesManagerUrl, data = request.data)
        else:
            #send string, info, stop
            titles = [i['title'] for i in requests.get("http://127.0.0.1:8003/api/filesManager/").json()]
            if 'FilesManager ON' in titles and 'Applications ON' in titles:
                if request.data["msg"] == "OK":
                    print("OK")
                elif request.data["msg"] == "0":
                    print("WAIT")
                elif request.data["msg"] == "Err":
                    print("ERROR")
                return Response({"msg" : "TAMOS MELOS"})
            else:
                self.service.turnOff()
        return Response({"message" : "AAAA "})