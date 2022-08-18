from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages, auth
from django.shortcuts import redirect
from .models import Account
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

#verfication email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils.encoding import force_text

#mail template
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
            auth.login(request, user)
            # messages.success(request, 'you are logged in.')
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
    return render(request, 'accounts/dashboard.html')
