from django.db import models
from rest_framework import serializers

# Created Product Model as Products
class DescriptionOfProduct(models.Model):
    description = models.TextField(verbose_name="description")
    
class Products(models.Model):
    brand_name = models.CharField(verbose_name="Brand Name",max_length=50,default="null")
    name_of_product = models.CharField(verbose_name="Name of Product",max_length=50,null=False)
    price = models.FloatField(verbose_name="Product Price",null=False)
    theme = models.CharField(verbose_name="Theme Name",max_length=100,default="null")
    descriptionPoint = models.TextField(verbose_name="description")
    product_url1 = models.URLField(verbose_name="Image 1",default="null")
    product_url2 = models.URLField(verbose_name="Image 2",default="null")
    product_url3 = models.URLField(verbose_name="Image 3",default="null")
    product_url4 = models.URLField(verbose_name="Image 4",default="null")

    