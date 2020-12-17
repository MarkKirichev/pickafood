from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from app.models import Restaurant, Order, OrderItem
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account with {username} has now been created! You\'re now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/index.html',
                  {
                      'form': form,
                      'restaurants': Restaurant.objects.all()
                  })


'''
Types of messages:
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    restaurants = Restaurant.objects.all()
    # user_order = Order.objects.get(order_profile=request.user.profile)

    context = {
          'user_form': user_form,
          'profile_form': profile_form,
          'restaurants': restaurants,
    }

    if not request.user.profile.is_restaurant_admin_profile == '':
        return render(request, 'users/admin_profile.html', context)
    else:
        user_order = Order.objects.filter(order_profile=request.user.profile)
        current = 0
        for current_order in user_order:
            orders = [item for item in OrderItem.objects.all() if item.user_order == current_order]
            current_str = "order_number_" + str(current)
            context[current_str] = orders
            current += 1
            # print(current_str)
            context['range'] = range(5)
        return render(request, 'users/common_profile.html', context)

'''
@login.required
def order_create(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user_order = request.user.profile
            return redirect('restaurant')
    else:
        form = CreateOrderForm()
    return render(request, 'index', {'form': form})
'''