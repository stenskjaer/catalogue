from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Manuscript, Text, Inspection

class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = '__all__'
        widgets = {
            'inspections': FilteredSelectMultiple('Inspection', False),
            'content': FilteredSelectMultiple('Text', False),
            'reproductions': FilteredSelectMultiple('Text', False),
        }


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'
        widgets = {
            'source': FilteredSelectMultiple('Manuscript', True),
        }

