from email.headerregistry import ContentDispositionHeader
from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import TemplateView
import requests


def test(request):
    key = 'httpbin_result'
    if cache.get(key) is None:
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        cache.set(key, data)

    return render(request, 'test/test.html', {'data': cache.get(key)})


class HomepageView(TemplateView):
    template_name = 'homepage.html'


def handler404(request, exception):
    return render(request, 'pages/404.html')
