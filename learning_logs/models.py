from users.models import Manager
from django.db import models
from django.conf import settings
from django.db.models.fields import CharField, NullBooleanField
from django.forms import ModelChoiceField

User = settings.AUTH_USER_MODEL


# Create your models here.
class Topic(models.Model):
    """Veneu Details"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=200, null=True)
    zip_code = models.IntegerField(null=False, default=33609)
    city = models.CharField(max_length=50, null=False, default='Tampa')
    State = CharField(null=False, max_length=50, default='Florida')
    country = CharField(null=False, max_length=50, default='United States')
    image = models.ImageField(null=True, blank=True, upload_to='arena_pics')
    logo = models.ImageField(null = True, blank=True, upload_to='menu_media')
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """A restuarant"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='menu_media')
    owner = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, null=True)
    section = models.CharField(max_length=50, null=True)
    delivery = models.BooleanField(default=True)
    pickup = models.BooleanField(default=True)
    active = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        if self.text > self.text[:50]:
            return f"{self.text[:50]} ..."
        else:
            return self.text
            


class Menu(models.Model):
    """A Menu"""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    title = models.TextField(max_length=50, null=False)

    class Meta:
        verbose_name_plural = 'menus'

    def __str__(self):
        return self.title

class Menu_item(models.Model):
    """An item on a menu"""
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='menu_items')
    quantity = models.IntegerField(default=0)
    delivery = models.BooleanField(default=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'menu items'

    def __str__(self):
        return self.title
    

