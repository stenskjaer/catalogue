from django.contrib import admin

from .models import *
from .forms import ManuscriptForm, CommentaryForm, AuthorityForm, CommentatorForm

class UrlInline(admin.TabularInline):
    model = OnlineMaterial
    extra = 1

class InspectionInline(admin.TabularInline):
    model = ManuscriptInspection
    extra = 1

class ContentInline(admin.TabularInline):
    model = ManuscriptContentCommentary
    extra = 1

class ReproductionInline(admin.TabularInline):
    model = Reproduction
    extra = 1

class AlternativeAuthorInline(admin.TabularInline):
    model = CommentatorAlternative
    extra = 1

class CommentariesInline(admin.TabularInline):
    model = Commentary
    extra = 1
    fields = ['title', 'relevance', 'mora_reference']


class ManuscriptAdmin(admin.ModelAdmin):
    form = ManuscriptForm
    inlines = [
        InspectionInline,
        UrlInline,
        ContentInline,
        ReproductionInline,
    ]

    list_display = [
        'town',
        'library',
        'shelfmark',
        'number',
        'date',
        'saeculo',
        'modified',
        'inspection',
    ]

    search_fields = [
        'town__town_name',
        'library__library_name',
        'number',
        'date',
        'saeculo',
        'shelfmark',
        'manuscriptcontentcommentary__content__title',
        'manuscriptcontentcommentary__manuscript__town__town_name',
        'manuscriptcontentcommentary__manuscript__library__library_name',
        'manuscriptcontentcommentary__manuscript__number',
    ]

    def inspection(self, obj):
        query = ManuscriptInspection.objects.select_related().filter(manuscript=obj)
        if query:
            return sorted([item.inspection_date for item in query])[0]
    inspection.admin_order_field = 'manuscriptinspection__inspection_date'

class CommentaryAdmin(admin.ModelAdmin):
    form = CommentaryForm
    inlines = [
        ContentInline,
        AlternativeAuthorInline,
    ]
    filter_horizontal = ['related_commentaries']

    list_display = [
        'commentator',
        'title',
        'date',
        'saeculo',
        'relevance',
        'witnesses',
        'reproductions',
        'modified',
    ]

    search_fields = [
        'commentator__name',
        'title',
        'date',
        'saeculo',
        'manuscriptcontentcommentary__content__title',
        'manuscriptcontentcommentary__manuscript__town__town_name',
        'manuscriptcontentcommentary__manuscript__library__library_name',
        'manuscriptcontentcommentary__manuscript__number',
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
                available =+ 1
        return '{0}/{1}'.format(available, witnesses)

    def queryset(self, request):
        # Prefetch related objects
        return super(CommentaryAdmin, self).queryset(request).select_related(['manuscriptcontentcommentary', 'reproduction'])


class AuthorityAdmin(admin.ModelAdmin):
    form = AuthorityForm


class CommentatorAdmin(admin.ModelAdmin):
    form = CommentatorForm
    inlines = [
        CommentariesInline,
        AlternativeAuthorInline,
    ]


admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(AuthorityText, AuthorityAdmin)
admin.site.register(Commentator, CommentatorAdmin)
admin.site.register(Authority)
admin.site.register(Translator)
admin.site.register(CommentaryType)
admin.site.register(Manuscript, ManuscriptAdmin)
admin.site.register(ManuscriptContentCommentary)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Library)
admin.site.register(Reproduction)
admin.site.register(Archive)
