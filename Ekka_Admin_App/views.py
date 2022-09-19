from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Account, UserProfile
from django.shortcuts import redirect
from category.models import CategoryMain, SubCategory
from category.forms import SubCategoryForm, CategoryMainForm
from store.models import Product, Variation, VariationManager
from carts.forms import ProductForm
from store.forms import variationForm
from orders.forms import OrderForm, OrderUpdateForm
from django.http import HttpResponse
from orders.models import Order, OrderProduct, Payment


# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.user.is_superuser:
        return render(request, 'Ekka_Admin_App/index.html')
    return HttpResponse('You are not authorized to view this page')

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

@login_required(login_url='login')
def sub_category_edit(request, pk):
    sub = SubCategory.objects.get(pk=pk)
    form = SubCategoryForm(instance=sub)

    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES, instance=sub )
        if form.is_valid():
            form.save()
            return redirect('sub_category')
        else: 
            print(form.errors)
        
    context = {
        'sub': sub,
        'edit_form': form,
    }
    return render(request, 'Ekka_Admin_App/Category/SubCategoryedit.html', context)


@login_required(login_url='login')
def sub_category_delete(request, pk):
    sub = SubCategory.objects.get(pk=pk)
    sub.delete()
    return redirect('sub_category')


# Product based views ##############################################################

@login_required(login_url='login')
def product_list(request):
    product = Product.objects.all()
    addProductForm = ProductForm
    if request.method == 'POST':
        addProductForm = ProductForm(request.POST, request.FILES)
        if addProductForm.is_valid():
            addProductForm.save()
            return redirect('product_list')
    context = {
        'product': product,
        'addProduct': addProductForm,
    }
    return render(request, 'Ekka_Admin_App/Products/product_list.html', context)

@login_required(login_url='login')
def product_edit(request, pk):
    Allproduct = Product.objects.all()
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else: 
            print(form.errors)
        
    context = {
        'product': Allproduct,
        'product_editing': product,
        'edit_form': form,
    }
    return render(request, 'Ekka_Admin_App/Products/product_edit.html', context)

@login_required(login_url='login')
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')


# product variations based views ##############################################################

@login_required(login_url='login')
def add_variations(requst):
    existing_variations = Variation.objects.all()
    if requst.method == 'POST':
        form = variationForm(requst.POST, requst.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_variations')
    form = variationForm

    context = {
        'existing_variations': existing_variations,
        'form': form,
    }
    return render(requst, 'Ekka_Admin_App/Variations/add_variations.html', context)

@login_required(login_url='login')
def edit_variations(request, pk):
    existing_variations = Variation.objects.all()
    variation = Variation.objects.get(pk=pk)
    form = variationForm(instance=variation)
    if request.method == 'POST':
        form = variationForm(request.POST, request.FILES, instance=variation)
        if form.is_valid():
            form.save()
            return redirect('add_variations')
        else: 
            print(form.errors)
        
    context = {
        'existing_variations': existing_variations,
        'variation_editing': variation,
        'form': form,
    }
    return render(request, 'Ekka_Admin_App/Variations/edit_variations.html', context)

@login_required(login_url='login')
def delete_variations(request, pk):
    variation = Variation.objects.get(pk=pk)
    variation.delete()
    return redirect('add_variations')


# Orders based views ##############################################################
@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.all()
    order_products = OrderProduct.objects.all() 
    print(order_update)
    context = {
        'orders': orders,
        'order_products': order_products,
    }
    return render(request, 'Ekka_Admin_App/Orders/order_list.html', context)

@login_required(login_url='login')
def order_update(request, pk):
    orders = Order.objects.get(pk=pk)
    update_order = Order.objects.get(pk=pk)
    form = OrderUpdateForm(instance=update_order)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST, instance=update_order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        else: 
            print(form.errors)
        
    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, 'Ekka_Admin_App/Orders/order_update.html', context)                          




