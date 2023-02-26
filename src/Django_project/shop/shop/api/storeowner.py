import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import StoreOwner
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------


class StoreOwnerView(View):
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
#Here we need registation as my StoreOwner has user
"""
    def get(self, request):
        owners = StoreOwner.objects.all()
        data = []
        for owner in owners:
           data.append({"date":owner.registrated_at, "id":owner.id})
        return self.data_status(data)

#-------------------------------------------------------------------------------

    def post(self, request):
        data = json.loads(request.body)
        owner = StoreOwner.objects.create(
            name=data['date']
        )
        owner.save()
        return self.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    def delete(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        owner.delete()
        return StoreOwnerView.ok_status()

#-------------------------------------------------------------------------------

    @staticmethod
    
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)

#-------------------------------------------------------------------------------

    @staticmethod
    def get_single(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreOwnerView.data_status({"id": owner.id, "name": owner.name})
    
#-------------------------------------------------------------------------------

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            storeowner = StoreOwner.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            storeowner.name = data["name"]
        storeowner.save()
        return StoreOwnerView.ok_status()"""