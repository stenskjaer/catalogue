from django.db import models

from catalogue.shared.models import BaseModel
from places.models import Country, Town
from smart_selects.db_fields import ChainedForeignKey


class Archive(BaseModel):
    archive_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, blank=True, null=True)
    town = ChainedForeignKey(
        Town,
        chained_field = 'country',
        chained_model_field = 'country',
        show_all = False,
        auto_choose = True,
        related_name = 'archive_town',
        blank=True,
        null=True,
    )

    def __str__(self):
        return '%s' % (self.archive_name)