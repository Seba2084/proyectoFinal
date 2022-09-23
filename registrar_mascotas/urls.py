from django.urls import path
from registrar_mascotas.views import *

urlpatterns = [
    path('', registrar_mascotas),
]