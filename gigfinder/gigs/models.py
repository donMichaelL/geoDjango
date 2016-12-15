from __future__ import unicode_literals
from django.contrib.gis.db import models


class Venue(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=200)
    # area[0].coords to get the coords as a tuple
    area = models.PolygonField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    venue = models.ForeignKey(Venue)

    def __str__(self):
        return "%s - %s" % (self.name, self.venue.name)
