# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-09 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='library_short_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
