# -*- coding: utf-8 -*-
from django.db import models
from django_markdown.models import MarkdownField

from catalogue.shared.functions import set_saeculo
from catalogue.shared.models import BaseModel
from references.models import TextEdition

class Author(BaseModel):
    name = models.CharField(max_length=200)
    birth = models.CharField(max_length=50, blank=True, null=True)
    death = models.CharField(max_length=50, blank=True, null=True)
    floruit = models.CharField(max_length=50, blank=True, null=True)
    note = MarkdownField(blank=True, null=True)
    literature = MarkdownField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        if self.birth and self.death:
            return '{0} ({1} – {2})'.format(
                self.name,
                'b. ' + self.birth,
                'd. ' + self.death,
            )
        elif self.birth:
            return '{0} ({1})'.format(
                self.name,
                'b. ' + self.birth,
            )
        elif self.death:
            return '{0} ({1})'.format(
                self.name,
                'd. ' + self.death,
            )
        else:
            return self.name


class Commentator(Author):
    pass


class Authority(Author):
    class Meta:
        verbose_name_plural = 'Authorities'


class Translator(Author):
    pass


class BaseText(BaseModel):
    title = models.CharField(max_length=500)
    title_addon = models.CharField('Title addon', max_length=255, blank=True, null=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    saeculo = models.CharField(max_length=50, null=True, blank=True)
    note = MarkdownField(blank=True, null=True)
    literature = MarkdownField(blank=True, null=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.date and self.saeculo == '':
            self.saeculo = set_saeculo(self)


class Commentary(BaseText):
    AUTHORSHIP = [
        ('certain', 'Certain'),
        ('possible', 'Possible'),
        ('disputed', 'Disputed'),
        ('dubious', 'Dubious'),
        ('untrue', 'Untrue'),
    ]
    RELEVANCE_HIGH = 1
    RELEVANCE_MID = 2
    RELEVANCE_LOW = 3
    RELEVANCE_UNKNOWN = 4
    RELEVANCE_NONE = 5
    RELEVANCE_CHOICES = (
        (RELEVANCE_HIGH, 'High'),
        (RELEVANCE_MID, 'Some'),
        (RELEVANCE_LOW, 'Low'),
        (RELEVANCE_UNKNOWN, 'Unknown'),
        (RELEVANCE_NONE, 'None'),
    )
    commentator = models.ForeignKey('Commentator', blank=False)
    authorship = models.CharField(max_length=10, blank=True, null=True, choices=AUTHORSHIP)
    commentary_type = models.ForeignKey('CommentaryType', blank=True, null=True)
    commentary_on = models.ForeignKey('AuthorityText', blank=True, null=True)
    after = models.CharField('After date (earliest)', max_length=55, blank=True, null=True)
    before = models.CharField('Before date (latest)', max_length=55, blank=True, null=True)
    incipit = models.TextField(max_length=1020, blank=True, null=True)
    explicit = models.TextField(max_length=1020, blank=True, null=True)
    mora_reference = models.CharField(max_length=20, blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True, default=RELEVANCE_UNKNOWN, choices=RELEVANCE_CHOICES)
    related_commentaries = models.ManyToManyField('self', symmetrical=True, blank=True)

    class Meta:
        verbose_name = 'Commentary'
        verbose_name_plural = 'Commentaries'
        ordering = ['commentator', 'title', 'modified']

    def __str__(self):
        return '%s: %s' % (self.commentator, self.title)


class AuthorityText(BaseText):
    author = models.ForeignKey('Authority', on_delete=models.CASCADE)
    translator = models.ForeignKey('Translator', related_name='translator', blank=True, null=True)
    class Meta:
        ordering = ['author']

    def __str__(self):
        return '%s by %s' % (self.title, self.author)


class CommentaryType(BaseModel):
    commentary_type = models.CharField(max_length=255)

    def __str__(self):
        return self.commentary_type


class CommentaryEdition(BaseModel):
    commentary = models.ForeignKey('Commentary')
    edition = models.ForeignKey(TextEdition)
    note = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Commentary editions'
        verbose_name = 'Commentary edition'

    def __str__(self):
        return '%s: %s' % (self.edition, self.commentary)


class CommentatorAlternative(BaseModel):
    commentator = models.ForeignKey('Commentator')
    commentary = models.ForeignKey('Commentary')
    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Alternative: %s' % (self.commentator)
