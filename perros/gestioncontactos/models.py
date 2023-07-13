from django.db import models

class Contactos(models.Model):
    apellido=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    sexo=models.CharField(max_length=1)
    dni=models.IntegerField()
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField()
    tienemascota=models.BooleanField()