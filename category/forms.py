from django import forms
from .models import SubCategory, CategoryMain

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'sub_category_name', 'slug', 'cat_sub_img', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'sub_category_name': forms.TextInput(attrs={'placeholder': 'Sub Category Name', 'class': 'form-control here slug-title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'cat_sub_img': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class CategoryMainForm(forms.ModelForm):
    class Meta:
        model = CategoryMain
        fields = ['category_name', 'slug', 'cat_main_img', 'description']
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Category Name', 'class': 'form-control here slug-title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'cat_main_img': forms.FileInput(attrs={'accept': 'image/*'}),
        }

        