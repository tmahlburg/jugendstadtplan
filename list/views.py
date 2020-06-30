from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from map.models import Location
from tagging.models import TaggedItem


def index(request):
    recieved_tags = request.GET.get('tags')
    page = request.GET.get('page', 1)
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
    there_are_public_locations = False
    for location in location_list:
        if location['is_public']:
            there_are_public_locations = True
    paginator = Paginator(location_list, 10)
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)
    tag_list = Location.tags.split(' ')
    tags = []
    for tag in tag_list:
        if (not recieved_tags or tag in recieved_tags):
            included = True
        else:
            included = False
        tags.append({'name': tag,
                     'included': included})

    context = {'locations': locations,
               'there_are_public_locations': there_are_public_locations,
               'tags': tags}
    return render(request,
                  'list/index.html',
                  context)
