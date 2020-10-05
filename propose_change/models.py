from django.db import models
from tagging.fields import TagField


class ChangeProposal(models.Model):
    """
    Data model for the locations and places on the map. Change proposal edition.
    """
    title = models.CharField(max_length=100, unique=True, verbose_name='Name')

    # location on the world using latitude (x) and longitude (y)
    latitude = models.FloatField()
    longitude = models.FloatField()

    tags = TagField()

    # possible image
    picture = models.ImageField(upload_to='static/pictures/',
                                null=True,
                                blank=True,
                                verbose_name='Bild')

    # possible homepage
    homepage = models.URLField(null=True,
                               blank=True,
                               verbose_name='Internetpräsenz')

    # possible address
    address = models.TextField(null=True, blank=True, verbose_name='Adresse')

    # possible opening hours, for now a simple text field
    # TODO: find a more sophisticated, semantically charged solution
    opening_hours = models.TextField(null=True,
                                     blank=True,
                                     verbose_name='Öffnungszeiten')

    is_public = models.BooleanField(default=False,
                                    verbose_name='Veröffentlicht')
