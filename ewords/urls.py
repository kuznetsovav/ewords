from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quotations/$', views.quotations, name='quotations'),
    url(r'^video/$', views.video, name='video'),
]