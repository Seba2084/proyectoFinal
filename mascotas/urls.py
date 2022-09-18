from django.urls import path
from mascotas.views import *

urlpatterns = [
    path('', buscar_mascotas),
]