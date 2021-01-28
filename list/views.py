from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from json import dumps
from typing import Dict, List

from map.models import Location
from tagging.models import TaggedItem


def index(request: HttpRequest) -> HttpResponse:
    """
    Returns a HTTP Response containing a page of a list with all the locations
    in the database and a list of all their tags.

    :param request: The request asking for the view.
    :type request: HttpRequest
    :return: The response containing the list view.
    :rtype: HttpResponse
    """
    recieved_tags = request.GET.get('tags')
    page = request.GET.get('page', 1)
    if (recieved_tags):
        location_list = get_locations_from_tags(recieved_tags)
    else:
        location_list = Location.objects.all().values()

    paginator = Paginator(location_list, 10)
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)

    tags = build_tag_list(location_list, recieved_tags)
    tags_json = dumps(tags)

    context = {'locations': locations,
               'there_are_public_locations':
                   there_are_public_locations(location_list),
               'tags': tags,
               'tags_json': tags_json}
    return render(request,
                  'list/index.html',
                  context)


def get_locations_from_tags(recieved_tags: str) -> List[Location]:
    """
    Returns all locations that correspond to the given tags, which are
    contained in a string, seperated by a , character.

    :param recieved_tags: The string containing the tags.
    :type recieved_tags: str
    :return: The locations that match the given tags.
    :rtype: List[Location]
    """
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
    return location_list


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

    recieved_tags = recieved_tags.split(',')

    tag_list = list(set(tag_list))
    tags = []
    for tag in tag_list:
        if (tag):
            if (not recieved_tags or tag in recieved_tags):
                included = True
            else:
                included = False
            tags.append({'name': tag,
                         'included': included})
    return tags
