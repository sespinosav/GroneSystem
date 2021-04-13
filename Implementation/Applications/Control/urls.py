from django.urls import path

from .views import ApplicationsView
from Control.service import ApplicationsService

app_name = "applications"

#Send ok intialization to kernel
service = ApplicationsService()
service.sendOkInit()

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('applications/', ApplicationsView.as_view(), name='API APPLICATIONS'),
]