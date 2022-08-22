from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']
    list_filter = ['date_added']
    search_fields = ['cart_id']
    class Meta:
        model = Cart

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'is_active']
    list_filter = ['product']
    search_fields = ['product']
    class Meta:
        model = CartItem


admin.site.register(Cart, CartAdmin)
admin.site.register( CartItem, CartItemAdmin)


