from django.urls import path
from payment.views import CreatePaymentRequest,StripePaymentData

urlpatterns = [
    path('<int:pk>/<int:count>',CreatePaymentRequest.as_view(),name="paymentRequest"),
    path('webhook',StripePaymentData.as_view(),name="webhook"),
]
