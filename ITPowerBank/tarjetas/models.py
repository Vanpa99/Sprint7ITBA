from django.db import models
from clientes.models import Cliente
from django.utils import timezone

# Create your models here.

class Marcatarjeta(models.Model):
    nombre = models.CharField(max_length=50)


class Tarjeta(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=16, unique=True)
    cvv = models.CharField(max_length=3)
    fecha_venc= models.DateField(default=timezone.now)
    fecha_emicion = models.DateField(default=timezone.now)
    marca = models.ForeignKey(Marcatarjeta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[("Debito", "Debito"), ("Credito", "Credito")])

    class Meta:
        db_table = 'tarjeta'

    def __str__(self):
        return f"Tarjeta {self.numero} ({self.tipo})"