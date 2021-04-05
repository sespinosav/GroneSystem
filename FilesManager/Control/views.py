from .models import Register
from .serializers import RegisterSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .service import FilesManagerService

import requests

class FilesManagerView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        if "cmd" in request.data:
            if request.data["cmd"] == "stop":
                service = FilesManagerService()
                requests.delete(url = "http://127.0.0.1:8003/api/filesManager/")
                service.turnOff()
            elif request.data["cmd"] == "send":
                requests.post(url = "http://127.0.0.1:8003/api/filesManager/", data = {"title":"log", "description": "register of log type",
                "body":request.data["msg"].strip(":")[1],"state": "allow"})
        if 'pk' not in kwargs:
            return self.list(request, *args, *kwargs)           
        registration = Register.objects.get(pk=kwargs['pk'])
        serializer = RegisterSerializer(registration)
        return Response({"registration" : serializer.data})

    def post(self, request, *args, **kwargs):
        if "msg" in request.data:
            if request.data["msg"] == "Applications TurOn OK":
                requests.post(url = "http://127.0.0.1:8003/api/filesManager/", data = {"title":"Applications ON", "description": "Applications Modules is on",
                "body":"Now you can use module applications for create applications","state": "allow"})
                return Response({"msg":"ok"})
            elif request.data["msg"] == "FilesManager TurnOn OK":
                requests.post(url = "http://127.0.0.1:8003/api/filesManager/", data = {"title":"FilesManager ON", "description": "FilesManager Modules is on",
                "body":"Now you can use FilesManager module for create applications","state": "allow"})
                return Response({"msg":"ok"})
        elif request.data['title'] == "Applications ON":
            service = FilesManagerService()
            service.sendOkInit()
            return self.create(request, *args, **kwargs)
        elif request.data['title'] == "FilesManager ON":
            return self.create(request, *args, **kwargs)
        if "cmd" in request.data:
            return self.create(request, *args, **kwargs)

    def delete(self, request, pk=None):
        if pk==None:
            Register.objects.all().delete()
            return Response({"msg" : "All files deleted"})
        registration = get_object_or_404(self.queryset, pk=pk)
        registration.delete()
        return Response({"message": f"Register with id {pk} has been deleted."},status=204)
