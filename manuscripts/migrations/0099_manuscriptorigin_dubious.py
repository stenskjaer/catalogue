# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0098_auto_20160205_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscriptorigin',
            name='dubious',
            field=models.BooleanField(default=False),
        ),
    ]