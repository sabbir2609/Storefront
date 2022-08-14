from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CollectionViewSet
from pprint import pprint

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)
pprint(router.urls)


urlpatterns = []

urlpatterns += router.urls
