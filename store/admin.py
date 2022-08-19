from django.contrib import admin
from .models import Product

# Register your models here.

class Product_modeladmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display  = ('product_name', 'slug', 'price', 'stock', 'is_available', 'Category_Main', 'sub_category', 'created_date', 'modified_date')
    list_display_links = ('product_name', 'slug')
    list_filter   = ('product_name', 'slug', 'price', 'description', 'images', 'stock', 'is_available', 'Category_Main', 'sub_category', 'created_date', 'modified_date')
    search_fields = ('product_name', 'slug', 'price', 'description', 'images', 'stock', 'is_available', 'Category_Main', 'sub_category', 'created_date', 'modified_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 25

admin.site.register(Product, Product_modeladmin)
