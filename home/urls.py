from django.urls import path
from .views import HomepageView, test

urlpatterns = [
    path('', view=HomepageView.as_view()),
    path('test/', test),

]
