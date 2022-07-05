from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize
from .models import Product
from .serializer import ProductSerializer


@api_view()
def product_list(request):
    return Response('OK')

@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)