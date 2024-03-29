from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import ChangeProposalForm
from map.models import Location


def index(request: HttpRequest) -> HttpResponse:
    """
    This function handles the propose_change view. It returns the form to
    propose a change, if it gets called with an HTTP-GET-request and a redirect
    to the 'map'-view, if it gets called with an HTTP-POST-request.

    :param request: The request this view gets called with.
    :type request: HttpRequest
    :return: An HTTP response with the form to propose a change or to redirect
             to the 'map' view.
    :rtype: HttpResponse
    """
    location_id = request.GET.get('id')
    if request.method == 'POST':
        form = ChangeProposalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/map')
    # it's a GET request
    form = ChangeProposalForm()
    form.fields['location_to_change'].initial = location_id

    location_title = ''
    if (location_id):
        location_title = Location.objects.get(pk=location_id).title

    context = {'location_id': location_id, 'location_title': location_title, 'form': form}
    return render(request, 'propose_change/index.html', context)
