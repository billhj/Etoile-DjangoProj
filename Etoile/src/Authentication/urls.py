'''
Created on Jun 6, 2013

@author: Jing
'''
from django.conf.urls import patterns, url

from Authentication import views

urlpatterns = patterns('',
    url(r'^authenticate/$', views.authenticate_view, name='authenticate_view'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^loggedin/', views.loggedin_view, name='loggedin_view'),
    url(r'^invalid/', views.invalid_view, name='invalid_view'),
)