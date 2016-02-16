from django.db import models


class BaseModel(models.Model):
    """
    All models are based on this abstract model. It adds
    datetime fields for creation and editing of each model instance.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Publication(BaseModel):
    REFERENCE_TYPE_CHOICES = (
        ('BK', 'Book'),
        ('EJL', 'Electronic Journal'),
        ('JL', 'Journal'),
        ('WB', 'Website'),
    )

    type = models.CharField(max_length=3, choices=REFERENCE_TYPE_CHOICES, default='BK')
    slug = models.CharField(max_length=128, unique=True)

    author = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    year = models.IntegerField(default=2000)

    series = models.CharField(max_length=512, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)

    isbn = models.CharField(max_length=17, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    publisher = models.CharField(max_length=128, blank=True, null=True)
    place = models.CharField(max_length=128, blank=True, null=True)

    abstract = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['author']

    def __str__(self):
        return '{0}, {1} [{2}]'.format(self.author, self.title, self.slug)


class Edition(Publication):
    def __str__(self):
        name = ''
        if self.author:
            name = self.author
        elif self.editor:
            name = self.editor

        name += ', {0}'.format(self.title[:18])
        return name
