from rest_framework import generics
from rest_framework.response import Response
from product.models import Products
from product.serializer import ProductSerializer


# created end point for return products which are stored in db
# created generic retrive class 
class GetProducts(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = ['pk']

    def get_queryset(self):
        obj = Products.objects.get(id=1)
        return obj
    def get(self, request, *args, **kwargs):
        obj = self.get_queryset()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
