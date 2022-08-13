from django.urls import path
from . import views
from .views import ProductList, ProductDetail, CollectionList

urlpatterns = [
    path('products/',ProductList.as_view()),
    path('products/<int:id>/', ProductDetail.as_view()),
    path('collections/', CollectionList.as_view()),
    path('collections/<int:id>/', views.collection_detail, name='collection-detail'),

    # for template view
    path('products-ls/', views.product_list_template),


]
