from django.urls import path

from .views import KernelView
import os

app_name = "kernel"
os.system("cmd /c start /min initGui.bat")


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('kernel/', KernelView.as_view(), name='API KERNEL'),
]