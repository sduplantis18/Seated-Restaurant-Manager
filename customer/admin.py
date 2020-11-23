from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem, Seatlocation

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Seatlocation)
