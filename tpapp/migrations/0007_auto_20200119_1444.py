# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-19 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpapp', '0006_auto_20200119_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdata',
            name='month',
            field=models.IntegerField(verbose_name=b'month'),
        ),
        migrations.AlterField(
            model_name='appdata',
            name='year',
            field=models.IntegerField(verbose_name=b'year'),
        ),
    ]
