from django.db import models

from catalogue.shared.models import BaseModel

class Author(BaseModel):
    name = models.CharField(max_length=200)
    birth = models.CharField(max_length=50, blank=True, null=True)
    death = models.CharField(max_length=50, blank=True, null=True)
    floruit = models.CharField(max_length=50, blank=True, null=True)
    viaf_url = models.URLField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    literature = models.TextField(blank=True, null=True)
    attachments = models.FileField(blank = True, upload_to='persons/%Y-%m-%d')

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
