from django import forms
from .models import Manuscript


class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = ['country', 'town', 'library', 'shelfmark', 'number',
                  'olim', 'date', 'date_earliest', 'date_latest', 'date',
                  'saeculo', 'origin', 'material', 'height', 'width',
                  'folios', 'layout', 'script', 'annotation', 'note',
                  'literature']
