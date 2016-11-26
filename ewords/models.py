from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, time
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday=models.DateField(default=timezone.now)
    hobby=models.TextField(blank=True)
    education=models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
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


class Video(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.TextField()
    youtube = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title



