from django.db import models

class registrar (models.Model):
    id_mascota = models.CharField(max_length=5, blank=True) 
    encontrador = models.CharField(max_length=20)
    fecha_encontrado = models.DateField()
    email = models.EmailField()
    lugar_encontrado = models.CharField(max_length=50)

    def __str__(self):
        return self.id_mascota, self.encontrador, self.email