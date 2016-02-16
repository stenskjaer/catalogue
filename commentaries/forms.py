from django import forms
from commentaries.models import Commentary, Commentator, AuthorityText


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentator', 'title', 'title_addon',
                  'commentary_type', 'commentary_on', 'authorship',
                  'date', 'saeculo', 'after', 'before', 'incipit',
                  'explicit', 'note', 'literature', 'mora_reference',
                  'relevance', 'related_commentaries']
        widgets = {
            'incipit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'explicit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }


class CommentatorForm(forms.ModelForm):
    class Meta:
        model = Commentator
        fields = ['name', 'birth', 'death', 'floruit', 'note', 'literature']


class AuthorityForm(forms.ModelForm):
    class Meta:
        model = AuthorityText
        fields = ['author', 'title', 'title_addon', 'translator', 'date', 'note', 'literature']