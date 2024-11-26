from django.db import models
from clientes.models import Cliente
from django.utils import timezone
from django.utils import timezone 
# Create your models here.


class Prestamos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=[("HIPOTECARIO", 'HIPOTECARIO'), ("PRENDARIO", 'PRENDARIO'), ("PERSONAL", 'PERSONAL')])
    fecha = models.DateField(default=timezone.now)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.CharField(max_length=10, default='Pendiente')
    aprobado = models.BooleanField(default=False)


    class Meta:
        db_table= "prestamo"


    def __str__(self):
        return f'Prestamos para el cliente {self.cliente} por un monto de ${self.monto}'