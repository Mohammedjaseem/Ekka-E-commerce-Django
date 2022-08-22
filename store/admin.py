from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class Product_modeladmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display  = ('product_name', 'price', 'stock', 'is_available', 'Category_Main', 'sub_category')
    list_filter   = ('product_name' , 'price', 'stock', 'is_available', 'Category_Main', 'sub_category')
    search_fields = ('product_name', 'slug', 'price', 'description',  'stock', 'is_available', 'Category_Main', 'sub_category', )

    filter_horizontal = ()
    list_per_page = 25

admin.site.register(Product, Product_modeladmin)

class Variation_modeladmin(admin.ModelAdmin):
    list_display  = ('Product', 'Variation_category', 'Variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter   = ('Product', 'Variation_category', 'Variation_value', 'is_active') 
    search_fields = ('Product', 'Variation_category', 'Variation_value', 'is_active')

    filter_horizontal = ()

    list_per_page = 25

admin.site.register(Variation, Variation_modeladmin)
