# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-19 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdata',
            name='month',
            field=models.TextField(verbose_name=b'month'),
        ),
        migrations.AlterField(
            model_name='appdata',
            name='year',
            field=models.TextField(verbose_name=b'year'),
        ),
    ]
