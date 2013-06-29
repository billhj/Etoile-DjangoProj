'''
Created on Jun 6, 2013

@author: Jing
'''
from django.conf.urls import patterns, url

from Publications import views

urlpatterns = patterns('',
    url(r'^1$', views.index, name='index'),
    url(r'^$', views.outputPublications, name='outputPublications'),
)