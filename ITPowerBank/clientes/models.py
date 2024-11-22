from django.db import models
from django.contrib.auth.models import User  # Modelo de usuario

# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación 1 a 1 con User
    nombre = models.CharField(max_length=100)  # Campo para el nombre del cliente
    apellido = models.CharField(max_length=100)  # Campo para el apellido del cliente
    dni = models.CharField(max_length=20, unique=True)  # Documento único
    direccion = models.TextField(blank=True)  # Dirección opcional

    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Representación en texto del cliente
