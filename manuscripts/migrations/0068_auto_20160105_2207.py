# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0067_translator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='translator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='manuscripts.Translator'),
        ),
    ]