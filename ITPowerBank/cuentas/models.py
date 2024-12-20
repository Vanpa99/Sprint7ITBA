from django.db import models
from clientes.models import Cliente

class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=50, choices=[('Cuenta corriente en Dolares', 'Cuenta corriente en Dolares'), ('Cuenta corriente en Pesos', 'Cuenta corriente en Pesos'), ('Cuenta Ahorro en Dolares', 'Cuenta Ahorro en Dolares'), ('Cuenta Ahorro Pesos', 'Cuenta Ahorro en Pesos')])

    class Meta:
        db_table = 'tipo_cuenta'

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con el cliente
    saldo = models.DecimalField(max_digits=15, decimal_places=2)  # Saldo de la cuenta
    numero = models.CharField(max_length=30, unique=True)  # Número único de cuenta
    tipo = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)  # Relación con tipo de cuenta

    class Meta:
        db_table = 'cuenta'

    def __str__(self):
        return f"Cuenta de {self.cliente} - Número: {self.numero} - Saldo: {self.saldo}"
