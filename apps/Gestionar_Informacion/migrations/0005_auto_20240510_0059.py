# Generated by Django 2.2.4 on 2024-05-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Informacion', '0004_auto_20240510_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='CedulaC',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='Placa',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
