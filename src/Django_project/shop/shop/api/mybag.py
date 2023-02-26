import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import MyBag
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------

class MyBagView(View):
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
        mybags = MyBag.objects.all()
        data = []
        for mybag in mybags:
           data.append({"total_price":mybag.total_price, "id":mybag.id})
        return self.data_status(data)

#-------------------------------------------------------------------------------

    def post(self, request):
        data = json.loads(request.body)
        mybag = MyBag.objects.create(
            total_price=data['total_price']
        )
        mybag.save()
        return self.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    def delete(request, id):
        try:
            mybag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        mybag.delete()
        return MyBagView.ok_status()
    
    #-------------------------------------------------------------------------------

    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_single(request, id)
        if request.method == "DELETE":
            return MyBagView.delete(request, id)
        if request.method == "PATCH":
            return MyBagView.edit(request, id)

#-------------------------------------------------------------------------------

    @staticmethod
    def get_single(request, id):
        try:
            mybag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return MyBagView.data_status({"id": mybag.id, "total_price": mybag.total_price})
    
#-------------------------------------------------------------------------------


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            mybag = MyBag.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            mybag.name = data["name"]
        mybag.save()
        return MyBagView.ok_status()