# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 17:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    replaces = [('manuscripts', '0001_initial'), ('manuscripts', '0002_manuscriptcontentcommentary'), ('manuscripts', '0003_manuscriptcontentcommentary'), ('manuscripts', '0004_auto_20160401_0801'), ('manuscripts', '0005_auto_20160405_2131'), ('manuscripts', '0006_auto_20160406_1005'), ('manuscripts', '0007_auto_20160406_1005'), ('manuscripts', '0008_auto_20160406_1008'), ('manuscripts', '0009_auto_20160406_1012'), ('manuscripts', '0010_auto_20160406_1015'), ('manuscripts', '0011_auto_20160406_1015'), ('manuscripts', '0012_auto_20160406_1016'), ('manuscripts', '0013_auto_20160406_1017'), ('manuscripts', '0014_auto_20160406_1017'), ('manuscripts', '0015_auto_20160406_1018'), ('manuscripts', '0016_auto_20160406_1019'), ('manuscripts', '0017_auto_20160406_1020'), ('manuscripts', '0018_auto_20160406_1020'), ('manuscripts', '0019_remove_reproduction_reproduction_coverage'), ('manuscripts', '0020_reproduction_reproduction_coverage'), ('manuscripts', '0021_auto_20160406_1025'), ('manuscripts', '0022_auto_20160406_1025'), ('manuscripts', '0023_reproduction_note'), ('manuscripts', '0024_auto_20160406_1030'), ('manuscripts', '0025_auto_20160409_1935'), ('manuscripts', '0026_auto_20160409_1949')]

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repositories', '0001_initial'),
        ('commentaries', '0001_squashed_0015_auto_20160601_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('shelfmark', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=30, null=True)),
                ('olim', models.CharField(blank=True, max_length=100, null=True)),
                ('date_earliest', models.CharField(blank=True, max_length=100, null=True)),
                ('date_latest', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('saeculo', models.CharField(blank=True, max_length=50, null=True)),
                ('material', models.CharField(blank=True, choices=[('parcment', 'Parchment'), ('paper', 'Paper')], max_length=50, null=True)),
                ('width', models.FloatField(blank=True, null=True, verbose_name='Width (in mm.)')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='Height (in mm.)')),
                ('dimension_note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Note about dimensions')),
                ('folios', models.CharField(blank=True, max_length=250, null=True)),
                ('layout', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('script', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('annotation', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('note', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('literature', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Country')),
                ('library', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='town', chained_model_field='library_town', on_delete=django.db.models.deletion.CASCADE, related_name='library', to='places.Library')),
            ],
            options={
                'ordering': ['town', 'library', 'shelfmark', 'number'],
            },
        ),
        migrations.CreateModel(
            name='ManuscriptInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('inspection_type', models.CharField(choices=[('digital', 'Digital reproduction'), ('situ', 'In situ'), ('microfilm', 'Microfilm')], max_length=10)),
                ('inspection_date', models.DateField()),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('manuscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Manuscript')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ManuscriptOrigin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dubious', models.BooleanField(default=False)),
                ('origin_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Country')),
                ('origin_town', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='origin_country', chained_model_field='country', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_town', to='places.Town')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OnlineMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(null=True)),
                ('manuscript', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Manuscript')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reproduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('media', models.CharField(choices=[('digital', 'Digital'), ('microfilm', 'Micro film')], max_length=100)),
                ('referencenumber', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archive', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='repositories.Archive')),
                ('manuscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Manuscript')),
                ('coverage', models.CharField(blank=True, choices=[('partial', 'Partial'), ('complete', 'Complete')], default='', max_length=15)),
                ('note', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='manuscript',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='manuscripts.ManuscriptOrigin'),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, related_name='town', to='places.Town'),
        ),
        migrations.AlterUniqueTogether(
            name='manuscript',
            unique_together=set([('country', 'town', 'library', 'shelfmark', 'number')]),
        ),
        migrations.CreateModel(
            name='ManuscriptContentCommentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('folios', models.CharField(blank=True, max_length=500, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commentaries.Commentary')),
                ('manuscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.Manuscript')),
                ('explicit', models.TextField(blank=True, null=True)),
                ('incipit', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Manuscript content (commentaries)',
                'verbose_name': 'Manuscript content (commentary)',
            },
        ),
    ]
