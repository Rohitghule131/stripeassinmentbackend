from cgitb import reset
from django.conf import settings
from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.response import Response
import stripe
from product.models import Products
from os import environ
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from payment.models import PaymentHistory
from payment.serializer import PaymentHistorySerailizer


stripe.api_key = environ.get('STRIPE_SECRET_KEY')

class CreatePaymentRequest(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        count = self.kwargs['count']
        product = Products.objects.get(id=id)
        stripe_payment_object = stripe.checkout.Session.create(
            line_items = [
                {
                    'price_data':{
                        'currency':'usd',
                        'unit_amount':int(product.price * 100),
                        'product_data':{
                            'name':'Head Phone'
                        }
                    },
                    'quantity':count,
                }
            ],
            mode='payment',
            metadata={
                'product_id':product.id
            },
            success_url = settings.BASE_URL + '?success=true',
            cancel_url = settings.BASE_URL + '?cancel=true'
        )
        print(stripe_payment_object,stripe_payment_object.url)
        return redirect(stripe_payment_object.url,code=303)

class My_WebHook(generics.CreateAPIView):
    serializer_class = PaymentHistorySerailizer

    def post(self, request, *args, **kwargs):
        payload = request.body
        serializer = PaymentHistorySerailizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return HttpResponse(status=200)