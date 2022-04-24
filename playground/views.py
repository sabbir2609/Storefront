from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def hello(request):
    query_set = Product.objects.all()
    for product in query_set:
        print(product)
    return render(request, 'hello.html', {'name': 'Sabbir'})
