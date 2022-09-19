from django.urls import path
from .views import HomepageView, TestView, RedisView

urlpatterns = [
    path('', view=HomepageView.as_view()),
    path('test/', view=TestView.as_view()),
    path('redis/', view=RedisView.as_view()),

]
