# Generated by Django 5.1.3 on 2024-11-25 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarjetas', '0002_alter_marcatarjeta_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarjeta',
            old_name='cliente_id',
            new_name='cliente',
        ),
    ]
