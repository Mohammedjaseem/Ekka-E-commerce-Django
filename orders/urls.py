
from django.urls import path, include
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('place_order/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('order_complete/', views.order_complete, name='order_complete'),
    
] 
