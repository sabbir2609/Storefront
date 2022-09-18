from django.urls import path
from .views import HomepageView, TestView

urlpatterns = [
    path('', view=HomepageView.as_view()),
    path('test/', view=TestView.as_view()),

]
