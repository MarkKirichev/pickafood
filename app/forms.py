from django import forms

from app.models import Order


class RestaurantOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'date',
            'time',
            'number_of_people',
            'name',
            'telephone_number',
            'email'
        ]
