# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20160527_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='attach',
            field=models.FileField(blank=True, upload_to='persons/%Y-%m-%d'),
        ),
        migrations.AddField(
            model_name='commentator',
            name='attach',
            field=models.FileField(blank=True, upload_to='persons/%Y-%m-%d'),
        ),
        migrations.AddField(
            model_name='translator',
            name='attach',
            field=models.FileField(blank=True, upload_to='persons/%Y-%m-%d'),
        ),
    ]