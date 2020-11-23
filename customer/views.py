from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
import datetime
from .models import *
import json

# Create your views here.
def home(request):
    return render(request, '../templates/customer/home.html')


def updateItem(request):
    data = json.loads(request.body)
    menuitemId = data['menuitemId']
    action = data['action']

    print('Action:', action)
    print('menuItem:', menuitemId)

    customer = request.user.customer
    menu_item = Menu_item.objects.get(id=menuitemId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, menu_item=menu_item)

    #if the user hits the add button on the front end add 1 item to the order
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    # else if the user hits the remove button remove 1 item from the order
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    #save the order item
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
   
    if request.user.is_authenticated:
        customer = request.user.is_authenticated
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        total = data['form']['total']
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.delivery == True:
            Seatlocation.objects.create(
                customer = customer,
                order = order,
                section = data['shipping']['section'],
                row = data['shipping']['row'],
                seat = data['shipping']['seat'],
            )

    else:
        print('User is not logged in')

    


    return JsonResponse('Payment Complete', safe=False)


#Display all items in a cart for the logged in customer
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 ,'shipping':True}
    context = {'items':items, 'order':order}
    return render(request, '../templates/customer/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items  = order.orderitem_set.all()
    else:
        #create empty cart for now for non logged in users 
        order = {'get_cart_total':0, 'get_cart_items':0 }
        items = []

    context = {'items':items, 'order':order}
    return render(request, '../templates/customer/checkout.html', context)


def select_seat(request):
    return render(request, '../templates/customer/select_seat.html')