# Generated by Django 5.1.3 on 2024-11-25 00:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo_prestamos',
            },
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.tipo_prestamos')),
            ],
            options={
                'db_table': 'prestamos',
            },
        ),
    ]