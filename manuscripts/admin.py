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
    model = ManuscriptContent
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
        'library',
        'shelfmark',
        'number',
        'town',
        'created',
        'modified',
    ]


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
        'relevance',
        'created',
        'modified',
    ]


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
admin.site.register(ManuscriptContent)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Library)
admin.site.register(Reproduction)
admin.site.register(Archive)
