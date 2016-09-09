from django.db import models
from django_countries.fields import CountryField

from catalogue.shared.models import BaseModel
from smart_selects.db_fields import ChainedForeignKey


class Country(BaseModel):
    country = CountryField()

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return str(self.country.name)


class Town(BaseModel):
    country = models.ForeignKey(Country)
    town_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['town_name']

    def __str__(self):
        return self.town_name


class Library(BaseModel):
    library_country = models.ForeignKey(Country)
    library_town = ChainedForeignKey(
        Town,
        chained_field = 'library_country',
        chained_model_field = 'country',
        show_all = False,
        auto_choose = True,
        related_name = 'library_town'
    )
    library_name = models.CharField(max_length=255)
    library_short_name = models.CharField(max_length=255, null=True, blank=True)
    library_note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Libraries'
        ordering = ['library_name']


    def __str__(self):
        print_library = self.library_name
        if self.library_short_name:
            print_library = self.library_short_name
        return print_library
