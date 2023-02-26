import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import Purchase
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------

class PurchaseView(View):
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
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
           data.append({"total_price":purchase.total_price, "id":purchase.id})
        return self.data_status(data)
#-------------------------------------------------------------------------------

    def post(self, request):
        data = json.loads(request.body)
        purchase = Purchase.objects.create(
            total_price=data['total_price']
        )
        purchase.save()
        return self.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    def delete(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        purchase.delete()
        return PurchaseView.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_single(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)

#-------------------------------------------------------------------------------

    @staticmethod
    def get_single(request, id):
        try:
            purchase = ProcessLookupError.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return PurchaseView.data_status({"id": purchase.id, "total_price": purchase.total_price})
    
#-------------------------------------------------------------------------------

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            purchase = Purchase.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            purchase.name = data["name"]
        purchase.save()
        return PurchaseView.ok_status()