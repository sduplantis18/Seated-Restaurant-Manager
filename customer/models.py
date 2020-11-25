from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import NullBooleanField
from learning_logs.models import Entry, Topic, Menu_item
from users.models import Customer
from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered')
    )
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS) 
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

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
    #defines whether or not delivery is reuired or if it will be a pickup order
    def delivery(self):
        delivery = True
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.menu_item.delivery == False:
                delivery = False
        return delivery


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