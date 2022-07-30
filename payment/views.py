from django.conf import settings
from django.shortcuts import redirect
from rest_framework import generics
import stripe
from product.models import Products
from os import environ
from django.http import HttpResponse
from payment.models import PaymentHistory

# get Stripe Secrete key from env file 
stripe.api_key = environ.get('STRIPE_SECRET_KEY')

BASE_URL = environ.get('BASE_URL')

# get pk and count of product from end point 
# pk is for porduct id which will retrive from DB 
# redirect user from stripe payment 
# using for stripe checkout session 
class CreatePaymentRequest(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        count = self.kwargs['count']
        product = Products.objects.get(id=id)
        # created checkout session for user 
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
            success_url = BASE_URL + '?success=true',
            cancel_url = BASE_URL + '?cancel=true'
        )
        # if payment was successfull redirect user on base url which with the 
        # success=true query
        # else redirect user on base url with the cancel=true query
        return redirect(stripe_payment_object.url,code=303)

class My_WebHook(generics.CreateAPIView):
    def stripe_webhook(self,session):
        # trace and store data which stripe webhook forward to this end point
        # traced data store in DB 
        name = session["charges"]["data"][0]["billing_details"]["name"]
        email = session["charges"]["data"][0]["billing_details"]["email"]
        amount = (session["charges"]["data"][0]["amount"])/100
        city = session["charges"]["data"][0]["billing_details"]["address"]["city"]
        state = session["charges"]["data"][0]["billing_details"]["address"]["state"]
        country = session["charges"]["data"][0]["billing_details"]["address"]["country"]
        status = session["charges"]["data"][0]["status"]
        PaymentHistory.objects.create(name=name, email=email, amount=amount, city= city, state =state, country =country, status =status)
    def post (self,request):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None
        try:
            event = stripe.Webhook.construct_event(
            payload, sig_header, environ.get('STRIPE_SECRET_CLI_KEY')
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)
        if event['type'] == 'payment_intent.succeeded':
            session = event['data']['object']
        # For now, you only need to print out the webhook payload so you can see
        # the structure.
            self.stripe_webhook(session)
        return HttpResponse(status=200)