from django.contrib import admin

from .models import *
from .forms import ManuscriptForm, TextForm

class UrlInline(admin.TabularInline):
    model = OnlineMaterial
    extra = 1

class InspectionInline(admin.TabularInline):
    model = ManuscriptInspection
    extra = 1

class ContentInline(admin.TabularInline):
    model = ManuscriptContent
    extra = 1


class ManuscriptAdmin(admin.ModelAdmin):
    form = ManuscriptForm
    inlines = [
        InspectionInline,
        UrlInline,
        ContentInline,
    ]


class TextAdmin(admin.ModelAdmin):
    form = TextForm

admin.site.register(Text, TextAdmin)
admin.site.register(Author)
admin.site.register(Manuscript, ManuscriptAdmin)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Library)
admin.site.register(Reproduction)
admin.site.register(Archive)



