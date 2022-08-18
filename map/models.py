from django.db import models
from tagging.fields import TagField


class Location(models.Model):
    """
    Data model for the locations and places on the map.
    """
    title = models.CharField(max_length=100, unique=True, verbose_name='Name')

    # location on the world using latitude (x) and longitude (y)
    latitude = models.FloatField()
    longitude = models.FloatField()

    tags = TagField()

    # short description, why the location should be on the map
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Was macht diesen Ort besonders?')

    # possible image
    picture = models.ImageField(upload_to='static/pictures/',
                                null=True,
                                blank=True,
                                verbose_name='Bild')

    # possible homepage
    homepage = models.URLField(null=True,
                               blank=True,
                               verbose_name='Homepage')

    # possible facebook
    facebook = models.URLField(null=True,
                               blank=True,
                               verbose_name='Facebook')
    # possible instagram
    instagram = models.URLField(null=True,
                                blank=True,
                                verbose_name='Instagram')

    # possible tiktok
    tiktok = models.URLField(null=True,
                             blank=True,
                             verbose_name='TikTok')

    # possible twitter
    twitter = models.URLField(null=True,
                              blank=True,
                              verbose_name='Twitter')

    # possible address
    address = models.TextField(null=True, blank=True, verbose_name='Adresse')

    # possible opening hours, for now a simple text field
    # TODO: find a more sophisticated, semantically charged solution
    opening_hours = models.TextField(null=True,
                                     blank=True,
                                     verbose_name='Öffnungszeiten')

    is_on_placem = models.BooleanField(blank=True,
                                       verbose_name='Dieser Ort ist auf PLACEm zu finden')

    is_public = models.BooleanField(default=False,
                                    verbose_name='Veröffentlicht')
