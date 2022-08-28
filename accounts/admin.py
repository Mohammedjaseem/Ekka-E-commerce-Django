from django.contrib import admin
from .models import  Account, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html



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


class UserProfile_modelAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius: 50%;" />'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display  = ('thumbnail' ,'user', 'city', 'state', 'country', 'bio')
    list_filter   = ('user', 'city', 'state',  )
    search_fields = ('user', 'city', 'state',  )
    ordering = ('user',)
    
    list_per_page = 25

admin.site.register(UserProfile, UserProfile_modelAdmin)

