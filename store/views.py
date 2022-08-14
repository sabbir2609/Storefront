from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from django.db.models.aggregates import Count
from .models import OrderItem, Product, Collection, Review
from .serializer import ProductSerializer, CollectionSerializer, ReviewSerializer


class ProductViewSet(ModelViewSet):
    queryset =  Product.objects.select_related('collection').all()
    serializer_class =  ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error' : 'Product Can Not Be Deleted Because It Is Associated With An Order Item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

# Use ReadOnlyModelViewSet for block writing
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer  

    def destroy(self, request, *args, **kwargs):
        if Collection.products.count() > 0:
            return Response({'error':'Not Allowed! Associated with products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    