# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0041_remove_manuscript_catalogue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manuscript',
            name='reproductions',
        ),
        migrations.AddField(
            model_name='reproduction',
            name='manuscript',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Manuscript'),
            preserve_default=False,
        ),
    ]
