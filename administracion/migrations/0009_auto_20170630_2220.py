# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_auto_20170630_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='experienciaLaboral',
        ),
        migrations.AddField(
            model_name='experiencialaboral',
            name='alumno',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='administracion.Alumno'),
        ),
    ]