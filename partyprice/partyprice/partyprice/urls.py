# coding=UTF-8

from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('party_bl.urls')),
    # Examples:
    # url(r'^$', 'partyprice.views.home', name='home'),
    # url(r'^partyprice/', include('partyprice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)
