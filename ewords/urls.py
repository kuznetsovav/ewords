from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quotations/$', views.quotations, name='quotations'),
    url(r'^video/$', views.quotations, name='video'),
    url(r'^music/$', views.quotations, name='music'),
]