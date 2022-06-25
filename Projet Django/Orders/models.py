from django.db import models
from mesmerEyesApp.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

ORDER_STATUS = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered')
)

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ManyToManyField(Product, through='OrderRow')
    status = models.CharField(max_length=120,
                              choices=ORDER_STATUS,
                              default='created')
    order_date = models.DateTimeField(auto_now_add=True)
    postal_code=models.CharField(max_length=20,null=True)
    adress=models.CharField(max_length=250,null=True)
    city=models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.pk)

class OrderRow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity=models.FloatField(blank=True)
    amount=models.FloatField(blank=True)

    def __str__(self):
        return "OrderRow n° "+str(self.pk) 
