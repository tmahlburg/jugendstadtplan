from django.shortcuts import render

from .models import Location


def index(request):
    # TODO: tests
    all_locations = Location.objects.all().values()
    context = {'all_locations': all_locations,
               'all_locations_length': all_locations.count()}
    return render(request,
                  'map/index.html',
                  context)
