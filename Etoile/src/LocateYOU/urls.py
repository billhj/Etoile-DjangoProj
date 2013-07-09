'''
Created on Jun 6, 2013

@author: Jing
'''
from django.conf.urls import patterns, url

from LocateYOU import views

urlpatterns = patterns('',
#     url(r'^1$', views.index, name='index'),
    url(r'^outputMapInfo/$', views.outputMapInfo, name='outputMapInfo'),
    url(r'^showlocation/', views.showLocation, name='showLocation'),
    url(r'^$', views.locateU, name='locateU'),
)