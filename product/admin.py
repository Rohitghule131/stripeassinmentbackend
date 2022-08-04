from django.contrib import admin
from product.models import Products, DescriptionOfProduct


admin.site.register(DescriptionOfProduct)
admin.site.register(Products)