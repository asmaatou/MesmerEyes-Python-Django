from django import forms
from .models import *

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['postal_code','adress','city']

class OrderRowCreateForm(forms.ModelForm):
    class Meta:
        model = OrderRow
        fields = '__all__'