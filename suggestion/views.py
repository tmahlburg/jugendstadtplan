from django.shortcuts import render
from .forms import LocationForm


def index(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    form = LocationForm()
    context = {'lat': lat,
               'lng': lng,
               'form': form}
    return render(request,
                  'suggestion/index.html',
                  context)
