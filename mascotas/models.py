from distutils.command.upload import upload
from django.db import models

class mascota (models.Model):
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    Macho = 'M'
    Hembra = 'H'
    opciones_sexo = [(Macho, 'M'),(Hembra, 'H')]
    sexo = models.CharField(
        max_length=1,
        choices=opciones_sexo,
        default=Hembra)
    foto = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.especie, self.raza

class particularidades (models.Model):
    nombre_mascota = models.CharField(max_length=10)
    señas_particulares = models.CharField(max_length=100)
    Cachorro = 'C'
    Adulto = 'A'
    Viejito = 'V'
    opciones_edad = [(Cachorro, 'C'),(Adulto, 'A'),(Viejito, 'V')]
    edad = models.CharField(
        max_length=1,
        choices=opciones_edad,
        default=None)

    def __str__(self):
        return self.nombre_mascota, self.edad

