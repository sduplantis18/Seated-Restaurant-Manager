

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_runner = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now=True)


    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.email


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.user.email


class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    

    def __str__(self):
        return self.user.email

class Guest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", max_length=60, unique=False)
    phone_number = models.CharField(max_length=20)

