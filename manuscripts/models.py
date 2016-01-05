from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django_countries.fields import CountryField

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth = models.CharField(max_length=50, blank=True, null=True)
    death = models.CharField(max_length=50, blank=True, null=True)
    floruit = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    literature = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Text(models.Model):
    AUTHORSHIP = [
        ('certain', 'Certain'),
        ('possible', 'Possible'),
        ('disputed', 'Disputed'),
        ('dubious', 'Dubious'),
        ('untrue', 'Untrue'),
    ]
    commentary_type = models.ForeignKey('CommentaryType', blank=True, null=True)
    commentary_on = models.ForeignKey('Text', limit_choices_to={'commented_on': True}, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    authorship = models.CharField(max_length=10, blank=True, null=True, choices=AUTHORSHIP)
    translator = models.ForeignKey('Author', related_name='translator', blank=True, null=True)
    title = models.CharField(max_length=500)
    title_addon = models.CharField('Title addon', max_length=255, blank=True, null=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    incipit = models.TextField(max_length=1020, blank=True, null=True)
    explicit = models.TextField(max_length=1020, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    commented_on = models.BooleanField(default=False)
    literature = models.TextField(blank=True, null=True)
    mora_reference = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s by %s' % (self.title, self.author)


class CommentaryType(models.Model):
    commentary_type = models.CharField(max_length=255)

    def __str__(self):
        return self.commentary_type


class Country(models.Model):
    country = CountryField()

    def __str__(self):
        return str(self.country.name)


class Town(models.Model):
    country = models.ForeignKey(Country)
    town_name = models.CharField(max_length=255)

    def __str__(self):
        return self.town_name


class Library(models.Model):
    library_country = models.ForeignKey(Country)
    library_town = ChainedForeignKey(
        Town,
        chained_field = 'library_country',
        chained_model_field = 'country',
        show_all = True,
        auto_choose = True,
        related_name = 'library_town'
    )
    library_name = models.CharField(max_length=255)

    def __str__(self):
        return self.library_name


class OnlineMaterial(models.Model):
    url = models.URLField(null=True, blank=False)
    manuscript = models.ForeignKey('Manuscript', null=True, blank=False)


class Reproduction(models.Model):
    MEDIA_TYPES = (
        ('digital', 'Digital'),
        ('microfilm', 'Micro film'),
    )

    manuscript = models.ForeignKey('Manuscript')
    archive = models.ForeignKey('Archive', max_length=255)
    media = models.CharField(max_length=100, choices=MEDIA_TYPES)
    referencenumber = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return '%s %s' % (self.archive, self.referencenumber)


class Archive(models.Model):
    archive_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, blank=True, null=True)
    town = ChainedForeignKey(
        Town,
        chained_field = 'country',
        chained_model_field = 'country',
        show_all = True,
        auto_choose = True,
        related_name = 'archive_town',
        blank=True,
        null=True,
    )

    def __str__(self):
        return '%s' % (self.archive_name)


class ManuscriptContent(models.Model):
    manuscript = models.ForeignKey('Manuscript')
    content = models.ForeignKey('Text')
    folios = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=120, blank=True, null=True)


class ManuscriptInspection(models.Model):
    INSPECTION_TYPES = (
        ('digital', 'Digital reproduction'),
        ('situ', 'In situ')
    )
    manuscript = models.ForeignKey('Manuscript')
    inspector = models.CharField(max_length=255)
    inspection_type = models.CharField(max_length=10, choices=INSPECTION_TYPES)
    inspection_date = models.DateField()

    def __str__(self):
        return '%s by %s' % (self.inspection_date, self.inspector)

    
class Manuscript(models.Model):
    MATERIALS = (
        ('parcment', 'Parchment'),
        ('paper', 'Paper')
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
    shelfmark = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=30, null=True, blank=True)
    olim = models.CharField(max_length=100, null=True, blank=True)
    date_earliest = models.CharField(max_length=100, blank=True, null=True)
    date_latest = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=50, choices=MATERIALS, null=True, blank=True)
    width = models.FloatField('Width (in mm.)', blank=True, null=True)
    height = models.FloatField('Height (in mm.)', blank=True, null=True)
    dimension_note = models.CharField('Note about dimensions', max_length=255, blank=True, null=True)
    folios = models.CharField(max_length=20, null=True, blank=True)
    layout = models.TextField(blank=True, null=True)
    literature = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s, %s, %s %s' % (self.town, self.library, self.shelfmark, self.number)
