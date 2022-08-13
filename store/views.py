from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from django.db.models.aggregates import Count
from .models import Product, Collection
from .serializer import ProductSerializer, CollectionSerializer


class ProductList(ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.select_related('collection').all()

    def get_serializer_class(self):
        return ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetail(APIView):
    
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitems.count() > 0:
            return Response({'error' : 'Product Can Not Be Deleted Because It Is Associated With An Order Item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
@api_view(['GET','PUT','DELETE'])
def collection_detail(request, id):
    collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=id)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response({'error':'Not Allowed! Associated with products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Template view section

def product_list_template(request):
    queryset = Product.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/products.html', {'page_obj': page_obj})
