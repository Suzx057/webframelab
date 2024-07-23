from django import forms
from .models import Video, Author

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'published_date', 'short_detail', 'demo']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'phone', 'joined_date', 'type_author']
