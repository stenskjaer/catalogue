from django.contrib import admin
from catalogue.shared.functions import set_saeculo, truncate
from catalogue.shared.actions import export_as_csv_action

from commentaries.forms import TextForm
from commentaries.models import *
from manuscripts.admin import ContentInline
from manuscripts.models import ManuscriptContentCommentary, Reproduction
from commentaries.filterlists import CommentarySaeculo

# class EditionInline(admin.TabularInline):
#     model = CommentaryEdition
#     extra = 1


class AlternativeAuthorInline(admin.TabularInline):
    model = AuthorAlternative
    extra = 1


class CommentariesInline(admin.TabularInline):
    model = Text
    extra = 1
    fields = ['title', 'relevance', 'mora_reference']


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1
    fields = ['attachment']


class TextAdmin(admin.ModelAdmin):
    form = TextForm
    inlines = [
        ContentInline,
        # EditionInline,
        AttachmentInline,
        AlternativeAuthorInline,
    ]
    filter_horizontal = ['related_commentaries']

    list_filter = ('relevance', CommentarySaeculo, 'edition_coverage', 'commentary_type', 'commentary_on')

    list_display = [
        'author',
        'collected_title',
        'date',
        'saeculo',
        'relevance',
        'edition_coverage',
        'witnesses',
        'reproductions',
        'modified',
        'mora_reference',
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

    actions = [
        export_as_csv_action(
            "CSV Export",
            fields=['id', 'author', 'title', 'date', 'edition_coverage',
                    'witnesses', 'reproductions', 'modified', 'mora_reference']
        )
    ]

    def collected_title(self, obj):
        query = Text.objects.select_related().get(id=obj.id)
        if query.title_addon:
            return truncate(query.title + ' ({0})'.format(query.title_addon))
        else:
            return truncate(query.title)


    def witnesses(self, obj):
        query = ManuscriptContentCommentary.objects.select_related().filter(content=obj)

        return_list = []
        for item in query:
            folio_range = ''
            if item.folios:
                folio_range = '(ff. {})'.format(item.folios)

            ms = item.manuscript
            return_list.append(
                '%s, %s, %s %s %s' % (
                    ms.town,
                    ms.library,
                    ms.shelfmark,
                    ms.number,
                    folio_range
                )
            )
        return '<br/>'.join(return_list)
    witnesses.allow_tags = True

    def reproductions(self, obj):
        ms_query = ManuscriptContentCommentary.objects.select_related().filter(content=obj)
        witness_count = len(ms_query)
        repro_count = 0
        for item in ms_query:
            if Reproduction.objects.filter(manuscript=item.pk):
                repro_count =+ 1

        return '{0}/{1}'.format(repro_count, witness_count)

    def queryset(self, request):
        # Prefetch related objects
        return super(TextAdmin, self).queryset(request).select_related(['manuscriptcontentcommentary',
                                                                              'reproduction'])


admin.site.register(Text, TextAdmin)
admin.site.register(CommentaryType)
# admin.site.register(CommentaryEdition)
