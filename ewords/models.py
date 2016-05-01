from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, time

class MainQuote(models.Model):
    author = models.ForeignKey('auth.User')
    eng_text = models.TextField()
    eng_author = models.CharField(max_length=200)
    rus_text = models.TextField()
    rus_author = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.eng_author


class Quote(models.Model):
    author = models.ForeignKey('auth.User')
    eng_text = models.TextField()
    eng_author = models.CharField(max_length=200)
    rus_text = models.TextField()
    rus_author = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.eng_author


