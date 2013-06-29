from django.db import models
from django import forms


# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = (
                      ('M', 'Male'),
                      ('F', 'Female'),
                      )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    sex = models.CharField(verbose_name=u"Sex", max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    mobilephone = models.CharField(max_length=30, blank=True)
    workaddress = models.CharField(max_length=50, blank=True)
    workcity = models.CharField(max_length=60, blank=True)
    workstate_province = models.CharField(max_length=30, blank=True)
    workcountry = models.CharField(max_length=50, blank=True)
    workphone = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    personalstatement = models.CharField(max_length=2000, blank=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    def getId(self):
        return id
    
    def __unicode__(self):
        return self.email