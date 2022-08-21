from django.shortcuts import render, get_object_or_404, redirect 
from store.models import Product
from category.models import CategoryMain, SubCategory
from carts.views import _cart_id
from carts.models import CartItem as cart_item

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

def product_detail(request, category_slug=None, sub_category_slug=None, product_slug=None):
    product = None
    if product_slug != None:
        product = get_object_or_404(Product, slug=product_slug)
        in_cart = cart_item.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()

    context = {
        'product': product,
        'in_cart': in_cart,
        }
    return render(request, 'store/product_detail.html', context)