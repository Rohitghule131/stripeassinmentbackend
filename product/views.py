from rest_framework import generics
from rest_framework.response import Response
from product.models import Products
from product.serializer import ProductSerializer
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_webhook_view(request):
    # if request.method['POST']:
    payload = request.body
    event = None
    print(payload)
    print("payload")
    return HttpResponse(status=200)

class GetProducts(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = ['pk']

    def get_queryset(self):
        obj = Products.objects.all()
        return obj
    def get(self, request, *args, **kwargs):
        obj = self.get_queryset()
        serializer = self.get_serializer(obj,many=True)
        return Response(serializer.data)

#gutsy-fiery-brave-lead