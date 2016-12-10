from django.conf.urls import url
from . import views
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^idioms/$', views.quotations, name='quotations'),
    url(r'^video/$', views.video, name='video'),
    url(r'^video/new/$', views.video_new, name='video_new'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/new/$', views.articles_new, name='articles_new'),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.articles_detail, name='articles_detail'),
    url(r'^audio/$', views.audio, name='audio'),
    url(r'^audio/new/$', views.audio_new, name='audio_new'),
    url(r'^audio/(?P<pk>[0-9]+)/$', views.audio_detail, name='audio_detail'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^idioms/new/$', views.quotations_new, name='quotations_new'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^tinymce/', include('tinymce.urls')),
]
