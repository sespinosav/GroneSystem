from django.urls import path

from .views import FilesManagerView
from Control.service import FilesManagerService

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('filesManager/', FilesManagerView.as_view(), name='API FilesManager'),
    path('filesManager/<int:pk>', FilesManagerView.as_view(), name='API FilesManager'),
]