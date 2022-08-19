from django.shortcuts import render, get_object_or_404, redirect 
from store.models import Product
from category.models import CategoryMain, SubCategory

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        
        categories = get_object_or_404(CategoryMain, slug=category_slug)
        products = Product.objects.filter(Category_Main=categories, is_available=True)
        produ_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        produ_count = products.count()

    context = {
        'products': products,
        'produ_count': produ_count,
        }
    return render(request, 'store/store.html', context) 


def substore(request, category_slug=None, sub_category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        if sub_category_slug != None:
                categories = get_object_or_404(SubCategory, slug=sub_category_slug)
                products = Product.objects.filter(sub_category=categories, is_available=True)
                produ_count = products.count()
        else:
            products = Product.objects.all().filter(is_available=True)
            produ_count = products.count()

    context = {
        'products': products,
        'produ_count': produ_count,
        }
    return render(request, 'store/store.html', context) 