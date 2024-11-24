from django.db import models
from clientes.models import Cliente
# Create your models here.

class Marcatarjeta(models.Model):
    nombre = models.CharField(max_length=50)


class Tarjeta(models.Model):
    numero = models.CharField(max_length=16, unique=True)
    cvv = models.CharField(max_length=3)
    fecha_venc= models.DateField()
    fecha_emicion = models.DateField()
    marca = models.ForeignKey(Marcatarjeta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[("Debito", "Debito"), ("Credito", "Credito")])

    class Meta:
        db_table = 'tarjeta'

    def __str__(self):
        return f"Tarjeta {self.numero} ({self.tipo})"