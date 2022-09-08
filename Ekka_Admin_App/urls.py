from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),

    #user based urls 
    path('user_list', views.user_list, name='user_list'),
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('user_delete/<int:pk>', views.user_delete, name='user_delete'),
    path('user_block/<int:pk>', views.user_block, name='user_block'),
    path('user_unblock/<int:pk>', views.user_unblock, name='user_unblock'),

    #category based urls
    path('main_category', views.main_category, name='main_category'),
    path('main_category_edit/<int:pk>', views.main_category_edit, name='main_category_edit'),
    path('main_category_delete/<int:pk>', views.main_category_delete, name='main_category_delete'),

    #sub category based urls
    path('sub_category', views.sub_category, name='sub_category'),
    path('sub_category_edit/<int:pk>', views.sub_category_edit, name='sub_category_edit'),
    path('sub_category_delete/<int:pk>', views.sub_category_delete, name='sub_category_delete'),

    #product based urls
    path('product_list', views.product_list, name='product_list'),
    path('product_edit/<int:pk>', views.product_edit, name='product_edit'),
    path('product_delete/<int:pk>', views.product_delete, name='product_delete'),

    #Variations based urls
    path('add_variations', views.add_variations, name='add_variations'),
    path('edit_variations/<int:pk>', views.edit_variations, name='edit_variations'),
    path('delete_variations/<int:pk>', views.delete_variations, name='delete_variations'),

    #Order based urls
    path('order_list', views.order_list, name='order_list'),
    path('order_update/<int:pk>', views.order_update, name='order_update'),
]
