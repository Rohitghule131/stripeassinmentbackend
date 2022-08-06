from django.shortcuts import redirect
from rest_framework import generics
import stripe
from product.models import Products
from os import environ
from django.http import HttpResponse
from payment.models import PaymentHistory
from payment.serializer import PaymentHistoryDataSerializer

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
                        'unit_amount':int(product.price*100),
                        'product_data':{
                            'name':'Head Phone',
                            'images':[
                            product.product_url4
                            ]
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

class StripePaymentData(generics.CreateAPIView):
    serializer_class = PaymentHistoryDataSerializer

    def stripe_webhook(self,session):
        # trace and store data which stripe webhook forward to this end point
        # traced data store in DB 
        slice_data = session["charges"]["data"][0]
        data = {
            "name" : slice_data["billing_details"]["name"],
            "email" : slice_data["billing_details"]["email"],
            "amount" : (slice_data["amount"])/100,
            "city" : slice_data["billing_details"]["address"]["city"],
            "state" : slice_data["billing_details"]["address"]["state"],
            "country" : slice_data["billing_details"]["address"]["country"],
            "status" : slice_data["status"]
        }
        return data

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
            data = self.stripe_webhook(session)
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return HttpResponse(status=200)