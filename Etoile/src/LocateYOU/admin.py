'''
Created on 5 juin 2013

@author: huang
'''

from django.contrib import admin
from models import WorldBorder
from models import DeviceLocation
admin.site.register(WorldBorder)
admin.site.register(DeviceLocation)