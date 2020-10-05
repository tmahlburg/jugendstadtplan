from django.shortcuts import render
from django.contrib import messages

from .models import Location
from tagging.models import TaggedItem

def index(request, viewpoint='54.095166,13.3710154'):
    try:
        viewpoint = str_to_viewpoint(viewpoint)
    except ValueError:
        messages.error(request,
                       'Die angegebenen Koordinaten sind nicht erreichbar.\n'
                       + 'Karte wird auf den Koordinaten 0, 0 zentriert.')
        viewpoint = [0, 0]

    recieved_tags = request.GET.get('tags')

    if (recieved_tags):
        recieved_tags = recieved_tags.split(',')
        location_list = []
        title_list = []
        for tag in recieved_tags:
            locations = (TaggedItem.objects.get_by_model(Location,
                                                         tag).values())
            for location in locations:
                if location['title'] not in title_list:
                    location_list.append(location)
                    title_list.append(location['title'])
    else:
        location_list = Location.objects.all().values()

    tag_list = Location.tags.split(' ')
    tags = []
    for tag in tag_list:
        if (not recieved_tags or tag in recieved_tags):
            included = True
        else:
            included = False
        tags.append({'name': tag,
                     'included': included})


    context = {'locations': location_list,
               'viewpoint': viewpoint,
               'tags': tag_list}
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
    if (abs(viewpoint[0]) > 90 or abs(viewpoint[1]) > 90):
        raise ValueError('Viewpoint is not composed of valid coordinates.')
    return viewpoint
