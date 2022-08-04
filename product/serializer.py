from rest_framework import serializers
from product.models import Products, DescriptionOfProduct



class ProductWithDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionOfProduct
        fields = ['description']


class ProductSerializer(serializers.ModelSerializer):
    points = ProductWithDescriptionSerializer(many=True)
    class Meta:
        model = Products
        fields = [
            'brand_name',
            'name_of_product',
            'price',
            'theme',
            'product_url1',
            'product_url2',
            'product_url3',
            'product_url4',
            'points'
        ]