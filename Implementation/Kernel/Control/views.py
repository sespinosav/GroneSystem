from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Control.service import KernelService

import os
import requests

class KernelView(APIView):
    def __init__(self):
        self.service = KernelService()
        self.applicationsUrl = "http://127.0.0.1:8002/api/applications/"
        self.filesManagerUrl = "http://127.0.0.1:8003/api/filesManager/"

    def get(self, request):
        if "cmd" in request.data:
            if request.data["cmd"] == "stop":
                descriptions = [i['description'] for i in requests.get("http://127.0.0.1:8003/api/filesManager/").json()]
                count = 0
                countLog = 0
                countFile = 0
                requests.get(url = self.filesManagerUrl, data = request.data)
                requests.get(url = self.applicationsUrl, data = request.data)

                for i in descriptions:
                    if "GroneApp" in i:
                        count += 1
                    elif "GroneLog" in i:
                        countLog += 1
                    elif "GroneFile" in i:
                        countFile += 1

                os.system(f"cmd /c start /min killGui.bat {count} {countLog} {countFile}")
                os.system("cmd /c start /min killKernel.bat")
        elif request.data["msg"] == "Applications TurOn OK":
            return Response(requests.post(url = self.filesManagerUrl, data = request.data))
        elif request.data["msg"] == "FilesManager TurnOn OK":
            return Response(requests.post(url = self.filesManagerUrl, data = request.data))
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
        return Response({"message" : "GroneSystem HALT"})
    
    def post(self, request):
        if "cmd" in request.data:
            if request.data["cmd"] == "init":
                if request.data["dst"] == "APP":
                    return Response(requests.post(url = self.applicationsUrl, data = request.data))
                elif request.data["dst"] == "FILESMANAGER":
                    return Response(requests.get(url = self.filesManagerUrl, data = request.data))
            elif request.data["cmd"] == "load":
                if request.data["msg"] == "logs":
                    return Response(requests.get("http://127.0.0.1:8003/api/filesManager/").json())
                if request.data["msg"] == "files":
                    return Response(requests.get("http://127.0.0.1:8003/api/filesManager/").json())
            elif request.data["cmd"] == "create":
                    return Response(requests.get(url = self.filesManagerUrl, data = request.data))