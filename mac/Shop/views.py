from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index (request):
    # products=Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    #params = { 'no_of_slides': nSlides, 'range': range(1,nSlides), 'product': products }
    # allProds =[[products, range(1,nSlides), nSlides],
    #            [products, range(1,nSlides), nSlides]]

    allProds =[]
    catprods = Product.objects.values('category', 'id')
    cats ={item['category'] for item in catprods}
    for cat in cats:
        prod =Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params = { 'allProds': allProds}
    
    return render(request,'Shop/index.html', params)


def about (request):
   
    return render(request,'Shop/about.html')

def contact (request):
    return render(request,'Shop/index.html')

def tracker (request):
    return render(request,'Shop/index.html')

def search (request):
    return render(request,'Shop/index.html')

def productview (request):
    return render(request,'Shop/index.html')

def checkout (request):
    return render(request,'Shop/index.html')