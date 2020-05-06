from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from map.models import Location


def index(request):
    page = request.GET.get('page', 1)
    location_list = Location.objects.all().values()
    there_are_public_locations = False
    for location in location_list:
        if location.is_public:
            there_are_public_locations = True
    paginator = Paginator(location_list, 10)
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)

    context = {'locations': locations,
               'there_are_public_locations': there_are_public_locations}
    return render(request,
                  'list/index.html',
                  context)
