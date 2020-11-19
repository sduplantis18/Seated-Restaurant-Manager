from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import NullBooleanField
from learning_logs.models import Menu_item, Row, Seat, Section
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
    menu_item = models.ForeignKey(Menu_item, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section, null=False ,on_delete=CASCADE)
    row = models.ForeignKey(Row, null=False,on_delete=CASCADE)
    seat = models.ForeignKey(Seat, null=False, on_delete=CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    menu_item = models.ForeignKey(Menu_item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    row = models.ForeignKey(Row, on_delete=models.SET_NULL, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.SET_NULL, null=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
