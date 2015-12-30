# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0038_auto_20151230_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManuscriptInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspector', models.CharField(max_length=255)),
                ('inspection_type', models.CharField(choices=[('digital', 'Digital reproduction'), ('situ', 'In situ')], max_length=10)),
                ('inspection_date', models.DateField()),
                ('manuscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Manuscript')),
            ],
        ),
    ]
