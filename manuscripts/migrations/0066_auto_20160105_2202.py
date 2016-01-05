# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0065_auto_20160105_2132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Authority',
        ),
        migrations.AlterField(
            model_name='manuscriptcontent',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Commentary'),
        ),
    ]
