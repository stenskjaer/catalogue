# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0058_auto_20160105_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_role',
            field=models.IntegerField(blank=True, choices=[(1, 'Commentator'), (2, 'Authority'), (3, 'Translator')], default=1, null=True),
        ),
    ]