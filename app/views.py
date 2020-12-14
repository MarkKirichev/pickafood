from django.shortcuts import render
from .models import Restaurant

from django.http import HttpResponse, Http404
from django.template import loader


def index(request):
    return render(request, 'app/index.html')


def restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    return render(request, 'app/restaurant.html', {'restaurant': restaurant})
