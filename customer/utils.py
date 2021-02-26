import json
from users.models import Guest

from allauth.account.utils import user_email
from .models import *

# This function allows guest users to add items to a cart. Call this function from the Cart view on the customers views.py file
def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {} 

    print('Cart:', cart)
    items = []
    entry = {}
    topic = {}
    order = {'get_cart_total':0, 'get_cart_items':0 ,'shipping':False}
    cartItems = order['get_cart_items']
    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            menu_item = Menu_item.objects.get(id=i)

            total = (menu_item.price * cart[i]["quantity"])
            topic = Topic.objects.get(entry__menu__menu_item__id=i)
            print(topic)
            entry = Entry.objects.get(menu__menu_item__id = i)
            print(entry)
            
                
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'menu_item':{
                    'id':menu_item.id,
                    'name':menu_item.title,
                    'price':menu_item.price,
                    'image':menu_item.image,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
                }
            items.append(item)
        except:
            pass
            print('Something went wrong')
    return {'cartItems': cartItems, 'order': order, 'items':items, 'entry':entry, 'topic':topic}



def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)
        items  = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        #create empty cart for now for non logged in users 
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        print('Anonymous cart created')
    
    return {'items':items, 'order':order, 'cartItems':cartItems}
    

def guestOrder(request, data):
    print('User is not logged in')

    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']
    phone_number = data['phone_num']['phone']

    cookieData = cookieCart(request)
    items = cookieData['items']

    guest, created = Guest.objects.get_or_create(phone_number=phone_number)
    guest.name = name
    guest.email = email
    print(guest.phone_number)
    guest.save()

    order = Order.objects.create(
        guest = guest,
        complete = False,
        entry = cookieData['entry'], 
        topic = cookieData['topic']
    )
    print("Order Created")

    for item in items:
        menu_item = Menu_item.objects.get(id=item['menu_item']['id'])
        orderItem = OrderItem.objects.create(
            menu_item=menu_item,
            order=order,
            quantity=item['quantity'],
        )
    
    return guest, order