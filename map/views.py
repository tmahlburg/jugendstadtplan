from django.shortcuts import render

from .models import Location


def index(request, viewpoint='54.095166,13.3710154'):
    all_locations = Location.objects.all().values()
    viewpoint = str_to_viewpoint(viewpoint)
    context = {'all_locations': all_locations,
               'viewpoint': viewpoint}
    return render(request,
                  'map/index.html',
                  context)


def str_to_viewpoint(viewpoint):
    """
    Creates a viewpoint from a string.
    :param viewpoint: Viewpoint as a string, formatted like this: 'lat,long'
    :return: Viewpoint as list: [lat, long]
    """
    # split on ,
    viewpoint = viewpoint.split(',')
    # convert str to float
    viewpoint = [float(coord) for coord in viewpoint]

    return viewpoint
