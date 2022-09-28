from django import forms
opciones_estatus = (("Encontrada", 'Encontrada'),("Perdida", 'Perdida'))
opciones_sexo = (("Macho", 'M'),("Hembra", 'H'))

class registroDeMascotas(forms.Form):
    especie = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    estatus = forms.ChoiceField(choices=opciones_estatus)
    sexo = forms.ChoiceField(choices=opciones_sexo)
    #foto = forms.ImageField(upload_to = 'media/', blank=True)

