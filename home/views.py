from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'homepage.html'

def handler404(request, exception):
    return render(request, 'pages/404.html')