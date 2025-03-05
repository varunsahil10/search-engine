from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()
    # print(request)
    query = ''
    if request.method == 'GET':
        print(request.GET)
        query = request.GET.get('q')
        if query:
            products = products.filter(description__search=query)
    context = {
        'products': products,
        'q':query,
    }
    return render(request,'index.html',context)