from .models import *
from django import forms

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = '__all__'


class CategoriesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Categories
        fields = '__all__'


class BrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Brand
        fields = '__all__'
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Album_images
        fields = '__all__'