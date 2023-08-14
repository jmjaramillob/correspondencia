# Generated by Django 3.2.16 on 2022-11-21 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0002_alter_correspondencia_almacenado_az'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha_envio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha_recibido',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]