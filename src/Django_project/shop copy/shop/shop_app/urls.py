from django.urls import path 
from rest_framework import routers
from . import views

from django.urls import include

router = routers.DefaultRouter()
router.register("student", views.StoreCategoryViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls))
]
