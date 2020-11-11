from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, User, Manager, Runner

class CustomerSingupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned.data.get('first_name')
        user.first_name = self.cleaned.data.get('last_name')
        user.phone_number = self.cleaned.data.get('phone_number')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return user

    
class ManagerSingupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.first_name = self.cleaned.data.get('first_name')
        user.first_name = self.cleaned.data.get('last_name')
        user.phone_number = self.cleaned.data.get('phone_number')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.save()
        return user