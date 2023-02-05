from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to = "buyer/", blank=True, null=True )

class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="seller/", blank = True, null = True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="images", default="")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True )


class Stock(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="stock/", default="", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null = True)

