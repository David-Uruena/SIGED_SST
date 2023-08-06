from django.urls import path
from listachequeo.views import listachequeo

urlpatterns = [
    path('',listachequeo, name="listachequeo"),
]
