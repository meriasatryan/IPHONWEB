from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to = "buyer/", blank=True, null=True )
    name = models.CharField(max_length=100, blank=True, null=True)
    
class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="seller/", blank = True, null = True)

class Category(models.Model):
    name = models.CharField(max_length=100,  blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=100,  blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="images", default="")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank = True )

class Stock(models.Model):
    name = models.CharField(max_length=100,  blank=True, null=True)
    logo = models.ImageField(upload_to="stock/", default="", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null = True, blank=True)

###### My homework starts here

class StoreCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to="storecategory/", default="", blank=True, null=True)

class ItemCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to="itemcategory/", default="", blank=True, null=True)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to = "customer/", blank=True, null=True )

class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True )
    avatar = models.ImageField(upload_to="storeowner/", blank = True, null = True)
    registrated_at = models.DateTimeField(default=timezone.now)

class Store(models.Model):
    name = models.CharField(max_length=100,  blank=True, null=True)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE, null = True, blank=True )
    store_category = models.ForeignKey(StoreCategory,on_delete=models.CASCADE, null=True, blank=True)
   
class Item(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to="items/", blank = True, null = True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True, blank=True )
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=1000, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)

class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(Item)
    total_price = models.FloatField(blank=True, null=True)

class Purchase(models.Mode):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    total_price  = models.FloatField(blank=True, null=True)