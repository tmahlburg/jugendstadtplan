from django import forms
from map.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('title', 'latitude', 'longitude', 'tags', 'description', 'picture',
                  'homepage', 'facebook', 'instagram', 'tiktok', 'twitter', 'address', 'opening_hours', 'is_on_placem')
        help_texts = {
            'tags': ('Hier kannst du Tags eintragen, die den Ort einordnen. Willst du ein Kino eintragen? Schreib "kino". Ist der Ort ein Treffpunkt? Schreib "treff". Kann man dort außerdem auch Musik machen? Schreib "treff musik". Tags sollten vollständig klein geschrieben werden und mehrere Tags werden durch Leerzeichen getrennt.')
       }
