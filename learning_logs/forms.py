from django.forms.formsets import formset_factory
from users.models import Customer
from django import forms
from .models import Menu, Menu_item, Topic, Entry
from customer.models import Order, STATUS


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text','image', 'address', 'city', 'zip_code', 'State', 'country']
        labels = {'text':'Title', 'image':'Thumbnail', 'address':'Address', 'city':'City', 'zip_code':'Zip Code', 'State':'State', 'country':'Country'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'image']
        labels = {'text':'Restaurant:', 'image':'Thumbnail'}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['title']
        labels = {'title':'Menu Title'}


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu_item
        fields = ['title', 'price', 'image', 'quantity']
        labels = {'title': 'Menu Item', 'price':'price', 'image':'Thumbnail', 'quantity':'quantitiy'}


class Statusform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        labels = {'Update Status': STATUS}

StatusFormSet = formset_factory(Statusform)

