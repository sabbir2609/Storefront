from django.shortcuts import render
from store.models import Product

def say_hello(request):
    qs = Product.objects.all()
    for product in qs:
        print(product)

        
    return render(request, 'hello.html', {'name': 'Sabbir'})