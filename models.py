from django.db import models
from mascotas.models import mascota

class registrar (models.Model):
    ##estas son para víncular las bd, pero aún no sé como lograrlo, si se descomentan no hace las migraciones##
    #idmascot = mascota.especie 
    #idpet = ([idmascot,"mascota.especie"])
    #pet = models.CharField(max_length=20 ,choices=idmascot)
    encontrador = models.CharField(max_length=20)
    fecha_encontrado = models.DateField()
    email = models.EmailField()
    lugar_encontrado = models.CharField(max_length=50)

    def __str__(self):
        return self.mascot, self.encontrador, self.email