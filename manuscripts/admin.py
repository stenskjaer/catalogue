from django.contrib import admin

from .models import *
from .forms import ManuscriptForm, TextForm

class UrlInline(admin.TabularInline):
    model = OnlineMaterial
    extra = 1


class ContentInline(admin.TabularInline):
    model = ManuscriptContent
    extra = 3


class ManuscriptAdmin(admin.ModelAdmin):
    form = ManuscriptForm
    inlines = [
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
admin.site.register(Inspection)
admin.site.register(Reproduction)
admin.site.register(Archive)



