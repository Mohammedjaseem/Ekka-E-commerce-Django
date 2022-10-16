from django import forms
from .models import Product, Variation, ReviewRating

class variationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = ('Product' , 'Variation_category', 'Variation_value', 'is_active')
        widgets = {
            'Product': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'Variation_category': forms.Select(attrs={'placeholder': 'Variation Category', 'class': 'form-control here'}),
            'Variation_value': forms.TextInput(attrs={'placeholder': 'Variation Value', 'class': 'form-control here'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ('subject', 'review', 'rating')
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control here'}),
            'review': forms.Textarea(attrs={'placeholder': 'Review', 'class': 'form-control here'}),
            'rating': forms.Select(attrs={'class': 'form-control here'}),
        }
        

