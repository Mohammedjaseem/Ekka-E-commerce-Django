from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, Payment, OrderProduct
import json
from store.models import Product
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.

#payments view
def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])
    products = OrderProduct.objects.filter(order_id=order.id)
    print (body)
    # Store transaction details in transaction table
    payment = Payment(
        user             = request.user,
        payment_id       = body['transID'],
        payment_method   = body['payment_method'],
        amount_paid      = order.order_total,
        status           = body['status'],
    )
    payment.save()
 
    order.payment = payment
    order.is_ordered = True
    order.save()

    #move cart items to order items
    cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.price
        orderproduct.ordered = True
        orderproduct.save()

        #variations adding to order product
        #check variation variable name in orders cart and payment to avido confusing in future
        cart_item = CartItem.objects.get(id=item.id)
        product_variation = cart_item.variations.all()
        orderproduct = OrderProduct.objects.get(id=orderproduct.id)
        orderproduct.variation.set(product_variation)
        orderproduct.save()

        # Reduce the quantity of the sold products from orginal stock
        product = Product.objects.get(id=item.product_id)
        product.stock -= item.quantity
        product.save()

    # Empty the cart
    CartItem.objects.filter(user=request.user).delete() 

    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id,
    }

    # Send email to the user ( with order details )
    mail_subject = 'Thank you for your order.'
    message = render_to_string('orders/order_mail.html', {
        'user': request.user,
        'order': order,
        'items': cart_items,
        'url'   : 'http://127.0.0.1:8000/orders/order_complete/?' + 'order_number=' + order.order_number + '&payment_id=' + payment.payment_id,
        
    })
    
    to_email   = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.content_subtype = "html"
    send_email.send()

    # send order number & transcation id back to sendData method via JasonResponse
    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id,
    }
    return JsonResponse(data)



def place_order(request, total=0, quantity=0):
    current_user = request.user


    # if cart count is less than or equal to 0, then redirect to cart page
    cart_items_ttl = CartItem.objects.filter(user=current_user, is_active=True)
    cart_count = cart_items_ttl.count()
    if cart_count <= 0:
        return redirect('store')    

    grand_total = 0
    tax = 0
    for cart_items in cart_items_ttl:
        total += (cart_items.product.price * cart_items.quantity)
        quantity += cart_items.quantity

    tax = (2 * total) / 100
    grand_total = total + tax   

    if  request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing informaation uinside order table
            data = Order() 
            data.user = current_user
            data.first_name     = form.cleaned_data['first_name']
            data.last_name      = form.cleaned_data['last_name']
            data.phone          = form.cleaned_data['phone']
            data.email          = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country        = form.cleaned_data['country']
            data.state          = form.cleaned_data['state']
            data.city           = form.cleaned_data['city']
            data.order_note     = form.cleaned_data['order_note']
            data.order_total    = grand_total
            data.tax            = tax
            data.ip            = request.META.get('REMOTE_ADDR')
            data.save()

            #genarate order number and store in order table
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d  = datetime.date(yr, mt, dt)
            current_date = d.strftime("%d%m%Y") # like 20220305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user = current_user, is_ordered = False, order_number = order_number)
            context = {
                'order': order,
                'cart_items': cart_items_ttl,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            return render(request, 'orders/payments.html', context)
        else:
            return HttpResponse('Form is not valid')
    else:
        return redirect('checkout')


def order_complete(request):

    order_number = request.GET.get('order_number')
    transID = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)
        payment = Payment.objects.get(payment_id=transID)
        tax = (2 * order.order_total) / 100
        subtotal = order.order_total - tax
        subtotal = round(subtotal, 2)
        grand_total = order.order_total
        tax = round(tax, 2)
        context = {
            'user_name': order.user.full_name,
            'date': order.date ,
            'note': order.order_note,
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order_number,
            'transID': transID,
            'address': order.address,
            'subtotal': subtotal,
            'tax': tax,
            'grand_total': grand_total,
        }

        return render(request, 'orders/order_complete.html',context)

    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('/')
    
    




         
