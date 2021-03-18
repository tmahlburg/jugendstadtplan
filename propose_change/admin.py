from django.contrib import admin

from .models import ChangeProposal
from map.models import Location


@admin.register(ChangeProposal)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_title', 'location_to_change', 'change_proposal')

    def location_title(self, obj):
        return Location.objects.get(pk=obj.location_to_change.id).title

    location_title.short_description(
        'Ort zu dem eine Änderung vorgeschlagen wurde')
