# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20160527_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authority',
            old_name='viaf_id',
            new_name='viaf_url',
        ),
        migrations.RenameField(
            model_name='commentator',
            old_name='viaf_id',
            new_name='viaf_url',
        ),
        migrations.RenameField(
            model_name='translator',
            old_name='viaf_id',
            new_name='viaf_url',
        ),
    ]