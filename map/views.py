from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages

from typing import List, Dict
from json import dumps

from .models import Location
from tagging.models import TaggedItem


def index(request: HttpRequest,
          viewpoint: str =
          '54.08950301403954,13.40512275695801,14') -> HttpResponse:
    """
    Returns a HTTP repsonse with the map view, using all the public locations,
    the given or default viewpoint and all the used tags.

    :param request: The HTTP request asking for the view.
    :type request: HttpRequest
    :param viewpoint: Viewpoint of the map as a string, formatted like this:
                      'lat,long'
    :type viewpoint: str
    :return: The response containing the map view.
    :rtype: HttpResponse
    """
    try:
        viewpoint, zoom = str_to_viewpoint(viewpoint)
    except ValueError:
        messages.error(request,
                       'Die angegebenen Koordinaten sind nicht erreichbar.\n'
                       + 'Karte wird auf den Koordinaten 0, 0 zentriert.')
        viewpoint = [0, 0]
        zoom = 14

    recieved_tags = request.GET.get('tags')

    if (recieved_tags):
        location_list = get_locations_from_tags(recieved_tags)
        tags = build_tag_list(Location.objects.all().values(), recieved_tags)
    else:
        location_list = Location.objects.all().values()
        tags = build_tag_list(location_list, recieved_tags)

    tags_json = dumps(tags)

    context = {'locations': location_list,
               'viewpoint': viewpoint,
               'zoom': zoom,
               'tags': tags,
               'tags_json': tags_json}
    return render(request,
                  'map/index.html',
                  context)


def str_to_viewpoint(viewpoint: str) -> List[float]:
    """
    Creates a viewpoint from a string.

    :param viewpoint: Viewpoint as a string, formatted like this:
        'lat,long,zoom'
    :type viewpoint: str
    :return: Viewpoint as list: [lat, long] and zoom
    :rtype: List[float], int
    """
    # split on ,
    viewpoint = viewpoint.split(',')
    # convert str to float
    viewpoint = [float(coord) for coord in viewpoint]
    if (abs(viewpoint[0]) > 90 or abs(viewpoint[1]) > 90 or viewpoint[2] < 0):
        raise ValueError('Viewpoint is not composed of valid coordinates.')
    return viewpoint[0:2], int(viewpoint[2])


def get_locations_from_tags(recieved_tags: str) -> List[Location]:
    """
    Returns all locations that correspond to the given tags, which are
    contained in a string, seperated by a , character.

    :param recieved_tags: The string containing the tags seperated by
        commas.
    :type recieved_tags: str
    :return: The locations that match the given tags.
    :rtype: List[Location]
    """
    recieved_tags = recieved_tags.split(',')
    location_list = []
    title_list = []
    for tag in recieved_tags:
        locations = (TaggedItem.objects.get_by_model(Location, tag).values())
        for location in locations:
            if location['title'] not in title_list:
                location_list.append(location)
                title_list.append(location['title'])
    location_list = sorted(location_list, key=lambda k: k['title'])
    return location_list


def build_tag_list(locations: List[Location],
                   recieved_tags: str) -> List[Dict[str, bool]]:
    """
    Builds the the list of tags that match any public location.

    :param locations: The list of locations the tags could match.
    :type locations: List[Location]
    :param recieved_tags: Tags that are definitely included.
    :type recieved_tags: str
    :return: All tags and the information if they are included or not.
    :rtype: List[Dict[str, bool]]
    """
    tag_list = []
    for location in locations:
        if location['is_public']:
            tag_list.extend(location['tags'].split(' '))

    tag_list = list(set(tag_list))
    tags = []
    for tag in tag_list:
        if (tag):
            if (not recieved_tags or tag in recieved_tags.split(',')):
                included = True
            else:
                included = False
            tags.append({'name': tag,
                         'included': included})
    return tags
