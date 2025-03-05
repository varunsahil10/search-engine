from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()
    # print(request)
    if request.method == 'GET':
        print(request.GET)
        query = request.GET.get('q',None)
        if query:
            products = products.filter(name__icontains=query)
    context = {
        'products': products,
    }
    return render(request,'index.html',context)