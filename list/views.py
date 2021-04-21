from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from json import dumps
from typing import List

from map.views import get_locations_from_tags, build_tag_list
from map.models import Location


def index(request: HttpRequest) -> HttpResponse:
    """
    Returns a HTTP response containing a page of a list with all the locations
    in the database and a list of all their tags.

    :param request: The request asking for the view.
    :type request: HttpRequest
    :return: The response containing the list view.
    :rtype: HttpResponse
    """
    recieved_tags = request.GET.get('tags')
    rcv_by_or_for = request.GET.get('by_or_for')
    page = request.GET.get('page', 1)
    if recieved_tags:
        location_list = get_locations_from_tags(recieved_tags)
        tags = build_tag_list(Location.objects.all().values(), recieved_tags)
    else:
        location_list = Location.objects.order_by('title').values()
        tags = build_tag_list(location_list, recieved_tags)

    by_or_for = {'by': True,
                 'for': True}

    if rcv_by_or_for:
       by_or_for = {'by': False,
                    'for': False}
       rcv_by_or_for = rcv_by_or_for.split(',')
       for element in rcv_by_or_for:
           if element == 'by':
               by_or_for['by'] = True;
           elif element == 'for':
               by_or_for['for'] = True;

    paginator = Paginator(location_list, 10)
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)

    tags_json = dumps(tags)

    context = {'locations': locations,
               'there_are_public_locations':
                   there_are_public_locations(location_list),
               'tags': tags,
               'by_or_for': by_or_for,
               'tags_json': tags_json}
    return render(request,
                  'list/index.html',
                  context)


def there_are_public_locations(location_list: List[Location]) -> bool:
    """
    Checks if there are public locations.

    :param location_list: Locations to check.
    :type locaction_list: List[Location]
    :return: True if there are public locations, False if there aren't.
    :rtype: bool
    """
    for location in location_list:
        if location['is_public']:
            return True
    return False
