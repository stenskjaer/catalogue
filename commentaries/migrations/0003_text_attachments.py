# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 06:41
from __future__ import unicode_literals

import commentaries.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentaries', '0002_auto_20160620_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='attachments',
            field=models.FileField(blank=True, upload_to=commentaries.models.attachment_id_path),
        ),
    ]