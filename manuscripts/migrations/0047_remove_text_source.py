# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0046_author_floruit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='source',
        ),
    ]