# Generated by Django 5.1.3 on 2024-11-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarjetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcatarjeta',
            name='nombre',
            field=models.CharField(choices=[('VISA', 'VISA'), ('MASTERCARD', 'MASTERCARD')], max_length=50),
        ),
    ]
