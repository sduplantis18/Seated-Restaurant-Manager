
"""Defines url patterns for users"""

from django.contrib.auth import logout
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Registration page
    path('register/', views.register, name='register'),
    # Customer Registration page
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    # Manager Registration page
    path('manager_register/', views.manager_register.as_view(), name='manager_register'),
    # Login Page
    path('login/', views.login_request, name='login_request'),
    # Logout Page 
    path('logged_out/', views.logout_view, name='logout_view'),
]