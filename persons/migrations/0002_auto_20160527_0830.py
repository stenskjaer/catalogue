# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='viaf_id',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commentator',
            name='viaf_id',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translator',
            name='viaf_id',
            field=models.URLField(blank=True, null=True),
        ),
    ]
