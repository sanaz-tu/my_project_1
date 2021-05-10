from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Products


def index(request):
    products = Products.objects.all()
    return HttpResponse('Hello world')

def new(request):
    return HttpResponse('New products')