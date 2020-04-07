from django.db import models


class Location(models.Model):
    """
    Data model for the locations and places on the map.
    """
    title = models.CharField(max_length=100, unique=True)

    # location on the world using latitude (x) and longitude (y)
    latitude = models.FloatField()
    longitude = models.FloatField()

    # category of the location
    category = models.CharField(max_length=100)

    # possible image
    has_picture = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='pictures/')
    # if the location has opening hours, set this to true and set the following
    # fields

    # has_opening_hours = models.BooleanField(default=False)
    # TODO: Opening Hours: per day, maybe via an api?

    # TODO: Image?
