# Generated by Django 5.1.3 on 2024-11-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocuenta',
            name='nombre',
            field=models.CharField(choices=[('Cuenta corriente en Dolares', 'Cuenta corriente en Dolares'), ('Cuenta corriente en Pesos', 'Cuenta corriente en Pesos'), ('Cuenta Ahorro en Dolares', 'Cuenta Ahorro en Dolares'), ('Cuenta Ahorro Pesos', 'Cuenta Ahorro en Pesos')], max_length=50),
        ),
    ]
