from django import forms
from map.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('title', 'latitude', 'longitude', 'tags', 'description', 'picture',
                  'homepage', 'address', 'opening_hours', 'is_on_placem')
