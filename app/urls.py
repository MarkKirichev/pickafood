from django.urls import path

from . import views
from users import views as users_views
app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/<int:restaurant_id>', views.restaurant, name='restaurant'),
    path('register/', users_views.register, name='register'),
]
