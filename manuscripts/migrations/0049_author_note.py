# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0048_auto_20160102_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
