from django.conf.urls import patterns, include, url
from  django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$',direct_to_template , { 'template': 'index.html' } ),
     url(r'^index.htm$',direct_to_template , { 'template': 'index.html' } ),
    # url(r'^mandb/', include('mandb.foo.urls')),
     url('^by_name/(?P<name>\w+)/$','mandb.views.by_name'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
