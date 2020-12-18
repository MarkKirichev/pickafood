from django.urls import path

from .views import restaurant, index, delete_order, category

app_name = 'app'


urlpatterns = [
    path('', index, name='index'),
    path('restaurant/<int:restaurant_id>', restaurant, name='restaurant'),
    path('deleteOrder/<int:pk>', delete_order, name='delete'),
]
