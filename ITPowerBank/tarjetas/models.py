from django.db import models
from clientes.models import Cliente
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Tarjeta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=16, unique=True)
    cvv = models.CharField(max_length=3)
    fecha_venc= models.DateField(default= timezone.now() + timedelta(days=365) )
    fecha_emicion = models.DateField(default=timezone.now)
    marca = models.CharField(max_length=50, choices=[('VISA', 'Visa'), ('MASTERCARD', 'MasterCard')])
    tipo = models.CharField(max_length=10, choices=[("DEBITO", "Debito"), ("CREDITO", "Credito")])

    class Meta:
        db_table = 'tarjeta'

    def __str__(self):
        return f"Tarjeta Cliente: {self.cliente} {self.numero} ({self.tipo})"