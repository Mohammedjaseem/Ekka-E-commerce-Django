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


    path('sub_category', views.sub_category, name='sub_category'),

]
