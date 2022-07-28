from django.urls import path
from payment.views import CreatePaymentRequest,My_WebHook

urlpatterns = [
    path('<int:pk>/<int:count>',CreatePaymentRequest.as_view(),name="paymentRequest"),
    path('webhook',My_WebHook.as_view(),name="webhook"),
]
