from django.shortcuts import render, redirect
from .models import Restaurant, Order, MenuItem, Category
from .forms import RestaurantOrderForm
from django.views.generic import ListView
from users.additional_functionality import get_restaurant_name
import json

from django.http import HttpResponse, Http404, HttpResponseServerError
from django.views import View


def index(request):
    context = {
        'restaurants': Restaurant.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'app/index.html', context)


def restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    context = {
        'restaurant': restaurant,
        'restaurants': Restaurant.objects.all(),
        'form': RestaurantOrderForm(),
    }

    return render(request, 'app/restaurant.html', context)


def orderItem(request, pk):
    if request.method == "DELETE":
        order_for_deletion = Order.objects.get(pk=pk)
        order_items_for_deletion = order_for_deletion.orderitem_set.all()
        [item.delete() for item in order_items_for_deletion]
        order_for_deletion.delete()
        return redirect('profile')


def category(request, slug):
    slug_category_items = MenuItem.objects.filter(category__slug=slug)
    context = {
        'categories': slug_category_items,
        'restaurants': Restaurant.objects.all(),
    }

    [print(item) for item in context['categories']]

    return render(request, 'app/category.html', context)


def order(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        # Create order record from json data
        # or if there is an issue with the data return 400 error
        return HttpResponse("Got json data")