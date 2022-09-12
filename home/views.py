from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.core.mail import EmailMessage, BadHeaderError


def test(request):
    try:
        # send_mail('subject', 'message', 'sabbir@sabbir.inc', ['sabbirhasan2999@gmail.com'])
        # mail_admins('subject', 'message', html_message='message')

        message = EmailMessage(
            'subject', 'message', 'sabbir@sabbir.inc', ['sabbirhasan2999@gmail.com'])
        message.attach_file('home/static/images/demo.png')
        message.send()

    except BadHeaderError:
        pass
    return HttpResponse("Test- Mail")


class HomepageView(TemplateView):
    template_name = 'homepage.html'


def handler404(request, exception):
    return render(request, 'pages/404.html')
