from django.db import models
from tagging.fields import TagField

from map.models import Location

class ChangeProposal(models.Model):
    """
    Data model for proposals to change existing places.
    """

    location_to_change = models.ForeignKey(Location, on_delete=models.CASCADE)

    change_proposal = models.TextField(verbose_name='Was sollte hier anders sein?')
