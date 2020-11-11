from django.contrib import admin
from .models import User, Customer, Manager, Runner

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Manager)
