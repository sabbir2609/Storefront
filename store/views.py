from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db.models.aggregates import Count
from .models import Product, Collection
from .serializer import ProductSerializer, CollectionSerializer


class ProductViewSet(ModelViewSet):
    queryset =  Product.objects.select_related('collection').all()
    serializer_class =  ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response({'error' : 'Product Can Not Be Deleted Because It Is Associated With An Order Item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Use ReadOnlyModelViewSet for block writing
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer    

    def delete(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=pk)
        if collection.products.count() > 0:
            return Response({'error':'Not Allowed! Associated with products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
