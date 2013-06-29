from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Etoile.views.home', name='home'),
    # url(r'^Etoile/', include('Etoile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/', include('Authentication.urls')),
    url(r'^map/', include('LocateYOU.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^publications/', include('Publications.urls')),
    url(r'^$', include('PersonalSite.urls')),
)
