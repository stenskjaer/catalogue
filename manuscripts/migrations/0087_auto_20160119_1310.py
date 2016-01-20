# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 12:10
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0086_auto_20160119_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='literature',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='note',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basetext',
            name='literature',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basetext',
            name='note',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentator',
            name='literature',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentator',
            name='note',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='annotation',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='layout',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='literature',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='note',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='script',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='literature',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='note',
            field=django_markdown.models.MarkdownField(blank=True, null=True),
        ),
    ]