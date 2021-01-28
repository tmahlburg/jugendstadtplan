from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import LocationForm


def index(request: HttpRequest) -> HttpResponse:
    """
    This returns a page with the form to suggest a new location, if the given
    request is a 'GET', and it saves the given suggestion to the database and
    returns to the map view, if the request is a 'POST'.

    :param request: The HTTP request by which the view is requested.
    :type request: HttpRequest
    :return: The HTTP response with the suggestion page or the response
             redirecting to the 'map' view.
    :rtype: HttpResponse
    """
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/map')
    # if the request is a 'GET'
    form = LocationForm()
    form.fields['latitude'].initial = lat
    form.fields['longitude'].initial = lng
    context = {'lat': lat,
               'lng': lng,
               'form': form}
    return render(request,
                  'suggestion/index.html',
                  context)
