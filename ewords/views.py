from django.shortcuts import render
from .models import Quote
from .models import Video
from django.utils import timezone
import datetime

def index(request):
    return render(request, 'ewords/index.html', {})

def index(request):
    quotes = Quote.objects.all().filter(day_quote=True)
    return render(request, 'ewords/index.html', {'quotes': quotes})

def quotations(request):
    return render(request, 'ewords/quotations.html', {})

def quotations(request):
    quotes = Quote.objects.all()
    return render(request, 'ewords/quotations.html', {'quotes': quotes})

def video(request):
    return render(request, 'ewords/video.html', {})

def video(request):
    videos = Video.objects.all()
    return render(request, 'ewords/video.html', {'videos': videos})

