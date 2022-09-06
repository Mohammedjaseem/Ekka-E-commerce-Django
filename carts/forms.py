


from django import forms
from .models import Product, Variation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control here slug-title'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Slug', 'class': 'form-control here slug'}),
            'category_Main': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'sub_category': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'mrp_price': forms.NumberInput(attrs={'placeholder': 'MRP Price', 'class': 'form-control here'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form-control here'}),
            'short_desp': forms.TextInput(attrs={'placeholder': 'Short Description', 'class': 'form-control here'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'images': forms.FileInput(attrs={'accept': 'image/*'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Stock', 'class': 'form-control here'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }




