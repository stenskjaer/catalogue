from django.contrib import admin

from commentaries.forms import TextForm
from commentaries.models import *
from manuscripts.admin import ContentInline
from manuscripts.models import Manuscript

class EditionInline(admin.TabularInline):
    model = CommentaryEdition
    extra = 1


class AlternativeAuthorInline(admin.TabularInline):
    model = AuthorAlternative
    extra = 1


class CommentariesInline(admin.TabularInline):
    model = Text
    extra = 1
    fields = ['title', 'relevance', 'mora_reference']


class TextAdmin(admin.ModelAdmin):
    form = TextForm
    inlines = [
        ContentInline,
        EditionInline,
        AlternativeAuthorInline,
    ]
    filter_horizontal = ['related_commentaries']

    list_display = [
        'author',
        'title',
        'date',
        'saeculo',
        'relevance',
        'edition_coverage',
        'witnesses',
        'reproductions',
        'modified',
    ]

    search_fields = [
        'author__name',
        'title',
        'date',
        'saeculo',
        'note',
        'manuscriptcontentcommentary__content__title',
        'manuscriptcontentcommentary__manuscript__town__town_name',
        'manuscriptcontentcommentary__manuscript__library__library_name',
        'manuscriptcontentcommentary__manuscript__number',
        'manuscriptcontentcommentary__manuscript__shelfmark',
        'manuscriptcontentcommentary__manuscript__saeculo',
    ]

    def witnesses(self, obj):
        query = Manuscript.objects.select_related().filter(manuscriptcontentcommentary__content=obj)
        return '<br />'.join([item.overview for item in query])
    witnesses.allow_tags = True

    def reproductions(self, obj):
        ms_query = Manuscript.objects.select_related().filter(manuscriptcontentcommentary__content=obj)
        available = 0
        witnesses = len(ms_query)
        for ms in ms_query:
            if Manuscript.objects.select_related().filter(reproduction__manuscript=ms.pk):
                available = + 1
        return '{0}/{1}'.format(available, witnesses)

    def queryset(self, request):
        # Prefetch related objects
        return super(TextAdmin, self).queryset(request).select_related(['manuscriptcontentcommentary',
                                                                              'reproduction'])


admin.site.register(Text, TextAdmin)
admin.site.register(CommentaryType)
admin.site.register(CommentaryEdition)
