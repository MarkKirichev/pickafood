from django.urls import path

from . import views
app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/<int:restaurant_id>', views.restaurant, name='restaurant'),
]
