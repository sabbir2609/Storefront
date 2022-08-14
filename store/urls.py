from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import ProductViewSet, CollectionViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)

urlpatterns = []

urlpatterns += router.urls
