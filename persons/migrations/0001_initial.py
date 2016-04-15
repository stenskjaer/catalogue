# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('birth', models.CharField(blank=True, max_length=50, null=True)),
                ('death', models.CharField(blank=True, max_length=50, null=True)),
                ('floruit', models.CharField(blank=True, max_length=50, null=True)),
                ('note', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('literature', django_markdown.models.MarkdownField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Authorities',
            },
        ),
        migrations.CreateModel(
            name='Commentator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('birth', models.CharField(blank=True, max_length=50, null=True)),
                ('death', models.CharField(blank=True, max_length=50, null=True)),
                ('floruit', models.CharField(blank=True, max_length=50, null=True)),
                ('note', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('literature', django_markdown.models.MarkdownField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('birth', models.CharField(blank=True, max_length=50, null=True)),
                ('death', models.CharField(blank=True, max_length=50, null=True)),
                ('floruit', models.CharField(blank=True, max_length=50, null=True)),
                ('note', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('literature', django_markdown.models.MarkdownField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]