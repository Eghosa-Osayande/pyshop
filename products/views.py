from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})

def new_products(request):
    return HttpResponse('<h1>New Product</h1>')
