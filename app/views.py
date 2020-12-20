from django.shortcuts import render, redirect

from users.models import Profile
from .models import Restaurant, Order, MenuItem, Category, OrderItem
from .forms import RestaurantOrderForm
from django.views.generic import ListView
from users.additional_functionality import validate_order_input
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


def remove_order(request, pk):
    order_for_deletion = Order.objects.get(pk=pk)
    order_items_for_deletion = order_for_deletion.orderitem_set.all()
    [item.delete() for item in order_items_for_deletion]
    order_for_deletion.delete()
    return redirect('profile')


def category(request, slug):
    menu_items_per_category = MenuItem.objects.filter(category__slug=slug)
    try:
        category = Category.objects.get(slug=slug)
    except:
        raise Http404("Category does not exist")

    context = {
        'categories': menu_items_per_category,
        'restaurants': Restaurant.objects.all(),
        'category': category
    }

    return render(request, 'app/category.html', context)


def order(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)
        #redirect('profile')
        is_data_valid = validate_order_input(json_data)
        if is_data_valid:
            cart_items_dict = json_data['cart']['items'].values()

            if len(cart_items_dict) == 0:
                raise Http404("You cannot order 0 items!")

            restaurant = Restaurant.objects.get(name=json_data['restaurant'])
            profile = Profile.objects.get(user__username=json_data['user'])
            proper_date = str(json_data['date'])[6:] + '-' + json_data['date'][3:5] + '-' + json_data['date'][0:2]

            new_order = Order(date=proper_date,
                              time=json_data['time'],
                              number_of_people=json_data['peopleNumber'],
                              name=json_data['names'],
                              telephone_number=json_data['phoneInput'],
                              email=json_data['emailInput'],
                              order_restaurant=restaurant,
                              order_profile=profile)
            new_order.save()

            for order_item in cart_items_dict:
                new_order_item = OrderItem(name=MenuItem.objects.get(name=order_item['name']),
                                           user_order=new_order,
                                           number_ordered=int(order_item['count']))
                new_order_item.save()

            # redirect('profile')
            return HttpResponse('Success')
        else:
            raise Http404("Wrong data dimensions for order!")
        # or if there is an issue with the data return 400 error'''
    return HttpResponse("Didn't get JSON data")
