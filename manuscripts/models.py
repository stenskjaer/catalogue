from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django_countries.fields import CountryField
from django_markdown.models import MarkdownField

class BaseModel(models.Model):
    """
    All models are based on this abstract model. It adds
    datetimefields for creation and editing of each model instance.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        


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
    note = MarkdownField(blank=True, null=True)
    literature = MarkdownField(blank=True, null=True)

    def __str__(self):
        return self.title

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

    class Meta:
        verbose_name_plural = 'Libraries'
        ordering = ['library_name']

    def __str__(self):
        return self.library_name


class OnlineMaterial(BaseModel):
    url = models.URLField(null=True, blank=False)
    manuscript = models.ForeignKey('Manuscript', null=True, blank=False)


class Reproduction(BaseModel):
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

class CommentatorAlternative(BaseModel):
    commentator = models.ForeignKey('Commentator')
    commentary = models.ForeignKey('Commentary')
    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Alternative: %s' % (self.commentator)


class ManuscriptContent(BaseModel):
    manuscript = models.ForeignKey('Manuscript')
    content = models.ForeignKey('BaseText', null=True)
    folios = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.manuscript)


class ManuscriptInspection(BaseModel):
    INSPECTION_TYPES = (
        ('digital', 'Digital reproduction'),
        ('situ', 'In situ')
    )
    manuscript = models.ForeignKey('Manuscript')
    inspector = models.ForeignKey(User, limit_choices_to={'groups__name': 'Inspectors'})
    inspection_type = models.CharField(max_length=10, choices=INSPECTION_TYPES)
    inspection_date = models.DateField()

    def __str__(self):
        return '%s by %s' % (self.inspection_date, self.inspector)


class Manuscript(BaseModel):
    MATERIALS = (
        ('parcment', 'Parchment'),
        ('paper', 'Paper')
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
    material = models.CharField(max_length=50, choices=MATERIALS, null=True, blank=True)
    width = models.FloatField('Width (in mm.)', blank=True, null=True)
    height = models.FloatField('Height (in mm.)', blank=True, null=True)
    dimension_note = models.CharField('Note about dimensions', max_length=255, blank=True, null=True)
    folios = models.CharField(max_length=20, null=True, blank=True)
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

    @property
    def overview(self):
        return '%s, %s, %s %s' % (self.town, self.library, self.shelfmark, self.number)
