from django import forms
from .models import Manuscript, Commentary, Commentator, AuthorityText

class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = '__all__'


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = [ 'commentator', 'title', 'title_addon',
                   'commentary_type', 'commentary_on', 'authorship', 'date',
                   'after', 'before', 'incipit', 'explicit', 'note',
                   'literature', 'mora_reference', 'relevance']
        widgets = {
            'incipit': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'explicit': forms.Textarea(attrs={'rows':2, 'cols':40}),
        }

        
class AuthorityForm(forms.ModelForm):
    class Meta:
        model = AuthorityText
        fields = ['author', 'title', 'title_addon', 'translator', 'date', 'note', 'literature']
        

class CommentatorForm(forms.ModelForm):
    class Meta:
        model = Commentator
        fields = ['name', 'birth', 'death', 'floruit', 'note', 'literature']
