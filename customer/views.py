from users.models import Manager
from learning_logs.views import entry
from django.contrib import messages
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

    if request.user.is_authenticated:    
        '''
        Build query set to build the order object 
        '''
        print('Action:', action)
        print('menuItem:', menuitemId)
        print(Entry.objects.get(menu__menu_item__id=menuitemId))
        #get the customer who is logged in
        customer = request.user.customer
        #get the menu item from the JSON above and assign it to the id of menu item variable
        menu_item = Menu_item.objects.get(id=menuitemId)
        topic = Topic.objects.get(entry__menu__menu_item__id=menuitemId)
        entry = Entry.objects.get(menu__menu_item__id = menuitemId)
        order, created = Order.objects.get_or_create(customer=customer, entry=entry, topic=topic, complete=False)
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
    else:
        print("User is not logged in")
        



def processOrder(request):
    #set the transaction id
    transaction_id = datetime.datetime.now().timestamp()
    #store the json from data in the data variable
    data = json.loads(request.body)
    
    #Check to see if the user is authenticated and update the order
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete = False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        #if the total equals the get cart total then set order completed to true and order status to recieved.
        if total == order.get_cart_total:
            order.complete = True
            order.status = 'Received'
        order.save()

        #if the user selected delivery set the seat location
        if order.delivery == True:
            order.pickup = True
            order.save() #this code is bad. i am lazy. Im essentially hard coding this now, but should be using the ordertype form on the checkout page instead. 
            Seatlocation.objects.create(
                customer = customer,

                order = order,
                section = data['delivery']['section'],
                row = data['delivery']['row'],
                seat = data['delivery']['seat'],
            )

    else:
        print('User is not logged in')

    return JsonResponse('Payment Complete', safe=False)


#Display all items in a cart for the logged in customer
def cart(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            order = Order.objects.get(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        except:
            messages.warning(request, "You have not added anything to your cart yet.")
            return render(request, '../templates/customer/cart.html')
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 ,'shipping':True}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, '../templates/customer/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)
        items  = order.orderitem_set.all()
    else:
        #create empty cart for now for non logged in users 
        order = {'get_cart_total':0, 'get_cart_items':0 }
        items = []

    context = {'items':items, 'order':order}
    return render(request, '../templates/customer/checkout.html', context)

#not using this at the moment
def select_seat(request):
    return render(request, '../templates/customer/select_seat.html')


def order_complete(request):
    return render(request, '../templates/customer/order_complete.html')

def orders(request):
    """View open orders for a customer"""
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=True).order_by('-created_date')
        items = OrderItem.objects.filter(order__customer=customer)

    else:
        orders = []
        items = []
    context = {'orders':orders, 'items':items}
    return render(request, '../templates/customer/orders.html', context)


