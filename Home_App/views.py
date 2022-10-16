from django.shortcuts import render
from store.models import Product, deals
from category.models import CategoryMain, SubCategory

# Create your views here.
def index(request):
    products = Product.objects.all()
    new_arrivals = Product.objects.order_by('-id')
    trending = Product.objects.order_by('-stock')
    top_rated = Product.objects.order_by('?')
    dealsoftheday = deals.objects.all()
    best_sellers = Product.objects.order_by('-stock')
    sub_category = SubCategory.objects.all().order_by('?')

    print(sub_category)

    context = {
        'products': products,
        'new_arrivals': new_arrivals,
        'trending': trending,
        'top_rated': top_rated,
        'deal_of_the_day': dealsoftheday,
        'best_sellers': best_sellers,
        'sub_category': sub_category,
        }
    return render(request, 'home_page/home.html',context)
