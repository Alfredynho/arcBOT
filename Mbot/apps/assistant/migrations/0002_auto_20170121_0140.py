# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 05:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assistant',
            options={'verbose_name': 'Asistencia del BOT', 'verbose_name_plural': 'Asistencias del BOT'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Tipo de Categoria', 'verbose_name_plural': 'Tipo de Categorias'},
        ),
    ]