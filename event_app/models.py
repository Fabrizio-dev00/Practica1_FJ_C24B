from django.db import models

# Create your models here.
class Eventos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.IntegerField()
    lugar = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title