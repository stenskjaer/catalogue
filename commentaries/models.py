# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ValidationError
from django_markdown.models import MarkdownField

from catalogue.shared.functions import set_saeculo, truncate, attachment_id_path
from catalogue.shared.models import BaseModel
from persons.models import Commentator, Authority, Translator
import re

class Text(BaseModel):
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
    COVERAGE_NONE = 0
    COVERAGE_PARTIAL = 1
    COVERAGE_COMPLETE = 2
    COVERAGE_EARLY = 3
    EDITION_COVERAGE = (
        (COVERAGE_NONE, 'None'),
        (COVERAGE_PARTIAL, 'Partial'),
        (COVERAGE_COMPLETE, 'Full'),
        (COVERAGE_EARLY, 'Early print'),
    )
    TEXT_AUTHORITY = 1
    TEXT_COMMENTARY = 2
    TEXT_CHOICES = (
        (1, 'Authority text'),
        (2, 'Commentary'),
        (3, 'Summa or tractatus'),
        (4, 'Compilation or excerpts'),
    )

    title = models.CharField(max_length=500)
    title_addon = models.CharField('Title addon', max_length=255, blank=True, null=True)
    text_type = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    saeculo = models.CharField(max_length=50, null=True, blank=True)
    note = MarkdownField(blank=True, null=True)
    literature = MarkdownField(blank=True, null=True)
    author = models.ForeignKey(Commentator, blank=False)
    authorship = models.CharField(max_length=10, blank=True, null=True, choices=AUTHORSHIP)
    commentary_type = models.ForeignKey('CommentaryType', blank=True, null=True)
    commentary_on = models.ForeignKey('self', limit_choices_to=models.Q(text_type__contains=TEXT_AUTHORITY),
                                      blank=True, null=True)
    after = models.CharField('After date (earliest)', max_length=55, blank=True, null=True)
    before = models.CharField('Before date (latest)', max_length=55, blank=True, null=True)
    incipit = models.TextField(max_length=1020, blank=True, null=True)
    explicit = models.TextField(max_length=1020, blank=True, null=True)
    mora_reference = models.CharField(max_length=20, blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True, default=RELEVANCE_UNKNOWN, choices=RELEVANCE_CHOICES)
    related_commentaries = models.ManyToManyField('self', symmetrical=True, blank=True)
    edition_coverage = models.IntegerField(blank=True, default=COVERAGE_NONE, choices=EDITION_COVERAGE)

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        ordering = ['author', 'title', 'modified']

    def clean(self):
        if self.date and self.saeculo == '':
            self.saeculo = set_saeculo(self)
        mora_value = self.mora_reference
        if mora_value:
            reference_base = 'DA'
            regex_pattern = re.compile('([0-9]+)(.*?)$')
            if re.search(regex_pattern, mora_value):
                reference_number = re.search(regex_pattern, mora_value).group(1)
                reference_suffix = re.search(regex_pattern, mora_value).group(2)
            else:
                raise ValidationError("The Mora reference number must contain at least one digit.")

            if len(reference_number) > 3:
                raise ValidationError("The Mora reference number must not be longer than three digits.")
            if len(reference_number) == 3:
                self.mora_reference = reference_base + reference_number + reference_suffix
            elif len(reference_number) == 2:
                self.mora_reference = reference_base + '0' + reference_number + reference_suffix
            elif len(reference_number) == 1:
                self.mora_reference = reference_base + '00' + reference_number + reference_suffix

    def __str__(self):
        if self.title_addon:
            title_string = truncate(self.title + ' ({0})'.format(self.title_addon))
        else:
            title_string = truncate(self.title)
        return_string = '%s: %s' % (self.author, title_string)
        return truncate(return_string)


class CommentaryType(BaseModel):
    commentary_type = models.CharField(max_length=255)

    def __str__(self):
        return self.commentary_type


class Attachment(BaseModel):
    attachment = models.FileField(blank = True, upload_to = attachment_id_path)
    attached_to = models.ForeignKey('Text')

# class CommentaryEdition(BaseModel):
#     commentary = models.ForeignKey('Text')
#     edition = models.ForeignKey(TextEdition)
#     note = models.CharField(max_length=500, blank=True, null=True)

#     class Meta:
#         verbose_name_plural = 'Text editions'
#         verbose_name = 'Text edition'

#     def __str__(self):
#         return '%s: %s' % (self.edition, self.commentary)


class AuthorAlternative(BaseModel):
    author = models.ForeignKey(Commentator)
    commentary = models.ForeignKey('Text')
    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Alternative: %s' % (self.author)
