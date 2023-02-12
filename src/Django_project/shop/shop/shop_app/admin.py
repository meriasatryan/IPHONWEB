from django.contrib import admin
from .models import Buyer
from .models import Category
from .models import StoreCategory
from .models import ItemCategory
from .models import Customer
from .models import StoreOwner
from .models import Store
from .models import Item
from .models import MyBag
from .models import Purchase

# Register your models here.

class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "registrated_at", "user_info")
    
    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.user.first_name, obj.user.last_name)))
admin.site.register(Buyer, BuyerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.name, obj.id)))
admin.site.register(Category, CategoryAdmin)
        
#### My homework starts here 

class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.name)))
admin.site.register(StoreCategory, StoreCategoryAdmin)


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.name)))
admin.site.register(ItemCategory, ItemCategoryAdmin)
        

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "registered_at")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.user.name, obj.user.last_name, obj.registered_at) ))
admin.site.register(Customer, CustomerAdmin)


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ("name", "registered_at")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.user.name, obj.user.second_name, obj.registered_at)))
admin.site.register(StoreOwner, StoreOwnerAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "store_category")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.name, obj.store_category)))
admin.site.register(Store, StoreAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "info", "store")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.name, obj.category, obj.price, obj.quantity, obj.info, obj.store)))
admin.site.register(Item, ItemAdmin)


class MyBagAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.customer, obj.total_price)))
admin.site.register(MyBag,MyBagAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("items", "buy_time", "customer", "total_price")

    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.items, obj.buy_time, obj.customer, obj.total_price)))
admin.site.register(Purchase, PurchaseAdmin)




