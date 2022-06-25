from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    is_staff=models.BooleanField(default=False)
    name=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    picture=models.ImageField(default='profile2.png',null=True,blank=True)
    def __str__(self):
        return str(self.user)

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    is_staff=models.BooleanField(default=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    job=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    picture=models.ImageField(default='profile2.png',null=True,blank=True)
    def __str__(self):
        return str(self.user)
        
