from django.urls import path

from .views import restaurant, index, category, order

app_name = 'app'


urlpatterns = [
    path('', index, name='index'),
    path('restaurant/<int:restaurant_id>', restaurant, name='restaurant'),
    path('order', order, name='order')
]
