from rest_framework import serializers
from .models  import *
from .models import StoreCategory


class StoreCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreCategory
        fields = "__all__"


class GenericStoreCategorySerializer(serializers.ModelSerializer):
    users = StoreCategorySerializer(many = False)
    class Meta:
        model = StoreCategory
        fields = "__all__"