import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import Category
from django.core.exceptions import ObjectDoesNotExist

class CategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data":data, "status": "ok"}), 
            status = 200,
            content_type="application/json",
        )
    
    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}), status=200, content_type="application/json"
        )

    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
           data.append({"name":category.name, "id":category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(
            name=data['name']
        )
        category.save()
        return self.ok_status()
    
    @staticmethod
    def delete(request, id):
        try:
            category = Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return CategoryView.ok_status()
    
    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return CategoryView.get_single(request, id)
        if request.method == "DELETE":
            return CategoryView.delete(request, id)
        if request.method == "PATCH":
            return CategoryView.edit(request, id)
        
    @staticmethod
    def get_single(request, id):
        try:
            category = Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return CategoryView.data_status({"id": category.id, "name": category.name})