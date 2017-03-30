# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=180, null=True, verbose_name='Pregunta')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
        migrations.AddField(
            model_name='assistant',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant.Category', verbose_name='Categoria'),
        ),
    ]
