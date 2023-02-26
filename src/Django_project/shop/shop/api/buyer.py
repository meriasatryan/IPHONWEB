import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import Buyer
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------

class BuyerView(View):
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
        buyers = Buyer.objects.all()
        data = []
        for buyer in buyers:
           data.append({"name":buyer.name, "id":buyer.id})
        return self.data_status(data)
    
#Here I need to use registation as my Buyer has a user

    """def post(self, request):
        data = json.loads(request.body)
        buyer = Buyer.objects.create(
            name=data['name']
        )
        buyer.save()
        return self.ok_status()

    @staticmethod
    def delete(request, id):
        try:
            buyer = Buyer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        buyer.delete()
        return BuyerView.ok_status()
    
    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return BuyerView.get_single(request, id)
        if request.method == "DELETE":
            return BuyerView.delete(request, id)
        if request.method == "PATCH":
            return BuyerView.edit(request, id)
        
    @staticmethod
    def get_single(request, id):
        try:
            buyer = Buyer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return BuyerView.data_status({"id": buyer.id, "name": buyer.name})

"""