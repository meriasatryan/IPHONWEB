from django.contrib import admin
from .models import Buyer

# Register your models here.

class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "registrated_at", "user_info")
    
    def user_info(self,obj):
        return "{}".format(" ".join(list(obj.user.first_name, obj.user.last_name)))
admin.site.register(Buyer, BuyerAdmin)