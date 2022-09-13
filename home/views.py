from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .tasks import notify_customers


def test(request):
    notify_customers.delay('Hello')

    return HttpResponse('Notified')


class HomepageView(TemplateView):
    template_name = 'homepage.html'


def handler404(request, exception):
    return render(request, 'pages/404.html')
