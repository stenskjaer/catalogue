# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django_markdown.models import MarkdownField

from catalogue.shared.functions import set_saeculo
from catalogue.shared.models import BaseModel
from commentaries.models import Text
from places.models import Country, Town, Library
from repositories.models import Archive
from smart_selects.db_fields import ChainedForeignKey


class OnlineMaterial(BaseModel):
    url = models.URLField(null=True, blank=False)
    manuscript = models.ForeignKey('Manuscript', null=True, blank=False)


class Reproduction(BaseModel):
    MEDIA_TYPES = (
        ('digital', 'Digital'),
        ('microfilm', 'Micro film'),
    )
    REPRO_COVERAGE = (
        ('partial', 'Partial'),
        ('complete', 'Complete'),
    )
    manuscript = models.ForeignKey('Manuscript')
    archive = models.ForeignKey(Archive, max_length=255)
    media = models.CharField(max_length=100, choices=MEDIA_TYPES)
    referencenumber = models.CharField(max_length=255, blank=True, null=True)
    coverage = models.CharField(max_length=15, blank=True, choices=REPRO_COVERAGE)
    note = models.CharField(max_length=512, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.archive, self.referencenumber)


class ManuscriptContentCommentary(BaseModel):
    manuscript = models.ForeignKey('Manuscript')
    content = models.ForeignKey(Text, null=True)
    folios = models.CharField(max_length=500, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    incipit = models.TextField(blank=True, null=True)
    explicit = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Manuscript content (commentaries)'
        verbose_name = 'Manuscript content (commentary)'

    def __str__(self):
        return '%s' % (self.manuscript)


class ManuscriptInspection(BaseModel):
    INSPECTION_TYPES = (
        ('digital', 'Digital reproduction'),
        ('situ', 'In situ'),
        ('microfilm', 'Microfilm'),
    )
    manuscript = models.ForeignKey('Manuscript')
    inspector = models.ForeignKey(User, limit_choices_to={'groups__name': 'Inspectors'})
    inspection_type = models.CharField(max_length=10, choices=INSPECTION_TYPES)
    inspection_date = models.DateField()

    def __str__(self):
        return '%s by %s' % (self.inspection_date, self.inspector)


class ManuscriptOrigin(BaseModel):
    origin_country = models.ForeignKey(Country, blank=False, null=True)
    origin_town = ChainedForeignKey(
        Town,
        chained_field = 'origin_country',
        chained_model_field = 'country',
        show_all = False,
        auto_choose = True,
        related_name = 'origin_town',
        blank=True,
        null=True
    )
    dubious = models.BooleanField(default=False)

    def __str__(self):
        if self.dubious:
            dubious = '?'
        else:
            dubious = ''

        if self.origin_town:
            return '{0}, {1}{2}'.format(self.origin_country, self.origin_town, dubious)
        else:
            return '{0}{1}'.format(self.origin_country, dubious)


class Manuscript(BaseModel):
    MATERIALS = (
        ('parcment', 'Parchment'),
        ('paper', 'Paper'),
        ('combi', 'Parch. and pap.')
    )

    country = models.ForeignKey(Country, blank=False, null=True)
    town = ChainedForeignKey(
        Town,
        chained_field = 'country',
        chained_model_field = 'country',
        show_all = False,
        auto_choose = True,
        related_name = 'town'
    )
    library = ChainedForeignKey(
        Library,
        chained_field = 'town',
        chained_model_field = 'library_town',
        show_all = False,
        auto_choose = True,
        related_name = 'library'
    )
    shelfmark = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=30, null=True, blank=True)
    olim = models.CharField(max_length=100, null=True, blank=True)
    date_earliest = models.CharField(max_length=100, blank=True, null=True)
    date_latest = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    saeculo = models.CharField(max_length=50, null=True, blank=True)
    origin = models.ForeignKey('ManuscriptOrigin', blank=True, null=True, related_name='origin')
    material = models.CharField(max_length=50, choices=MATERIALS, null=True, blank=True)
    width = models.FloatField('Width (in mm.)', blank=True, null=True)
    height = models.FloatField('Height (in mm.)', blank=True, null=True)
    dimension_note = models.CharField('Note about dimensions', max_length=255, blank=True, null=True)
    folios = models.CharField(max_length=250, null=True, blank=True)
    layout = MarkdownField(blank=True, null=True)
    script = MarkdownField(blank=True, null=True)
    annotation = MarkdownField(blank=True, null=True)
    note = MarkdownField(blank=True, null=True)
    literature = MarkdownField(null=True, blank=True)


    class Meta:
        ordering = ['town', 'library', 'shelfmark', 'number']
        unique_together = ['country', 'town', 'library', 'shelfmark', 'number']

    def __str__(self):
        return '%s, %s, %s %s' % (self.town, self.library, self.shelfmark, self.number)

    def clean(self):
        if self.date and self.saeculo == '':
            self.saeculo = set_saeculo(self)


    @property
    def overview(self):
        return '%s, %s, %s %s' % (self.town, self.library, self.shelfmark, self.number)
