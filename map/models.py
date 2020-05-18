from django.db import models


class Location(models.Model):
    """
    Data model for the locations and places on the map.
    """
    title = models.CharField(max_length=100, unique=True)

    # location on the world using latitude (x) and longitude (y)
    latitude = models.FloatField()
    longitude = models.FloatField()


    # possible image
    picture = models.ImageField(upload_to='static/pictures/',
                                null=True,
                                blank=True)

    # possible homepage
    homepage = models.URLField(null=True, blank=True)

    # possible address
    address = models.TextField(null=True, blank=True)

    # possible opening hours, for now a simple text field
    # TODO: find a more sophisticated, semantically charged solution
    opening_hours = models.TextField(null=True, blank=True)

    is_public = models.BooleanField(default=False)
