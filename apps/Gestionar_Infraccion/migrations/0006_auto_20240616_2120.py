# Generated by Django 2.2.4 on 2024-06-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Infraccion', '0005_delete_intentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraccion_transito',
            name='NumeroInfraccion',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
