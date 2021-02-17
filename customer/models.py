import os
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import NullBooleanField
from learning_logs.models import Entry, Topic, Menu_item, User
from users.models import Customer
from django.db import models
from django.db.models.signals import post_save
from twilio.rest import Client

# Create your models here.
STATUS = (
        ('Submitted', 'Submitted'),
        ('Received', 'Recieved'),
        ('Ready for Pickup', 'Ready for Pickup'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered'),
    )

class Order(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS) 
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    pickup = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


    @property
    #TODO need to create a better way to solve this problem. There is now attributes on the entry model to allow the restaurant to set whether or not they want to allow delivery or pickup.
    #defines whether or not delivery is reuired or if it will be a pickup order
    def delivery(self):  
        delivery = True
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.menu_item.delivery == False:
                delivery = False
        return delivery

#TODO Need to move the signal functions below into their own singals.py file and reference them in the models. 
# This is a django signal function that gets called when the Order object is updated. It checks to see if the status of the order changed to "Recieved"    
def order_received(sender, instance, created, **kwargs):
    if created == False:
        if instance.status == 'Received':
            account_sid = 'ACdadc7f168882c4eb4ba972ebd766abbf'
            auth_token = '42317e9f733c29be3409092db6e940c4'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body = 'We got your order! Once your order is ready we will notify you here. Thank you!',
                from_= '+17733094920',
                to = '+1'+ instance.customer.phone_number,
            )
            print(message.sid)
        elif instance.status == 'Ready for Pickup':
            account_sid = 'ACdadc7f168882c4eb4ba972ebd766abbf'
            auth_token = '42317e9f733c29be3409092db6e940c4'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body = 'Your order is ready! please come to pickup window and be ready to present your order number. Thank you!',
                from_= '+17733094920',
                to = '+1'+ instance.customer.phone_number,
            )
            print(message.sid)
    else:
        print('this is a new order')
post_save.connect(order_received, sender=Order)


class OrderItem(models.Model):
    menu_item = models.ForeignKey(Menu_item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item.title

    @property
    def get_total(self):
        total = self.menu_item.price * self.quantity
        return total
    

class Seatlocation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    section = models.CharField(max_length=25)
    row = models.CharField(max_length=10)
    seat =  models.IntegerField()

    def __str__(self):
        return self.section