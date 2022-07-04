from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

# more: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

# view low inventory product
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # more: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options
    list_display = ['title', 'unit_price','inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10

    list_filter = ['collection', 'last_update', InventoryFilter]
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return f'Low ({product.inventory} Item)'
        return f'OK - {product.inventory} '

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    # more: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name'] 
    search_fields = ['first_name__istartswith', 'last_name__istartswith'] # lookup-type case insensitive

    # didn't get this section will review
    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at', 'customer']



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    # didn't get this section will review
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?' 
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>',url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product') # for Count() import this => from django.db.models import Count
        )

