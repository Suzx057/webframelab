from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['citizenid', 'firstname', 'lastname', 'expire_date', 'blood_type']