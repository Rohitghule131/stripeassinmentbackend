from django.urls import path
from product.views import GetProducts

urlpatterns = [
    path('',GetProducts.as_view(),name="products"),
]
