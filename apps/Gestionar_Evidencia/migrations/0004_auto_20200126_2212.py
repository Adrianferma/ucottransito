# Generated by Django 2.2.4 on 2020-01-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Evidencia', '0003_auto_20200126_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myimage',
            name='id_Evidencia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='myimage',
            name='model_pic',
            field=models.FileField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
