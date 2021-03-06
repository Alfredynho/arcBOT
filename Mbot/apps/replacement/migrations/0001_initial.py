# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 23:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_code', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Codigo Repuesto')),
                ('description', models.TextField(blank=True, help_text='Cantidad maxima de caracteres 120', null=True, validators=[django.core.validators.MaxValueValidator(120)], verbose_name='Descripcion')),
                ('stock', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Cantidad')),
                ('brand', models.CharField(blank=True, default='USM', max_length=100, null=True, verbose_name='Marca')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Precio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagenes/repuestos/%Y/%m/%d', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Repuesto',
                'verbose_name_plural': 'Repuestos',
            },
        ),
    ]
