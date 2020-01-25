# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-19 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.TextField(verbose_name=b'content')),
                ('month', models.TextField(verbose_name=b'content')),
                ('temperature', models.FloatField(verbose_name=b'temperature')),
                ('precipitaton', models.FloatField(verbose_name=b'precipitation')),
            ],
        ),
    ]
