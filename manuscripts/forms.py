from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Manuscript, Commentary

class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = '__all__'
        widgets = {
            'content': FilteredSelectMultiple('Commentary', False),
            'reproductions': FilteredSelectMultiple('Commentary', False),
        }


class TextForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = '__all__'
        widgets = {
            'incipit': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'explicit': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'source': FilteredSelectMultiple('Manuscript', True),
        }

