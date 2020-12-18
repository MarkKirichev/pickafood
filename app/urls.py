from django.urls import path

from .views import restaurant, index, orderItem, category, order

app_name = 'app'


urlpatterns = [
    path('', index, name='index'),
    path('restaurant/<int:restaurant_id>', restaurant, name='restaurant'),
    # make it a DELETE view on order/id
    path('order/<int:pk>', orderItem, name='orderItem'),
    path('order', order, name='order')
]
