# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0024_auto_20151230_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='library_country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='library',
            name='library_town',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='library_country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, related_name='library_town', show_all=True, to='manuscripts.Town'),
        ),
    ]
