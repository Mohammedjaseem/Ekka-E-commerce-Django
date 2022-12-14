from django.urls import path
from .import views
from Home_App import urls as Home_App_urls
from django.conf.urls import include

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home',include('Home_App.urls')),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('order_details/<order_id>/', views.order_details, name='order_details'),
    path('cancel_order/<order_id>/', views.cancel_order, name='cancel_order'),

]
