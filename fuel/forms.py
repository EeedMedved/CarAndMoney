from django import forms

from .models import Refill


class RefillForm(forms.ModelForm):
    class Meta:
        model = Refill
        fields = ('refillDate', 'mileage', 'liters', 'gas_station', 'price', 'comment')
