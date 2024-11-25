from django.db import models
from clientes.models import Cliente
from django.utils import timezone
# Create your models here.

class Tipo_prestamos(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "tipo_prestamos"


class Prestamos(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_prestamos, on_delete=models.CASCADE)
    fecha =models.DateTimeField(default=timezone.now)
    monto = models.DecimalField(max_digits=15, decimal_places=2)


    class Meta:
        db_table= "prestamos"


    def __str__(self):
        return f'Prestamos para el cliente ${self.cliente_id} por un monto de ${self.monto}'