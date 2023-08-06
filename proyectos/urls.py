from django.urls import path
from proyectos.views import proyectos

urlpatterns = [
    path('',proyectos, name="proyectos"),
]
