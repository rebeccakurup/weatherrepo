# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-19 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tpapp', '0004_auto_20200119_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appdata',
            old_name='precipitaton',
            new_name='precipitation',
        ),
    ]
