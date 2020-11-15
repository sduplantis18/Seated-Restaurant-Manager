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
