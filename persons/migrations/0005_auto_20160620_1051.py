# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20160620_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authority',
            old_name='attach',
            new_name='attachments',
        ),
        migrations.RenameField(
            model_name='commentator',
            old_name='attach',
            new_name='attachments',
        ),
        migrations.RenameField(
            model_name='translator',
            old_name='attach',
            new_name='attachments',
        ),
    ]
