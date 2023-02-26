import json
from django.views.generic import View
from django.http import HttpResponse
from ..shop_app.models import Buyer

class BuyerView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data":data, "status": "ok"}), 
            status = 200,
            content_type="application/json"
        )

    def get(self, request):
        buyers = Buyer.objects.all()
        data = []
        for buyer in buyers:
           data.append({"name":buyer.name, "id":buyer.registrated_at})
        return self.data_status(data)

    def pos(self, request):
        pass
    