from django import forms
from django.contrib.auth.models import User
from ewords.models import UserProfile
from ewords.models import Quote
from ewords.models import MapUserQuote
from ewords.models import Video
from ewords.models import Article
from ewords.models import Audio


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

class AddtomeForm(forms.ModelForm):

    class Meta:
        model=MapUserQuote
        fields=('user','quote')


class VideoForm(forms.ModelForm):

    class Meta:
        model=Video
        fields = ('title','description','link','youtube','incognito')

class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields = ('title','short_description','description','link','tag','incognito')


class AudioForm(forms.ModelForm):

    class Meta:
        model=Audio
        fields = ('title','file','lyrics_eng', 'lyrics_rus','link','tag','incognito')


