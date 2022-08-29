from django.shortcuts import render
#import forms here
from .forms import RegistrationForm
from .forms import UserForm
from .forms import UserProfileForm


from django.contrib import messages, auth
from django.shortcuts import redirect
from .models import Account
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

#import orders
from orders.models import Order, OrderProduct
from django.core.exceptions import ObjectDoesNotExist




#import account details
from accounts.models import Account, UserProfile 

#verfication email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


#mail template
from django.core.mail import send_mail
from django.template.loader import render_to_string

from carts.views import _cart_id
from carts.models import Cart, CartItem

import requests
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            username = email.split('@')[0]
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            user = Account.objects.create(username=username ,full_name=full_name, email=email, password=password)
            user.phone_number = phone_number
            user.set_password(request.POST['password'])
            user.save()


            #user activation
            current_site = get_current_site(request) #this should be imported 
            mail_subject = 'Activate your Ekka Ecom account.'
            user.save()

            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), 
                'token': default_token_generator.make_token(user),
            })
            
            to_email = form.cleaned_data.get('email')
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.content_subtype = "html"
            send_email.send()
            # messages.success(request, 'Please confirm your email address to complete the registration')
            return redirect('login?command=verification&email='+email)
            
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            try:
                cart =  Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
      
                    for item in cart_item:
                        item.user = user
                        #item.save()

                    # Geting the product variations by cat id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))

                    # Geting the product variations by cat id to acces his product variation
                    cart_item = CartItem.objects.filter(user = user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        exising_variation = item.variations.all()
                        ex_var_list.append(list(exising_variation))
                        id.append(item.id)

                    # to get common product variations
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user 
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
 

                    # for item in cart_item:
                    #     item.user = user
                    #     item.save()
            except:
                pass
            auth.login(request, user)
            # messages.success(request, 'you are logged in.')
            url = request.META.get('HTTP_REFERER')
            try:
                query  = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    return redirect(params['next'])
                
            except:
                 return redirect('/')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
        
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'you are logged out.')
    return redirect('login')

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = urlsafe_base64_decode(uidb64)
        user = Account._default_manager.get(pk=uid) 
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and default_token_generator.check_token(user, token):  
        user.is_active = True  
        user.save()  
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login') 

    else:  
        messages.error(request, 'Activation link is invalid!')
        return redirect('register')  


@login_required(login_url='login')
def dashboard(request): 
    user = request.user
    orders = Order.objects.order_by('-created_at').filter(user_id=user.id, is_ordered=True)
    orders_count = orders.count()
    product_ordered = OrderProduct.objects.filter(user_id=user.id).order_by('-created_at')
    

    context = {
        'profile': user,
        'orders_count': orders_count,
        'user': user,
        'product_ordered': product_ordered,
        'orders': orders,
        
    }
    return render(request, 'accounts/dashboard.html', context)



def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            #reset pasword
            current_site = get_current_site(request) #this should be imported 
            mail_subject = 'Reset your account passowrd.'
            user.save()
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), 
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.content_subtype = "html"
            send_email.send()

            messages.success(request, 'Password reset link has been sent to your email.')
            return redirect('login')
        
        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgotPassword')

    return render(request, 'accounts/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):  
    try:  
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid) 
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and default_token_generator.check_token(user, token):  
        request.session['uid'] = uid
        messages.success(request, 'Please enter your new password.')
        return redirect('resetPassword')
    else:
        messages.error(request, 'Password reset link has been expired!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid') 
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password has been reset successfully.')
            return redirect('login')

        else:
            messages.error(request, 'Password does not match')
            return redirect('resetPassword')
    else:
        template = 'accounts/resetPassword.html'
        return render(request, template)

@login_required(login_url='login')
def changePassword(request):
    user = request.user
    if request.method == 'POST':
        current_password = request.POST['current_password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            sucess = user.check_password(current_password)
            if sucess:
                user = Account.objects.get(pk=request.user.pk)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password has been Changed, Please login to.')
                return redirect('login')

        else:
            messages.error(request, 'Password does not match')
            return redirect('changePassword')
    else:
        template = 'accounts/changePassword.html'
        return render(request, template)



@login_required(login_url='login')
def user_profile(request):
    try:
       #userprofile  = get_object_or_404(UserProfile, user=request.user)
       userprofile = UserProfile.objects.get(user=request.user)

    except ObjectDoesNotExist:
        # created new userprofile if not exist for the user
        userprofile = UserProfile.objects.create(user=request.user)
        userprofile.save()

    user         = request.user
    profile_data = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
            
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': user,
        'profile_data': profile_data,
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def order_details(request, order_id):
    order_details = OrderProduct.objects.filter(order__order_number=order_id)
    order         = Order.objects.get(order_number=order_id)

    #total amount in order details
    for i in order_details:
        total = i.product_price * i.quantity
        i.total = total

    #tax calculating 
    for item in order_details:
        item.tax = (i.total * 2)/100
        total = i.total + item.tax

    #items count
    items_count = order_details.count()

    context = {
        'order_detail': order_details,
        'order': order,
        'tax': item.tax,
        'total': i.total,
    }
    return render(request, 'accounts/order_details.html', context)   