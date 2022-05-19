from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    carga = models.DateField()
    edad = models.IntegerField()

    def __str__(self):
      return "El nombre es %s tiene %s años y fue cargado la fecha %s" % (self.nombre, self.edad, self.carga)