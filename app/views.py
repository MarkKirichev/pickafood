from django.shortcuts import render, redirect
from .models import Restaurant, Order, MenuItem, Category
from .forms import RestaurantOrderForm
from django.views.generic import ListView
from users.additional_functionality import get_restaurant_name


from django.http import HttpResponse, Http404


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


def delete_order(request, pk):
    order_for_deletion = Order.objects.get(pk=pk)
    order_items_for_deletion = order_for_deletion.orderitem_set.all()
    [item.delete() for item in order_items_for_deletion]
    order_for_deletion.delete()
    return redirect('profile')


def category(request, slug):
    slug_category_items = [item for item in MenuItem.objects.all() if get_restaurant_name(item.category.name) == slug]
    context = {
        'categories': slug_category_items,
        'restaurants': Restaurant.objects.all(),
        'range': range(50),
    }

    [print(item.name) for item in context['categories']]

    return render(request, 'app/category.html', context)
