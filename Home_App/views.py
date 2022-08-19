from django.shortcuts import render
from store.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        }
    return render(request, 'home_page/home.html',context)