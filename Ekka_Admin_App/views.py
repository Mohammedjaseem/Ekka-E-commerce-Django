from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Account, UserProfile
from django.shortcuts import redirect
from category.models import CategoryMain, SubCategory
from category.forms import SubCategoryForm, CategoryMainForm
from store.models import Product, Variation


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'Ekka_Admin_App/dashboard.html')


# User based views ##############################################################

@login_required(login_url='login')
def user_list(request):
    profile = UserProfile.objects.all().order_by('-user__date_joined')
    context = {
        'user': profile,
    }
    return render(request, 'Ekka_Admin_App/users/user_list.html', context)

@login_required(login_url='login')
def user_profile(request, pk):
    profile = UserProfile.objects.get(user__pk=pk)
    context = {
        'user': profile,
    }
    return render(request, 'Ekka_Admin_App/users/user_profile.html', context)

@login_required(login_url='login')
def user_delete(request, pk):
    user = Account.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')

@login_required(login_url='login')
def user_block(request, pk):
    user = Account.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect('user_list')

@login_required(login_url='login')
def user_unblock(request, pk):
    user = Account.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect('user_list')

# User based views ends here ##############################################################

# Category based views ##############################################################

@login_required(login_url='login')
def main_category(request):
    if request.method == 'POST':
        form = CategoryMainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_category')
    data = SubCategory.objects.all()
    main = CategoryMain.objects.all()
    form = CategoryMainForm()
    context = {
        'main': main,
        'sub': data,
        'form': form,
    }
    return render(request, 'Ekka_Admin_App/Category/MainCategory.html', context)

def main_category_edit(request, pk):
    main = CategoryMain.objects.get(pk=pk)
    data = SubCategory.objects.all()
    form = CategoryMainForm(instance=main)
    mains = CategoryMain.objects.all()

    if request.method == 'POST':
        form = CategoryMainForm(request.POST, instance=main)
        if form.is_valid():
            form.save()
            return redirect('main_category')
        else: 
            print(form.errors)
        
    context = {
        'main': main,
        'edit_form': form,
        'sub': data,
        'mains': mains,
    }
    return render(request, 'Ekka_Admin_App/Category/MainCategoryedit.html', context)

@login_required(login_url='login')
def main_category_delete(request, pk):
    main = CategoryMain.objects.get(pk=pk)
    main.delete()
    return redirect('main_category')


# Sub Category based views ##############################################################

@login_required(login_url='login')
def sub_category(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sub_category')
    data = SubCategory.objects.all()
    form = SubCategoryForm()
    context = {
        'sub': data,
        'form': form,
      
    }
    return render(request, 'Ekka_Admin_App/Category/SubCategory.html', context)




