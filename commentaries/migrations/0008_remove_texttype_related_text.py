# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentaries', '0007_auto_20160415_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texttype',
            name='related_text',
        ),
    ]
