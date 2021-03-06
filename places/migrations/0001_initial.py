# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('library_name', models.CharField(max_length=255)),
                ('library_note', models.TextField(blank=True, null=True)),
                ('library_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Country')),
            ],
            options={
                'verbose_name_plural': 'Libraries',
                'ordering': ['library_name'],
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('town_name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Country')),
            ],
            options={
                'ordering': ['town_name'],
            },
        ),
        migrations.AddField(
            model_name='library',
            name='library_town',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='library_country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, related_name='library_town', to='places.Town'),
        ),
    ]
