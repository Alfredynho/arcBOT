# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-16 01:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replacement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='description',
            field=models.TextField(blank=True, help_text='Cantidad maxima de caracteres 120', null=True, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(120)], verbose_name='Descripcion'),
        ),
    ]
