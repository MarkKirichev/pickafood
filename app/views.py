from django.shortcuts import render, redirect
from .models import Restaurant, Order, MenuItem, Category, OrderItem
from .forms import RestaurantOrderForm
from django.views.generic import ListView
from users.additional_functionality import check_for_everything
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
    try:
        category = Category.objects.get(slug=slug)
    except:
        raise Http404("Category does not exist")

    context = {
        'categories': slug_category_items,
        'restaurants': Restaurant.objects.all(),
        'category': category
    }

    return render(request, 'app/category.html', context)


def order(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        redirect('profile')
        '''check = check_for_everything(json_data)
        if check:
            cart_items_dict = json_data['cart']['items'].values()

            if len(cart_items_dict) == 0:
                raise Http404("You cannot order 0 items!")

            new_order = Order(date=json_data['date'],
                              time=json_data['time'],
                              number_of_people=json_data['peopleNumber'],
                              name=json_data['names'],
                              telephone_number=json_data['phoneInput'],
                              email=json_data['emailInput'],
                              order_restaurant=...,
                              order_profile=...)
            new_order.save()

            for order_item in cart_items_dict:
                new_order_item = OrderItem(name=order_item['name'],
                                           user_order=new_order,
                                           number_ordered=order_item['count'])
                new_order_item.save()

            redirect('profile')
        else:
            print(json_data)
            raise Http404("Wrong data dimensions for order!")
        # or if there is an issue with the data return 400 error'''
    return HttpResponse("Didn't get JSON data")
