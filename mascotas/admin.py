from django.contrib import admin
from .models import *
from registrar_mascotas.models import *

# Register your models here.
admin.site.register(mascota)
admin.site.register(particularidades)
admin.site.register(registrar)