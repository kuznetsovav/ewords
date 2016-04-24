from django.shortcuts import render
from .models import MainQuote
from django.utils import timezone
import datetime

def index(request):
    return render(request, 'ewords/index.html', {})

def index(request):
    mainquotes = MainQuote.objects.all().filter(created_date=datetime.date.today())
    return render(request, 'ewords/index.html', {'mainquotes': mainquotes})

def quotations(request):
    return render(request, 'ewords/quotations.html', {})

def video(request):
    return render(request, 'ewords/video.html', {})

def music(request):
    return render(request, 'ewords/music.html', {})
