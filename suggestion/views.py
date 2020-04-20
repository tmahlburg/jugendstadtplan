from django.shortcuts import render


def index(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    context = {'lat': lat,
               'lng': lng}
    return render(request,
                  'suggestion/index.html',
                  context)
