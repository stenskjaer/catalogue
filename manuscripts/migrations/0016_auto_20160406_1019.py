# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0015_auto_20160406_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reproduction',
            name='archive',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='repositories.Archive'),
        ),
    ]
