from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title','slug','description','inventory','unit_price','price_with_tax','collection')
        # fields = '__all__' # bad practice

    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
   
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset= Collection.objects.all(),
    #     view_name='collection-detail'
    # )

    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)

    # overriding validate method
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Password Do Not Match')
    #     else:
    #         return data

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

        # updating data

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance