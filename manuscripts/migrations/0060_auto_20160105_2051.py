# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0059_auto_20160105_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorship', models.CharField(blank=True, choices=[('certain', 'Certain'), ('possible', 'Possible'), ('disputed', 'Disputed'), ('dubious', 'Dubious'), ('untrue', 'Untrue')], max_length=10, null=True)),
                ('title', models.CharField(max_length=500)),
                ('title_addon', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title addon')),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('incipit', models.TextField(blank=True, max_length=1020, null=True)),
                ('explicit', models.TextField(blank=True, max_length=1020, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('literature', models.TextField(blank=True, null=True)),
                ('mora_reference', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commentator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth', models.CharField(blank=True, max_length=50, null=True)),
                ('death', models.CharField(blank=True, max_length=50, null=True)),
                ('floruit', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('literature', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='commentary',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Commentator'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='commentary_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Text'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='commentary_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.CommentaryType'),
        ),
    ]
