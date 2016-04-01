from django import forms
from commentaries.models import Commentary, AuthorityText


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentator', 'title', 'title_addon',
                  'commentary_type', 'commentary_on', 'authorship',
                  'date', 'saeculo', 'after', 'before', 'incipit',
                  'explicit', 'note', 'literature', 'edition_coverage',
                  'mora_reference', 'relevance', 'related_commentaries']
        widgets = {
            'incipit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'explicit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }


class AuthorityTextForm(forms.ModelForm):
    class Meta:
        model = AuthorityText
        fields = ['author', 'title', 'title_addon', 'translator', 'date', 'note', 'literature']
