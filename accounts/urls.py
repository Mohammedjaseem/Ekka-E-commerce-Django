from django.urls import path
from .import views
from Home_App import urls as Home_App_urls
from django.conf.urls import include

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home',include('Home_App.urls')),
]
