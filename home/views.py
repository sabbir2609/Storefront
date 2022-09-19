from django.shortcuts import render
from django.views.generic import TemplateView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
import requests
import logging


logger = logging.getLogger(__name__)  # home.views


class TestView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'test/log-test.html', {'data': data})


class RedisView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'test/redis-test.html', {'data': data})


class HomepageView(TemplateView):
    template_name = 'homepage.html'


def handler404(request, exception):
    return render(request, 'pages/404.html')
