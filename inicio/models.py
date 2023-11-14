from django.db import models

# Create your models here.

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'