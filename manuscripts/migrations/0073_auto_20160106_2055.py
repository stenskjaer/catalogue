# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 19:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0072_auto_20160106_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 54, 59, 42226, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='archive',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 2, 766036, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authority',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 3, 922161, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authority',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 5, 71795, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basetext',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 6, 216166, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basetext',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 7, 368053, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentarytype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 8, 639978, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentarytype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 9, 968317, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentator',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 11, 7443, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentator',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 12, 103899, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 13, 239781, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 14, 535829, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 16, 671760, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 18, 191342, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manuscript',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 19, 695067, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manuscript',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 21, 79245, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manuscriptcontent',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 22, 535343, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manuscriptcontent',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 24, 471381, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manuscriptinspection',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 25, 966849, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manuscriptinspection',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 27, 342599, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinematerial',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 28, 710742, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinematerial',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 30, 110669, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reproduction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 33, 838951, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reproduction',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 35, 894301, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='town',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 37, 910804, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='town',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 39, 430572, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='translator',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 6, 19, 55, 42, 102610, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='translator',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 6, 19, 55, 43, 918214, tzinfo=utc)),
            preserve_default=False,
        ),
    ]