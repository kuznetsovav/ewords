from django import forms
from django.contrib.auth.models import User
from ewords.models import UserProfile
from ewords.models import Quote

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthday', 'hobby', 'education')

class QuoteForm(forms.ModelForm):

    class Meta:
        model=Quote
        fields = ('category','eng_text','eng_author','rus_text','rus_author','image_link','incognito')