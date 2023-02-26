import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import Customer
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------

class CustomerView(View):
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
#Here I need to use registation as my Buyer has a user
    def get(self, request):
        customers = Customer.objects.all()
        data = []
        for customer in customers:
           data.append({"name":customer.name, "id":customer.id})
        return self.data_status(data)
#-------------------------------------------------------------------------------
    def post(self, request):
        data = json.loads(request.body)
        customer = Customer.objects.create(
            name=data['name']
        )
        customer.save()
        return self.ok_status()
    
#-------------------------------------------------------------------------------
 
    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        customer.delete()
        return CustomerView.ok_status()
    
 #-------------------------------------------------------------------------------
   
    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_single(request, id)
        if request.method == "DELETE":
            return CustomerView.delete(request, id)
        if request.method == "PATCH":
            return CustomerView.edit(request, id)

   #-------------------------------------------------------------------------------


    @staticmethod
    def get_single(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return CustomerView.data_status({"id": customer.id, "name": customer.name})
    
#-------------------------------------------------------------------------------

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            customer.name = data["name"]
        customer.save()
        return CustomerView.ok_status()