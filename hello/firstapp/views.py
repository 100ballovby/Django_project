from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Привет, user! Это мой сайт!')


def about(request):
    return HttpResponse('<h1>О нас</h1>')
