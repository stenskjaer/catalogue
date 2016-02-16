# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commentaries', '0001_initial'),
    ]

    operations = [
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
            model_name='commentary',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Commentator'),
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
    ]
