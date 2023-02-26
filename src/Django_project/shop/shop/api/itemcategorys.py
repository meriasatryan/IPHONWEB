import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import ItemCategory
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------


class ItemCategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data":data, "status": "ok"}), 
            status = 200,
            content_type="application/json",
        )

#-------------------------------------------------------------------------------

    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}), status=200, content_type="application/json"
        )

#-------------------------------------------------------------------------------

    def get(self, request):
        itemcategories = ItemCategory.objects.all()
        data = []
        for category in itemcategories:
           data.append({"name":category.name, "id":category.id})
        return self.data_status(data)

#-------------------------------------------------------------------------------

    def post(self, request):
        data = json.loads(request.body)
        category = ItemCategory.objects.create(
            name=data['name']
        )
        category.save()
        return self.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    def delete(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return ItemCategoryView.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.delete(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.edit(request, id)

#-------------------------------------------------------------------------------

    @staticmethod
    def get_single(request, id):
        try:
            itemcategory = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemCategoryView.data_status({"id": itemcategory.id, "name": itemcategory.name})

#-------------------------------------------------------------------------------

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            itemcategory = ItemCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            itemcategory.name = data["name"]
        itemcategory.save()
        return ItemCategoryView.ok_status()