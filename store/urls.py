from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),

    # for template view
    path('products-ls/', views.product_list_template),


]
