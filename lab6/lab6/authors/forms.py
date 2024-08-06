# authors/forms.py

from django import forms
from django.forms import modelformset_factory
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name' ,'video_title']

AuthorFormSet = modelformset_factory(Author, form=AuthorForm, extra=2)