from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'order_note','payment_method']


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status']
        widgets = {
            'order_status': forms.Select(attrs={'class': 'form-control'})
        }
        