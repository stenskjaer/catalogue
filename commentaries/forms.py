from django import forms
from commentaries.models import Text


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['author', 'title', 'title_addon', 'text_type',
                  'commentary_type', 'commentary_on', 'authorship',
                  'date', 'saeculo', 'after', 'before', 'incipit',
                  'explicit', 'note', 'literature', 'edition_coverage',
                  'mora_reference', 'relevance', 'related_commentaries']
        widgets = {
            'incipit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'explicit': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }

    text_type = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=Text.TEXT_CHOICES)
