# Generated by Django 2.2.4 on 2024-07-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Infraccion', '0011_auto_20240707_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos_coip',
            name='Articulo',
            field=models.TextField(),
        ),
    ]