from django.db import models
from rest_framework import serializers

# Created Product Model as Products
class Products(models.Model):
    name_of_product = models.CharField(verbose_name="Name of Product",max_length=50,null=False)
    price = models.FloatField(verbose_name="Product Price",null=False)
    descriptionPoint = models.TextField(verbose_name="description")
    