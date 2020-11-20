from django.http import request
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, '../templates/customer/home.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items, 'order':order}
    return render(request, '../templates/customer/cart.html', context)


def checkout(request):
    return render(request, '../templates/customer/checkout.html')

