from django.contrib import admin

from .models import Text, Author, Manuscript, Country, Town, Library, Inspection, Reproductions, Archive
from .forms import ManuscriptForm, TextForm

class ManuscriptAdmin(admin.ModelAdmin):
    form = ManuscriptForm

class TextAdmin(admin.ModelAdmin):
    form = TextForm

admin.site.register(Text, TextAdmin)
admin.site.register(Author)
admin.site.register(Manuscript, ManuscriptAdmin)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Library)
admin.site.register(Inspection)
admin.site.register(Reproductions)
admin.site.register(Archive)



