from django.shortcuts import render
from .models import Restaurant

from django.http import HttpResponse, Http404


def index(request):

    context = {
        'restaurants': Restaurant.objects.all()
    }

    return render(request, 'app/index.html', context)


def restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    return render(request, 'app/restaurant.html',
                  {
                      'restaurant': restaurant,
                      'restaurants': Restaurant.objects.all()
                  })
