from django.contrib import admin
from .models import  Account
from django.contrib.auth.admin import UserAdmin



class Account_modeladmin(UserAdmin):
    list_display  = ('username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email')
    list_filter   = ('username', 'email', 'date_joined')
    search_fields = ('username', 'email')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('date_joined',)
     
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 25

admin.site.register(Account, Account_modeladmin)

