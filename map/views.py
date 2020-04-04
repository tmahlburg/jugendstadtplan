from django.shortcuts import render

from .models import Location


def index(request):
    all_locations = Location.objects.all().values()
    context = {'all_locations': all_locations}
    return render(request,
                  'map/index.html',
                  context)
