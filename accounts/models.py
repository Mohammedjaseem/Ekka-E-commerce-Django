from django.db import models
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email    =self.normalize_email(email),
            username =username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email    =self.normalize_email(email),
            password =password,
            username =username,
        )
        user.is_admin     = True
        user.is_active    = True
        user.is_staff     = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username      = models.CharField(max_length=50)#removed uniq due to diffrent doamins and auto generation of id in the mails
    email         = models.EmailField(max_length=255, unique=True)
    phone_number  = models.CharField(max_length=20, blank=True) 
    full_name     = models.CharField(max_length=50, blank=True) 
   
    #required fields for AbstractBaseUser
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin 

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    #one to one relationship with the user ( user can have only one profile | if we use forgin key then one user can have many profiles) 
    address_line_1  = models.CharField(max_length=150, blank=True)
    address_line_2  = models.CharField(max_length=150, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    city            = models.CharField(max_length=100, blank=True)
    state           = models.CharField(max_length=100, blank=True)
    country         = models.CharField(max_length=100, blank=True)
    bio             = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.full_name
    
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'


     

     