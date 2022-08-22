from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product as Prouct_modle, Variation
from .models import Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Prouct_modle.objects.get(id=product_id) #to get product from product table using product id
    product_variation = []
    if request.method == 'POST':
         for item in request.POST:
            key   = item
            value = request.POST[key]
            
            try:  #,
                variation = Variation.objects.get(Product=product, Variation_category__iexact=key, Variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass 
                
    try:
        cart = Cart.objects.get(cart_id  = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        ) #creating a new cart if the cart is not present in the session 
    cart.save()

    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item  = CartItem.objects.filter(product=product ,cart=cart)
        # existing vartions in cart -- from database
        #current variations in cart - product varitions
        ex_var_list = []
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(item.id)

        print(ex_var_list)

        if product_variation in ex_var_list:
            #incres the quantity if the variation is already in cart
            index = ex_var_list.index(product_variation)
            item_id = id[index]
            item = CartItem.objects.get(product=product, id = item_id)
            item.quantity += 1
            item.save() 

 
        else:
            # create new cart item if the variation is not in cart
            item = CartItem.objects.create(product=product, quantity=1 , cart=cart)
            item.save()

            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
                #cart_item.quantity += 1 #cart_item.quantity is the quantity of the product in the cart
            item.save()
    else: 
        cart_item    = CartItem.objects.create(
            product  =  product, 
            quantity = 1, 
            cart     = cart
            )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()  
    return redirect('cart')



def remove_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Prouct_modle, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else: 
            cart_item.delete()
    except:
        pass
    return redirect('cart')



def remove_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Prouct_modle, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    

    except ObjectDoesNotExist:
        pass #we can ignore
    
    tax_percentage = 2 #15% tax
    tax = (tax_percentage * total) / 100
    grand_total = total + tax
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax_percentage': tax_percentage,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)

def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    

    except ObjectDoesNotExist:
        pass #we can ignore
    
    tax_percentage = 2 #15% tax
    tax = (tax_percentage * total) / 100
    grand_total = total + tax
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax_percentage': tax_percentage,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/checkout.html', context)

