from django import forms
from map.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('title', 'latitude', 'longitude', 'tags', 'picture',
                  'homepage', 'address', 'opening_hours')
