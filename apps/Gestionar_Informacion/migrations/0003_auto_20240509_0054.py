# Generated by Django 2.2.4 on 2024-05-09 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Informacion', '0002_remove_conductor_puntos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conductor',
            name='FechaCaducidadLicencia',
        ),
        migrations.RemoveField(
            model_name='conductor',
            name='FechaEmisionLicencia',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='FechaCaducidadMatricula',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='FechaMatricula',
        ),
    ]