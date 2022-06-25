from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/',Proceed_To_Checkout,name="checkout"),
]
