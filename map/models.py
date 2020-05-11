from django.db import models


class LocationCategory(models.Model):
    """
    Data model for the categories of the locations and places.
    """
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{}".format(self.title)


class Location(models.Model):
    """
    Data model for the locations and places on the map.
    """
    title = models.CharField(max_length=100, unique=True)

    # location on the world using latitude (x) and longitude (y)
    latitude = models.FloatField()
    longitude = models.FloatField()

    # TODO: have a extensible list of locations (-> drop down menu)
    # category of the location
    category = models.ForeignKey(LocationCategory, on_delete=models.CASCADE)

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
