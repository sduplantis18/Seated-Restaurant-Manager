from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from allauth.account.views import SignupForm, SignupView
from django.http import request
from . models import User, Customer, Manager
from . forms import CustomerSingupForm, ManagerSingupForm



# Create your views here.

class customer_register(SignupView):
    model = User
    form_class = CustomerSingupForm
    template_name = '../templates/account/customer_register.html'
    success_url = '/'

    def validation(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('users:login')

class manager_register(SignupView):
    model = User
    form_class = ManagerSingupForm
    template_name = '../templates/account/manager_register.html'
    success_url = '/'

    def validation(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('users:login')

def logout_view(request):
    logout(request)
    return render(request, '../templates/registration/logged_out.html')

''' 
# No longer using custom login function. Leaving for historical purposes. 
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome")
                return redirect('learning_logs:index')
            else: 
                messages.error(request, "Email or Password is incorrect.")

        else: 
            messages.error(request, "Invalid email or password")
    # Display the login page
    return render(request, '../templates/account/login.html',context={'form':AuthenticationForm()})
'''


