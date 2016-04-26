from django.contrib import admin

from manuscripts.forms import ManuscriptForm, ContentInlineForm
from manuscripts.models import *


class UrlInline(admin.TabularInline):
    model = OnlineMaterial
    extra = 1


class InspectionInline(admin.TabularInline):
    model = ManuscriptInspection
    extra = 1


class WishlisthInline(admin.TabularInline):
    model = ReproductionWishlist
    extra = 0


class ContentInline(admin.StackedInline):
    form = ContentInlineForm
    model = ManuscriptContentCommentary
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
        WishlisthInline,
    ]

    list_display = [
        'town',
        'library',
        'shelfmark',
        'number',
        'date',
        'saeculo',
        'origin',
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

admin.site.register(Manuscript, ManuscriptAdmin)
admin.site.register(ManuscriptContentCommentary)
admin.site.register(Reproduction)
admin.site.register(ManuscriptOrigin)
admin.site.register(ReproductionWishlist)
