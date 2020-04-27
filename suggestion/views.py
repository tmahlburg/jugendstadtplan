from django.shortcuts import render
from .forms import LocationForm
from map.models import Location
from django.shortcuts import redirect


def index(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/map')
    else:
        form = LocationForm()
        form.fields['latitude'].initial = lat
        form.fields['longitude'].initial = lng
        context = {'lat': lat,
                   'lng': lng,
                   'form': form}
    return render(request,
                  'suggestion/index.html',
                  context)
