from django.shortcuts import render

from .models import Location


def index(request, viewpoint=[54.095166, 13.3710154]):
    all_locations = Location.objects.all().values()
    context = {'all_locations': all_locations,
               'viewpoint': viewpoint}
    return render(request,
                  'map/index.html',
                  context)
