from django import forms
from .models import Manuscript, ManuscriptContentCommentary


class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = ['country', 'town', 'library', 'shelfmark', 'number',
                  'olim', 'date', 'date_earliest', 'date_latest', 'date',
                  'saeculo', 'origin', 'material', 'height', 'width',
                  'folios', 'layout', 'script', 'annotation', 'note',
                  'literature']


class ContentInlineForm(forms.ModelForm):
    class Meta:
        model = ManuscriptContentCommentary
        fields = ['content', 'folios', 'incipit', 'explicit', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'incipit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'explicit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }

