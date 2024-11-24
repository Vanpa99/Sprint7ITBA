from django.db import models

# Create your models here.
class Movimiento(models.Model):
    numero_cuenta = models.IntegerField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    tipo_operacion = models.CharField(max_length=50)
    hora = models.DateTimeField


    class Meta:
        db_table = "movimientos"


    def __str__(self):
        return f"Movimiento {self.numero_cuenta} - Monto: {self.monto}"
