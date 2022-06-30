from django.contrib import admin
from . import models

# more: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # more: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    # more: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

admin.site.register(models.Collection)