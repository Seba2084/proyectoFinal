from django.shortcuts import render

def registrar_mascotas(request):
    return render (request, "registrar_mascotas.html")
