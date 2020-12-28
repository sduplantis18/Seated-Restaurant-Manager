from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, User, Manager




# Customer singup using AllAuth "SignupForm"  
class CustomerSingupForm(SignupForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, request):
        user = super(CustomerSingupForm, self).save(request)
        user.is_customer = True
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.save()
        return user

# Manager singup using AllAuth "SignupForm"   
class ManagerSingupForm(SignupForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, request):
        user = super(ManagerSingupForm, self).save(request)
        user.is_manager = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.phone_number = self.cleaned_data.get('phone_number')
        manager.save()
        return user