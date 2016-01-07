# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0073_auto_20160106_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authority',
            options={'verbose_name_plural': 'Authorities'},
        ),
        migrations.AlterModelOptions(
            name='authoritytext',
            options={'ordering': ['author']},
        ),
        migrations.AlterModelOptions(
            name='commentary',
            options={'ordering': ['commentator', 'modified'], 'verbose_name': 'Commentary', 'verbose_name_plural': 'Commentaries'},
        ),
        migrations.AlterModelOptions(
            name='commentator',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'ordering': ['library_name'], 'verbose_name_plural': 'Libraries'},
        ),
        migrations.AlterModelOptions(
            name='translator',
            options={'ordering': ['name']},
        ),
    ]
