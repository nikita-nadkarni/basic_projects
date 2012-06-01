from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noncmsproject.views.home', name='home'),
    # url(r'^noncmsproject/', include('noncmsproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^index/$', 'firstapp.views.index'),
    url(r'^books/$', 'firstapp.views.book_view'),
    # Uncomment the next line to enable the admin:
    
    url(r'^admin/', include(admin.site.urls)),
    
)
