from itertools import product
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum


def hello(request):
    # queryset = Product.objects.all()
    # for product in query_set:
    #     print(product)

    # product = Product.objects.filter(pk=0).first()
    # queryset = Product.objects.filter(unit_price__range=(20, 30))

    # And OP

    # queryset = Product.objects.filter(inventory__lt=10, unit_price__range=(20, 30))
    # queryset=Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # https://docs.djangoproject.com/en/4.0/topics/db/queries/#complex-lookups-with-q-objects

    # OR OP with Q obj
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    # AND with Q obj
    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))

    # OR NOT
    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))

    # F object for refarencing
    # queryset = Product.objects.filter(inventory=F('unit_price'))

    # Sorting Data
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by
    # ascending
    # queryset = Product.objects.order_by('title')

    # descending
    # queryset = Product.objects.order_by('-title')

    # multiple sorting
    # queryset = Product.objects.order_by('unit_price','-title')

    # make it reverse
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()

    # accessing individual element
    # product = Product.objects.order_by('unit_price')[0] # order_by returns a queryset
    # product = Product.objects.earliest('unit_price') # earliest retuarns first object ascending
    # product = Product.objects.latest('unit_price') # latest retuarns first object descnding

    # more complex Query
    # queryset = Product.objects.filter(Q(title__startswith='Soup')).order_by('unit_price')

    # limiting result
    # queryset = Product.objects.all() [:5]

    # queryset = OrderItem.objects.values('product__id').distinct()

    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    # dont use only 😒
    # queryset = Product.objects.only('id', 'title')

    # dnt use defer method either
    # queryset = Product.objects.defer('id', 'title')

    # select related object

    # queryset = Product.objects.select_related('collection').all()

    # prefetch_related (n)
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection')

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    

    return render(request, 'hello.html', {'name': 'Sabbir', 'products': list(queryset)})
