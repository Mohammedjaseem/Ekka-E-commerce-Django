from django import forms
from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = Account
        fields = ['full_name', 'email', 'phone_number', 'password', 'confirm_password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password: 
            raise forms.ValidationError('Password does not match!')

        return cleaned_data 


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name', 'email', 'phone_number']
        widgets = {
            'full_name'   : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email'       : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'


class UserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address_line_1', 'address_line_2', 'profile_picture', 'city', 'state', 'country', 'bio']
        widgets = {
            'address_line_1' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'address_line_2' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}),
            'city'           : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'country'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'bio'            : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        self.fields['address_line_1'].widget.attrs['placeholder'] = 'Address Line 1'
        self.fields['address_line_2'].widget.attrs['placeholder'] = 'Address Line 2'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['bio'].widget.attrs['placeholder'] = 'Bio'
        self.fields['profile_picture'].widget.attrs['placeholder'] = 'Profile Picture'
        





