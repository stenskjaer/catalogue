from django.contrib import admin

from .models import *
from .forms import ManuscriptForm, CommentaryForm, AuthorityForm

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
    ]

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

admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(AuthorityText, AuthorityAdmin)
admin.site.register(Commentator)
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
