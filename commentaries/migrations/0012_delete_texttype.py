# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentaries', '0011_auto_20160415_2216'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TextType',
        ),
    ]
