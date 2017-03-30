# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre Promocion')),
                ('descripcion', models.TextField(blank=True, help_text='Maximo de caracteres 126', null=True, verbose_name='Descripcion')),
                ('fechas_promocion', models.TextField(blank=True, help_text='Maximo de caracteres 90', null=True, verbose_name='Tiempo de la promocion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/promociones/%Y/%m/%d', verbose_name='Imagen')),
            ],
            options={
                'verbose_name_plural': 'Promociones',
                'verbose_name': 'Promocion',
            },
        ),
    ]