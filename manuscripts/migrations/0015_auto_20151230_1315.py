# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0014_auto_20151230_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Country')),
                ('town', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, related_name='archive_town', show_all=True, to='manuscripts.Town')),
            ],
        ),
        migrations.RemoveField(
            model_name='manuscript',
            name='reproduction',
        ),
        migrations.AddField(
            model_name='manuscript',
            name='reproduction',
            field=models.ManyToManyField(blank=True, to='manuscripts.Reproductions'),
        ),
        migrations.AlterField(
            model_name='reproductions',
            name='archive',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Archive'),
        ),
    ]
