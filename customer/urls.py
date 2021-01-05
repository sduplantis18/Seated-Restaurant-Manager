from os import name, stat
from django.contrib.auth import logout
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'customer'
urlpatterns = [
    # Customer Home page
    path('home/', views.home, name='home'),
    # Cart
    path('cart/', views.cart, name='cart'),
    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    # Updateitem
    path('update_item/', views.updateItem, name="update_item"),
    # process order
    path('process_order/', views.processOrder, name="process_order"),
    # display select a seat 
    path('select_seat/', views.select_seat, name="select_seat"),
    # Display completed order
    path('order_complete/', views.order_complete, name='order_complete'),
    # track order
    path('orders/', views.orders, name='orders'),
    # Display a dashboard for the vendor
    path('my_restaurant/', views.my_restaurant, name='my_restaurant'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

