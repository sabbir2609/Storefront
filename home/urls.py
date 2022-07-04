from django.urls import path
from .views import HomepageView
urlpatterns = [
    path('', view=HomepageView.as_view())
]