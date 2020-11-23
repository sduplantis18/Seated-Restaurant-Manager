from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.http import request
from . models import User, Customer, Manager
from . forms import CustomerSingupForm, ManagerSingupForm



# Create your views here.

class customer_register(CreateView):
    model = User
    form_class = CustomerSingupForm
    template_name = '../templates/registration/customer_register.html'
    success_url = '/'

    def validation(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('customer:home')

class manager_register(CreateView):
    model = User
    form_class = ManagerSingupForm
    template_name = '../templates/registration/manager_register.html'
    success_url = '/'

    def validation(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('learning_logs:topics')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Welcome")
                return redirect('learning_logs:index')
            else: 
                messages.error(request, "Invalid username or password")

        else: 
            messages.error(request, "Invalid username or password")
    # Display the login page
    return render(request, '../templates/registration/login.html',context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return render(request, '../templates/registration/logged_out.html')