"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .api.category import CategoryView
from .api.buyer import BuyerView
from .api.customer import CustomerView
from .api.stores import StoreView
from .api.itemcategorys import ItemCategoryView
from .api.items import ItemView
from .api.mybag import MyBagView
from .api.purchase import PurchaseView
from .api.storecategory import StoreCategoryView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/category", CategoryView.as_view()),
    path("api/category/<int:id>", CategoryView.check_view), 
    path("api/customer", CustomerView.as_view()), 
    path("api/customer/<int:id>", CustomerView.check_view),
    path("api/store", StoreView.as_view()), 
    path("api/stores/<int:id>", StoreView.check_view),
    path("api/itemcategory", ItemCategoryView.as_view()), 
    path("api/itemcategorys/<int:id>", ItemCategoryView.check_view),
    path("api/item", ItemView.as_view()), 
    path("api/items/<int:id>", ItemView.check_view),
    path("api/mybag", MyBagView.as_view()), 
    path("api/mybag/<int:id>", MyBagView.check_view),
    path("api/purchase", PurchaseView.as_view()), 
    path("api/purchase/<int:id>", PurchaseView.check_view),
    path("api/storecategory", StoreCategoryView.as_view()), 
    path("api/storecategory/<int:id>", StoreCategoryView.check_view),


]



