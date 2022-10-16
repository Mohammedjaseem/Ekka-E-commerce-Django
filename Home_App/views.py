from django.shortcuts import render
from store.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    new_arrivals = Product.objects.order_by('-id')
    trending = Product.objects.order_by('-stock')
    top_rated = Product.objects.order_by('?')

    context = {
        'products': products,
        'new_arrivals': new_arrivals,
        'trending': trending,
        'top_rated': top_rated,
        }
    return render(request, 'home_page/home.html',context)
