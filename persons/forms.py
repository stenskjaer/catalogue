from django import forms
from persons.models import Commentator


class CommentatorForm(forms.ModelForm):
    class Meta:
        model = Commentator
        fields = ['name', 'birth', 'death', 'floruit', 'viaf_url', 'note', 'literature', 'attachments']
