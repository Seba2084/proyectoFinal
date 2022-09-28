from django.shortcuts import render
from registrar_mascotas.forms import *
from mascotas.models import *

opciones_estatus = (("Encontrada", 'Encontrada'),("Perdida", 'Perdida'))
opciones_sexo = (("Macho", 'M'),("Hembra", 'H'))

def registrar_mascotas(request):
    if request.method == "POST":
        form = registroDeMascotas(request.POST)
        if form.is_valid():
            mascota = form.cleaned_data
            mascota = mascota( especie = mascota['especie'],raza = mascota['raza'],color = mascota['color'], estatus = mascota[forms.ChoiceField(choices=opciones_estatus, widget=forms.RadioSelect)],sexo = mascota[forms.ChoiceField(choices=opciones_sexo, widget=forms.RadioSelect)])
            mascota.save()
            return render(request, "registrar_mascotas.html")
    else:
        form = registroDeMascotas()
    return render(request, "registrar_mascotas.html", {"form": form})
