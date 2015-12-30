from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Author(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Text(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    source = models.ManyToManyField('Manuscript', blank=True)

    def __str__(self):
        return '%s by %s (%s)' % (self.title, self.author, self.date)


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return self.country_name


class Town(models.Model):
    country = models.ForeignKey(Country)
    town_name = models.CharField(max_length=255)

    def __str__(self):
        return self.town_name


class Library(models.Model):
    library_town = models.ForeignKey(Town)
    library_name = models.CharField(max_length=255)

    def __str__(self):
        return self.library_name


class Inspection(models.Model):
    INSPECTION_TYPES = (
        ('digital', 'Digital reproduction'),
        ('situ', 'In situ')
    )
    inspector = models.CharField(max_length=255)
    inspection_type = models.CharField(max_length=10, choices=INSPECTION_TYPES)
    inspection_date = models.DateField()

    def __str__(self):
        return '%s, %s (%s)' % (self.inspector, self.inspection_type, self.inspection_date)
    

class Manuscript(models.Model):
    MATERIALS = (
        ('parcment', 'Parchment'),
        ('paper', 'Paper')
    )
    PERIODS = (
        ('13.2', '1226-1250'),
        ('13.3', '1250-1275'),
        ('13.4', '1276-1300'),
        ('14.1', '1301-1325'),
        ('14.2', '1326-1350'),
        ('14.3', '1351-1375'),
        ('14.4', '1376-1400'),
        ('15.1', '1401-1425'),
        ('15.2', '1426-1450')
    )
    
    country = models.ForeignKey(Country, blank=False, null=True)
    town = ChainedForeignKey(
        Town,
        chained_field = 'country',
        chained_model_field = 'country',
        show_all = True,
        auto_choose = True,
        related_name = 'town'
    )
    library = ChainedForeignKey(
        Library,
        chained_field = 'town',
        chained_model_field = 'library_town',
        show_all = True,
        auto_choose = True,
        related_name = 'library'
    )
    shelfmark = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=30, blank=True)
    olim = models.CharField(max_length=100, blank=True)
    period = models.CharField(max_length=100, blank=True, choices=PERIODS)
    date = models.CharField(max_length=50, blank=True)
    material = models.CharField(max_length=50, choices=MATERIALS, blank=True)
    width = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    folios = models.CharField(max_length=20, blank=True)
    inspections = models.ManyToManyField('Inspection', blank=True)
    content = models.ManyToManyField('Text', blank=True)
    literature = models.TextField(blank=True)
    # reproduction = models.

    def __str__(self):
        return '%s, %s, %s %s' % (self.town, self.library, self.shelfmark, self.number)
    
