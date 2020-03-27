from django.db import models


class Location(models.Model):
    """
    Data model for the locations and places on the map.
    """
    title = models.CharField(max_length=100)

    # location on the world using latitude (x), longitude (y) and altitude(z)
    # (altitude in relation to sea level)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.SmallIntegerField(default=0)

    # if the location has opening hours, set this to true and set the following
    # fields

    # has_opening_hours = models.BooleanField(default=False)
    # TODO: Opening Hours: per day, maybe via an api?

    # TODO: Image?
