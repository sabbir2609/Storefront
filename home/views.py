from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
import requests
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView


class TestView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'test/test.html', {'data': data})


class HomepageView(TemplateView):
    template_name = 'homepage.html'


def handler404(request, exception):
    return render(request, 'pages/404.html')
