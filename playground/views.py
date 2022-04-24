from itertools import product
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def hello(request):
    # queryset = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # product = Product.objects.filter(pk=0).first()

    queryset = Product.objects.filter(unit_price__range=(20, 30))
    return render(request, 'hello.html', {'name': 'Sabbir', 'products': queryset})
