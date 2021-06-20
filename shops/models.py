# Create your models here.

from django.contrib.gis.db import models as geomodels
from django.db import models





class Shop(models.Model):

    name = models.CharField(max_length=100)

    location = geomodels.PointField()

    address = models.CharField(max_length=100)

    city = models.CharField(max_length=50)





class Post (models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

  # """ def __str__(self):
   #     return self.latitude
   #"""
