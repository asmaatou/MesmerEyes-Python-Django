from django.db import models

gender=(
    ("W","Women"),
    ("M","Men"),
    ("M/W","Both"),
)

Rating=(
    ("1","one star"),
    ("2","two stars"),
    ("3","three stars"),
    ("4","four stars"),
    ("5","five stars"),
)

class Categories(models.Model):
    Name_cat=models.CharField(max_length=30)
    Desc_cat=models.CharField(max_length=300)

    def __str__(self):
        return self.Name_cat
    
    
class Brand(models.Model):
    Name_gam=models.CharField(max_length=30)
    Desc_gam=models.CharField(max_length=300)
    img_brand=models.ImageField(upload_to='brand/',null=True,blank=True)

    def __str__(self):
        return self.Name_gam


class Product(models.Model):
    Name_prod=models.CharField(max_length=20)
    Price=models.FloatField(blank=True)
    Desc_prod=models.TextField(max_length=1000,blank=True)
    Details=models.TextField(max_length=1000,blank=True)
    img_prod=models.ImageField(upload_to="products/",null=True,blank=True)
    nbr_stock=models.IntegerField()
    Gender=models.CharField(max_length=100, choices = gender , blank=True)
    Rating=models.CharField(max_length=100,choices = Rating, blank=True)
    is_sale = models.BooleanField(default=False)
    id_cat=models.ForeignKey(Categories,on_delete=models.CASCADE)
    id_ga=models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name_prod


class Album_images(models.Model):
    img=models.ImageField(upload_to='Others/',null=True)
    title=models.CharField(max_length=20,blank=True)
    id_product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
