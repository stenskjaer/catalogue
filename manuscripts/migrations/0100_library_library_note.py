# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0099_manuscriptorigin_dubious'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='library_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]