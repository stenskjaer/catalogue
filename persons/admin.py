from django.contrib import admin
from persons.forms import CommentatorForm
from persons.models import Authority, Translator, Commentator
from commentaries.admin import CommentariesInline, AlternativeAuthorInline


class CommentatorAdmin(admin.ModelAdmin):
    form = CommentatorForm
    inlines = [
        CommentariesInline,
        AlternativeAuthorInline,
    ]


admin.site.register(Authority)
admin.site.register(Translator)
admin.site.register(Commentator, CommentatorAdmin)