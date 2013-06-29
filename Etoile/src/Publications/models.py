from django.db import models

# Create your models here.
class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 60, unique = True)
    authors = models.CharField(max_length = 500, blank=True)
    journal = models.CharField(max_length = 500, blank=True)
    coverimagepath = models.CharField(max_length = 100, blank=True)
    year = models.DateField(blank=True)
    abstract = models.CharField(max_length = 2000, blank=True)
    citation = models.CharField(max_length = 500, blank=True)
    bibtex = models.CharField(max_length = 500, blank=True)
    
    def getId(self):
        return id
    
    def __unicode__(self):
        return self.name
    
