from django.shortcuts import render

# understand data structure
from map.models import Location

def index(request):
    all_locations = Location.objects.all().values()
    context = {'all_locations': all_locations}
    return render(request,
                  'list/index.html',
                  context)
