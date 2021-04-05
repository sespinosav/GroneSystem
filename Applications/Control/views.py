from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .service import ApplicationsService

class ApplicationsView(APIView):

    def get(self, request):
        if request.data["cmd"] == "stop":
            service = ApplicationsService()
            service.turnOff()

        return Response({"message" : "get method allow "})

    def post(self, request):
        return Response({"message" : "post method allow", "data_post" : f'{request.data["message"]}'})