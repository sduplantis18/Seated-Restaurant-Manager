from django.contrib.auth import logout
from django.urls import path, include
from . import views


app_name = 'customer'
urlpatterns = [
    # Customer Home page
    path('home/', views.home, name='home'),
]