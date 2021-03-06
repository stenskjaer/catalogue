# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    # replaces = [('commentaries', '0001_initial'), ('commentaries', '0002_auto_20160329_1506'), ('commentaries', '0003_auto_20160329_1509'), ('commentaries', '0004_auto_20160329_1515'), ('commentaries', '0005_commentaryedition_coverage'), ('commentaries', '0006_auto_20160401_0820'), ('commentaries', '0007_auto_20160401_0823'), ('commentaries', '0008_auto_20160403_1953')]

    initial = True

    # dependencies = [
    #     ('references', '0002_auto_20160216_0846'),
    # ]

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
            name='BaseText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('title_addon', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title addon')),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('saeculo', models.CharField(blank=True, max_length=50, null=True)),
                ('note', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('literature', django_markdown.models.MarkdownField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentaryEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.TextEdition')),
            ],
            options={
                'verbose_name_plural': 'Commentary editions',
                'verbose_name': 'Commentary edition',
            },
        ),
        migrations.CreateModel(
            name='CommentaryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('commentary_type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
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
            name='CommentatorAlternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('commentator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentaries.Commentator')),
            ],
            options={
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
        migrations.CreateModel(
            name='AuthorityText',
            fields=[
                ('basetext_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commentaries.BaseText')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentaries.Authority')),
                ('translator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='commentaries.Translator')),
            ],
            options={
                'ordering': ['author'],
            },
            bases=('commentaries.basetext',),
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('basetext_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commentaries.BaseText')),
                ('authorship', models.CharField(blank=True, choices=[('certain', 'Certain'), ('possible', 'Possible'), ('disputed', 'Disputed'), ('dubious', 'Dubious'), ('untrue', 'Untrue')], max_length=10, null=True)),
                ('after', models.CharField(blank=True, max_length=55, null=True, verbose_name='After date (earliest)')),
                ('before', models.CharField(blank=True, max_length=55, null=True, verbose_name='Before date (latest)')),
                ('incipit', models.TextField(blank=True, max_length=1020, null=True)),
                ('explicit', models.TextField(blank=True, max_length=1020, null=True)),
                ('mora_reference', models.CharField(blank=True, max_length=20, null=True)),
                ('relevance', models.IntegerField(blank=True, choices=[(1, 'High'), (2, 'Some'), (3, 'Low'), (4, 'Unknown'), (5, 'None')], default=4, null=True)),
                ('commentary_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commentaries.AuthorityText')),
                ('commentary_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commentaries.CommentaryType')),
                ('commentator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Commentator')),
                ('related_commentaries', models.ManyToManyField(blank=True, related_name='_commentary_related_commentaries_+', to='commentaries.Commentary')),
                ('edition_coverage', models.IntegerField(blank=True, choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Commentaries',
                'ordering': ['commentator', 'title', 'modified'],
                'verbose_name': 'Commentary',
            },
            bases=('commentaries.basetext',),
        ),
        migrations.AddField(
            model_name='commentatoralternative',
            name='commentary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentaries.Commentary'),
        ),
        migrations.AddField(
            model_name='commentaryedition',
            name='commentary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentaries.Commentary'),
        ),
        migrations.AlterField(
            model_name='authoritytext',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Authority'),
        ),
        migrations.AlterField(
            model_name='authoritytext',
            name='translator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='persons.Translator'),
        ),
        migrations.AlterField(
            model_name='commentatoralternative',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Commentator'),
        ),
        migrations.DeleteModel(
            name='Authority',
        ),
        migrations.DeleteModel(
            name='Commentator',
        ),
        migrations.DeleteModel(
            name='Translator',
        ),
        migrations.AlterField(
            model_name='authoritytext',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentaries.Authority'),
        ),
        migrations.AlterField(
            model_name='authoritytext',
            name='translator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='commentaries.Translator'),
        ),
        migrations.AlterField(
            model_name='commentatoralternative',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentaries.Commentator'),
        ),
        migrations.AlterField(
            model_name='authoritytext',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Authority'),
        ),
        migrations.AlterField(
            model_name='authoritytext',
            name='translator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='persons.Translator'),
        ),
        migrations.AlterField(
            model_name='commentatoralternative',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Commentator'),
        ),
    ]
