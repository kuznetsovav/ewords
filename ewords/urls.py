from django.conf.urls import url
from . import views
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^idioms/$', views.quotations, name='quotations'),
    url(r'^video/$', views.video, name='video'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^idioms/new/$', views.quotations_new, name='quotations_new'),
    url(r'^profile/$', views.profile, name='profile'),
]
