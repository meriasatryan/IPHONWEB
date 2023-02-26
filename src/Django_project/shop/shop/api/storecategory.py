import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import StoreCategory
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------

class StoreCategoryView(View):
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
        categories = StoreCategory.objects.all()
        data = []
        for category in categories:
           data.append({"name":category.name, "id":category.id})
        return self.data_status(data)
#-------------------------------------------------------------------------------

    def post(self, request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(
            name=data['name']
        )
        category.save()
        return self.ok_status()
    
    #-------------------------------------------------------------------------------

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return StoreCategoryView.ok_status()
    
    #-------------------------------------------------------------------------------

    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)

    #-------------------------------------------------------------------------------
  
    @staticmethod
    def get_single(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreCategoryView.data_status({"id": category.id, "name": category.name})
    
#-------------------------------------------------------------------------------

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            storecategory = StoreCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            storecategory.name = data["name"]
        storecategory.save()
        return StoreCategoryView.ok_status()