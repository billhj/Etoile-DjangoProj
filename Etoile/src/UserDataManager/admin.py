'''
Created on 5 juin 2013

@author: huang
'''

from django.contrib import admin
from models import UserInfo
from models import Device
admin.site.register(UserInfo)
admin.site.register(Device)