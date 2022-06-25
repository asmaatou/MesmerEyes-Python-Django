from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class CustomerFormCustomer(ModelForm):
    class Meta:
        model= Customer
        fields = '__all__'
        exclude = ['user']

class AdminForm(ModelForm):
    class Meta:
        model= Admin
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

