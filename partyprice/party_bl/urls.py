# coding=UTF-8
from django.conf.urls import patterns, url

from party_bl import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)