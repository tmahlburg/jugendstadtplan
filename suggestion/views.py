from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

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
            send_mail(subject='[jugendstadtplan]Neuer Ort '
                              + form.cleaned_data['title'],
                      message='Hallo,\n'
                              + 'es wurde ein neuer Ort vorgeschlagen: "'
                              + form.cleaned_data['title'] + '"\n'
                              + 'In dieser Liste kann der Vorschlag angesehen '
                              + 'werden:\n'
                              + 'https://'
                              + request.get_host()
                              + '/admin/map/location/',
                      from_email=None,
                      recipient_list=[''],
                      fail_silently=False,
                     )
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
