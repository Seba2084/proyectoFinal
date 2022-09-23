from django.shortcuts import render

def buscar_mascotas(request):
    return render (request, "buscar_mascotas.html")
