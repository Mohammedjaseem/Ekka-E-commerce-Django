from django.contrib import admin
from .models import CategoryMain
from .models import SubCategory

#Register your models here.


class CategoryMain_modeladmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display  = ('category_name', 'slug', 'description', 'cat_main_img')
    list_display_links = ('category_name', 'slug')
    list_filter   = ('category_name', 'slug', 'description')
    search_fields = ('category_name', 'slug', 'description')

     
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 25

admin.site.register(CategoryMain, CategoryMain_modeladmin)

class SubCategory_modeladmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('sub_category_name',)}
    list_display  = ('category','sub_category_name', 'slug', 'description', 'cat_sub_img')
    list_display_links = ('sub_category_name', 'slug')
    list_filter   = ('sub_category_name', 'slug', 'description')
    search_fields = ('sub_category_name', 'slug', 'description')

     
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 25

admin.site.register(SubCategory, SubCategory_modeladmin)


