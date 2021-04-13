from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .service import ApplicationsService

import requests

class ApplicationsView(APIView):

    def get(self, request):
        if request.data["cmd"] == "stop":
            service = ApplicationsService()
            service.turnOff()

        return Response({"message" : "get method allow "})

    def post(self, request):
        if "cmd" in request.data:
            if request.data["cmd"] == "init":
                return Response(requests.post("http://127.0.0.1:8001/api/kernel/", {"cmd":"init", "src":"APP", "dst":"FILESMANAGER", "msg":request.data["msg"]}))