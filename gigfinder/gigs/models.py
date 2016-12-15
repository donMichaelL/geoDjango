from __future__ import unicode_literals
from django.contrib.gis.db import models


class Venue(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()


class Event(models.Model):
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    venue = models.ForeignKey(Venue)
