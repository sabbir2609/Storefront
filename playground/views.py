from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return render(request, 'hello.html', {'name': 'Sabbir'})
