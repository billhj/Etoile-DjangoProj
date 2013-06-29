'''
Created on Jun 6, 2013

@author: Jing
'''
from django.conf.urls import patterns, url

from Authentication import views

urlpatterns = patterns('',
    url(r'^$', views.login_view, name='login_view'),
)