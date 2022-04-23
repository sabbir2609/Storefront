from django.shortcuts import render
from store.models import Product


def hello(request):
    # queryset = Product.objects.all()
    product = Product.objects.get(pk=1)
    return render(request, 'hello.html', {'name': 'Sabbir'})
