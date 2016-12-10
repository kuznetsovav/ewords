from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, time
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday=models.DateField(default=timezone.now)
    hobby=models.TextField(blank=True)
    education=models.TextField(blank=True)
    picture = models.ImageField(upload_to='ewords/static/images', blank=True)
    created_date=models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.birthday)


class Quote(models.Model):
    author = models.ForeignKey('auth.User')
    category = models.CharField(max_length=200)
    eng_text = models.TextField()
    eng_author = models.CharField(max_length=200)
    rus_text = models.TextField()
    rus_author = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    incognito = models.BooleanField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.eng_author

class MapUserQuote(models.Model):
    user=models.CharField(max_length=200)
    quote=models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)


class Video(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.TextField()
    youtube = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    incognito = models.BooleanField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    short_description = HTMLField(max_length=500)
    description = HTMLField()
    link = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    incognito = models.BooleanField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Audio(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='ewords/ewords/static/audio')
    lyrics_eng = HTMLField()
    lyrics_rus = HTMLField()
    link = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    incognito = models.BooleanField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title




