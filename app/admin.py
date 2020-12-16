from django.contrib import admin
from .models import Restaurant, PaymentMethod, MenuItem, OpeningHours, Location, Category, Order, OrderItem
from django import forms

admin.site.register(PaymentMethod)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)


class MenuItemInline(admin.StackedInline):
    model = MenuItem


class OpeningHoursInline(admin.StackedInline):
    model = OpeningHours


class RestaurantAdminForm(forms.ModelForm):
    model = Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline, OpeningHoursInline]
    filter_horizontal = ['payment_methods']
    form = RestaurantAdminForm


admin.site.register(Restaurant, RestaurantAdmin)
