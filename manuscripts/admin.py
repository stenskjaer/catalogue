from django.contrib import admin

from .models import *
from .forms import ManuscriptForm, TextForm, AuthorityForm

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
        # ContentInline,
        ReproductionInline,
    ]

    list_display = [
        'library',
        'shelfmark',
        'number',
        'town',
    ]

    list_filter = [
        'country',
    ]


class TextAdmin(admin.ModelAdmin):
    form = TextForm
    # inlines = [
    #     ContentInline,
    # ]

    list_display = [
        'commentator',
        'title',
        'date',
    ]


class AuthorityAdmin(admin.ModelAdmin):
    form = AuthorityForm

admin.site.register(Commentary, TextAdmin)
admin.site.register(AuthorityText, AuthorityAdmin)
admin.site.register(Commentator)
admin.site.register(Authority)
admin.site.register(Translator)
admin.site.register(CommentaryType)
admin.site.register(Manuscript, ManuscriptAdmin)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Library)
admin.site.register(Reproduction)
admin.site.register(Archive)
