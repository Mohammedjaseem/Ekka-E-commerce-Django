from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email     = forms.EmailField(required=True, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Please enter your email'}))
    username  = forms.CharField(required=True, label="User Name", widget=forms.TextInput(attrs={'placeholder': 'Please enter your user name'}))
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password'}))
    phone_number = forms.CharField(required=True, label="Phone Number", widget=forms.TextInput(attrs={'placeholder': 'Please enter your phone number'}))

    class Meta:
        model = Account
        fields = ['full_name','username', 'email', 'phone_number', 'password']
        


# class LoginForm(forms.Form):
