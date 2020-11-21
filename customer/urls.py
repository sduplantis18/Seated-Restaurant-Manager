from django.contrib.auth import logout
from django.urls import path, include
from . import views


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
]